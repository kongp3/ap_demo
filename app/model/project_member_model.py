class ProjectMemberModel:
    def __init__(self, id, project_id, username, role, organization, audit_unit):
        self.id = id
        self.project_id = project_id
        self.username = username
        self.role = role
        self.organization = organization
        self.audit_unit = audit_unit 