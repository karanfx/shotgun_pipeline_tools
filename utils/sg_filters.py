import shotgun_api3.shotgun as SG
from pprint import pprint
import os

#SG instance with API KEY
#test variables
sg = SG.Shotgun('https://testvfx.shotgrid.autodesk.com', 'testscript', 'byjzbl-abBmd3ohtpebhjkadu')

proj_name = "glacier_test_project"

seq_name = "seq_001"
shot_name = "001_001"

#Get Codes and Ids
#Get the Lists
def list_project(sg):
    proj_list = sg.find("Project", ['code'])
    return proj_list

def list_seq(sg,proj_name):
    sg_shots = sg.find("Sequence", [['project.Project.name', 'is', proj_name]], ['code'])
    return sg_shots

def list_shot(sg,proj_name):
    sg_shots = sg.find("Shot", [['project.Project.name', 'is', proj_name]], ['code'])
    return sg_shots

def list_shot2(sg,proj_name):
    
    sg_shots = sg.find("Shot", [['project.Project.name', 'is', proj_name]],
                    ['code', 'sg_sequence.Sequence.sg_status_list'])
    return sg_shots

#Get Ids
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

def get_task_id(sg,proj_name,shot_name,task):
    proj_id = get_proj_id(sg,proj_name)
    shot_id = get_shot_id(sg,proj_name,shot_name)

    filters = [ ['project', 'is', {'type': 'Project', 'id': proj_id}],
            ['entity', 'is',{'type':'Shot', 'id': shot_id}],
            ['content', 'is', task] ]
    task = sg.find_one('Task', filters)

    return task['id']

def get_user_id(sg,username):

    user = sg.find_one("HumanUser", [["login", "is", username]], ["id"])
    return user["id"]

def get_task_full_id(sg,proj_name,seq_name,shot_name,task):
    task_ids = {'Project':get_proj_id(sg,proj_name),
                'Sequence':get_seq_id(sg,proj_name,seq_name),
                'Shot':get_shot_id(sg,proj_name,shot_name),
                'Task':get_task_id(sg,proj_name,shot_name,task)
                }
    return task_ids

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

def create_shot(sg,proj_name,seq_name,shot_name,status,desp):
    
    proj_id = get_proj_id(sg,proj_name)
    seq_id = get_seq_id(sg,proj_name,seq_name)

    shot_data = {
    'project': {"type":"Project","id": proj_id},
    'sg_sequence': {"type":"Sequence","id": seq_id},
    'code': shot_name,
    'description': desp,
    'sg_status_list': status
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
             'sg_task': {'type': 'Task', 'id': ids['task']},
             'user': {'type': 'HumanUser', 'id': user_id} }

    result = sg.create('Version', ver_data)
    pprint(result)


# create_seq(sg,proj_name,'seq_002','wtg','seq crated from API')
# create_shot(sg,proj_name,'seq_002','002_001','wtg','shot02 crated from API')

# test = list_shot2(sg,proj_name)
# test = list_project(sg)
# test = list_seq(sg,proj_name)
# create_version(sg,proj_name)
# test = get_shot_id(sg,proj_name,shot_name)

# test = get_proj_id(sg,proj_name)
# test = get_seq_id(sg,proj_name,seq_name)
# test = get_task_id(sg,proj_name,shot_name,"FX")
# test = get_user_id(sg,"fedej32881@tipent.com")
test = get_task_full_id(sg,proj_name,seq_name,shot_name,"FX")

pprint(test)
