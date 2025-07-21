from app.model.audit_plan_model import AuditPlanModel

class AuditPlanService:
    def __init__(self):
        self.data = []
        self.next_id = 1

    def list(self):
        return self.data

    def add(self, item):
        item['id'] = self.next_id
        self.next_id += 1
        self.data.append(item)
        return {'msg': '添加成功', 'item': item}

    def update(self, item_id, item):
        for i, d in enumerate(self.data):
            if d['id'] == item_id:
                self.data[i].update(item)
                return {'msg': '更新成功', 'item': self.data[i]}
        return {'msg': '未找到', 'item_id': item_id}

    def delete(self, item_id):
        for i, d in enumerate(self.data):
            if d['id'] == item_id:
                self.data.pop(i)
                return {'msg': '删除成功', 'item_id': item_id}
        return {'msg': '未找到', 'item_id': item_id} 