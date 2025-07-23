export const auditPlanList = [{
  plan_code: "1",// 方案编号
  plan_name: "A公司“两金”专项审计方案",//方案名称
  project_name: "A公司“两金”专项审计",
  date: "2025-01-01",//编制日期
  source: "",//编制依据
  remark: "",//备注
  items: [{//审计事项树
      item_code: "01",
      item_name: "基本信息核实",
      details: {},
      childs: [{
          item_code: "011",
          item_name: "组织架构",
          details: {
              item_code: "011", //事项编号
              item_name: "组织架构",//事项名称
              method: "查阅公司组织架构图，访谈相关负责人，核实岗位设置与职责分工。",
              source: "《公司法》、企业内部管理制度",
              material: "公司组织架构图、岗位职责说明书"
          },
      },{
          item_code: "012",
          item_name: "管理制度",
          details: {
              item_code: "012", //事项编号
              item_name: "管理制度",//事项名称
              method: "获取并查阅公司主要管理制度文件，检查制度执行情况。",
              source: "《企业内部控制基本规范》及配套指引",
              material: "公司管理制度汇编、制度执行记录"
          },
      }]
  },{
      item_code: "02",
      item_name: "会计科目核实",
      details: {},
      childs: [
        {
            item_code: "021",
            item_name: "应收账款",
            details: {
                item_code: "021", //事项编号
                item_name: "应收账款管理",//事项名称
                method: "抽查应收账款明细，核对合同、发票及回款记录，分析账龄结构。",
                source: "《企业会计准则第14号——收入》",
                material: "应收账款明细表、合同、发票、回款凭证"
            },
        },{
          item_code: "022",
          item_name: "其他应收款",
          details: {
              item_code: "022", //事项编号
              item_name: "应收账款管理",//事项名称
              method: "抽查应收账款明细，核对合同、发票及回款记录，分析账龄结构。",
              source: "《企业会计准则第14号——收入》",
              material: "应收账款明细表、合同、发票、回款凭证"
          },
      },{
        item_code: "023",
        item_name: "预付账款",
        details: {
            item_code: "023", //事项编号
            item_name: "预付账款",//事项名称
            method: "检查预付账款合同、付款凭证，核实预付对象及用途。",
            source: "《企业会计准则第14号——收入》",
            material: "预付账款明细表、合同、付款凭证"
        },
    }]
  },{
      item_code: "03",
      item_name: "业务核实",
      details: {},
      childs: [{
          item_code: "031",
          item_name: "基础标准",
          details: {
              item_code: "031", //事项编号
              item_name: "基础标准",//事项名称
              method: "查阅公司基础管理标准文件，核实标准执行情况。",
              source: "《企业内部控制基本规范》",
              material: "基础标准文件、执行记录"
          },
      },{
          item_code: "032",
          item_name: "信用管理",
          details: {
              item_code: "032", //事项编号
              item_name: "信用管理",//事项名称
              method: "检查客户信用评估资料，分析信用政策执行情况。",
              source: "《企业内部控制应用指引第13号——销售业务》",
              material: "客户信用评估表、信用政策文件"
          },
      },{
          item_code: "033",
          item_name: "销售合同",
          details: {
              item_code: "033", //事项编号
              item_name: "销售合同",//事项名称
              method: "抽查销售合同，核对合同条款与实际业务一致性。",
              source: "《合同法》、企业销售管理制度",
              material: "销售合同文本、合同审批记录"
          },
      },{
          item_code: "034",
          item_name: "销售计划",
          details: {
              item_code: "034", //事项编号
              item_name: "销售计划",//事项名称
              method: "查阅年度及月度销售计划，分析计划完成情况。",
              source: "企业内部管理制度",
              material: "销售计划表、销售完成情况分析报告"
          },
      },{
          item_code: "035",
          item_name: "技术设计",
          details: {
              item_code: "035", //事项编号
              item_name: "技术设计",//事项名称
              method: "抽查技术设计文件，核实设计流程及审批记录。",
              source: "《工程建设标准强制性条文》",
              material: "技术设计文件、设计审批表"
          },
      },{
          item_code: "036",
          item_name: "生产计划",
          details: {
              item_code: "036", //事项编号
              item_name: "生产计划",//事项名称
              method: "查阅生产计划及实际产量数据，分析计划执行偏差。",
              source: "企业生产管理制度",
              material: "生产计划表、产量统计报表"
          },
      },{
          item_code: "037",
          item_name: "材料采购",
          details: {
              item_code: "037", //事项编号
              item_name: "材料采购",//事项名称
              method: "抽查采购合同及发票，核实采购流程合规性。",
              source: "《招标投标法》、企业采购管理制度",
              material: "采购合同、发票、采购审批单"
          },
      }]
  }],
  attach: [{
      filename: "关于A公司“两金”专项审计方案的附件",
      filesize: 111024,
      createor: "张三",
      create_date: "2025-01-01 09:00:00"
  }]
},{
  plan_code: "2",// 方案编号
  plan_name: "B公司两金专项审计方案",//方案名称
  project_name: "B公司环保设施建设项目竣工建设项目审计",
  date: "2025-02-01",//编制日期
  source: "",//编制依据
  remark: "",//备注
  items: [{//审计事项树
      item_code: "01",
      item_name: "基本信息核实",
      details: {},
      childs: [{
          item_code: "011",
          item_name: "组织架构",
          details: {
              item_code: "011", //事项编号
              item_name: "组织架构",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      }]
  },{
      item_code: "02",
      item_name: "会计科目核实",
      details: {},
      childs: [{
            item_code: "021",
            item_name: "应收账款",
            details: {
                item_code: "021", //事项编号
                item_name: "应收账款管理",//事项名称
                method: "抽查应收账款明细，核对合同、发票及回款记录，分析账龄结构。",
                source: "《企业会计准则第14号——收入》",
                material: "应收账款明细表、合同、发票、回款凭证"
            },
        },{
          item_code: "022",
          item_name: "其他应收款",
          details: {
              item_code: "022", //事项编号
              item_name: "应收账款管理",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
        item_code: "023",
        item_name: "预付账款",
        details: {
            item_code: "023", //事项编号
            item_name: "预付账款",//事项名称
            method: "",//审计程序和方法
            source: "",//相关法律法规和监管规定
            material: ""//需提供材料
        },
    }]
  },{
      item_code: "03",
      item_name: "业务核实",
      details: {},
      childs: [{
          item_code: "031",
          item_name: "基础标准",
          details: {
              item_code: "031", //事项编号
              item_name: "基础标准",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "033",
          item_name: "销售合同",
          details: {
              item_code: "033", //事项编号
              item_name: "销售合同",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "034",
          item_name: "销售计划",
          details: {
              item_code: "034", //事项编号
              item_name: "销售计划",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "035",
          item_name: "技术设计",
          details: {
              item_code: "035", //事项编号
              item_name: "技术设计",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "036",
          item_name: "生产计划",
          details: {
              item_code: "036", //事项编号
              item_name: "生产计划",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "037",
          item_name: "材料采购",
          details: {
              item_code: "037", //事项编号
              item_name: "材料采购",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      }]
  }],
  attach: [{
      filename: "关于A公司“两金”专项审计方案的附件",
      filesize: 111024,
      createor: "张三",
      create_date: "2025-02-01 09:00:00"
  }]
},{
  plan_code: "3",// 方案编号
  plan_name: "C公司两金专项审计方案",//方案名称
  project_name: "关于对C公司招投标业务的专项审计",
  date: "2025-03-01",//编制日期
  source: "",//编制依据
  remark: "",//备注
  items: [{//审计事项树
      item_code: "01",
      item_name: "基本信息核实",
      details: {},
      childs: [{
          item_code: "011",
          item_name: "组织架构",
          details: {
              item_code: "011", //事项编号
              item_name: "组织架构",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "012",
          item_name: "管理制度",
          details: {
              item_code: "012", //事项编号
              item_name: "管理制度",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      }]
  },{
      item_code: "02",
      item_name: "会计科目核实",
      details: {},
      childs: [{
            item_code: "021",
            item_name: "应收账款",
            details: {
                item_code: "021", //事项编号
                item_name: "应收账款管理",//事项名称
                method: "抽查应收账款明细，核对合同、发票及回款记录，分析账龄结构。",
                source: "《企业会计准则第14号——收入》",
                material: "应收账款明细表、合同、发票、回款凭证"
            },
        },{
          item_code: "022",
          item_name: "其他应收款",
          details: {
              item_code: "022", //事项编号
              item_name: "应收账款管理",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
        item_code: "023",
        item_name: "预付账款",
        details: {
            item_code: "023", //事项编号
            item_name: "预付账款",//事项名称
            method: "",//审计程序和方法
            source: "",//相关法律法规和监管规定
            material: ""//需提供材料
        },
    }]
  },{
      item_code: "03",
      item_name: "业务核实",
      details: {},
      childs: [{
          item_code: "031",
          item_name: "基础标准",
          details: {
              item_code: "031", //事项编号
              item_name: "基础标准",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "032",
          item_name: "信用管理",
          details: {
              item_code: "032", //事项编号
              item_name: "信用管理",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "033",
          item_name: "销售合同",
          details: {
              item_code: "033", //事项编号
              item_name: "销售合同",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "034",
          item_name: "销售计划",
          details: {
              item_code: "034", //事项编号
              item_name: "销售计划",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      },{
          item_code: "035",
          item_name: "技术设计",
          details: {
              item_code: "035", //事项编号
              item_name: "技术设计",//事项名称
              method: "",//审计程序和方法
              source: "",//相关法律法规和监管规定
              material: ""//需提供材料
          },
      }]
  }],
  attach: [{
      filename: "关于C公司“两金”专项审计方案的附件",
      filesize: 111024,
      createor: "张三",
      create_date: "2025-03-01 09:00:00"
  }]
}]; 