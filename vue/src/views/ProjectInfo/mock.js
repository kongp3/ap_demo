// 审计机构数据字典 - 提取自projectList中的organization属性
export const organizationOptions = [
  { label: '集团审计部', value: '集团审计部' },
  { label: 'A公司审计部', value: 'A公司审计部' },
  { label: 'B公司审计部', value: 'B公司审计部' },
  { label: 'C公司审计部', value: 'C公司审计部' },
  { label: 'D公司审计部', value: 'D公司审计部' },
  { label: 'E公司审计部', value: 'E公司审计部' },
  { label: 'F公司审计部', value: 'F公司审计部' },
  { label: 'G公司审计部', value: 'G公司审计部' },
  { label: 'H公司审计部', value: 'H公司审计部' },
  { label: 'J公司审计部', value: 'J公司审计部' }
]

// 获取所有审计机构（去重）
export const getAllOrganizations = () => {
  const organizations = [...new Set(projectList.map(item => item.organization))]
  return organizations.map(org => ({ label: org, value: org }))
}

export const projectList =[
    {
      project_code: "202520001124JZ008",
      project_name: "A公司“两金”专项审计",
      state: "进行中",
      year: "2025",
      leader: "张三",
      type: "专项审计",
      organization: "集团审计部",
      start_date: "2025-06-09",
      end_date: "",
      audit_unit: "A公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ007",
      project_name: "关于对A公司总经理李某明同志任期经济责任暨经营管理状况审计",
      state: "已完成",
      year: "2024",
      leader: "张三",
      type: "专项审计",
      organization: "集团审计部",
      start_date: "2024-07-09",
      end_date: "2024-09-20",
      audit_unit: "A公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ009",
      project_name: "B公司环保设施建设项目竣工建设项目审计",
      state: "进行中",
      year: "2025",
      leader: "李四",
      type: "建设项目审计",
      organization: "集团审计部",
      start_date: "2025-07-09",
      end_date: "",
      audit_unit: "B公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ010",
      project_name: "关于对C公司招投标业务的专项审计",
      state: "已完成",
      year: "2024",
      leader: "王五",
      type: "专项审计",
      organization: "集团审计部",
      start_date: "2024-07-09",
      end_date: "2024-10-20",
      audit_unit: "A公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ011",
      project_name: "D公司内部内部控制审计",
      state: "已取消",
      year: "2025",
      leader: "张三",
      type: "内部控制审计",
      organization: "集团审计部",
      start_date: "2025-06-09",
      end_date: "",
      audit_unit: "D公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ012",
      project_name: "关于对B公司招投标业务的专项审计",
      state: "已完成",
      year: "2025",
      leader: "王五",
      type: "专项审计",
      organization: "集团审计部",
      start_date: "2025-03-09",
      end_date: "2025-06-20",
      audit_unit: "B公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ013",
      project_name: "关于对A公司招投标业务的专项审计",
      state: "已完成",
      year: "2025",
      leader: "王五",
      type: "专项审计",
      organization: "集团审计部",
      start_date: "2025-05-09",
      end_date: "2025-06-21",
      audit_unit: "A公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ014",
      project_name: "C公司环保设施建设项目竣工建设项目审计",
      state: "已取消",
      year: "2025",
      leader: "李四",
      type: "建设项目审计",
      organization: "集团审计部",
      start_date: "2024-07-09",
      end_date: "",
      audit_unit: "C公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ015",
      project_name: "F公司环保设施建设项目竣工建设项目审计",
      state: "已完成",
      year: "2024",
      leader: "李四",
      type: "专项审计",
      organization: "集团审计部",
      start_date: "2024-03-09",
      end_date: "2024-06-20",
      audit_unit: "F公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ016",
      project_name: "F公司内部内部控制审计",
      state: "进行中",
      year: "2025",
      leader: "王五",
      type: "内部控制审计",
      organization: "集团审计部",
      start_date: "2025-07-12",
      end_date: "",
      audit_unit: "F公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ017",
      project_name: "D公司内部内部控制审计",
      state: "已完成",
      year: "2024",
      leader: "张三",
      type: "内部控制审计",
      organization: "集团审计部",
      start_date: "2024-07-09",
      end_date: "2024-09-20",
      audit_unit: "D公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ018",
      project_name: "G公司内部内部控制审计",
      state: "已完成",
      year: "2025",
      leader: "张三",
      type: "专项审计",
      organization: "集团审计部",
      start_date: "2024-02-09",
      end_date: "2025-06-20",
      audit_unit: "G公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ019",
      project_name: "H公司内部内部控制审计",
      state: "已完成",
      year: "2024",
      leader: "张三",
      type: "内部控制审计",
      organization: "集团审计部",
      start_date: "2024-07-09",
      end_date: "2024-09-20",
      audit_unit: "H公司",
      remark: ""
    },
    {
      project_code: "202520001124JZ020",
      project_name: "J公司内部内部控制审计",
      state: "已完成",
      year: "2025",
      leader: "张三",
      type: "内部控制审计",
      organization: "集团审计部",
      start_date: "2025-01-09",
      end_date: "2025-06-20",
      audit_unit: "J公司",
      remark: ""
    }
  ]