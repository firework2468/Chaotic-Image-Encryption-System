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
import com.dna.system.domain.SysPayRecord;
import com.dna.system.service.ISysPayRecordService;
import com.dna.common.utils.poi.ExcelUtil;
import com.dna.common.core.page.TableDataInfo;

/**
 * vip会员购买记录Controller
 *
 * @author dna
 * @date 2021-05-22
 */
@RestController
@RequestMapping("/system/record")
public class SysPayRecordController extends BaseController
{
    @Autowired
    private ISysPayRecordService sysPayRecordService;

    /**
     * 查询vip会员购买记录列表
     */
    @PreAuthorize("@ss.hasPermi('system:record:list')")
    @GetMapping("/list")
    public TableDataInfo list(SysPayRecord sysPayRecord)
    {
        startPage();
        List<SysPayRecord> list = sysPayRecordService.selectSysPayRecordList(sysPayRecord);
        return getDataTable(list);
    }

    /**
     * 导出vip会员购买记录列表
     */
    @PreAuthorize("@ss.hasPermi('system:record:export')")
    @Log(title = "vip会员购买记录", businessType = BusinessType.EXPORT)
    @GetMapping("/export")
    public AjaxResult export(SysPayRecord sysPayRecord)
    {
        List<SysPayRecord> list = sysPayRecordService.selectSysPayRecordList(sysPayRecord);
        ExcelUtil<SysPayRecord> util = new ExcelUtil<SysPayRecord>(SysPayRecord.class);
        return util.exportExcel(list, "vip会员购买记录数据");
    }

    /**
     * 获取vip会员购买记录详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:record:query')")
    @GetMapping(value = "/{recordId}")
    public AjaxResult getInfo(@PathVariable("recordId") Integer recordId)
    {
        return AjaxResult.success(sysPayRecordService.selectSysPayRecordById(recordId));
    }

    /**
     * 新增vip会员购买记录
     */
    @PreAuthorize("@ss.hasPermi('system:record:add')")
    @Log(title = "vip会员购买记录", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody SysPayRecord sysPayRecord)
    {
        return toAjax(sysPayRecordService.insertSysPayRecord(sysPayRecord));
    }

    /**
     * 修改vip会员购买记录
     */
    @PreAuthorize("@ss.hasPermi('system:record:edit')")
    @Log(title = "vip会员购买记录", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody SysPayRecord sysPayRecord)
    {
        return toAjax(sysPayRecordService.updateSysPayRecord(sysPayRecord));
    }

    /**
     * 删除vip会员购买记录
     */
    @PreAuthorize("@ss.hasPermi('system:record:remove')")
    @Log(title = "vip会员购买记录", businessType = BusinessType.DELETE)
	@DeleteMapping("/{recordIds}")
    public AjaxResult remove(@PathVariable Integer[] recordIds)
    {
        return toAjax(sysPayRecordService.deleteSysPayRecordByIds(recordIds));
    }
}
