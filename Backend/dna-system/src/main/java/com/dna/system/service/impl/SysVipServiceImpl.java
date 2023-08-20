package com.dna.system.service.impl;

import java.util.List;
import com.dna.common.utils.DateUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.dna.system.mapper.SysVipMapper;
import com.dna.system.domain.SysVip;
import com.dna.system.service.ISysVipService;

/**
 * vip会员等级Service业务层处理
 *
 * @author dna
 * @date 2021-05-22
 */
@Service
public class SysVipServiceImpl implements ISysVipService
{
    @Autowired
    private SysVipMapper sysVipMapper;

    /**
     * 查询vip会员等级
     *
     * @param vipId vip会员等级ID
     * @return vip会员等级
     */
    @Override
    public SysVip selectSysVipById(Integer vipId)
    {
        return sysVipMapper.selectSysVipById(vipId);
    }

    /**
     * 查询vip会员等级列表
     *
     * @param sysVip vip会员等级
     * @return vip会员等级
     */
    @Override
    public List<SysVip> selectSysVipList(SysVip sysVip)
    {
        return sysVipMapper.selectSysVipList(sysVip);
    }

    /**
     * 新增vip会员等级
     *
     * @param sysVip vip会员等级
     * @return 结果
     */
    @Override
    public int insertSysVip(SysVip sysVip)
    {
        sysVip.setCreateTime(DateUtils.getNowDate());
        return sysVipMapper.insertSysVip(sysVip);
    }

    /**
     * 修改vip会员等级
     *
     * @param sysVip vip会员等级
     * @return 结果
     */
    @Override
    public int updateSysVip(SysVip sysVip)
    {
        sysVip.setUpdateTime(DateUtils.getNowDate());
        return sysVipMapper.updateSysVip(sysVip);
    }

    /**
     * 批量删除vip会员等级
     *
     * @param vipIds 需要删除的vip会员等级ID
     * @return 结果
     */
    @Override
    public int deleteSysVipByIds(Integer[] vipIds)
    {
        return sysVipMapper.deleteSysVipByIds(vipIds);
    }

    /**
     * 删除vip会员等级信息
     *
     * @param vipId vip会员等级ID
     * @return 结果
     */
    @Override
    public int deleteSysVipById(Integer vipId)
    {
        return sysVipMapper.deleteSysVipById(vipId);
    }
}
