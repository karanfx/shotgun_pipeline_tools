#Submit the concerns and reports
from PySide6 import QtWidgets
import PySide6.QtGui
import qdarkstyle
import os
import json
import shotgun_api3.shotgun as SG


import utils.sg_filters as sg_utils
import ui.create_version_ui_ui


#API KEY

# API KEY
from data.import_creds import SG_CRED
sg = SG_CRED()

#Email Form
class create_version(ui.create_version_ui_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(create_version,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier - Publish Version")
        self.setWindowIcon(PySide6.QtGui.QIcon("D:\\Work\\python_dev\\QT_project_launcher\\bin\\logo\\favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))

        # Populate Data
        self.populate_proj()
        self.Proj_CBx.currentTextChanged.connect(self.populate_shot)
        self.Shot_CBx.currentTextChanged.connect(self.populate_task)
        
        # Update version name
        self.Proj_CBx.currentTextChanged.connect(self.set_vers_name)
        self.Shot_CBx.currentTextChanged.connect(self.set_vers_name)
        self.task_CBx.currentTextChanged.connect(self.set_vers_name)

        self.vers_TB.clicked.connect(self.manual_dir)
        
        #Update publish button
        ok_button = self.Ok_Cancel_BBx.button(QtWidgets.QDialogButtonBox.Save)
        ok_button.setText("Publish")
        self.Ok_Cancel_BBx.accepted.connect(self.publish_version)
        

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
        # cur_seq = sg_utils.get_seq_id(sg,cur_proj,"seq_002")
        # print(cur_seq)

        vers_path = self.vers_LE.text()
        vers_name = self.Ver_name_LE.text()
        vers_desc = self.desc_TE.toPlainText()

        username = "tezz.y"
        status = "rev"

        # import utils.sg_filters as filter
        ids = sg_utils.get_task_full_id(sg,cur_proj,None,cur_shot,cur_task)
        # print(ids)
        sg_utils.create_version(sg,ids,username,vers_name,vers_path,status,vers_desc)

        print('Pubished')


    def manual_dir(self):
        man_path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if man_path:
            self.vers_LE.setText(man_path)

        if not man_path:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, pick the path")

    def set_vers_name(self):
        shot = self.Shot_CBx.currentText()
        task = self.task_CBx.currentText()
        vers = 'v001'

        self.Ver_name_LE.setText(shot + '_' + task + '_' + vers)
