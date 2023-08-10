import shotgun_api3 as SG
import studio_globals
# SG.Shotgun.create()
import pprint


import api_key

sg = SG.Shotgun('https://testvfx.shotgrid.autodesk.com', 'testscript', 'byjzbl-abBmd3ohtpebhjkadu')
# sg = api_key.apikey()
result = sg.find(studio_globals.ENTITY_WIDGET,
                 filters=[['sg_status_list', 'is', 'ip']],
                 fields=['code', 'sg_shot'])
print(result)