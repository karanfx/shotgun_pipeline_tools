#Submit the concerns and reports
from PySide6 import QtWidgets
import PySide6.QtGui
import qdarkstyle
import os
import json
import shotgun_api3.shotgun as SG

import utils.sg_filters as sg_utils
import ui.publish_asset_ui_ui


#API KEY

# API KEY
from data.import_creds import SG_CRED
sg = SG_CRED()


#Email Form
class publish_asset(ui.publish_asset_ui_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(publish_asset,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier - Publish Version")
        self.setWindowIcon(PySide6.QtGui.QIcon("D:\\Work\\python_dev\\QT_project_launcher\\bin\\logo\\favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))


        # Populate Data
        self.populate_proj()
        self.Proj_CBx.currentTextChanged.connect(self.populate_asset)
        self.Asset_CBx.currentTextChanged.connect(self.populate_task)
        
        # Update version name
        self.Proj_CBx.currentTextChanged.connect(self.set_vers_name)
        self.Asset_CBx.currentTextChanged.connect(self.set_vers_name)
        self.asset_type_CBx.currentTextChanged.connect(self.set_vers_name)

        self.asset_path_TB.clicked.connect(self.manual_dir)
        
        #Update publish button
        ok_button = self.Ok_Cancel_BBx.button(QtWidgets.QDialogButtonBox.Save)
        ok_button.setText("Publish")
        self.Ok_Cancel_BBx.accepted.connect(self.publish_asset)
        

    def populate_proj(self):
        self.Proj_CBx.clear()
        proj_id = sg_utils.list_project(sg)
        proj_name = []
        for p in proj_id:
            proj_name.append(p['name'])

        self.Proj_CBx.addItems(proj_name)

    def populate_asset(self):
        self.Asset_CBx.clear()
        proj_name = self.Proj_CBx.currentText()
  
        # seq = sg_utils.list_all_shot(sg,proj_name)
        seq = sg_utils.list_assets(sg,proj_name)
        seq_list = []
        for s in seq:
            seq_list.append(s['code'])
        # print(seq_list)

        self.Asset_CBx.addItems(seq_list)

    def populate_task(self):
        self.asset_type_CBx.clear()
        user_name = "ramesh.r"
        proj_name = self.Proj_CBx.currentText()
        shot_name = self.Asset_CBx.currentText()

        #Alternate mathods 
        # proj_items = self.proj_lW.selectedItems()
        # proj_name = [item.text() for item in proj_items]
        # proj_name = str(proj_name[0])
        
        shot = sg_utils.list_asset_tasks(sg,proj_name,shot_name)
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
        
        self.asset_type_CBx.addItems(shot_list)
       


    def publish_asset(self):

        cur_proj = self.Proj_CBx.currentText()
        cur_asset = self.Asset_CBx.currentText()
        cur_task = self.asset_type_CBx.currentText()

        vers_path = self.asset_path_LE.text()
        vers_name = self.asset_name_LE.text()
        vers_desc = self.desc_TE.toPlainText()

        username = "ramesh.r"
        status = "rev"
        sg_utils.create_asset(sg,cur_proj,cur_asset,cur_task,username,vers_name,vers_path,status,vers_desc)

        print('Published')
        # import utils.sg_filters as filter
        # ids = filter.get_task_full_id(sg,cur_proj,"",cur_shot,cur_task)
        # filter.create_version(sg,ids,username,vers_name,vers_path,status,vers_desc)


    def manual_dir(self):
        man_path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if man_path:
            self.asset_path_LE.setText(man_path)

        if not man_path:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, pick the path")

    def set_vers_name(self):
        shot = self.Asset_CBx.currentText()
        task = self.asset_type_CBx.currentText()
        vers = 'v001'

        self.asset_name_LE.setText(shot + '_' + task + '_' + vers)
