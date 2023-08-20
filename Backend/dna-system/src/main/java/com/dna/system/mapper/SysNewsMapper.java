package com.dna.system.mapper;

import java.util.List;
import com.dna.system.domain.SysNews;

/**
 * 新闻Mapper接口
 * 
 * @author dna
 * @date 2021-05-15
 */
public interface SysNewsMapper 
{
    /**
     * 查询新闻
     * 
     * @param newsId 新闻ID
     * @return 新闻
     */
    public SysNews selectSysNewsById(Long newsId);

    /**
     * 查询新闻列表
     * 
     * @param sysNews 新闻
     * @return 新闻集合
     */
    public List<SysNews> selectSysNewsList(SysNews sysNews);

    /**
     * 新增新闻
     * 
     * @param sysNews 新闻
     * @return 结果
     */
    public int insertSysNews(SysNews sysNews);

    /**
     * 修改新闻
     * 
     * @param sysNews 新闻
     * @return 结果
     */
    public int updateSysNews(SysNews sysNews);

    /**
     * 删除新闻
     * 
     * @param newsId 新闻ID
     * @return 结果
     */
    public int deleteSysNewsById(Long newsId);

    /**
     * 批量删除新闻
     * 
     * @param newsIds 需要删除的数据ID
     * @return 结果
     */
    public int deleteSysNewsByIds(Long[] newsIds);
}
