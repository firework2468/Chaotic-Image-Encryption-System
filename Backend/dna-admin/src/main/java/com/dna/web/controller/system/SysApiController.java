package com.dna.web.controller.system;

import com.dna.system.domain.SysNews;
import com.dna.system.domain.SysVip;
import com.dna.system.service.ISysNewsService;
import com.dna.common.core.controller.BaseController;
import com.dna.common.core.page.TableDataInfo;
import com.dna.system.service.ISysVipService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @author ：miracle.cui
 * @description：TODO
 * @date ：2021/5/17 12:52
 */
@RestController
@RequestMapping("/portal/api")
public class SysApiController extends BaseController {

    @Autowired
    private ISysNewsService newsService;
    @Autowired
    private ISysVipService vipService;

    @GetMapping("/news")
    public TableDataInfo getNewsList(){
        startPage();
        List<SysNews> list = newsService.selectSysNewsList(new SysNews());
        return getDataTable(list);
    }
    @GetMapping("/vip")
    public List<SysVip> getVipList(){
        List<SysVip> list = vipService.selectSysVipList(new SysVip());
        return list;
    }

}
