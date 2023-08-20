<template>
  <div class="app-container">

    <div class="bottom clearfix">
      <span>我的权益： </span>
      <el-tag type="danger">有效期：{{record.expire}}</el-tag>
      <el-tag type="warning" style="margin: auto 25px">使用次数：{{record.number}}次</el-tag>
      <el-tag type="success">价格：{{record.price}}元</el-tag>
    </div>

    <el-table v-loading="loading" :data="recordList">
      <el-table-column label="序号" align="center" prop="recordId" />
      <el-table-column label="用户" align="center" prop="user.userName" />
      <el-table-column label="会员等级" align="center" prop="vip.name" />
      <el-table-column label="购买时间" align="center" prop="createTime" />
    </el-table>

    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />
  </div>
</template>

<script>
import { listRecord, getRecord } from "@/api/system/record";

export default {
  name: "Record",
  components: {
  },
  data() {
    return {
      // 遮罩层
      loading: true,
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        name: null,
        path: null
      },
      // 总条数
      total: 0,
      // vip会员购买记录表格数据
      recordList: [],
      record:{}
    };
  },
  created() {
    this.getList();
  },
  methods: {
    /** 查询vip会员购买记录列表 */
    getList() {
      this.loading = true;
      listRecord(this.queryParams).then(response => {
        this.loading = false;
        this.record = response.rows[0].vip;
        this.recordList = response.rows;
        this.total = response.total;
      });
    },
  }
};
</script>
