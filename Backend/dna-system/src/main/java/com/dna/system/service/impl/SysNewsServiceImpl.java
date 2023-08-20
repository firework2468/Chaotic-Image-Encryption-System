package com.dna.system.service.impl;

import java.util.List;
import com.dna.common.utils.DateUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.dna.system.mapper.SysNewsMapper;
import com.dna.system.domain.SysNews;
import com.dna.system.service.ISysNewsService;

/**
 * 新闻Service业务层处理
 * 
 * @author dna
 * @date 2021-05-15
 */
@Service
public class SysNewsServiceImpl implements ISysNewsService 
{
    @Autowired
    private SysNewsMapper sysNewsMapper;

    /**
     * 查询新闻
     * 
     * @param newsId 新闻ID
     * @return 新闻
     */
    @Override
    public SysNews selectSysNewsById(Long newsId)
    {
        return sysNewsMapper.selectSysNewsById(newsId);
    }

    /**
     * 查询新闻列表
     * 
     * @param sysNews 新闻
     * @return 新闻
     */
    @Override
    public List<SysNews> selectSysNewsList(SysNews sysNews)
    {
        return sysNewsMapper.selectSysNewsList(sysNews);
    }

    /**
     * 新增新闻
     * 
     * @param sysNews 新闻
     * @return 结果
     */
    @Override
    public int insertSysNews(SysNews sysNews)
    {
        sysNews.setCreateTime(DateUtils.getNowDate());
        return sysNewsMapper.insertSysNews(sysNews);
    }

    /**
     * 修改新闻
     * 
     * @param sysNews 新闻
     * @return 结果
     */
    @Override
    public int updateSysNews(SysNews sysNews)
    {
        sysNews.setUpdateTime(DateUtils.getNowDate());
        return sysNewsMapper.updateSysNews(sysNews);
    }

    /**
     * 批量删除新闻
     * 
     * @param newsIds 需要删除的新闻ID
     * @return 结果
     */
    @Override
    public int deleteSysNewsByIds(Long[] newsIds)
    {
        return sysNewsMapper.deleteSysNewsByIds(newsIds);
    }

    /**
     * 删除新闻信息
     * 
     * @param newsId 新闻ID
     * @return 结果
     */
    @Override
    public int deleteSysNewsById(Long newsId)
    {
        return sysNewsMapper.deleteSysNewsById(newsId);
    }
}
