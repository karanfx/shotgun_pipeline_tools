import shotgun_api3
class sgfunc:
    def __init__(self):
        self.sg_key = shotgun_api3.Shotgun(site_url, script_name, script_key)
        test_attri = "test parent attribute"
        #Get the API Cred 
        print('initialise')

    def _find_entities(self, entity_type, filters, fields):
            return self.sg_key.find(entity_type, filters, fields)
    
    def _find_one_entities(self, entity_type, filters, fields):
        return self.sg_key.find_one(entity_type, filters, fields)
    
    def _create_entities(self, entity_type, data):
            return self.sg_key.create(entity_type, data)
     
    def _update_entities(self, entity_type, filters, data):
            return self.sg_key.update(entity_type, filters, data)
    
    def _delete_entities(self, entity_type, filters, fields):
            return self.sg_key.delete(entity_type, filters, fields)
    #Populate the Functions

    def get_func():
        pass

    #Get functions to get the details about the task,shot,seq

    #Try to make a entity functions with can retriver all the required data and save it for later use

    #Functions to Create version, task, shot, seq

    #Functions to Update status and other details for particular task, shot, seq

    #Functions to delete all those stuff as well

    #
    def get_task():

        print('Tasks')

    class sg_vfx():
        def __init__(self):
            super().__init__()
            

        def vfx_shot():
            print('get the vfx_shot')


class sg_game(sgfunc):

    def game_asset():
        print('Game Asset')


class sg_episodic(sg_game):

    def ep_shot():
        print('Episodic shot')

# sgfunc

# sgfunc.get_task()

# sgfunc.sg_vfx.vfx_shot()

# sg_game.get_task()

# sg_game.game_asset()

# sg_episodic.get_task()

# sg_episodic.sg_vfx.vfx_shot()


# vfx_proj = sg_episodic.sg_vfx

# vfx_proj.vfx_shot()

class ParentClass:
    def __init__(self):
        self.parent_var = "parent test var"

    def parent_func(self):
        self.parent_var = "modified parent var"

    class ChildClass:
        def __init__(self, parent_instance):
            self.parent_instance = parent_instance  # Store a reference to the parent instance

        def child_func(self):
            # Access parent_var through the parent_instance
            parent_var = self.parent_instance.parent_var
            print("Child accessing parent_var:", parent_var)

# Create an instance of the parent class
parent_obj = ParentClass()

# Create an instance of the child class and pass the parent instance as an argument
child_obj = parent_obj.ChildClass(parent_obj)

# Access parent_var from the child class
child_obj.child_func()
