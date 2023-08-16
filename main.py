from typing import Optional
from PySide6 import QtWidgets,QtGui
import PySide6.QtCore
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
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))

        #Call/Trigger functions
        self.user_name = self.user_LE.text()

        self.populate_proj()
        self.toolssetup()
        # self.populate_task_by_artist()

        self.proj_lW.currentItemChanged.connect(self.populate_seq)
        self.proj_lW.currentItemChanged.connect(self.populate_task)
        self.task_treeWid.currentItemChanged.connect(self.setcur_task)
        self.Launch_PB.clicked.connect(self.opentool)

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

    def populate_task(self):
        self.task_treeWid.clear()
        user_name = self.user_LE.text()
        proj_name = self.proj_lW.currentItem().text()

        #Alternate mathods 
        # proj_items = self.proj_lW.selectedItems()
        # proj_name = [item.text() for item in proj_items]
        # proj_name = str(proj_name[0])
        
        shot = sg_utils.list_tasks(sg,proj_name,'001_001')
        
        for s in shot:
            # print(s)
            shot_list=[]
            for k,v in s.items():
                str(v)
                # print(v)
                shot_list.append(v)
                
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
        sel_task = [item.text(2) for item in sel_task]
        # sel_task = str(sel_task[2])
        print(sel_task)
        task = 'Current Task :'+ str(sel_task)
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


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    applaunch = sg_main()
    applaunch.show()
    app.exec()
