from app.model.document_archive_model import DocumentArchive
from app.model.project_info_model import ProjectInfo
from app.util.database import db_session
from sqlalchemy.exc import SQLAlchemyError

class DocumentArchiveService:
    @staticmethod
    def list():
        """
        查询所有文书归档信息
        :return: 文书列表或错误信息
        """
        try:
            docs = db_session.query(DocumentArchive).all()
            return [DocumentArchiveService.to_dict(d) for d in docs]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def get_by_id(item_id):
        """
        按主键查询文书归档信息
        :param item_id: 文书ID
        :return: 文书信息或错误信息
        """
        try:
            doc = db_session.query(DocumentArchive).filter_by(id=item_id).first()
            if not doc:
                return None
            return DocumentArchiveService.to_dict(doc)
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def query_by_attr(**kwargs):
        """
        按指定属性查询文书归档信息，返回列表
        :param kwargs: 属性名=属性值
        :return: 文书列表或错误信息
        """
        try:
            docs = db_session.query(DocumentArchive).filter_by(**kwargs).all()
            return [DocumentArchiveService.to_dict(d) for d in docs]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def paginate(page=1, per_page=10, **kwargs):
        """
        分页查询文书归档信息，可带属性过滤
        :param page: 页码
        :param per_page: 每页数量
        :param kwargs: 属性名=属性值
        :return: 分页结果dict
        """
        try:
            query = db_session.query(DocumentArchive)
            if kwargs:
                query = query.filter_by(**kwargs)
            total = query.count()
            items = query.offset((page-1)*per_page).limit(per_page).all()
            return {
                'total': total,
                'page': page,
                'per_page': per_page,
                'items': [DocumentArchiveService.to_dict(d) for d in items]
            }
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def add(item):
        """
        新增文书归档，包含外键和唯一性校验
        :param item: dict
        :return: 结果dict
        """
        required = ['project_id', 'file_name', 'file_path']
        for f in required:
            if not item.get(f):
                return {'msg': f'{f}为必填项', 'error': True}
        # 外键存在性校验
        project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
        if not project:
            return {'msg': '所属项目不存在', 'error': True}
        # 同项目文件名唯一
        exists = db_session.query(DocumentArchive).filter_by(project_id=item['project_id'], file_name=item['file_name']).first()
        if exists:
            return {'msg': '同项目下文件名已存在', 'error': True}
        try:
            doc = DocumentArchive(
                project_id=item['project_id'],
                file_name=item['file_name'],
                file_path=item['file_path'],
                remark=item.get('remark')
            )
            db_session.add(doc)
            db_session.commit()
            return {'msg': '添加成功', 'item': DocumentArchiveService.to_dict(doc)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def update(item_id, item):
        """
        更新文书归档，包含外键和唯一性校验
        :param item_id: 文书ID
        :param item: dict
        :return: 结果dict
        """
        try:
            doc = db_session.query(DocumentArchive).filter_by(id=item_id).first()
            if not doc:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            # 外键存在性校验
            if 'project_id' in item and item['project_id'] != doc.project_id:
                project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
                if not project:
                    return {'msg': '所属项目不存在', 'error': True}
            # 同项目文件名唯一
            if 'file_name' in item and (item['file_name'] != doc.file_name or ('project_id' in item and item['project_id'] != doc.project_id)):
                pid = item.get('project_id', doc.project_id)
                exists = db_session.query(DocumentArchive).filter_by(project_id=pid, file_name=item['file_name']).first()
                if exists:
                    return {'msg': '同项目下文件名已存在', 'error': True}
            for f in ['project_id', 'file_name', 'file_path']:
                if f in item and not item[f]:
                    return {'msg': f'{f}为必填项', 'error': True}
            for k, v in item.items():
                setattr(doc, k, v)
            db_session.commit()
            return {'msg': '更新成功', 'item': DocumentArchiveService.to_dict(doc)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def delete(item_id):
        """
        删除文书归档
        :param item_id: 文书ID
        :return: 结果dict
        """
        try:
            doc = db_session.query(DocumentArchive).filter_by(id=item_id).first()
            if not doc:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            db_session.delete(doc)
            db_session.commit()
            return {'msg': '删除成功', 'item_id': item_id}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def to_dict(obj):
        """
        ORM对象转dict
        :param obj: DocumentArchive对象
        :return: dict
        """
        return {
            'id': obj.id,
            'project_id': obj.project_id,
            'file_name': obj.file_name,
            'file_path': obj.file_path,
            'remark': obj.remark
        } 