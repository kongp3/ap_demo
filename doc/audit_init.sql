-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: audit-pioneer
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aging`
--

DROP TABLE IF EXISTS `aging`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aging` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `company_name` varchar(256) DEFAULT NULL COMMENT '企业名称',
  `category` varchar(64) DEFAULT NULL COMMENT '行业分类',
  `amount` decimal(10,0) NOT NULL COMMENT '应收账款金额',
  `rate` double DEFAULT NULL COMMENT '应收账款金额占比',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='企业账龄表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aging`
--

LOCK TABLES `aging` WRITE;
/*!40000 ALTER TABLE `aging` DISABLE KEYS */;
INSERT INTO `aging` VALUES (1,'沈阳城市公用集团煤炭有限公司','零售业',300000,0.3),(2,'上海建工集团股份有限公司','建筑业',100000,0.1),(3,'众泰汽车股份有限公司','制造业',600000,0.6);
/*!40000 ALTER TABLE `aging` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aging_detail`
--

DROP TABLE IF EXISTS `aging_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aging_detail` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `aging_id` int NOT NULL COMMENT '账龄ID',
  `company_name` varchar(256) DEFAULT NULL COMMENT '企业名称',
  `risk_value` int DEFAULT NULL COMMENT '风险值',
  `remark` varchar(64) DEFAULT NULL COMMENT '账龄风险期分类',
  `min_days` int DEFAULT NULL COMMENT '最小天数',
  `max_days` int DEFAULT NULL COMMENT '最大天数',
  `rate` double DEFAULT NULL COMMENT '占比',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='企业账龄分布表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aging_detail`
--

LOCK TABLES `aging_detail` WRITE;
/*!40000 ALTER TABLE `aging_detail` DISABLE KEYS */;
INSERT INTO `aging_detail` VALUES (1,2,'众泰汽车股份有限公司',0,'正常期',0,60,0.1),(2,2,'众泰汽车股份有限公司',1,'关注期',61,120,0.5),(3,2,'众泰汽车股份有限公司',2,'次级风险',121,180,0.2),(4,2,'众泰汽车股份有限公司',3,'可疑风险',181,360,0.2),(5,2,'众泰汽车股份有限公司',4,'损失风险',360,NULL,0),(6,3,'上海建工集团股份有限公司',0,'正常期',0,90,0.1),(7,3,'上海建工集团股份有限公司',1,'关注期',91,180,0.6),(8,3,'上海建工集团股份有限公司',2,'次级风险',180,360,0.3),(9,3,'上海建工集团股份有限公司',3,'可疑风险',361,720,0),(10,3,'上海建工集团股份有限公司',4,'损失风险',720,NULL,0),(11,1,'沈阳城市公用集团煤炭有限公司',0,'正常期',0,30,0.6),(12,1,'沈阳城市公用集团煤炭有限公司',1,'关注期',31,60,0.4),(13,1,'沈阳城市公用集团煤炭有限公司',2,'次级风险',61,NULL,0),(14,1,'沈阳城市公用集团煤炭有限公司',3,'可疑风险',NULL,NULL,0),(15,1,'沈阳城市公用集团煤炭有限公司',4,'损失风险',NULL,NULL,0);
/*!40000 ALTER TABLE `aging_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_draft`
--

DROP TABLE IF EXISTS `audit_draft`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit_draft` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `company_name` varchar(256) DEFAULT NULL COMMENT '被审计单位名称',
  `status` varchar(16) DEFAULT NULL COMMENT '底稿状态',
  `matter` varchar(64) DEFAULT NULL COMMENT '审计事项',
  `name` varchar(1000) DEFAULT NULL COMMENT '底稿名称',
  `code` varchar(16) DEFAULT NULL COMMENT '底稿编码',
  `focus` varchar(128) DEFAULT NULL COMMENT '关联关注点',
  `operator` varchar(64) DEFAULT NULL COMMENT '取证人',
  `draft_id` int DEFAULT NULL COMMENT '引用底稿',
  `source` varchar(256) DEFAULT NULL COMMENT '记录来源',
  `model` varchar(16) DEFAULT NULL COMMENT '风险模版',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '变更时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='审计底稿';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_draft`
--

LOCK TABLES `audit_draft` WRITE;
/*!40000 ALTER TABLE `audit_draft` DISABLE KEYS */;
INSERT INTO `audit_draft` VALUES (17,'中国第四冶金建设有限责任公司','草稿','应收账款','应收账款审计底稿','10001','账龄信息、企业信息','AI审计助手',NULL,'综合信息库','客商综合分析','2025-07-13 07:11:50','2025-07-13 07:11:50');
/*!40000 ALTER TABLE `audit_draft` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_result`
--

DROP TABLE IF EXISTS `audit_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit_result` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `company_name` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '企业名称',
  `process` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '审计过程',
  `conclusion` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '审计结论',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='审计结果表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_result`
--

LOCK TABLES `audit_result` WRITE;
/*!40000 ALTER TABLE `audit_result` DISABLE KEYS */;
INSERT INTO `audit_result` VALUES (18,'中国第四冶金建设有限责任公司','1. 数据收集：通过企业信用报告获取股东出资、财务数据透明度等关键信息\n2. 风险评分：依据客商风险评分系统评估上海建工集团（21分）、沈阳城市公用集团煤炭（22分）、众泰汽车（22分）\n3. 合规核查：专项检查非货币出资评估报告（特别是土地使用权和\'其他\'出资方式）\n4. 财务验证：\n   - 比对应收账款规模与行业数据\n   - 抽样检查大额应收款的合同/验收单据\n   - 重新计算坏账准备金计提金额','1. 高风险集中：三家主要客商均为高风险（评分>20），其中众泰汽车应收账款占比达10%\n2. 坏账准备不足：按账龄分析法测算应补提坏账准备约X万元（较现有计提增加X%）\n3. 管理缺陷：\n   - 未建立客户信用分级管理制度\n   - 逾期账款催收记录不完整\n4. 特殊风险：企业财务数据不透明，且存在股东出资合规性疑问（特别是\'其他\'出资方式）');
/*!40000 ALTER TABLE `audit_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_result_attach`
--

DROP TABLE IF EXISTS `audit_result_attach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit_result_attach` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `detail_id` int NOT NULL COMMENT '客商详情ID',
  `name` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '附件名称',
  `url` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '附件url',
  `filesize` int DEFAULT NULL COMMENT '附件大小',
  `date_time` datetime DEFAULT NULL COMMENT '上传时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='审计结果-客商附件';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_result_attach`
--

LOCK TABLES `audit_result_attach` WRITE;
/*!40000 ALTER TABLE `audit_result_attach` DISABLE KEYS */;
INSERT INTO `audit_result_attach` VALUES (37,37,'对上海建工集团股份有限公司的审计建议','http://121.43.233.12:9000/audit/attach_上海建工集团股份有限公司.docx',1024,'2025-07-13 07:16:26'),(38,38,'对沈阳城市公用集团煤炭有限公司的审计建议','http://121.43.233.12:9000/audit/attach_沈阳城市公用集团煤炭有限公司.docx',1024,'2025-07-13 07:16:26'),(39,39,'对众泰汽车股份有限公司的审计建议','http://121.43.233.12:9000/audit/attach_众泰汽车股份有限公司.docx',1024,'2025-07-13 07:16:26');
/*!40000 ALTER TABLE `audit_result_attach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_result_detail`
--

DROP TABLE IF EXISTS `audit_result_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit_result_detail` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `audit_id` int DEFAULT NULL COMMENT '审计结果ID',
  `customer_name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '客商名称',
  `title` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标题',
  `level` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '风险等级',
  `desc` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '问题描述',
  `suggest` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '审计建议',
  `date_time` datetime DEFAULT NULL COMMENT '生成时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='审计结果-客商详情';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_result_detail`
--

LOCK TABLES `audit_result_detail` WRITE;
/*!40000 ALTER TABLE `audit_result_detail` DISABLE KEYS */;
INSERT INTO `audit_result_detail` VALUES (37,18,'上海建工集团股份有限公司','高风险应收账款清收问题','高风险','1. 固定问题：存在4次被执行记录及4起败诉案件，显示重大偿债风险\n2. 专项问题：超额抵质押（2分）进一步限制偿债能力\n3. 款项特征：账龄虽未超期但金额占比2%，且客户涉诉可能导致支付延迟','1. 立即启动法律催收程序\n2. 暂停新项目合作\n3. 要求客户提供银行保函等增信措施','2025-07-13 07:16:26'),(38,18,'沈阳城市公用集团煤炭有限公司','高风险集中度风险','高风险','1. 固定问题：6%的应收账款占比显著高于行业均值（建筑业通常<3%）\n2. 专项问题：4次被执行记录且全部败诉，清偿可能性极低\n3. 持续经营风险：主营业务变更2次反映经营不稳定','1. 计提100%专项坏账准备\n2. 列入交易黑名单\n3. 核查历史交易是否涉及利益输送','2025-07-13 07:16:26'),(39,18,'众泰汽车股份有限公司','超高风险敞口问题','高风险','1. 固定问题：10%的应收账款占比形成重大风险敞口\n2. 专项问题：虽无败诉但作为被告案件达4起，且存在超额抵质押（2分）\n3. 行业风险：汽车行业景气度下行加剧回收风险','1. 立即停止所有赊销\n2. 协商债务重组（如债转股）\n3. 每季度核查客户财务状况','2025-07-13 07:16:26');
/*!40000 ALTER TABLE `audit_result_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '企业唯一ID',
  `enterprise_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '企业全称',
  `short_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '企业简称',
  `credit_code` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '统一社会信用代码',
  `registration_num` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '工商注册号',
  `legal_representative` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '法定代表人',
  `registered_capital` decimal(18,2) DEFAULT NULL COMMENT '注册资本(万元)',
  `enterprise_status` enum('存续','注销','吊销','迁出','停业') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '存续' COMMENT '企业状态',
  `establishment_date` date DEFAULT NULL COMMENT '成立日期',
  `operating_period_start` date DEFAULT NULL COMMENT '营业期限开始',
  `operating_period_end` date DEFAULT NULL COMMENT '营业期限结束(空值表示长期)',
  `registered_address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '注册地址',
  `office_address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '办公地址',
  `contact_phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '联系电话',
  `contact_email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '联系邮箱',
  `official_website` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '官方网站',
  `enterprise_type` enum('有限责任公司','股份有限公司','集团公司','合伙企业','个体工商户','外资企业') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '企业类型',
  `industry_category` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '行业类别',
  `business_scope` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci COMMENT '经营范围',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `version` int unsigned DEFAULT '1' COMMENT '数据版本号',
  `is_deleted` tinyint(1) DEFAULT '0' COMMENT '软删除标记(0:正常 1:删除)',
  PRIMARY KEY (`id`),
  UNIQUE KEY `credit_code` (`credit_code`),
  UNIQUE KEY `idx_credit_code` (`credit_code`),
  KEY `idx_enterprise_name` (`enterprise_name`),
  KEY `idx_legal_rep` (`legal_representative`),
  KEY `idx_establish_date` (`establishment_date`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='企业基本信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'沈阳城市公用集团煤炭有限公司',NULL,NULL,NULL,NULL,NULL,'存续',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2025-07-01 07:42:26','2025-07-01 07:42:26',1,0);
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL COMMENT '主键',
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '客户名称',
  `company_id` int NOT NULL COMMENT '所属企业ID'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='客户关系表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'沈阳城市公用集团煤炭有限公司',1),(2,'上海建工集团股份有限公司',2),(3,'众泰汽车股份有限公司',3);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_cache`
--

DROP TABLE IF EXISTS `index_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `index_cache` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `issue` varchar(2000) DEFAULT NULL COMMENT '问题',
  `company_name` varchar(256) DEFAULT NULL COMMENT '企业名称',
  `data` varchar(2000) DEFAULT NULL COMMENT '缓存数据',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='指标缓存';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_cache`
--

LOCK TABLES `index_cache` WRITE;
/*!40000 ALTER TABLE `index_cache` DISABLE KEYS */;
INSERT INTO `index_cache` VALUES (3,NULL,'众泰汽车股份有限公司','{\"company_name\":\"众泰汽车股份有限公司\",\"paid_in_capital_ratio\":0.4025,\"establishment_years\":26,\"operation_expiry_years\":0,\"capital_reduction_ratio\":0.0021,\"main_business_change_count\":1,\"enforcement_count\":1,\"enforcement_ratio\":0.0065,\"penalty_abnormal_count\":0,\"asset_liability_ratio\":0,\"current_ratio\":0,\"quick_ratio\":0,\"negative_cash_flow_years\":0,\"ar_turnover_decline_years\":0,\"branch_cancellation_ratio\":0,\"excess_pledge\":0,\"defendant_cases\":18,\"lose_cases\":0,\"aging_over_concern_ratio\":0.4,\"ar_amount_ratio\":0.6}'),(4,'','沈阳城市公用集团煤炭有限公司','{\"company_name\": \"沈阳城市公用集团煤炭有限公司\", \"paid_in_capital_ratio\": 1.0, \"establishment_years\": 13, \"operation_expiry_years\": 7, \"capital_reduction_ratio\": -3.0, \"main_business_change_count\": 5, \"enforcement_count\": 8, \"enforcement_ratio\": 0.128970625, \"penalty_abnormal_count\": 0, \"asset_liability_ratio\": 0, \"current_ratio\": 0, \"quick_ratio\": 0, \"negative_cash_flow_years\": 0, \"ar_turnover_decline_years\": 0, \"branch_cancellation_ratio\": 0, \"excess_pledge\": 0, \"defendant_cases\": 22, \"lose_cases\": 10, \"aging_over_concern_ratio\": 0.0, \"ar_amount_ratio\": 0.3}'),(5,'','上海建工集团股份有限公司','{\"company_name\":\"上海建工集团股份有限公司\",\"paid_in_capital_ratio\":0.3025,\"establishment_years\":26,\"operation_expiry_years\":0,\"capital_reduction_ratio\":0.0021,\"main_business_change_count\":2,\"enforcement_count\":51,\"enforcement_ratio\":0.0065,\"penalty_abnormal_count\":0,\"asset_liability_ratio\":0,\"current_ratio\":0,\"quick_ratio\":0,\"negative_cash_flow_years\":0,\"ar_turnover_decline_years\":0,\"branch_cancellation_ratio\":0,\"excess_pledge\":0,\"defendant_cases\":34,\"lose_cases\":5,\"aging_over_concern_ratio\":0.3,\"ar_amount_ratio\":0.1}'),(6,'固定',NULL,'\"{\\\"text\\\": \\\"根据提供的企业信用报告内容，从应收账款审计角度可提炼以下关键信息及风险点：\\\\n\\\\n**1. 股东出资合规性**\\\\n- 鹰潭国资委（持股24.65%）2010年以土地使用权出资，后修改为\\\\\\\"土地使用权+其他\\\\\\\"方式，需关注：\\\\n  ✓ 土地使用权评估价值是否公允（需核查评估报告）\\\\n  ✓ \\\\\\\"其他\\\\\\\"出资方式的合法性及资产权属证明\\\\n  ✓ 出资资产是否存在抵押/权属争议\\\\n\\\\n- 北京安宝房产（持股73.35%）2017年货币出资已实缴，风险较低\\\\n\\\\n- 中国节能环保（持股10.2%）2012年以\\\\\\\"其他\\\\\\\"方式出资，需特别核查：\\\\n  ✓ 非货币出资的具体内容（技术入股？债权转股权？）\\\\n  ✓ 是否完成权属变更及税务处理\\\\n\\\\n**2. 财务数据不透明风险**\\\\n- 企业主动选择不公示所有财务数据（资产/负债/收入/利润等）\\\\n- 审计需重点验证：\\\\n  ✓ 应收账款规模与行业地位的匹配性\\\\n  ✓ 大额应收款对象是否涉及关联方（如股东方）\\\\n  ✓ 坏账计提政策的合理性\\\\n\\\\n**3. 异常点提示**\\\\n- 中国节能环保集团作为央企子公司仅持股10.2%，却以\\\\\\\"其他\\\\\\\"方式出资，需核查是否存在代持协议\\\\n- 鹰潭国资委出资方式变更未说明原因，可能涉及出资瑕疵\\\\n- 2017年后无新增股东/增资记录，需关注企业持续经营能力\\\\n\\\\n**审计建议：**\\\\n① 重点核查非货币出资的评估报告及权属文件\\\\n② 通过银行流水验证货币出资真实性\\\\n③ 要求企业提供内部财务资料核对应收账款账龄\\\\n④ 对前五大客户实施函证程序\\\\n\\\\n（注：因企业未公示财务数据，实际审计中需依据《中国注册会计师审计准则第1502号》考虑审计范围受限的影响）\\\"}\"');
/*!40000 ALTER TABLE `index_cache` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model`
--

DROP TABLE IF EXISTS `model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '模版名称',
  `scene` char(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '场景（1:应收账款）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='风险评估模版';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model`
--

LOCK TABLES `model` WRITE;
/*!40000 ALTER TABLE `model` DISABLE KEYS */;
INSERT INTO `model` VALUES (1,'应收账款回收风险模版1','1');
/*!40000 ALTER TABLE `model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rule`
--

DROP TABLE IF EXISTS `rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rule` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `model_id` int NOT NULL COMMENT '模版ID',
  `dimension` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '维度',
  `index` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '指标',
  `desc` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '指标描述',
  `level` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '级别',
  `score` int NOT NULL COMMENT '分数',
  `weight` double DEFAULT NULL COMMENT '权重',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='评分规则';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rule`
--

LOCK TABLES `rule` WRITE;
/*!40000 ALTER TABLE `rule` DISABLE KEYS */;
INSERT INTO `rule` VALUES (1,1,'企业资质','paid_in_capital_ratio','实缴资本占比','>=0.5',0,0.4,'最新一年中股东及出资信息中实缴出资额/企业注册资本'),(2,1,'企业资质','paid_in_capital_ratio','实缴资本占比','>=0.3且<0.5',2,0.4,''),(3,1,'企业资质','paid_in_capital_ratio','实缴资本占比','<0.3',4,0.4,''),(4,1,'企业资质','capital_reduction_ratio','减资比例','0',0,0.4,NULL),(5,1,'企业资质','capital_reduction_ratio','减资比例','<0.5',0,0.4,NULL),(6,1,'企业资质','capital_reduction_ratio','减资比例','>=0.5且<0.7',2,0.4,NULL),(7,1,'企业资质','capital_reduction_ratio','减资比例','>=0.7',4,0.4,NULL),(8,1,'企业资质','establishment_years','成立年限','>=1',0,0.4,NULL),(9,1,'企业资质','establishment_years','成立年限','<1',1,0.4,NULL),(10,1,'企业资质','operation_expiry_years','经营到期年限','>=1',0,0.4,NULL),(11,1,'企业资质','operation_expiry_years','经营到期年限','<1',1,0.4,NULL),(12,1,'合规经营','defendant_cases','作为被告的案件数','<2',0,0.4,NULL),(13,1,'合规经营','defendant_cases','作为被告的案件数','>=2且<=4',2,0.4,NULL),(14,1,'合规经营','defendant_cases','作为被告的案件数','>=4',4,0.4,NULL),(15,1,'合规经营','lose_cases','败诉案件数','0',0,0.4,NULL),(16,1,'合规经营','lose_cases','败诉案件数','1',2,0.4,NULL),(17,1,'合规经营','lose_cases','败诉案件数','>=2',4,0.4,NULL),(18,1,'合规经营','enforcement_count','被执行次数','0',0,0.4,NULL),(19,1,'合规经营','enforcement_count','被执行次数','1',1,0.4,NULL),(20,1,'合规经营','enforcement_count','被执行次数','2',2,0.4,NULL),(21,1,'合规经营','enforcement_count','被执行次数','3',3,0.4,NULL),(22,1,'合规经营','enforcement_count','被执行次数','>=4',4,0.4,NULL),(23,1,'合规经营','enforcement_ratio','被执行比例','>=0.7',2,0.4,NULL),(24,1,'合规经营','enforcement_ratio','被执行比例','>=0.5且<0.7',1,0.4,NULL),(25,1,'合规经营','enforcement_ratio','被执行比例','<0.5',0,0.4,NULL),(26,1,'合规经营','penalty_abnormal_count','行政处罚与经营异常次数','0',0,0.4,NULL),(27,1,'合规经营','penalty_abnormal_count','行政处罚与经营异常次数','1',0,0.4,NULL),(28,1,'合规经营','penalty_abnormal_count','行政处罚与经营异常次数','>=2',2,0.4,NULL),(29,1,'财务健康\r','asset_liability_ratio','资产负债率','>=0.7',1,0.4,NULL),(30,1,'财务健康\r','asset_liability_ratio','资产负债率','＜0.7',0,0.4,NULL),(31,1,'财务健康\r','negative_cash_flow_years','经营净现金流连续为负年数','1',0,0.4,NULL),(32,1,'财务健康\r','negative_cash_flow_years','经营净现金流连续为负年数','>=2',1,0.4,NULL),(33,1,'财务健康\r','ar_turnover_decline_years','应收账款周转率同比下降年数','1',0,0.4,NULL),(34,1,'财务健康\r','ar_turnover_decline_years','应收账款周转率同比下降年数','>=2',1,0.4,NULL),(35,1,'财务健康\r','branch_cancellation_ratio','分支机构注销比例','<0.5',0,0.4,NULL),(36,1,'财务健康\r','branch_cancellation_ratio','分支机构注销比例','>=0.5且<0.7',2,0.4,NULL),(37,1,'财务健康\r','branch_cancellation_ratio','分支机构注销比例','>=0.7',4,0.4,NULL),(38,1,'财务健康\r','main_business_change_count','主营业务方向变更次数','＞=1',2,0.4,NULL),(39,1,'财务健康\r','main_business_change_count','主营业务方向变更次数','＜1',0,0.4,NULL),(40,1,'财务健康\r','excess_pledge','超额抵质押','＞=0',2,0.4,NULL),(41,1,'财务健康','excess_pledge','超额抵质押','＜0',0,0.4,NULL),(42,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','0',0,0.4,NULL),(43,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','1',1,0.4,NULL),(44,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','2',2,0.4,NULL),(45,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','3',3,0.4,NULL),(46,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','4',4,0.4,NULL),(47,1,'账龄分布','ar_amount_ratio','应收账款金额占比','>0且<=0.1',2,0.2,NULL),(48,1,'账龄分布','ar_amount_ratio','应收账款金额占比','>0.1且<=0.2',4,0.2,NULL),(49,1,'账龄分布','ar_amount_ratio','应收账款金额占比','>0.2且<=0.3',6,0.2,NULL),(50,1,'账龄分布','ar_amount_ratio','应收账款金额占比','>0.3且<=0.5',8,0.2,NULL),(51,1,'账龄分布','ar_amount_ratio','应收账款金额占比','>0.5',10,0.2,NULL),(52,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','5',5,0.4,NULL),(53,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','6',6,0.4,NULL),(54,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','7',7,0.4,NULL),(55,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','8',8,0.4,NULL),(56,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','9',9,0.4,NULL),(57,1,'账龄分布','aging_over_concern_ratio','账龄超关注期占比','10',10,0.4,NULL);
/*!40000 ALTER TABLE `rule` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-14  1:51:18
