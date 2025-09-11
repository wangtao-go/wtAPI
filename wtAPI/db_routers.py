# db_routers.py

class PostgresRouter:
    """
    将指定的应用或模型路由到 'postgreswt' 数据库
    """
    route_app_labels = {'apiserver'}  # 替换成你的应用名，比如 'product'

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'postgreswt'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'postgreswt'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('postgreswt',)
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            if db == 'postgreswt':
                return True  # 允许在 postgreswt 上进行迁移
            else:
                return False  # 禁止在其他数据库上迁移这些模型
        return None  # 其他应用按默认处理









