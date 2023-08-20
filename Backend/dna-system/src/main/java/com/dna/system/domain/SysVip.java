package com.dna.system.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.dna.common.annotation.Excel;
import com.dna.common.core.domain.BaseEntity;

/**
 * vip会员等级对象 sys_vip
 *
 * @author dna
 * @date 2021-05-22
 */
public class SysVip extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** vipId */
    private Integer vipId;

    /** 等级名称 */
    @Excel(name = "等级名称")
    private String name;

    /** 有效期 */
    @Excel(name = "有效期")
    private String expire;

    /** 次数 */
    @Excel(name = "次数")
    private Integer number;

    /** 价格 */
    @Excel(name = "价格")
    private String price;

    /** 图片 */
    @Excel(name = "图片")
    private String avatar;

    public void setVipId(Integer vipId)
    {
        this.vipId = vipId;
    }

    public Integer getVipId()
    {
        return vipId;
    }
    public void setName(String name)
    {
        this.name = name;
    }

    public String getName()
    {
        return name;
    }
    public void setExpire(String expire)
    {
        this.expire = expire;
    }

    public String getExpire()
    {
        return expire;
    }
    public void setNumber(Integer number)
    {
        this.number = number;
    }

    public Integer getNumber()
    {
        return number;
    }
    public void setPrice(String price)
    {
        this.price = price;
    }

    public String getPrice()
    {
        return price;
    }
    public void setAvatar(String avatar)
    {
        this.avatar = avatar;
    }

    public String getAvatar()
    {
        return avatar;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
                .append("vipId", getVipId())
                .append("name", getName())
                .append("expire", getExpire())
                .append("number", getNumber())
                .append("price", getPrice())
                .append("createBy", getCreateBy())
                .append("avatar", getAvatar())
                .append("createTime", getCreateTime())
                .append("updateBy", getUpdateBy())
                .append("updateTime", getUpdateTime())
                .toString();
    }
}
