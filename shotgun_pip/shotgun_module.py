import shotgun_api3

class ShotgunAPI:
    def __init__(self, site_url, script_name, script_key):
            self.sg = shotgun_api3.Shotgun(site_url, script_name, script_key)


    def _find_entities(self, entity_type, filters, fields):
        return self.sg.find(entity_type, filters, fields)
         

    class VFX:
        # def __init__(self, sg_key):
        #     self.sg = sg_key
         
        def __init__(self, site_url, script_name, script_key):
            self.sg = shotgun_api3.Shotgun(site_url, script_name, script_key)


        def _find_entities(self, entity_type, filters, fields):
            return self.sg.find(entity_type, filters, fields)
         
        # Common functions for all project types
        def get_sequences(self, project_name=None):
            sequence_filters = []
            sequence_fields = ["id", "code"]  # Add more fields as needed
            
            if project_name:
                sequence_filters.append(["project.Project.name", "is", project_name])
                
            return self._find_entities("Sequence", sequence_filters, sequence_fields)
        
        def get_shots(self, project_name=None, sequence_name=None):
            shot_filters = []
            shot_fields = ["id", "code", "sg_status"]  # Add more fields as needed
            
            if project_name:
                shot_filters.append(["project.Project.name", "is", project_name])
            if sequence_name:
                shot_filters.append(["sg_sequence.Sequence.code", "is", sequence_name])
                
            return self._find_entities("Shot", shot_filters, shot_fields)
        
        def get_tasks(self, project_name=None, sequence_name=None, shot_name=None):
            task_filters = []
            task_fields = ["id", "content", "sg_status"]  # Add more fields as needed
            
            if project_name:
                task_filters.append(["project.Project.name", "is", project_name])
            if sequence_name:
                task_filters.append(["entity.Shot.sg_sequence.Sequence.code", "is", sequence_name])
            if shot_name:
                task_filters.append(["entity.Shot.code", "is", shot_name])
                
            return self._find_entities("Task", task_filters, task_fields)
        
        def get_versions(self, project_name=None, sequence_name=None, shot_name=None):
            version_filters = []
            version_fields = ["id", "code", "description"]  # Add more fields as needed
            
            if project_name:
                version_filters.append(["project.Project.name", "is", project_name])
            if sequence_name:
                version_filters.append(["entity.Shot.sg_sequence.Sequence.code", "is", sequence_name])
            if shot_name:
                version_filters.append(["entity.Shot.code", "is", shot_name])
                
            return self._find_entities("Version", version_filters, version_fields)
        
        def get_entity_id_by_name(self, entity_type, entity_name, project_name=None):
            entity_filters = [["code", "is", entity_name]]
            entity_fields = ["id"]
            
            if project_name:
                entity_filters.append(["project.Project.name", "is", project_name])
                
            entity = self._find_entities(entity_type, entity_filters, entity_fields)
            if entity:
                return entity[0]["id"]
            else:
                return None
        
        def update_entity_details(self, entity_type, entity_id, data):
            # Placeholder for updating entity details
            pass

        # Project-specific functions for VFX projects
        def get_vfx_metadata(self, project_name=None):
            # Placeholder for getting VFX-specific metadata
            pass
        
        def create_vfx_shot(self, project_name, sequence_name, shot_data):
            # Placeholder for creating a VFX shot
            pass
        
        def update_vfx_shot(self, shot_id, updated_data):
            # Placeholder for updating a VFX shot
            pass

    class Episodic():

        def __init__(self, site_url, script_name, script_key):
            self.sg = shotgun_api3.Shotgun(site_url, script_name, script_key)


        def _find_entities(self, entity_type, filters, fields):
            return self.sg.find(entity_type, filters, fields)
         
        # Common functions for all project types
        def get_sequences(self, project_name=None):
            sequence_filters = []
            sequence_fields = ["id", "code"]  # Add more fields as needed
            
            if project_name:
                sequence_filters.append(["project.Project.name", "is", project_name])
                
            return self._find_entities("Sequence", sequence_filters, sequence_fields)
        
        def get_shots(self, project_name=None, sequence_name=None):
            shot_filters = []
            shot_fields = ["id", "code", "sg_status"]  # Add more fields as needed
            
            if project_name:
                shot_filters.append(["project.Project.name", "is", project_name])
            if sequence_name:
                shot_filters.append(["sg_sequence.Sequence.code", "is", sequence_name])
                
            return self._find_entities("Shot", shot_filters, shot_fields)
        
        def get_tasks(self, project_name=None, sequence_name=None, shot_name=None):
            task_filters = []
            task_fields = ["id", "content", "sg_status"]  # Add more fields as needed
            
            if project_name:
                task_filters.append(["project.Project.name", "is", project_name])
            if sequence_name:
                task_filters.append(["entity.Shot.sg_sequence.Sequence.code", "is", sequence_name])
            if shot_name:
                task_filters.append(["entity.Shot.code", "is", shot_name])
                
            return self._find_entities("Task", task_filters, task_fields)
        
        def get_versions(self, project_name=None, sequence_name=None, shot_name=None):
            version_filters = []
            version_fields = ["id", "code", "description"]  # Add more fields as needed
            
            if project_name:
                version_filters.append(["project.Project.name", "is", project_name])
            if sequence_name:
                version_filters.append(["entity.Shot.sg_sequence.Sequence.code", "is", sequence_name])
            if shot_name:
                version_filters.append(["entity.Shot.code", "is", shot_name])
                
            return self._find_entities("Version", version_filters, version_fields)
        # Project-specific functions for episodic projects
        def get_episodic_metadata(self, project_name=None):
            # Placeholder for getting episodic-specific metadata
            pass
        
        def create_episodic_shot(self, project_name, sequence_name, shot_data):
            # Placeholder for creating an episodic shot
            pass
        
        def update_episodic_shot(self, shot_id, updated_data):
            # Placeholder for updating an episodic shot
            pass

    class Game():
        # Project-specific functions for game projects
        def get_game_metadata(self, project_name=None):
            # Placeholder for getting game-specific metadata
            pass
        
        def create_game_asset(self, project_name, asset_data):
            # Placeholder for creating a game asset
            pass
        
        def update_game_asset(self, asset_id, updated_data):
            # Placeholder for updating a game asset
            pass






if __name__ == "__main__":
    
    import json
    #Import userID and tool dirs
    api_key = "E:\Work\python_dev\shotgun_pipeline\data\key.json"
    with open(api_key,"r") as uf:
        api_cred = json.load(uf)

    #Get Creds
    site = api_cred.get('SERVER_PATH')
    script_name = api_cred.get('SCRIPT_NAME')
    script_key = api_cred.get('SCRIPT_KEY')


    from pprint import pprint
    # SG = ShotgunAPI(site, script_name, script_key)

    # Retrieve data for a specific project, sequence, or shot (provide appropriate IDs)
    project_id = 122
    sequence_id = 41
    shot_id = 1174

    project_name="glacier_test_project"
    seq_name = "GTP_AB"
    shot_name="GTP_AB_001"

    # project_name= "Demo: Animation"
    # seq_name= "bunny_010"
    # print(SG.get_sequences(project_name="glacier_test_project"))

    # pprint(SG.get_shots(project_name=project_name))

    # pprint(SG.get_tasks(project_name=project_name,sequence_name=seq_name))
    # pprint(SG.VFX.get_shots(project_name,seq_name))

    # sg = ShotgunAPI(site,script_name,script_key)
    vfxproj = ShotgunAPI.VFX(site, script_name, script_key)

    # pprint(vfxproj.get_shots(project_name,seq_name))
    # pprint(vfxproj.get_tasks(project_name=project_name,sequence_name=seq_name,shot_name=shot_name))
    pprint(vfxproj.get_versions(project_name=project_name,sequence_name=seq_name,shot_name=shot_name))

    ep_project_name="test_episodic"
    ep_name = "episode_AA_001"
    ep_shot_name="AA_001_0100"

    ep_proj = ShotgunAPI.Episodic(site,script_name,script_key)

    ep_proj.get_shots(ep_project_name)