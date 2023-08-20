package com.dna.web.controller.system;

import java.util.List;
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
import com.dna.system.domain.SysVip;
import com.dna.system.service.ISysVipService;
import com.dna.common.utils.poi.ExcelUtil;
import com.dna.common.core.page.TableDataInfo;

/**
 * vip会员等级Controller
 *
 * @author dna
 * @date 2021-05-22
 */
@RestController
@RequestMapping("/system/vip")
public class SysVipController extends BaseController
{
    @Autowired
    private ISysVipService sysVipService;

    /**
     * 查询vip会员等级列表
     */
    @PreAuthorize("@ss.hasPermi('system:vip:list')")
    @GetMapping("/list")
    public TableDataInfo list(SysVip sysVip)
    {
        startPage();
        List<SysVip> list = sysVipService.selectSysVipList(sysVip);
        return getDataTable(list);
    }

    @GetMapping("/vip")
    public List<SysVip> getVipList(){
        List<SysVip> list = sysVipService.selectSysVipList(new SysVip());
        return list;
    }

    /**
     * 导出vip会员等级列表
     */
    @PreAuthorize("@ss.hasPermi('system:vip:export')")
    @Log(title = "vip会员等级", businessType = BusinessType.EXPORT)
    @GetMapping("/export")
    public AjaxResult export(SysVip sysVip)
    {
        List<SysVip> list = sysVipService.selectSysVipList(sysVip);
        ExcelUtil<SysVip> util = new ExcelUtil<SysVip>(SysVip.class);
        return util.exportExcel(list, "vip会员等级数据");
    }

    /**
     * 获取vip会员等级详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:vip:query')")
    @GetMapping(value = "/{vipId}")
    public AjaxResult getInfo(@PathVariable("vipId") Integer vipId)
    {
        return AjaxResult.success(sysVipService.selectSysVipById(vipId));
    }

    /**
     * 新增vip会员等级
     */
    @PreAuthorize("@ss.hasPermi('system:vip:add')")
    @Log(title = "vip会员等级", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody SysVip sysVip)
    {
        return toAjax(sysVipService.insertSysVip(sysVip));
    }

    /**
     * 修改vip会员等级
     */
    @PreAuthorize("@ss.hasPermi('system:vip:edit')")
    @Log(title = "vip会员等级", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody SysVip sysVip)
    {
        return toAjax(sysVipService.updateSysVip(sysVip));
    }

    /**
     * 删除vip会员等级
     */
    @PreAuthorize("@ss.hasPermi('system:vip:remove')")
    @Log(title = "vip会员等级", businessType = BusinessType.DELETE)
	@DeleteMapping("/{vipIds}")
    public AjaxResult remove(@PathVariable Integer[] vipIds)
    {
        return toAjax(sysVipService.deleteSysVipByIds(vipIds));
    }
}
