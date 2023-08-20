package com.dna.system.service.impl;

import java.util.ArrayList;
import java.util.List;
import com.dna.common.utils.DateUtils;
import com.dna.common.utils.SecurityUtils;
import com.dna.system.domain.SysUserRole;
import com.dna.system.mapper.SysUserRoleMapper;
import org.springframework.stereotype.Service;
import com.dna.system.mapper.SysPayRecordMapper;
import com.dna.system.domain.SysPayRecord;
import com.dna.system.service.ISysPayRecordService;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.Resource;

/**
 * vip会员购买记录Service业务层处理
 *
 * @author dna
 * @date 2021-05-22
 */
@Service
public class SysPayRecordServiceImpl implements ISysPayRecordService
{
    @Resource
    private SysPayRecordMapper sysPayRecordMapper;
    @Resource
    private SysUserRoleMapper userRoleMapper;

    /**
     * 查询vip会员购买记录
     *
     * @param recordId vip会员购买记录ID
     * @return vip会员购买记录
     */
    @Override
    public SysPayRecord selectSysPayRecordById(Integer recordId)
    {
        return sysPayRecordMapper.selectSysPayRecordById(recordId);
    }

    /**
     * 查询vip会员购买记录列表
     *
     * @param sysPayRecord vip会员购买记录
     * @return vip会员购买记录
     */
    @Override
    public List<SysPayRecord> selectSysPayRecordList(SysPayRecord sysPayRecord)
    {
        return sysPayRecordMapper.selectSysPayRecordList(sysPayRecord);
    }

    /**
     * 新增vip会员购买记录
     *
     * @param sysPayRecord vip会员购买记录
     * @return 结果
     */
    @Override
    @Transactional
    public int insertSysPayRecord(SysPayRecord sysPayRecord)
    {
        sysPayRecord.setUserId(SecurityUtils.getLoginUser().getUser().getUserId());
        sysPayRecord.setCreateBy(SecurityUtils.getUsername());
        sysPayRecord.setCreateTime(DateUtils.getNowDate());
        userRoleMapper.deleteUserRoleByUserId(SecurityUtils.getLoginUser().getUser().getUserId());
        SysUserRole userRole = new SysUserRole();
        userRole.setRoleId(3l);
        userRole.setUserId(SecurityUtils.getLoginUser().getUser().getUserId());
        List<SysUserRole> list = new ArrayList<>();
        list.add(userRole);
        userRoleMapper.batchUserRole(list);
        return sysPayRecordMapper.insertSysPayRecord(sysPayRecord);
    }

    /**
     * 修改vip会员购买记录
     *
     * @param sysPayRecord vip会员购买记录
     * @return 结果
     */
    @Override
    public int updateSysPayRecord(SysPayRecord sysPayRecord)
    {
        sysPayRecord.setUpdateTime(DateUtils.getNowDate());
        return sysPayRecordMapper.updateSysPayRecord(sysPayRecord);
    }

    /**
     * 批量删除vip会员购买记录
     *
     * @param recordIds 需要删除的vip会员购买记录ID
     * @return 结果
     */
    @Override
    public int deleteSysPayRecordByIds(Integer[] recordIds)
    {
        return sysPayRecordMapper.deleteSysPayRecordByIds(recordIds);
    }

    /**
     * 删除vip会员购买记录信息
     *
     * @param recordId vip会员购买记录ID
     * @return 结果
     */
    @Override
    public int deleteSysPayRecordById(Integer recordId)
    {
        return sysPayRecordMapper.deleteSysPayRecordById(recordId);
    }
}
