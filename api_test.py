import shotgun_api3.shotgun as SG
import studio_globals
import logging
from pprint import pprint

# studio_globals.py

entity_type_map = {
  'Widget': 'CustomEntity01',
  'Foobar': 'CustomEntity02',
  'Baz': 'CustomNonProjectEntity01',
}

# or even simpler, you could use a global like this
ENTITY_WIDGET = 'CustomEntity01'
ENTITY_FOOBAR = 'CustomEntity02'
ENTITY_BAZ = 'CustomNonProjectEntity01'


sg = SG.Shotgun('https://testvfx.shotgrid.autodesk.com', 'testscript', 'byjzbl-abBmd3ohtpebhjkadu')

# result = sg.find(studio_globals.ENTITY_WIDGET,
#                  filters=[['sg_status_list', 'is', 'ip']],
#                  fields=['code', 'sg_shot'])
# # print(result)

# filters = [['id', 'is', 1174]]
# result = sg.find_one('Shot', filters)
# pprint.pprint(result)

# data = {'project': {'type': 'glacier_test_project','id': 122},
#         'code': '001_002',
#         'description': 'test shot from api',
#         'task_template': '' }

#Create Shot 
shot_data = {
        "project": {"type": "Project", "id": 122},
        "sg_sequence": {"type": "Sequence", "id": 41},
        "code": "001_002",
        'sg_status_list': "ip"
    }

# result = sg.create('Shot', shot_data)

seq_data = {
        "project": {"type": "Project", "id": 122},
        "sg_sequence": {"type": "Sequence", "id": 41},
        "code": "001_002",
        'sg_status_list': "ip"
    }

#Find the Shot
shot_filter = [ ['project', 'is', {'type': 'Project', 'id': 122}],
            ["sg_sequence",'is', {"type": "Sequence", "id": 41}],
            ['code', 'is', '001_001'] ]

shot = sg.find_one('Shot',shot_filter)

#Find the Task
task_filter = [ ['project', 'is', {'type': 'Project', 'id': 122}],
            ['entity', 'is',{'type':'Shot', 'id': shot['id']}],
            ['content', 'is', 'FX'] ]

task = sg.find_one('Task',task_filter)

pprint(shot)
pprint(task)

# #Create a version
# ver_data = { 'project': {'type': 'Project','id': 122},
#          'code': '001_002_anim_v02',
#          'description': 'version from api',
#          'sg_path_to_frames': 'D:/test_seq/test_explosion_v012.mp4',
#          'sg_status_list': 'rev',
#          'entity': {'type': 'Shot', 'id': shot['id']},
#          'sg_task': {'type': 'Task', 'id': task['id']},
#          'user': {'type': 'HumanUser', 'id': 121} }

# result = sg.create('Version', ver_data)
# pprint(result)


# # Get shot codes and sequence status all in one query
# project_name = 'glacier_test_project'
# sg_shots = sg.find("Shot", [['project.Project.name', 'is', project_name]],
#                    ['code', 'sg_sequence.Sequence.sg_status_list'])
# pprint(sg_shots)


# result = sg.schema_field_read('Asset', 'shots')
# pprint(result)

# #get SG Info
# pprint.pprint(sg.info())

# pprint.pprint([symbol for symbol in sorted(dir(sg)) if not symbol.startswith('_')])