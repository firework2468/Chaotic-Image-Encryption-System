<template>
  <el-row :gutter="20">
    <el-col :sm="24" :lg="24">
      <el-menu
        :default-active="'1'"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        @select="handleSelect"
        active-text-color="#ffd04b">
        <h3 class="title" style="float: left">基于DNA编码的混沌图像加密系统</h3>
        <el-menu-item index="1" >首页</el-menu-item>
        <el-submenu index="2">
          <template slot="title">会员管理</template>
          <el-menu-item index="2-1">购买会员套餐</el-menu-item>
          <el-menu-item index="2-2">查看购买记录</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">图像管理</template>
          <el-menu-item index="3-1">上传图片</el-menu-item>
          <el-menu-item index="3-2">图片列表</el-menu-item>
          <el-menu-item index="3-3">查看操作历史</el-menu-item>
        </el-submenu>
        <el-submenu v-if="token !== undefined"  style="float: right">
          <template slot="title">{{user.userName}}</template>
          <el-menu-item><router-link to="/user/profile">个人中心</router-link></el-menu-item>
          <el-menu-item @click.native="logout">退出登录</el-menu-item>
        </el-submenu>
        <el-menu-item style="float: right" v-if="token === undefined">
          <el-button type="text"><router-link to="/register">注册</router-link></el-button>
          <el-button type="text"><router-link to="/login">登录</router-link></el-button>
        </el-menu-item>
      </el-menu>
    </el-col>

    <el-col :sm="24" :lg="24" v-if="active == '1'">
      <el-col>
        <el-carousel :interval="4000" type="card" height="300px">
          <el-carousel-item >
            <el-image src="/static/img/1.png"></el-image>
            <h3 class="medium"></h3>
          </el-carousel-item>
          <el-carousel-item >
            <el-image src="/static/img/2.png"></el-image>
            <h3 class="medium"></h3>
          </el-carousel-item>
          <el-carousel-item >
            <el-image src="/static/img/banner.jpg"></el-image>
            <h3 class="medium"></h3>
          </el-carousel-item>
          <el-carousel-item >
            <el-image src="/static/img/3.png"></el-image>
            <h3 class="medium"></h3>
          </el-carousel-item>
          <el-carousel-item >
            <el-image src="/static/img/4.png"></el-image>
            <h3 class="medium"></h3>
          </el-carousel-item>
        </el-carousel>
      </el-col>
      <el-col>
        <el-table v-loading="loading" :data="newsList"
                  :show-header="false" style="margin-top: 25px"
                  @click="newsDetail">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <span v-html='props.row.newsContent'></span>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column label="角色编号" prop="newsId" />
          <el-table-column label="新闻标题" prop="newsTitle" :show-overflow-tooltip="true"  />
          <el-table-column label="作者" prop="author" :show-overflow-tooltip="true"  />
          <el-table-column label="发布时间" prop="createTime" :show-overflow-tooltip="true"  />
        </el-table>

        <pagination
          v-show="total>0"
          :total="total"
          :page.sync="queryParams.pageNum"
          :limit.sync="queryParams.pageSize"
          @pagination="getNewsList"
        />

      </el-col>
    </el-col>
    <el-col :sm="24" :lg="24" v-if="active == '2-1'" style="margin-top:150px">
      <el-col :span="6" :offset="1" v-for="vip in vipList">
        <el-card shadow="hover">
          <div style="padding: 0 14px;">
            <div class="bottom clearfix">
              <el-tag type="danger">有效期：{{vip.expire}}</el-tag><br>
              <el-tag type="warning" style="">使用次数：{{vip.number}}次</el-tag><br>
              <el-tag type="success">价格：{{vip.price}}元</el-tag>
              <el-tag type="success">价格：{{vip.price}}元</el-tag>
            </div>
            <div class="bottom clearfix">
              <span>{{vip.name}}</span>
              <el-button type="text" class="button" @click="pay(vip)">点击购买</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-col>

    <el-col :sm="24" :lg="24" v-if="active == '2-2'">
      <record></record>
    </el-col>

    <el-col :sm="24" :lg="24" v-if="active == '3-1'">
      <images></images>
    </el-col>
    <el-col :sm="24" :lg="24" v-if="active == '3-2'">
      <report></report>
    </el-col>
    <el-col :sm="24" :lg="24" v-if="active == '3-3'">
      <operLog></operLog>
    </el-col>
  </el-row>
</template>

<script>
  import { listVip, listMenu } from "@/api/portal/api";
  import {addRecord} from "@/api/system/record";
  import images from "../system/storage/index";
  import report from "../system/storage/report";
  import record from "../system/record/index";
  import operLog from "../monitor/operlog/index";
  import { getToken } from "@/utils/auth";

export default {
  name: "index",
  components: { images, report, record, operLog },
  data() {
    return {
      // 遮罩层
      loading: true,
      newsList:null,
      vipList: null,
      active:"1",
      // 总条数
      total: 0,
      token: undefined,
      user: {},
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10
      },
    };
  },
  created() {
    this.getNewsList()
    this.getInfo()
    this.getVipList()
  },
  methods: {
    getNewsList(){
      listMenu().then(response => {
        this.newsList = response.rows;
        this.total = response.total;
        this.loading = false;
      })
    },
    newsDetail(){
      console.log(1111)
      window.open(href, "_blank");
    },
    getVipList(){
      listVip().then(response => {
        this.vipList = response
      })
    },
    handleSelect(key, keyPath) {
      this.active = key;
    },
    pay(vip){
      addRecord({vipId:vip.vipId}).then(response => {
        if (response.code == 200)
          this.msgSuccess("购买成功");
      });
    },
    async logout() {
      this.$confirm('确定注销并退出系统吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$store.dispatch('LogOut').then(() => {
          location.href = '/portal/index';
        })
      })
    },
    getInfo(){
      this.token = getToken()
      if (this.token !== undefined){

        this.$store.dispatch("GetInfo", this.registerForm).then(res => {
          this.user = res.user;
        }).catch(() => {
          this.loading = false;
        });
      }
    }
  },
};
</script>

<style scoped lang="scss">
  .title {
  margin: 0px auto 0px auto 10px auto;
  color: white;
  }

  .el-carousel__item h3 {
    margin-top:50px;
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    bottom: 0;
    margin: 0;
    padding: 15px;
    position: absolute;
    width: 100%;
    background: #0003;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;

  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;

  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
</style>

