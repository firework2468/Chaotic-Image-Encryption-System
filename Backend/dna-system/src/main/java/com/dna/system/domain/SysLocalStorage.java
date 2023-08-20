package com.dna.system.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.dna.common.annotation.Excel;
import com.dna.common.core.domain.BaseEntity;

/**
 * 本地存储对象 sys_local_storage
 *
 * @author dna
 * @date 2021-05-23
 */
public class SysLocalStorage extends BaseEntity {
    private static final long serialVersionUID = 1L;

    /**
     * ID
     */
    private Long storageId;

    /**
     * 加密状态
     */
    @Excel(name = "加密状态")
    private String encode;

    /**
     * 文件名
     */
    @Excel(name = "文件名")
    private String name;

    /**
     * 加密后路径
     */
    @Excel(name = "加密后路径")
    private String encryptedPath;

    /**
     * 路径
     */
    @Excel(name = "路径")
    private String path;

    /**
     * 类型
     */
    @Excel(name = "类型")
    private String type;

    /**
     * 审核状态
     */
    @Excel(name = "审核状态")
    private String status;

    /**
     * 存储名称
     */
    @Excel(name = "存储名称")
    private String localName;

    /**
     * 密钥
     */
    @Excel(name = "密钥")
    private String keyValue;

    private String filePath;


    public void setStorageId(Long storageId) {
        this.storageId = storageId;
    }

    public Long getStorageId() {
        return storageId;
    }

    public void setEncode(String encode) {
        this.encode = encode;
    }

    public String getEncode() {
        return encode;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setEncryptedPath(String encryptedPath) {
        this.encryptedPath = encryptedPath;
    }

    public String getEncryptedPath() {
        return encryptedPath;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public String getPath() {
        return path;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getStatus() {
        return status;
    }

    public void setLocalName(String localName) {
        this.localName = localName;
    }

    public String getLocalName() {
        return localName;
    }

    public void setKeyValue(String keyValue) {
        this.keyValue = keyValue;
    }

    public String getKeyValue() {
        return keyValue;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this, ToStringStyle.MULTI_LINE_STYLE)
                .append("storageId", getStorageId())
                .append("encode", getEncode())
                .append("name", getName())
                .append("encryptedPath", getEncryptedPath())
                .append("path", getPath())
                .append("type", getType())
                .append("status", getStatus())
                .append("createBy", getCreateBy())
                .append("updateBy", getUpdateBy())
                .append("createTime", getCreateTime())
                .append("updateTime", getUpdateTime())
                .append("localName", getLocalName())
                .append("keyValue", getKeyValue())
                .append("filePath", getFilePath())
                .toString();
    }
}