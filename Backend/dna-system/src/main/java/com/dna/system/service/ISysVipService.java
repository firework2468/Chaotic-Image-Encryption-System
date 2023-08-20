package com.dna.system.service;

import java.util.List;
import com.dna.system.domain.SysVip;

/**
 * vip会员等级Service接口
 * 
 * @author dna
 * @date 2021-05-22
 */
public interface ISysVipService 
{
    /**
     * 查询vip会员等级
     * 
     * @param vipId vip会员等级ID
     * @return vip会员等级
     */
    public SysVip selectSysVipById(Integer vipId);

    /**
     * 查询vip会员等级列表
     * 
     * @param sysVip vip会员等级
     * @return vip会员等级集合
     */
    public List<SysVip> selectSysVipList(SysVip sysVip);

    /**
     * 新增vip会员等级
     * 
     * @param sysVip vip会员等级
     * @return 结果
     */
    public int insertSysVip(SysVip sysVip);

    /**
     * 修改vip会员等级
     * 
     * @param sysVip vip会员等级
     * @return 结果
     */
    public int updateSysVip(SysVip sysVip);

    /**
     * 批量删除vip会员等级
     * 
     * @param vipIds 需要删除的vip会员等级ID
     * @return 结果
     */
    public int deleteSysVipByIds(Integer[] vipIds);

    /**
     * 删除vip会员等级信息
     * 
     * @param vipId vip会员等级ID
     * @return 结果
     */
    public int deleteSysVipById(Integer vipId);
}
