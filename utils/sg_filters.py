import shotgun_api3.shotgun as SG
from pprint import pprint
import os
import json

#SG instance with API KEY
#test variables

#API KEY
cred_file = "E:/Work/python_dev/Glacier_shotgun_Tools/creds/key.json"

with open(cred_file,'r') as cred:
    creds = json.load(cred)

SERVER = creds.get('SERVER_PATH')
SCRIPT_NAME = creds.get('SCRIPT_NAME')
API_KEY = creds.get('SCRIPT_KEY')

sg = SG.Shotgun(SERVER, SCRIPT_NAME, API_KEY)

#TEST DATA
proj_name = "glacier_test_project"
seq_name = "seq_001"
shot_name = "001_001"

#Get Codes and Ids
#Get the Lists
def list_project(sg):
    proj_list = sg.find("Project",[], ['name'])
    return proj_list

def list_seq(sg,proj_name):
    sg_shots = sg.find("Sequence", [['project.Project.name', 'is', proj_name]], ['code'])
    return sg_shots

def list_all_shot(sg,proj_name):
    sg_shots = sg.find("Shot", [['project.Project.name', 'is', proj_name]], ['code'])
    return sg_shots

def list_shot(sg,proj_name,seq_name):
    filters = [['project.Project.name', 'is', proj_name],["sg_sequence.Sequence.code", "is", seq_name]]
    sg_shots = sg.find("Shot", filters, ['code'])
    return sg_shots

def list_shot2(sg,proj_name):
    
    sg_shots = sg.find("Shot", [['project.Project.name', 'is', proj_name]],
                    ['code', 'sg_sequence.Sequence.sg_status_list'])
    return sg_shots

def list_assets(sg,proj_name):
    sg_shots = sg.find("Asset", [['project.Project.name', 'is', proj_name]], ['code'])
    return sg_shots

def list_asset_tasks(sg,proj_name,asset_name):
    shot_id = get_asset_id(sg,proj_name,asset_name)
    task_filter = [['project.Project.name', 'is', proj_name],["entity.Asset.code", "is", asset_name] ]
    fields = ['content','code','sg_status_list','description',
              'start_date','due_date','duration','dependent_task_id','task_id']
    tasks = sg.find("Task",task_filter,fields)

    return tasks

def list_tasks(sg,proj_name,shot_name):
    shot_id = get_shot_id(sg,proj_name,shot_name)
    task_filter = [['project.Project.name', 'is', proj_name],["entity.Shot.code", "is", shot_name] ]
    fields = ['content','code','sg_status_list','description',
              'start_date','due_date','duration','dependent_task_id','task_id']
    tasks = sg.find("Task",task_filter,fields)

    return tasks


#Get Ids by name
def get_proj_id(sg,proj_name):
    proj_filter = [["name","is",proj_name]]
    proj_id = sg.find_one("Project",proj_filter,["id"])

    return proj_id["id"]

def get_seq_id(sg,proj_name,seq_name):
    seq_filters = [["code", "is", seq_name],
                    ['project.Project.name', 'is', proj_name]]
    seq = sg.find_one("Sequence",seq_filters)

    # print(type(shot))
    return seq['id']

def get_shot_id(sg,proj_name,shot_name):
    shot_filters = [["code", "is", shot_name],
                    ['project.Project.name', 'is', proj_name]]
    shot = sg.find_one("Shot",shot_filters)

    return shot['id']

def get_asset_id(sg,proj_name,shot_name):
    shot_filters = [["code", "is", shot_name],
                    ['project.Project.name', 'is', proj_name]]
    shot = sg.find_one("Asset",shot_filters)

    return shot['id']

def get_task_id(sg,proj_name,shot_name,task):
    proj_id = get_proj_id(sg,proj_name)
    shot_id = get_shot_id(sg,proj_name,shot_name)

    filters = [ ['project', 'is', {'type': 'Project', 'id': proj_id}],
            ['entity', 'is',{'type':'Shot', 'id': shot_id}],
            ['content', 'is', task] ]
    task = sg.find_one('Task', filters)

    return task['id']

def get_asset_task_id(sg,proj_name,asset_name,task):
    proj_id = get_proj_id(sg,proj_name)
    asset_id = get_asset_id(sg,proj_name,asset_name)

    filters = [ ['project', 'is', {'type': 'Project', 'id': proj_id}],
            ['entity', 'is',{'type':'Shot', 'id': asset_id}],
            ['content', 'is', task] ]
    task = sg.find_one('Task', filters)

    return task['id']

def get_task_template_id(sg,template_name):
    filters = [['code','is', template_name ]]
    template = sg.find_one('TaskTemplate', filters)
    return template

def get_user_id(sg,username):

    user = sg.find_one("HumanUser", [["login", "is", username]], ["id"])
    return user["id"]

def get_task_full_id(sg,proj_name,seq_name,shot_name,task):
    
    if seq_name == None:
        seq = None
    else:
        seq = get_seq_id(sg,proj_name,seq_name)
    
    task_ids = {'Project':get_proj_id(sg,proj_name),
                'Sequence':seq,
                'Shot':get_shot_id(sg,proj_name,shot_name),
                'Task':get_task_id(sg,proj_name,shot_name,task)
                }
    return task_ids

def get_tasks_by_artist(sg,username):
    artist_id = get_user_id(sg,username)
    task_filters = [["task_assignees", "in", {"type": "HumanUser", "id": artist_id}]]
    task_fields = ["id", "content", "project", "entity", "sg_status"]
    
    assigned_tasks = sg.find("Task", task_filters, task_fields)

    return assigned_tasks

def update_task_status(task_id, new_status):
        task_data = {
            "sg_status_list": new_status
        }
        sg.update("Task", task_id, task_data)
        

#Creating Shot and Seq
def create_seq(sg,proj_name,seq_name,status,desp):
    proj_id = get_proj_id(sg,proj_name)
    seq_data = {
    'project': {"type":"Project","id": proj_id},
    'code': seq_name,
    'description': desp,
    'sg_status_list': status
    }
    result = sg.create("Sequence",seq_data)
    print(result)

def create_task(sg,proj_name,shot_name,start_date,due_date,dept):
    proj_id = get_proj_id(sg,proj_name)
    shot_id = get_shot_id(sg,proj_name,shot_name)
    data = {
        'project': {'type':'Project', 'id':proj_id},
        'content': dept,
        'start_date': start_date,
        'due_date': due_date,
        'entity': {'type':'Shot', 'id':shot_id}
        }
    result = sg.create('Task', data)

    # return result

def create_shot(sg,proj_name,seq_name,shot_name,status,template,desp):
    
    proj_id = get_proj_id(sg,proj_name)
    seq_id = get_seq_id(sg,proj_name,seq_name)
    

    shot_data = {
    'project': {"type":"Project","id": proj_id},
    'sg_sequence': {"type":"Sequence","id": seq_id},
    'code': shot_name,
    'description': desp,
    'sg_status_list': status,
    'task_template': template
    }
    result = sg.create("Shot",shot_data)
    print(result)

def create_version(sg,ids,username,ver_name,vers_path,status,desc):
    
    # ids = get_task_full_id(sg,proj_name,seq_name,shot_name,task)
    user_id = get_user_id(sg,username)

    #Create a version
    ver_data = { 'project': {'type': 'Project','id': ids['Project']},
             'code': ver_name,
             'description': desc,
             'sg_path_to_frames': vers_path,
             'sg_status_list': status,
             'entity': {'type': 'Shot', 'id': ids['Shot']},
             'sg_task': {'type': 'Task', 'id': ids['Task']},
             'user': {'type': 'HumanUser', 'id': user_id} }

    result = sg.create('Version', ver_data)
    pprint(result)

def create_asset(sg,proj_name,asset_name,task,username,ver_name,vers_path,status,desc):
    proj_id = get_proj_id(sg,proj_name)
    asset_id = get_asset_id(sg,proj_name,asset_name)
    task_id = get_asset_task_id(sg,proj_name,asset_name,task)
    # ids = get_task_full_id(sg,proj_name,seq_name,shot_name,task)
    user_id = get_user_id(sg,username)

    #Create a version
    ver_data = { 'project': {'type': 'Project','id': proj_id},
                "entity": {"type": "Asset", "id": asset_id},
             'code': ver_name,
             'description': desc,
             'sg_path_to_frames': vers_path,
             'sg_status_list': status,
             'sg_task': {'type': 'Task', 'id': task_id},
             'user': {'type': 'HumanUser', 'id': user_id} }

    result = sg.create('Version', ver_data)
    pprint(result)


if __name__ == "__main__":
    # create_seq(sg,proj_name,'seq_002','wtg','seq crated from API')
    # create_shot(sg,proj_name,'seq_002','002_001','wtg','shot02 crated from API')

    # test = list_shot(sg,proj_name,seq_name)
    # test = list_project(sg)
    # test = list_seq(sg,proj_name)
    # test = list_assets(sg,proj_name)
    # create_version(sg,proj_name)
    # test = get_shot_id(sg,proj_name,shot_name)

    # test = get_proj_id(sg,proj_name)
    test = get_seq_id(sg,proj_name,seq_name)
    # test = get_task_id(sg,proj_name,shot_name,"FX")
    # test = get_user_id(sg,"fedej32881@tipent.com")
    # test = get_task_full_id(sg,proj_name,seq_name,shot_name,"FX")

    # test = get_tasks_by_artist(sg,"ramesh.r")
    # test = create_task(sg,proj_name,'001_002','2023-08-16','2023-08-20','FX')
    # test = list_tasks(sg,proj_name,shot_name)
    # test = sg.schema_entity_read({'type': 'Project', 'id': 122})
    # test = sg.schema_read({'type': 'Project', 'id': 122})
    # pprint(test)
    
