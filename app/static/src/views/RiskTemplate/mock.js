// 风险模版数据 - 基于audit_pioneer_rule表结构
export const riskTemplateData = [
  {id: 1, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "paid_in_capital_ratio", desc: "实缴资本占比", level: ">=0.5", score: 0, weight: 0.4},
  {id: 2, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "paid_in_capital_ratio", desc: "实缴资本占比", level: ">=0.3且<0.5", score: 2, weight: 0.4},
  {id: 3, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "paid_in_capital_ratio", desc: "实缴资本占比", level: "<0.3", score: 4, weight: 0.4},
  {id: 4, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: "0", score: 0, weight: 0.4},
  {id: 5, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: "<0.5", score: 0, weight: 0.4},
  {id: 6, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: ">=0.5且<0.7", score: 2, weight: 0.4},
  {id: 7, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: ">=0.7", score: 4, weight: 0.4},
  {id: 8, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "establishment_years", desc: "成立年限", level: ">=1", score: 0, weight: 0.4},
  {id: 9, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "establishment_years", desc: "成立年限", level: "<1", score: 1, weight: 0.4},
  {id: 10, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "operation_expiry_years", desc: "经营到期年限", level: ">=1", score: 0, weight: 0.4},
  {id: 11, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "企业资质", index: "operation_expiry_years", desc: "经营到期年限", level: "<1", score: 1, weight: 0.4},
  {id: 12, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "defendant_cases", desc: "作为被告的案件数", level: "<2", score: 0, weight: 0.4},
  {id: 13, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "defendant_cases", desc: "作为被告的案件数", level: ">=2且<=4", score: 2, weight: 0.4},
  {id: 14, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "defendant_cases", desc: "作为被告的案件数", level: ">=4", score: 4, weight: 0.4},
  {id: 15, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "lose_cases", desc: "败诉案件数", level: "0", score: 0, weight: 0.4},
  {id: 16, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "lose_cases", desc: "败诉案件数", level: "1", score: 2, weight: 0.4},
  {id: 17, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "lose_cases", desc: "败诉案件数", level: ">=2", score: 4, weight: 0.4},
  {id: 18, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "0", score: 0, weight: 0.4},
  {id: 19, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "1", score: 1, weight: 0.4},
  {id: 20, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "2", score: 2, weight: 0.4},
  {id: 21, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "3", score: 3, weight: 0.4},
  {id: 22, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: ">=4", score: 4, weight: 0.4},
  {id: 23, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_ratio", desc: "被执行比例", level: ">=0.7", score: 2, weight: 0.4},
  {id: 24, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_ratio", desc: "被执行比例", level: ">=0.5且<0.7", score: 1, weight: 0.4},
  {id: 25, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "enforcement_ratio", desc: "被执行比例", level: "<0.5", score: 0, weight: 0.4},
  {id: 26, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "penalty_abnormal_count", desc: "行政处罚与经营异常次数", level: "0", score: 0, weight: 0.4},
  {id: 27, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "penalty_abnormal_count", desc: "行政处罚与经营异常次数", level: "1", score: 0, weight: 0.4},
  {id: 28, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "合规经营", index: "penalty_abnormal_count", desc: "行政处罚与经营异常次数", level: ">=2", score: 2, weight: 0.4},
  {id: 29, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "asset_liability_ratio", desc: "资产负债率", level: ">=0.7", score: 1, weight: 0.4},
  {id: 30, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "asset_liability_ratio", desc: "资产负债率", level: "＜0.7", score: 0, weight: 0.4},
  {id: 31, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "negative_cash_flow_years", desc: "经营净现金流连续为负年数", level: "1", score: 0, weight: 0.4},
  {id: 32, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "negative_cash_flow_years", desc: "经营净现金流连续为负年数", level: ">=2", score: 1, weight: 0.4},
  {id: 33, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "ar_turnover_decline_years", desc: "应收账款周转率同比下降年数", level: "1", score: 0, weight: 0.4},
  {id: 34, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "ar_turnover_decline_years", desc: "应收账款周转率同比下降年数", level: ">=2", score: 1, weight: 0.4},
  {id: 35, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "branch_cancellation_ratio", desc: "分支机构注销比例", level: "<0.5", score: 0, weight: 0.4},
  {id: 36, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "branch_cancellation_ratio", desc: "分支机构注销比例", level: ">=0.5且<0.7", score: 2, weight: 0.4},
  {id: 37, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "branch_cancellation_ratio", desc: "分支机构注销比例", level: ">=0.7", score: 4, weight: 0.4},
  {id: 38, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "main_business_change_count", desc: "主营业务方向变更次数", level: "＞=1", score: 2, weight: 0.4},
  {id: 39, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "main_business_change_count", desc: "主营业务方向变更次数", level: "＜1", score: 0, weight: 0.4},
  {id: 40, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "excess_pledge", desc: "超额抵质押", level: "＞=0", score: 2, weight: 0.4},
  {id: 41, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "财务健康", index: "excess_pledge", desc: "超额抵质押", level: "＜0", score: 0, weight: 0.4},
  {id: 42, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "0", score: 0, weight: 0.4},
  {id: 43, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "1", score: 1, weight: 0.4},
  {id: 44, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "2", score: 2, weight: 0.4},
  {id: 45, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "3", score: 3, weight: 0.4},
  {id: 46, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "4", score: 4, weight: 0.4},
  {id: 47, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0且<=0.1", score: 2, weight: 0.2},
  {id: 48, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.1且<=0.2", score: 4, weight: 0.2},
  {id: 49, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.2且<=0.3", score: 6, weight: 0.2},
  {id: 50, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.3且<=0.5", score: 8, weight: 0.2},
  {id: 51, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.5", score: 10, weight: 0.2},
  {id: 52, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "5", score: 5, weight: 0.4},
  {id: 53, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "6", score: 6, weight: 0.4},
  {id: 54, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "7", score: 7, weight: 0.4},
  {id: 55, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "8", score: 8, weight: 0.4},
  {id: 56, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "9", score: 9, weight: 0.4},
  {id: 57, model_id: 20250715001, model_name: "综合风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "10", score: 10, weight: 0.4},
  {id: 58, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "paid_in_capital_ratio", desc: "实缴资本占比", level: ">=0.5", score: 0, weight: 0.4},
  {id: 59, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "paid_in_capital_ratio", desc: "实缴资本占比", level: ">=0.3且<0.5", score: 2, weight: 0.4},
  {id: 60, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "paid_in_capital_ratio", desc: "实缴资本占比", level: "<0.3", score: 4, weight: 0.4},
  {id: 61, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: "0", score: 0, weight: 0.4},
  {id: 62, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: "<0.5", score: 0, weight: 0.4},
  {id: 63, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: ">=0.5且<0.7", score: 2, weight: 0.4},
  {id: 64, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "capital_reduction_ratio", desc: "减资比例", level: ">=0.7", score: 4, weight: 0.4},
  {id: 65, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "establishment_years", desc: "成立年限", level: ">=1", score: 0, weight: 0.4},
  {id: 66, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "establishment_years", desc: "成立年限", level: "<1", score: 1, weight: 0.4},
  {id: 67, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "operation_expiry_years", desc: "经营到期年限", level: ">=1", score: 0, weight: 0.4},
  {id: 68, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "企业资质", index: "operation_expiry_years", desc: "经营到期年限", level: "<1", score: 1, weight: 0.4},
  {id: 69, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "defendant_cases", desc: "作为被告的案件数", level: "<2", score: 0, weight: 0.4},
  {id: 70, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "defendant_cases", desc: "作为被告的案件数", level: ">=2且<=4", score: 2, weight: 0.4},
  {id: 71, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "defendant_cases", desc: "作为被告的案件数", level: ">=4", score: 4, weight: 0.4},
  {id: 72, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "lose_cases", desc: "败诉案件数", level: "0", score: 0, weight: 0.4},
  {id: 73, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "lose_cases", desc: "败诉案件数", level: "1", score: 2, weight: 0.4},
  {id: 74, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "lose_cases", desc: "败诉案件数", level: ">=2", score: 4, weight: 0.4},
  {id: 75, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "0", score: 0, weight: 0.4},
  {id: 76, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "1", score: 1, weight: 0.4},
  {id: 77, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "2", score: 2, weight: 0.4},
  {id: 78, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: "3", score: 3, weight: 0.4},
  {id: 79, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_count", desc: "被执行次数", level: ">=4", score: 4, weight: 0.4},
  {id: 80, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_ratio", desc: "被执行比例", level: ">=0.7", score: 2, weight: 0.4},
  {id: 81, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_ratio", desc: "被执行比例", level: ">=0.5且<0.7", score: 1, weight: 0.4},
  {id: 82, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "enforcement_ratio", desc: "被执行比例", level: "<0.5", score: 0, weight: 0.4},
  {id: 83, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "penalty_abnormal_count", desc: "行政处罚与经营异常次数", level: "0", score: 0, weight: 0.4},
  {id: 84, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "penalty_abnormal_count", desc: "行政处罚与经营异常次数", level: "1", score: 0, weight: 0.4},
  {id: 85, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "合规经营", index: "penalty_abnormal_count", desc: "行政处罚与经营异常次数", level: ">=2", score: 2, weight: 0.4},
  {id: 86, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "asset_liability_ratio", desc: "资产负债率", level: ">=0.7", score: 1, weight: 0.4},
  {id: 87, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "asset_liability_ratio", desc: "资产负债率", level: "＜0.7", score: 0, weight: 0.4},
  {id: 88, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "negative_cash_flow_years", desc: "经营净现金流连续为负年数", level: "1", score: 0, weight: 0.4},
  {id: 89, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "negative_cash_flow_years", desc: "经营净现金流连续为负年数", level: ">=2", score: 1, weight: 0.4},
  {id: 90, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "ar_turnover_decline_years", desc: "应收账款周转率同比下降年数", level: "1", score: 0, weight: 0.4},
  {id: 91, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "ar_turnover_decline_years", desc: "应收账款周转率同比下降年数", level: ">=2", score: 1, weight: 0.4},
  {id: 92, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "branch_cancellation_ratio", desc: "分支机构注销比例", level: "<0.5", score: 0, weight: 0.4},
  {id: 93, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "branch_cancellation_ratio", desc: "分支机构注销比例", level: ">=0.5且<0.7", score: 2, weight: 0.4},
  {id: 94, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "branch_cancellation_ratio", desc: "分支机构注销比例", level: ">=0.7", score: 4, weight: 0.4},
  {id: 95, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "main_business_change_count", desc: "主营业务方向变更次数", level: "＞=1", score: 2, weight: 0.4},
  {id: 96, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "main_business_change_count", desc: "主营业务方向变更次数", level: "＜1", score: 0, weight: 0.4},
  {id: 97, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "excess_pledge", desc: "超额抵质押", level: "＞=0", score: 2, weight: 0.4},
  {id: 98, model_id: 20250715002, model_name: "客商风险分析模版", dimension: "财务健康", index: "excess_pledge", desc: "超额抵质押", level: "＜0", score: 0, weight: 0.4},
  {id: 99, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "0", score: 0, weight: 0.4},
  {id: 100, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "1", score: 1, weight: 0.4},
  {id: 101, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "2", score: 2, weight: 0.4},
  {id: 102, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "3", score: 3, weight: 0.4},
  {id: 103, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "4", score: 4, weight: 0.4},
  {id: 104, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0且<=0.1", score: 2, weight: 0.2},
  {id: 105, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.1且<=0.2", score: 4, weight: 0.2},
  {id: 106, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.2且<=0.3", score: 6, weight: 0.2},
  {id: 107, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.3且<=0.5", score: 8, weight: 0.2},
  {id: 108, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "ar_amount_ratio", desc: "应收账款金额占比", level: ">0.5", score: 10, weight: 0.2},
  {id: 109, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "5", score: 5, weight: 0.4},
  {id: 110, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "6", score: 6, weight: 0.4},
  {id: 111, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "7", score: 7, weight: 0.4},
  {id: 112, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "8", score: 8, weight: 0.4},
  {id: 113, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "9", score: 9, weight: 0.4},
  {id: 114, model_id: 20250715003, model_name: "账龄风险分析模版", dimension: "账龄分布", index: "aging_over_concern_ratio", desc: "账龄超关注期占比", level: "10", score: 10, weight: 0.4}
];

// 模版信息数据
export const templateInfoData = [
  {
    id: 20250715001,
    name: '综合风险分析模版',
    description: '适用于一般企业的财务风险评估',
    create_time: '2024-01-15 10:30:00',
    update_time: '2024-01-20 14:25:00',
    status: '启用',
    rule_count: 5
  },
  {
    id: 20250715002,
    name: '客商风险分析模版',
    description: '适用于金融机构的合规风险评估',
    create_time: '2024-01-18 09:15:00',
    update_time: '2024-01-22 16:40:00',
    status: '启用',
    rule_count: 3
  },
  {
    id: 20250715003,
    name: '账龄风险分析模版',
    description: '适用于制造业的市场风险评估',
    create_time: '2024-01-25 11:20:00',
    update_time: '2024-01-28 13:50:00',
    status: '启用',
    rule_count: 4
  }
];

// 维度选项
export const dimensionOptions = [
  { label: '企业资质', value: '企业资质' },
  { label: '合规经营', value: '经营风险' },
  { label: '财务健康', value: '财务健康' },
  { label: '企业资质', value: '企业资质' },
  { label: '财务健康', value: '财务健康' },
  { label: '账龄分布', value: '账龄分布' }
];

// 级别选项
export const levelOptions = [
  { label: '低风险', value: '低风险' },
  { label: '中风险', value: '中风险' },
  { label: '高风险', value: '高风险' }
];

// 获取指定模版的规则数据
export const getRulesByModelId = (modelId) => {
  return riskTemplateData.filter(rule => rule.model_id === modelId);
};

// 获取所有模版信息
export const getAllTemplates = () => {
  return templateInfoData;
};

// 根据ID获取模版信息
export const getTemplateById = (id) => {
  return templateInfoData.find(template => template.id === id);
};

// 获取模版详情数据（规则数据）
export const getTemplateDetail = (modelId) => {
  return riskTemplateData.filter(rule => rule.model_id === modelId);
};