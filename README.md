
## 工程目录
audit_system/
├── app/                  # 应用核心代码
│   ├── controllers/      # 路由控制器
│   ├── models/           # 数据库模型
│   ├── services/         # 业务逻辑
│   ├── static/           # 静态资源
│   └── utils/            # 工具类
├── migrations/           # 数据库迁移脚本
├── config.py             # 应用配置
├── requirements.txt      # Python依赖
└── run.py                # 应用入口

## 工程启动
### 1. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 运行应用

```bash
python run.py
```

## API接口
### 1. 提交审计数据

**URL**: `POST /api/audit/save`

**请求参数**:

```json
{
    "process": "审计过程描述",
    "conclusion": "审计结论总结",
    "customer": [
        {
            "customer_name": "客商A",
            "title": "高风险问题",
            "level": "high",
            "desc": "问题详细描述",
            "suggest": "改进建议"
        },
        {
            "customer_name": "客商B",
            "title": "合规性问题",
            "level": "medium",
            "desc": "另一个问题描述",
            "suggest": "另一个建议"
        }
    ]
}
```

**成功响应**:

```json
{
    "message": "Audit data saved successfully",
    "audit_id": 1
}
```

### 2. 按客商名称查询

**URL**: `GET /api/audit/query/by_customer?customer_name=客商名称`

**成功响应**:

```json
[
    {
        "process": "审计过程描述",
        "conclusion": "审计结论总结",
        "customer": [
            {
                "customer_name": "客商A",
                "title": "高风险问题",
                "level": "high"
            },
            {
                "customer_name": "客商B",
                "title": "合规性问题",
                "level": "medium"
            }
        ]
    }
]
```

### 3. 按审计ID查询

**URL**: `GET /api/audit/query/by_audit_id?audit_id=1`

**成功响应**:

```json
{
    "audit_id": 1,
    "process": "审计过程描述",
    "conclusion": "审计结论总结",
    "customers": [
        {
            "customer_name": "客商A",
            "title": "高风险问题",
            "level": "high",
            "desc": "问题详细描述",
            "suggest": "改进建议",
            "attach": [
                {
                    "name": "审计报告.pdf",
                    "url": "https://example.com/files/report.pdf",
                    "filesize": 1024,
                    "dateTime": "2023-07-15T10:30:00"
                }
            ]
        }
    ]
}
```

