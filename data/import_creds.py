import json
import shotgun_api3 as SG

def SG_CRED():
    #API KEY
    cred_file = "E:/Work/python_dev/Glacier_shotgun_Tools/creds/key.json"

    with open(cred_file,'r') as cred:
        creds = json.load(cred)

    SERVER = creds.get('SERVER_PATH')
    SCRIPT_NAME = creds.get('SCRIPT_NAME')
    API_KEY = creds.get('SCRIPT_KEY')

    sg = SG.Shotgun(SERVER, SCRIPT_NAME, API_KEY)
    return sg