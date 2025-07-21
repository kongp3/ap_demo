class ReportSettingModel:
    def __init__(self, id, project_id, setting_name, value, remark):
        self.id = id
        self.project_id = project_id
        self.setting_name = setting_name
        self.value = value
        self.remark = remark 