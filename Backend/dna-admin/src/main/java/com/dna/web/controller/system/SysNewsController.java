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
import com.dna.system.domain.SysNews;
import com.dna.system.service.ISysNewsService;
import com.dna.common.utils.poi.ExcelUtil;
import com.dna.common.core.page.TableDataInfo;

/**
 * 新闻Controller
 * 
 * @author dna
 * @date 2021-05-15
 */
@RestController
@RequestMapping("/system/news")
public class SysNewsController extends BaseController
{
    @Autowired
    private ISysNewsService sysNewsService;

    /**
     * 查询新闻列表
     */
    @PreAuthorize("@ss.hasPermi('system:news:list')")
    @GetMapping("/list")
    public TableDataInfo list(SysNews sysNews)
    {
        startPage();
        List<SysNews> list = sysNewsService.selectSysNewsList(sysNews);
        return getDataTable(list);
    }

    /**
     * 导出新闻列表
     */
    @PreAuthorize("@ss.hasPermi('system:news:export')")
    @Log(title = "新闻", businessType = BusinessType.EXPORT)
    @GetMapping("/export")
    public AjaxResult export(SysNews sysNews)
    {
        List<SysNews> list = sysNewsService.selectSysNewsList(sysNews);
        ExcelUtil<SysNews> util = new ExcelUtil<SysNews>(SysNews.class);
        return util.exportExcel(list, "新闻数据");
    }

    /**
     * 获取新闻详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:news:query')")
    @GetMapping(value = "/{newsId}")
    public AjaxResult getInfo(@PathVariable("newsId") Long newsId)
    {
        return AjaxResult.success(sysNewsService.selectSysNewsById(newsId));
    }

    /**
     * 新增新闻
     */
    @PreAuthorize("@ss.hasPermi('system:news:add')")
    @Log(title = "新闻", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody SysNews sysNews)
    {
        return toAjax(sysNewsService.insertSysNews(sysNews));
    }

    /**
     * 修改新闻
     */
    @PreAuthorize("@ss.hasPermi('system:news:edit')")
    @Log(title = "新闻", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody SysNews sysNews)
    {
        return toAjax(sysNewsService.updateSysNews(sysNews));
    }

    /**
     * 删除新闻
     */
    @PreAuthorize("@ss.hasPermi('system:news:remove')")
    @Log(title = "新闻", businessType = BusinessType.DELETE)
	@DeleteMapping("/{newsIds}")
    public AjaxResult remove(@PathVariable Long[] newsIds)
    {
        return toAjax(sysNewsService.deleteSysNewsByIds(newsIds));
    }
}
