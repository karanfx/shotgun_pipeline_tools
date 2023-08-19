from typing import Optional
from PySide6 import QtWidgets,QtGui
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import qdarkstyle
import os
import json
import shotgun_api3.shotgun as SG

import ui.main_window
import utils.sg_filters as sg_utils

#API KEY
sg = SG.Shotgun('https://testvfx.shotgrid.autodesk.com', 'testscript', 'byjzbl-abBmd3ohtpebhjkadu')


class sg_main(ui.main_window.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(sg_main,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier - Shotgun API Tool")
        self.setWindowIcon(PySide6.QtGui.QIcon("D:\\Work\\python_dev\\QT_project_launcher\\bin\\logo\\favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))

        #Call/Trigger functions
        self.user_name = self.user_LE.text()

        self.populate_proj()
        self.toolssetup()
        
        # self.populate_task_by_artist()

        self.proj_lW.currentItemChanged.connect(self.populate_seq)
        self.seq_lW.currentItemChanged.connect(self.populate_shot)
        self.Shot_LW.currentItemChanged.connect(self.populate_task)
        self.task_treeWid.currentItemChanged.connect(self.setcur_task)
        self.Launch_PB.clicked.connect(self.opentool)

        # Config Action buttions
        self.action_publish_version.triggered.connect(self.create_version)
        self.action_publish_assets.triggered.connect(self.publish_asset)

    def populate_proj(self):
        self.proj_lW.clear()
        proj_id = sg_utils.list_project(sg)
        proj_name = []
        for p in proj_id:
            proj_name.append(p['name'])

        self.proj_lW.addItems(proj_name)

    def populate_seq(self):
        self.seq_lW.clear()
        proj_name = self.proj_lW.currentItem().text()
  
        seq = sg_utils.list_seq(sg,proj_name)
        seq_list = []
        for s in seq:
            seq_list.append(s['code'])
        # print(seq_list)

        self.seq_lW.addItems(seq_list)

    def populate_shot(self):
        self.Shot_LW.clear()
        proj_name = self.proj_lW.currentItem().text()
        seq_name = self.seq_lW.currentItem().text()
  
        seq = sg_utils.list_shot(sg,proj_name,seq_name)
        shot_list = []
        for s in seq:
            shot_list.append(s['code'])
        # print(shot_list)

        self.Shot_LW.addItems(shot_list)

    def populate_task(self):
        self.task_treeWid.clear()
        user_name = self.user_LE.text()
        proj_name = self.proj_lW.currentItem().text()
        shot_name = self.Shot_LW.currentItem().text()

        #Alternate mathods 
        # proj_items = self.proj_lW.selectedItems()
        # proj_name = [item.text() for item in proj_items]
        # proj_name = str(proj_name[0])
        
        shot = sg_utils.list_tasks(sg,proj_name,shot_name)
        
        for s in shot:
            # print(s)
            shot_list=[]
            for k,v in s.items():
                str(v)
                # print(v)
                shot_list.append(v)
                
            #Format Task List
            shot_list.pop(0)
            shot_list.insert(0,shot_list[1])
            shot_list.pop(1)
            print(shot_list)

            item = QtWidgets.QTreeWidgetItem(list(shot_list))
            self.task_treeWid.addTopLevelItem(item)

    def populate_task_by_artist(self):
        self.task_treeWid.clear()
        user_name = 'ramesh.r'
        # user_name = self.user_LE.text()
        
        # proj_items = self.proj_lW.selectedItems()
        
        # proj_name = [item.text() for item in proj_items]
        # proj_name = str(proj_name[0])
        
        # shot = sg_utils.list_tasks(sg,proj_name,'001_001')
        task = sg_utils.get_tasks_by_artist(sg,user_name)
        
        # for s in task:
        #     print(s)
        #     shot_list=[]
        #     for k,v in s.items():
        #         str(v)
        #         # print(v)
        #         shot_list.append(v)
                
        #     # print(shot_list)
        #     item = QtWidgets.QTreeWidgetItem(list(shot_list))
        #     self.task_treeWid.addTopLevelItem(item)
        print(task)
        item = QtWidgets.QTreeWidgetItem(list(task))
        self.task_treeWid.addTopLevelItem(item)

    def setcur_task(self):
        # sel_task = self.task_treeWid.currentItem()
        sel_task = self.task_treeWid.selectedItems()
        sel_task = [item.text(0) for item in sel_task]
        print(sel_task)
        task = 'Current Task :   '+ str(sel_task[0])
        self.sel_task_LB.setText(task)

    def toolssetup(self):
        tooldata ={"Houdini": "C:/Program Files/Side Effects Software/Houdini 18.5.596/bin/houdinifx.exe",
                    "Blender" : "C:/Program Files/Blender Foundation/Blender 3.4/blender-launcher.exe",
                    "Unreal" : "C:/Program Files/Epic Games/UE_5.1/Engine/Binaries/Win64/UnrealEditor.exe",
                    "Discord" : "C:/Users/PERMAN/AppData/Local/Discord/Update.exe"}
        self.soft_CB.addItems(tooldata)    
    
    def opentool(self):
        tooldata ={"Houdini": "C:/Program Files/Side Effects Software/Houdini 18.5.596/bin/houdinifx.exe",
                    "Blender" : "C:/Program Files/Blender Foundation/Blender 3.4/blender-launcher.exe",
                    "Unreal" : "C:/Program Files/Epic Games/UE_5.1/Engine/Binaries/Win64/UnrealEditor.exe",
                    "Discord" : "C:/Users/PERMAN/AppData/Local/Discord/Update.exe"}
        toolname = self.soft_CB.currentText()
        
        os.startfile(tooldata[toolname]) 

    def create_version(self):
        import utils.create_version 
        vers_dlg = utils.create_version.create_version()
        vers_dlg.exec()

    def publish_asset(self):
        import utils.publish_asset 
        vers_dlg = utils.publish_asset.publish_asset()
        vers_dlg.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    applaunch = sg_main()
    applaunch.show()
    app.exec()
