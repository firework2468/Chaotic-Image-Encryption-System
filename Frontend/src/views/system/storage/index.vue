<template>
  <div class="app-container">
    <el-form :model="queryParams" ref="queryForm" :inline="true" v-show="showSearch" label-width="68px">
      <el-form-item label="文件名" prop="name">
        <el-input
          v-model="queryParams.name"
          placeholder="请输入文件名"
          clearable
          size="small"
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>

    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          icon="el-icon-plus"
          size="mini"
          @click="handleAdd"
          v-hasPermi="['system:storage:add']"
        >上传</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="success"
          plain
          icon="el-icon-edit"
          size="mini"
          :disabled="single"
          @click="handleUpdate"
          v-hasPermi="['system:storage:edit']"
        >修改</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="danger"
          plain
          icon="el-icon-delete"
          size="mini"
          :disabled="multiple"
          @click="handleDelete"
          v-hasPermi="['system:storage:remove']"
        >删除</el-button>
      </el-col>
      <right-toolbar :showSearch.sync="showSearch" @queryTable="getList"></right-toolbar>
    </el-row>

    <el-table v-loading="loading" :data="storageList" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="ID" align="center" prop="storageId" />
      <el-table-column label="文件名" align="center" prop="name" />
      <el-table-column prop="path" label="预览图">
        <template slot-scope="{row}">
          <el-image
            :src="row.path"
            :preview-src-list="[row.path]"
            fit="contain"
            lazy
            class="el-avatar"
          >
            <div slot="error">
              <i class="el-icon-document" />
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column label="类型" align="center" prop="type" />
      <el-table-column label="审核状态" align="center" prop="status" >
        <template slot-scope="scope">
          <el-tag  v-if="scope.row.status == 'agree'" type="success">通过</el-tag>
          <el-tag  v-else-if="scope.row.status == 'refuse'" type="danger">拒绝</el-tag>
          <el-tag  v-else type="info">待审核</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作人" align="center" prop="createBy" />
      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
            v-hasPermi="['system:storage:edit']"
          >修改</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
            v-hasPermi="['system:storage:remove']"
          >删除</el-button>
          <el-button
            size="mini"
            type="text"
            v-if="scope.row.status == 'agree' && scope.row.encode == 'decrypted'"
            icon="el-icon-lock"
            @click="handleEncrypt(scope.row)"
            v-hasPermi="['system:storage:encrypt']"
          >加密</el-button>
          <el-button
            size="mini"
            type="text"
            v-if="scope.row.status == 'agree' && scope.row.encode == 'encrypted'"
            icon="el-icon-unlock"
            @click="handleDecrypt(scope.row)"
            v-hasPermi="['system:storage:encrypt']"
          >解密</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />

    <!-- 添加或修改本地存储对话框 -->
    <el-dialog :title="title" :visible.sync="open" width="500px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-input v-model="form.status" type="hidden" value="draft" />
        <el-input v-model="form.encode" type="hidden" value="decrypted" />
        <el-form-item label="文件名" prop="name">
          <el-input v-model="form.name" placeholder="请输入文件名" />
        </el-form-item>

        <!--   上传文件   -->
        <el-form-item label="路径">
          <imageUpload v-model="form.path"/>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { listStorage, getStorage, delStorage, addStorage, updateStorage, imgEncrypt, imgDecrypt } from "@/api/system/storage";
import ImageUpload from '@/components/ImageUpload';
export default {
  name: "Storage",
  components: {
    ImageUpload,
  },
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 显示搜索条件
      showSearch: true,
      // 总条数
      total: 0,
      // 本地存储表格数据
      storageList: [],
      // 弹出层标题
      title: "",
      // 是否显示弹出层
      open: false,
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        name: null,
        path: null
      },
      // 表单参数
      form: {},
      // 表单校验
      rules: {
      }
    };
  },
  created() {
    this.getList();
  },
  methods: {
    /** 查询本地存储列表 */
    getList() {
      this.loading = true;
      listStorage(this.queryParams).then(response => {
        this.storageList = response.rows;
        this.total = response.total;
        this.loading = false;
      });
    },
    // 取消按钮
    cancel() {
      this.open = false;
      this.reset();
    },
    // 表单重置
    reset() {
      this.form = {
        storageId: null,
        encryptedPath: null,
        name: null,
        suffix: null,
        path: null,
        type: null,
        size: null,
        createBy: null,
        updateBy: null,
        createTime: null,
        updateTime: null
      };
      this.resetForm("form");
    },
    /** 搜索按钮操作 */
    handleQuery() {
      this.queryParams.pageNum = 1;
      this.getList();
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.resetForm("queryForm");
      this.handleQuery();
    },
    // 多选框选中数据
    handleSelectionChange(selection) {
      this.ids = selection.map(item => item.storageId)
      this.single = selection.length!==1
      this.multiple = !selection.length
    },
    /** 新增按钮操作 */
    handleAdd() {
      this.reset();
      this.open = true;
      this.title = "添加本地存储";
      this.form.status = "draft";
      this.form.encode = "decrypted";
    },
    // 提交上传文件
    submitFileForm() {
      this.$refs.upload.submit();
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      this.reset();
      const storageId = row.storageId || this.ids
      getStorage(storageId).then(response => {
        this.form = response.data;
        this.open = true;
        this.title = "修改本地存储";
      });
    },
    /** 提交按钮 */
    submitForm() {
      this.$refs["form"].validate(valid => {
        if (valid) {
          if (this.form.storageId != null) {
            updateStorage(this.form).then(response => {
              this.msgSuccess("修改成功");
              this.open = false;
              this.getList();
            });
          } else {
            addStorage(this.form).then(response => {
              this.msgSuccess("新增成功");
              this.open = false;
              this.getList();
            });
          }
        }
      });
    },
    /** 删除按钮操作 */
    handleDelete(row) {
      const storageIds = row.storageId || this.ids;
      this.$confirm('是否确认删除本地存储编号为"' + storageIds + '"的数据项?', "警告", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        }).then(function() {
          return delStorage(storageIds);
        }).then(() => {
          this.getList();
          this.msgSuccess("删除成功");
        })
    },
    /** 加密按钮操作 */
    handleEncrypt(row) {
      let storageId = row.storageId
      imgEncrypt(row).then(res=>{
        this.msgSuccess("加密成功");
        this.getList();
      })
    },
    /** 解密按钮操作 */
    handleDecrypt(row) {
      imgDecrypt(row).then(res=>{
        this.msgSuccess("解密成功");
        this.getList();
      })
    }
  }
};
</script>
