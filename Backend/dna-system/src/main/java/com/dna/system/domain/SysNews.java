package com.dna.system.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.dna.common.annotation.Excel;
import com.dna.common.core.domain.BaseEntity;

/**
 * 新闻对象 sys_news
 * 
 * @author dna
 * @date 2021-05-15
 */
public class SysNews extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 新闻id */
    private Long newsId;

    /** 新闻标题 */
    @Excel(name = "新闻标题")
    private String newsTitle;

    private String avatar;

    /** 新闻作者 */
    @Excel(name = "新闻作者")
    private String author;

    /** 新闻类型（1通知 2新闻） */
    @Excel(name = "新闻类型", readConverterExp = "1=通知,2=新闻")
    private String newsType;

    /** 新闻内容 */
    @Excel(name = "新闻内容")
    private String newsContent;

    /** 新闻状态（0正常 1关闭） */
    @Excel(name = "新闻状态", readConverterExp = "0=正常,1=关闭")
    private String status;

    public void setNewsId(Long newsId) 
    {
        this.newsId = newsId;
    }

    public Long getNewsId() 
    {
        return newsId;
    }
    public void setNewsTitle(String newsTitle) 
    {
        this.newsTitle = newsTitle;
    }

    public String getNewsTitle() 
    {
        return newsTitle;
    }
    public void setAvatar(String avatar) 
    {
        this.avatar = avatar;
    }

    public String getAvatar() 
    {
        return avatar;
    }
    public void setAuthor(String author) 
    {
        this.author = author;
    }

    public String getAuthor() 
    {
        return author;
    }
    public void setNewsType(String newsType) 
    {
        this.newsType = newsType;
    }

    public String getNewsType() 
    {
        return newsType;
    }
    public void setNewsContent(String newsContent) 
    {
        this.newsContent = newsContent;
    }

    public String getNewsContent() 
    {
        return newsContent;
    }
    public void setStatus(String status) 
    {
        this.status = status;
    }

    public String getStatus() 
    {
        return status;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("newsId", getNewsId())
            .append("newsTitle", getNewsTitle())
            .append("avatar", getAvatar())
            .append("author", getAuthor())
            .append("newsType", getNewsType())
            .append("newsContent", getNewsContent())
            .append("status", getStatus())
            .append("createBy", getCreateBy())
            .append("createTime", getCreateTime())
            .append("updateBy", getUpdateBy())
            .append("updateTime", getUpdateTime())
            .append("remark", getRemark())
            .toString();
    }
}
