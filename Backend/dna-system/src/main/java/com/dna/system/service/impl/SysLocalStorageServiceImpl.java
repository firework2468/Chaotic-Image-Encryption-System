package com.dna.system.service.impl;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.List;

import com.dna.common.config.DnaConfig;
import com.dna.common.utils.DateUtils;
import com.dna.common.utils.SecurityUtils;
import com.dna.common.utils.file.FileUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.dna.system.mapper.SysLocalStorageMapper;
import com.dna.system.domain.SysLocalStorage;
import com.dna.system.service.ISysLocalStorageService;

import javax.annotation.Resource;

/**
 * 本地存储Service业务层处理
 *
 * @author dna
 * @date 2021-05-15
 */
@Service
public class SysLocalStorageServiceImpl implements ISysLocalStorageService
{
    @Resource
    private SysLocalStorageMapper sysLocalStorageMapper;

    /**
     * 查询本地存储
     *
     * @param storageId 本地存储ID
     * @return 本地存储
     */
    @Override
    public SysLocalStorage selectSysLocalStorageById(Long storageId)
    {
        SysLocalStorage sysLocalStorage = sysLocalStorageMapper.selectSysLocalStorageById(storageId);
        sysLocalStorage.setFilePath(DnaConfig.getUploadPath() + sysLocalStorage.getPath().replace("http://localhost:8080/profile/upload", ""));
        return sysLocalStorage;
    }

    /**
     * 查询本地存储列表
     *
     * @param sysLocalStorage 本地存储
     * @return 本地存储
     */
    @Override
    public List<SysLocalStorage> selectLocalStorageList(SysLocalStorage sysLocalStorage)
    {
        return sysLocalStorageMapper.selectLocalStorageList(sysLocalStorage);
    }

    /**
     * 新增本地存储
     *
     * @param sysLocalStorage 本地存储
     * @return 结果
     */
    @Override
    public int insertSysLocalStorage(SysLocalStorage sysLocalStorage) {
        String path = sysLocalStorage.getPath();
        sysLocalStorage.setType(path.split("\\.")[path.split("\\.").length-1]);
        sysLocalStorage.setLocalName(path.replace("*/", ""));

        sysLocalStorage.setCreateBy(SecurityUtils.getUsername());
        sysLocalStorage.setCreateTime(DateUtils.getNowDate());

        return sysLocalStorageMapper.insertSysLocalStorage(sysLocalStorage);
    }

    /**
     * 修改本地存储
     *
     * @param sysLocalStorage 本地存储
     * @return 结果
     */
    @Override
    public int updateSysLocalStorage(SysLocalStorage sysLocalStorage)
    {
        sysLocalStorage.setUpdateTime(DateUtils.getNowDate());
        return sysLocalStorageMapper.updateSysLocalStorage(sysLocalStorage);
    }

    /**
     * 批量删除本地存储
     *
     * @param storageIds 需要删除的本地存储ID
     * @return 结果
     */
    @Override
    public int deleteSysLocalStorageByIds(Long[] storageIds)
    {
        return sysLocalStorageMapper.deleteSysLocalStorageByIds(storageIds);
    }

    /**
     * 删除本地存储信息
     *
     * @param storageId 本地存储ID
     * @return 结果
     */
    @Override
    public int deleteSysLocalStorageById(Long storageId)
    {
        return sysLocalStorageMapper.deleteSysLocalStorageById(storageId);
    }
}
