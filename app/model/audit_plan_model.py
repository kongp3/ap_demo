class AuditPlanModel:
    def __init__(self, id, project_id, plan_name, items, remark):
        self.id = id
        self.project_id = project_id
        self.plan_name = plan_name
        self.items = items
        self.remark = remark 