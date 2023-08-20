package com.dna.system.mapper;

import java.util.List;
import com.dna.system.domain.SysLocalStorage;

/**
 * 本地存储Mapper接口
 *
 * @author dna
 * @date 2021-05-15
 */
public interface SysLocalStorageMapper
{
    /**
     * 查询本地存储
     *
     * @param storageId 本地存储ID
     * @return 本地存储
     */
    public SysLocalStorage selectSysLocalStorageById(Long storageId);

    /**
     * 查询本地存储列表
     *
     * @param sysLocalStorage 本地存储
     * @return 本地存储集合
     */
    public List<SysLocalStorage> selectLocalStorageList(SysLocalStorage sysLocalStorage);

    /**
     * 新增本地存储
     *
     * @param sysLocalStorage 本地存储
     * @return 结果
     */
    public int insertSysLocalStorage(SysLocalStorage sysLocalStorage);

    /**
     * 修改本地存储
     *
     * @param sysLocalStorage 本地存储
     * @return 结果
     */
    public int updateSysLocalStorage(SysLocalStorage sysLocalStorage);

    /**
     * 删除本地存储
     *
     * @param storageId 本地存储ID
     * @return 结果
     */
    public int deleteSysLocalStorageById(Long storageId);

    /**
     * 批量删除本地存储
     *
     * @param storageIds 需要删除的数据ID
     * @return 结果
     */
    public int deleteSysLocalStorageByIds(Long[] storageIds);
}
