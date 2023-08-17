#Submit the concerns and reports
from PySide6 import QtWidgets
import PySide6.QtGui
import qdarkstyle
import os
import json
import shotgun_api3.shotgun as SG

import utils.sg_filters as sg_utils
import ui.create_version_ui_ui

sg = SG.Shotgun('https://testvfx.shotgrid.autodesk.com', 'testscript', 'byjzbl-abBmd3ohtpebhjkadu')


#Email Form
class create_version(ui.create_version_ui_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(create_version,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Report")
        self.setWindowIcon(PySide6.QtGui.QIcon("D:\\Work\\python_dev\\QT_project_launcher\\bin\\logo\\favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))

        self.Ok_Cancel_BBx.accepted.connect(self.publish_version)

        self.populate_proj()
        self.Proj_CBx.currentTextChanged.connect(self.populate_shot)
        self.Shot_CBx.currentTextChanged.connect(self.populate_task)
        
    # def populate_project(self):
    #     prodirs = [ name for name in os.listdir(studio_dir) if os.path.isdir(os.path.join(studio_dir, name)) ]
    #     self.project_cB.addItems(prodirs)

    def populate_proj(self):
        self.Proj_CBx.clear()
        proj_id = sg_utils.list_project(sg)
        proj_name = []
        for p in proj_id:
            proj_name.append(p['name'])

        self.Proj_CBx.addItems(proj_name)

    def populate_shot(self):
        self.Shot_CBx.clear()
        proj_name = self.Proj_CBx.currentText()
  
        seq = sg_utils.list_all_shot(sg,proj_name)
        seq_list = []
        for s in seq:
            seq_list.append(s['code'])
        # print(seq_list)

        self.Shot_CBx.addItems(seq_list)

    def populate_task(self):
        self.task_CBx.clear()
        user_name = "ramesh.r"
        proj_name = self.Proj_CBx.currentText()
        shot_name = self.Shot_CBx.currentText()

        #Alternate mathods 
        # proj_items = self.proj_lW.selectedItems()
        # proj_name = [item.text() for item in proj_items]
        # proj_name = str(proj_name[0])
        
        shot = sg_utils.list_tasks(sg,proj_name,shot_name)
        shot_list = []
        for s in shot:
            # print(s)
            s_list=[]
            for k,v in s.items():
                str(v)
                # print(v)
                s_list.append(v)
            
            shot_list.append(s_list[2])
        print(shot_list)
        
        self.task_CBx.addItems(shot_list)
            # item = QtWidgets.QTreeWidgetItem(list(shot_list))
            # self.task_treeWid.addTopLevelItem(item)

    # def populate_task_by_artist(self):
    #     self.task_treeWid.clear()
    #     user_name = 'ramesh.r'
    #     # user_name = self.user_LE.text()
        
    #     # proj_items = self.proj_lW.selectedItems()
        
    #     # proj_name = [item.text() for item in proj_items]
    #     # proj_name = str(proj_name[0])
        
    #     # shot = sg_utils.list_tasks(sg,proj_name,'001_001')
    #     task = sg_utils.get_tasks_by_artist(sg,user_name)
        
    #     # for s in task:
    #     #     print(s)
    #     #     shot_list=[]
    #     #     for k,v in s.items():
    #     #         str(v)
    #     #         # print(v)
    #     #         shot_list.append(v)
                
    #     #     # print(shot_list)
    #     #     item = QtWidgets.QTreeWidgetItem(list(shot_list))
    #     #     self.task_treeWid.addTopLevelItem(item)
    #     print(task)
    #     item = QtWidgets.QTreeWidgetItem(list(task))
    #     self.task_treeWid.addTopLevelItem(item)


    def publish_version(self):

        cur_proj = self.Proj_CBx.currentText()
        cur_shot = self.Shot_CBx.currentText()
        cur_task = self.task_CBx.currentText()

        vers_path = self.vers_LE.text()
        vers_name = self.Ver_name_LE.text()
        vers_desc = self.desc_TE.toPlainText()

        username = "ramesh.r"
        status = "rev"

        import utils.sg_filters as filter
        ids = filter.get_task_full_id(sg,cur_proj,"",cur_shot,cur_task)
        filter.create_version(sg,ids,username,vers_name,vers_path,status,vers_desc)


            