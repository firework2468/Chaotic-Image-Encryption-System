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
          plain
          size="mini"
          :disabled="single"
          @click="handle"
          v-hasPermi="['system:storage:report']"
        >加密结果</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          size="mini"
          :disabled="single"
          @click="handlez"
          v-hasPermi="['system:storage:report']"
        >直方图</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="success"
          plain
          size="mini"
          :disabled="single"
          @click="handlex"
          v-hasPermi="['system:storage:report']"
        >相邻相关性像素分析</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="info"
          plain
          size="mini"
          :disabled="single"
          @click="handles"
          v-hasPermi="['system:storage:report']"
        >信息熵分析</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="warning"
          plain
          size="mini"
          :disabled="single"
          @click="handlem"
          v-hasPermi="['system:storage:report']"
        >密钥敏感性</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="danger"
          plain
          size="mini"
          :disabled="single"
          @click="handlec"
          v-hasPermi="['system:storage:report']"
        >差分攻击分析</el-button>
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
    </el-table>

    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />

    <!-- 添加或修改本地存储对话框 -->
    <el-dialog :title="title" :visible.sync="open" width="900px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-form-item v-if="show == 'encryptRes'">
          <el-col :span="12">
            <el-image :src="form.encrypt" ></el-image>
          </el-col>
          <el-table v-loading="loading" :data="form.key">
            <el-table>
              <el-table-column label="" align="center" prop="name"/>
              <el-table-column label="x0" align="center" prop="x0"/>
              <el-table-column label="x1" align="center" prop="x1"/>
              <el-table-column label="x2" align="center" prop="x2"/>
              <el-table-column label="X0" align="center" prop="X0"/>
              <el-table-column label="Y0" align="center" prop="Y0"/>
              <el-table-column label="Z0" align="center" prop="Z0"/>
              <el-table-column label="WO" align="center" prop="WO"/>
              <el-table-column label="size" align="center" prop="size"/>
            </el-table>
          </el-table>
        </el-form-item>


        <el-form-item v-if="show == 'zanalysis'">
          <el-col :span="12">
            <el-image :src="form.r1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.r2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'zanalysis'">
          <el-col :span="12">
            <el-image :src="form.g1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.g2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'zanalysis'">
          <el-col :span="12">
            <el-image :src="form.b1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.b2"></el-image>
          </el-col>
        </el-form-item>


        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.hor_R1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.hor_R2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.hor_G1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.hor_G2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.hor_B1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.hor_B2"></el-image>
          </el-col>
        </el-form-item>

        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.ver_R1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.ver_R2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.ver_G1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.ver_G2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.ver_B1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.ver_B2"></el-image>
          </el-col>
        </el-form-item>

        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.dia_R1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.dia_R2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.dia_G1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.dia_G2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'xanalysis'">
          <el-col :span="12">
            <el-image :src="form.dia_B1"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.dia_B2"></el-image>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'xanalysis'">

          <el-col :span="12">
            <el-table v-loading="loading" :data="form.result1">
              <el-table-column label="名称" align="center" prop="name" />
              <el-table-column label="R" align="center" prop="R" />
              <el-table-column label="G" align="center" prop="G" />
              <el-table-column label="B" align="center" prop="B" />
            </el-table>
          </el-col>
          <el-col :span="12">
            <el-table v-loading="loading" :data="form.result2">
              <el-table-column label="名称" align="center" prop="name" />
              <el-table-column label="R" align="center" prop="R" />
              <el-table-column label="G" align="center" prop="G" />
              <el-table-column label="B" align="center" prop="B" />
            </el-table>
          </el-col>
        </el-form-item>
        <el-form-item v-if="show == 'sanalysis'">
          <el-table v-loading="loading" :data="form.result">
            <el-table-column label="名称" align="center" prop="name" />
            <el-table-column label="R" align="center" prop="R" />
            <el-table-column label="G" align="center" prop="G" />
            <el-table-column label="B" align="center" prop="B" />
          </el-table>
        </el-form-item>

        <el-form-item v-if="show == 'manalysis'">
          <el-col :span="12">
            <el-image :src="form.decrypt"></el-image>
          </el-col>
          <el-col :span="12">
            <el-image :src="form.encrypt"></el-image>
          </el-col>
        </el-form-item>

        <el-form-item v-if="show == 'canalysis'">
          <el-col :span="24">
            <el-table v-loading="loading" :data="form.result">
              <el-table-column label="名称" align="center" prop="name" />
              <el-table-column label="R" align="center" prop="R" />
              <el-table-column label="G" align="center" prop="G" />
              <el-table-column label="B" align="center" prop="B" />
            </el-table>
          </el-col>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import { listStorage, zanalysis, xanalysis, sanalysis, manalysis, canalysis, encryptRes} from "@/api/system/storage";
import ImageUpload from '@/components/ImageUpload';
export default {
  name: "Report",
  components: {
    ImageUpload,
  },
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      rows: [],
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
      show: null,
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
      this.zanalysis = false
      this.xanalysis = false
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
      this.rows = selection
    },
    /** 加密结果 */
    handle(row) {
      encryptRes(this.rows[0]).then(response => {
        this.open = true;
        this.show = "encryptRes";
        this.form = response.data;
        this.title = "加密结果";
      });
    },
    /** 直方图分析 */
    handlez(row) {
      zanalysis(this.rows[0]).then(response => {
        this.open = true;
        this.show = "zanalysis";
        this.form = response.data;
        this.title = "直方图分析";
      });
    },
    /** 相邻相关性像素分析 */
    handlex(row) {
      xanalysis(this.rows[0]).then(response => {
        this.open = true;
        this.show = "xanalysis";
        this.form = response.data;
        console.log(response.data)
        this.title = "相邻相关性像素分析";
      });
    },
    /** 密钥敏感性 */
    handlem(row) {
      manalysis(this.rows[0]).then(response => {
        this.form ={}
        this.open = true;
        this.show = "manalysis";
        this.form = response.data;
        this.title = "密钥敏感性";
      });
    },
    /** 信息熵分析 */
    handles(row) {
      sanalysis(this.rows[0]).then(response => {
        this.form ={}
        this.open = true;
        this.show = "sanalysis";
        this.form = response.data;
        this.title = "信息熵分析";
      });
    },
    /** 差分攻击分析 */
    handlec(row) {
      canalysis(this.rows[0]).then(response => {
        this.form ={}
        this.open = true;
        this.show = "canalysis";
        this.form = response.data;
        console.log(this.form)
        this.title = "差分攻击分析";
      });
    }
  }
};
</script>
