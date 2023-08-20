package com.dna.web.controller.system;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.dna.common.utils.http.HttpUtils;
import com.dna.system.mapper.SysLocalStorageMapper;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.dna.common.annotation.Log;
import com.dna.common.core.controller.BaseController;
import com.dna.common.core.domain.AjaxResult;
import com.dna.common.enums.BusinessType;
import com.dna.system.domain.SysLocalStorage;
import com.dna.system.service.ISysLocalStorageService;
import com.dna.common.utils.poi.ExcelUtil;
import com.dna.common.core.page.TableDataInfo;

import javax.annotation.Resource;

/**
 * 本地存储Controller
 *
 * @author dna
 * @date 2021-05-15
 */
@RestController
@RequestMapping("/system/storage")
public class SysLocalStorageController extends BaseController
{
    @Autowired
    private ISysLocalStorageService sysLocalStorageService;

    @Resource
    private SysLocalStorageMapper sysLocalStorageMapper;


    private String url = "http://localhost:3000";

    /**
     * 查询本地存储列表
     */
    @GetMapping("/list")
    public TableDataInfo list(SysLocalStorage sysLocalStorage)
    {
        startPage();
        List<SysLocalStorage> list = sysLocalStorageService.selectLocalStorageList(sysLocalStorage);
        return getDataTable(list);
    }

    /**
     * 导出本地存储列表
     */
    @PreAuthorize("@ss.hasPermi('system:storage:export')")
    @Log(title = "本地存储", businessType = BusinessType.EXPORT)
    @GetMapping("/export")
    public AjaxResult export(SysLocalStorage sysLocalStorage)
    {
        List<SysLocalStorage> list = sysLocalStorageService.selectLocalStorageList(sysLocalStorage);
        ExcelUtil<SysLocalStorage> util = new ExcelUtil<SysLocalStorage>(SysLocalStorage.class);
        return util.exportExcel(list, "本地存储数据");
    }

    /**
     * 获取本地存储详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:storage:query')")
    @GetMapping(value = "/{storageId}")
    public AjaxResult getInfo(@PathVariable("storageId") Long storageId)
    {
        return AjaxResult.success(sysLocalStorageService.selectSysLocalStorageById(storageId));
    }

    /**
     * 新增本地存储
     */
    @PreAuthorize("@ss.hasPermi('system:storage:add')")
    @Log(title = "本地存储", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody SysLocalStorage sysLocalStorage)
    {
        return toAjax(sysLocalStorageService.insertSysLocalStorage(sysLocalStorage));
    }

    /**
     * 修改本地存储
     */
    @PreAuthorize("@ss.hasPermi('system:storage:edit')")
    @Log(title = "本地存储", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody SysLocalStorage sysLocalStorage)
    {
        return toAjax(sysLocalStorageService.updateSysLocalStorage(sysLocalStorage));
    }

    /**
     * 删除本地存储
     */
    @PreAuthorize("@ss.hasPermi('system:storage:remove')")
    @Log(title = "本地存储", businessType = BusinessType.DELETE)
	@DeleteMapping("/{storageIds}")
    public AjaxResult remove(@PathVariable Long[] storageIds)
    {
        return toAjax(sysLocalStorageService.deleteSysLocalStorageByIds(storageIds));
    }

    @Log(title = "图片加密", businessType = BusinessType.ENCRYPT)
    //@PreAuthorize("@ss.hasPermi('system:storage:encrypt')")
    @PostMapping("/encrypted")
    public AjaxResult imgEncrypted(@RequestBody SysLocalStorage localStorage) {


        JSONObject obj = new JSONObject();
        obj.fluentPut("id", localStorage.getStorageId());
        obj.fluentPut("imageUrl", localStorage.getPath());
        String result = HttpUtils.sendPost(url+"/encrypt", obj);
        JSONObject jsonObject = JSONObject.parseObject(result);
        localStorage.setEncryptedPath(jsonObject.getString("url"));
        localStorage.setKeyValue(jsonObject.getString("key"));
        localStorage.setEncode("encrypted");
        SysLocalStorage sysLocalStorage = new SysLocalStorage();
        sysLocalStorage.setStorageId(localStorage.getStorageId());
        sysLocalStorage.setEncode("encrypted");
        sysLocalStorageMapper.updateSysLocalStorage(sysLocalStorage);
        return success(JSONObject.toJSONString(localStorage));
    }

    @Log(title = "图片解密", businessType = BusinessType.DECRYPT)
    @PreAuthorize("@ss.hasPermi('system:storage:encrypt')")
    @PostMapping("/decrypted")
    public AjaxResult imgDecrypt(@RequestBody SysLocalStorage localStorage)
    {
        JSONObject obj = new JSONObject();
        obj.fluentPut("id", localStorage.getStorageId());
        obj.fluentPut("imageUrl", localStorage.getEncryptedPath());
        HttpUtils.sendPost(url+"/decrypt", obj);
        localStorage.setEncode("decrypted");
        return toAjax(true);
    }

    @Log(title = "图片加密结果", businessType = BusinessType.DECRYPT)
    @GetMapping("/encryptRes")
    public AjaxResult encryptRes(SysLocalStorage localStorage)
    {
        String key = HttpUtils.sendGet(url+"/static/" + localStorage.getStorageId() + "/key.json","");

        Map<String, Object> imgMap = new HashMap<>();
        imgMap.put("encrypt", url+"/static/" + localStorage.getStorageId() + "/encrypt.png");
        imgMap.put("key", JSONObject.parseArray(key));
        return AjaxResult.success(imgMap);
    }

    @Log(title = "直方图分析", businessType = BusinessType.DECRYPT)
    @PreAuthorize("@ss.hasPermi('system:storage:report')")
    @GetMapping("/zanalysis")
    public AjaxResult zanalysis(SysLocalStorage localStorage)
    {
        Map<String, Object> imgMap = new HashMap<>();

        imgMap.put("b1", url+"/static/" + localStorage.getStorageId() + "/histogram/B1.png");
        imgMap.put("g1", url+"/static/" + localStorage.getStorageId() + "/histogram/G1.png");
        imgMap.put("r1", url+"/static/" + localStorage.getStorageId() + "/histogram/R1.png");
        imgMap.put("b2", url+"/static/" + localStorage.getStorageId() + "/histogram/B2.png");
        imgMap.put("g2", url+"/static/" + localStorage.getStorageId() + "/histogram/G2.png");
        imgMap.put("r2", url+"/static/" + localStorage.getStorageId() + "/histogram/R2.png");
        return AjaxResult.success(imgMap);
    }

    @Log(title = "相邻相关性像素分析", businessType = BusinessType.DECRYPT)
    @PreAuthorize("@ss.hasPermi('system:storage:report')")
    @GetMapping("/xanalysis")
    public AjaxResult xanalysis(SysLocalStorage localStorage)
    {
        String[] params = {"hor_B", "hor_G", "hor_R", "ver_B", "ver_G", "ver_R", "dia_B", "dia_G", "dia_R"};
        Map<String, Object> imgMap = new HashMap<>();
        for (String param:params){
            imgMap.put(param+"1", url+"/static/" + localStorage.getStorageId() + "/correlation1/"+param+".png");
        }
        for (String param:params){
            imgMap.put(param+"2", url+"/static/" + localStorage.getStorageId() + "/correlation2/"+param+".png");
        }
        String result1 = HttpUtils.sendGet(url+"/static/" + localStorage.getStorageId() + "/correlation1/coefficient.json","");
        String result2 = HttpUtils.sendGet(url+"/static/" + localStorage.getStorageId() + "/correlation2/coefficient.json","");

        imgMap.put("result1", JSONObject.parseArray(result1));
        imgMap.put("result2", JSONObject.parseArray(result2));

        return AjaxResult.success(imgMap);
    }

    @Log(title = "信息熵分析", businessType = BusinessType.DECRYPT)
    @PreAuthorize("@ss.hasPermi('system:storage:report')")
    @GetMapping("/sanalysis")
    public AjaxResult sanalysis(SysLocalStorage localStorage)
    {
        String result = HttpUtils.sendGet(url+"/static/"
                + localStorage.getStorageId() + "/information_entropy/data.json", "");
        Map<String, Object> imgMap = new HashMap<>();
        imgMap.put("result", JSONObject.parseArray(result));
        return AjaxResult.success(imgMap);
    }

    @Log(title = "密钥敏感性", businessType = BusinessType.DECRYPT)
    @PreAuthorize("@ss.hasPermi('system:storage:report')")
    @GetMapping("/manalysis")
    public AjaxResult manalysis(SysLocalStorage localStorage)
    {
        Map<String, Object> imgMap = new HashMap<>();
        imgMap.put("decrypt", url+"/static/" + localStorage.getStorageId() + "/key_sensitive/decrypt.png");
        imgMap.put("encrypt", url+"/static/" + localStorage.getStorageId() + "/origin.png");
        return AjaxResult.success(imgMap);
    }

    @Log(title = "差分攻击分析", businessType = BusinessType.DECRYPT)
    @PreAuthorize("@ss.hasPermi('system:storage:report')")
    @GetMapping("/canalysis")
    public AjaxResult canalysis(SysLocalStorage localStorage)
    {
        String npcr = HttpUtils.sendGet(url+"/static/"
                + localStorage.getStorageId() + "/differential_attack/npcr.json", "");
        String uaci = HttpUtils.sendGet(url+"/static/"
                + localStorage.getStorageId() + "/differential_attack/uaci.json", "");

        Map<String, Object> imgMap = new HashMap<>();
        JSONArray jsonArray = JSONObject.parseArray(npcr);
        jsonArray.addAll(JSONObject.parseArray(uaci));
        imgMap.put("result", jsonArray);
        return AjaxResult.success(imgMap);
    }
}
