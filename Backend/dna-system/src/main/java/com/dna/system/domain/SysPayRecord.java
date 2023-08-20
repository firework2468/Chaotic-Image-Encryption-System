package com.dna.system.domain;

import com.dna.common.core.domain.entity.SysUser;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.dna.common.annotation.Excel;
import com.dna.common.core.domain.BaseEntity;

/**
 * vip会员购买记录对象 sys_pay_record
 *
 * @author dna
 * @date 2021-05-22
 */
public class SysPayRecord extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 主键 */
    private Integer recordId;

    /** 用户id */
    @Excel(name = "用户id")
    private Long userId;

    /** 会员等级id */
    @Excel(name = "会员等级id")
    private Integer vipId;

    private SysUser user;

    private SysVip vip;

    public void setRecordId(Integer recordId)
    {
        this.recordId = recordId;
    }

    public Integer getRecordId()
    {
        return recordId;
    }
    public void setUserId(Long userId)
    {
        this.userId = userId;
    }

    public Long getUserId()
    {
        return userId;
    }
    public void setVipId(Integer vipId)
    {
        this.vipId = vipId;
    }

    public Integer getVipId()
    {
        return vipId;
    }

    public SysUser getUser() {
        return user;
    }

    public void setUser(SysUser user) {
        this.user = user;
    }

    public SysVip getVip() {
        return vip;
    }

    public void setVip(SysVip vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("recordId", getRecordId())
            .append("userId", getUserId())
            .append("vipId", getVipId())
            .append("createBy", getCreateBy())
            .append("createTime", getCreateTime())
            .append("updateBy", getUpdateBy())
            .append("updateTime", getUpdateTime())
            .toString();
    }
}
