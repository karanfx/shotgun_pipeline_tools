import shotgun_api3

class ShotgunDataRetriever:
    def __init__(self, site_url, script_name, script_key):
        self.sg = shotgun_api3.Shotgun(site_url, script_name, script_key)
        
    def _find_entities(self, entity_type, filters, fields):
        return self.sg.find(entity_type, filters, fields)
    
    def get_assets(self, project_id=None, sequence_id=None, shot_id=None):
        asset_filters = [["project", "is", {"type": "Project", "id": project_id}]] if project_id else []
        asset_fields = ["id", "code", "sg_status","description"]  # Add more fields as needed
        return self._find_entities("Asset", asset_filters, asset_fields)
    
    def get_shots(self, project_id=None, sequence_id=None):
        shot_filters = [
            ["project", "is", {"type": "Project", "id": project_id}],
            ["sg_sequence", "is", {"type": "Sequence", "id": sequence_id}]
        ] if project_id and sequence_id else []
        shot_fields = ["id", "code", "sg_status","description"]  # Add more fields as needed
        return self._find_entities("Shot", shot_filters, shot_fields)
    
    def get_tasks(self, project_id=None, shot_id=None):
        task_filters = [
            ["project", "is", {"type": "Project", "id": project_id}],
            ["entity.Shot", "is", {"type": "Shot", "id": shot_id}]
        ] if project_id and shot_id else []
        task_fields = ["id", "content", "sg_status","description"]  # Add more fields as needed
        return self._find_entities("Task", task_filters, task_fields)
    
    def get_versions(self, project_id=None, shot_id=None):
        version_filters = [
            ["project", "is", {"type": "Project", "id": project_id}],
            ["entity.Shot", "is", {"type": "Shot", "id": shot_id}]
        ] if project_id and shot_id else []
        version_fields = ["id", "code","sg_status", "description"]  # Add more fields as needed
        return self._find_entities("Version", version_filters, version_fields)
    
    def list_tasks(self,project_id = None,shot_id = None):
        # shot_id = get_shot_id(sg,proj_name,shot_id)
        task_filter = [['project', 'is', project_id],["entity.Shot", "is", shot_id] ]
        fields = ['content','code','sg_status_list','description',
                'start_date','due_date','duration','dependent_task_id','task_id']
        tasks = self._find_entities("Task",task_filter,fields)

        return tasks



import json
#Import userID and tool dirs
api_key = "E:\Work\python_dev\shotgun_pipeline\data\key.json"
with open(api_key,"r") as uf:
    api_cred = json.load(uf)

#Get Creds
site = api_cred.get('SERVER_PATH')
script_name = api_cred.get('SCRIPT_NAME')
script_key = api_cred.get('SCRIPT_KEY')



if __name__ == "__main__":
    
    data_retriever = ShotgunDataRetriever(site, script_name, script_key)

    # Retrieve data for a specific project, sequence, or shot (provide appropriate IDs)
    project_id = 122
    sequence_id = 41
    shot_id = 1174

    # assets = data_retriever.get_assets(project_id=project_id)
    # print("Assets:")
    # for asset in assets:
    #     print(asset)

    # shots = data_retriever.get_shots(project_id=project_id, sequence_id=sequence_id)
    # print("Shots:")
    # for shot in shots:
    #     print(shot)

    
    tasks = data_retriever.get_tasks(project_id=project_id, shot_id=shot_id)
    print("Tasks:")
    print(tasks)
    for task in tasks:
        print(task)

    # tasks = data_retriever.list_tasks(project_id=project_id, shot_id=shot_id)
    # print("Tasks:")
    # print(tasks)
    # for task in tasks:
    #     print(task)

    # versions = data_retriever.get_versions(project_id=project_id, shot_id=shot_id)
    # print("Versions:")
    # for version in versions:
    #     print(version)
