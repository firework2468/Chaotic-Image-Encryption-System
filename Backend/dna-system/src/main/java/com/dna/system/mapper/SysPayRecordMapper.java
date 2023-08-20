package com.dna.system.mapper;

import java.util.List;
import com.dna.system.domain.SysPayRecord;

/**
 * vip会员购买记录Mapper接口
 * 
 * @author dna
 * @date 2021-05-22
 */
public interface SysPayRecordMapper 
{
    /**
     * 查询vip会员购买记录
     * 
     * @param recordId vip会员购买记录ID
     * @return vip会员购买记录
     */
    public SysPayRecord selectSysPayRecordById(Integer recordId);

    /**
     * 查询vip会员购买记录列表
     * 
     * @param sysPayRecord vip会员购买记录
     * @return vip会员购买记录集合
     */
    public List<SysPayRecord> selectSysPayRecordList(SysPayRecord sysPayRecord);

    /**
     * 新增vip会员购买记录
     * 
     * @param sysPayRecord vip会员购买记录
     * @return 结果
     */
    public int insertSysPayRecord(SysPayRecord sysPayRecord);

    /**
     * 修改vip会员购买记录
     * 
     * @param sysPayRecord vip会员购买记录
     * @return 结果
     */
    public int updateSysPayRecord(SysPayRecord sysPayRecord);

    /**
     * 删除vip会员购买记录
     * 
     * @param recordId vip会员购买记录ID
     * @return 结果
     */
    public int deleteSysPayRecordById(Integer recordId);

    /**
     * 批量删除vip会员购买记录
     * 
     * @param recordIds 需要删除的数据ID
     * @return 结果
     */
    public int deleteSysPayRecordByIds(Integer[] recordIds);
}
