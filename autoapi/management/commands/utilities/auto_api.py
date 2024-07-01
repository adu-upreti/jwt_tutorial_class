
from .base_tasks import BaseTask

class AutoApi:
    tasks = [{'utilities': ['permissions', 'pagination', 'importbase']}, 'serializers', 'viewsets', 'routers']

    def __init__(self, app_name):
        self.app_name = app_name

    def make_apis(self):
        for task in self.tasks:
            task_obj = BaseTask(self.app_name, task)
            task_obj.run()

    


            

    