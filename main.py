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
        self.populate_proj()

        self.proj_lW.currentItemChanged.connect(self.populate_seq)
        self.proj_lW.currentItemChanged.connect(self.populate_task)

    def populate_proj(self):
        self.proj_lW.clear()
        proj_id = sg_utils.list_project(sg)
        proj_name = []
        for p in proj_id:
            proj_name.append(p['name'])

        self.proj_lW.addItems(proj_name)

    def populate_seq(self):
        self.seq_lW.clear()
        proj_items = self.proj_lW.selectedItems()
        
        proj_name = [item.text() for item in proj_items]
        proj_name = str(proj_name[0])
        
        seq = sg_utils.list_seq(sg,proj_name)
        seq_list = []
        for s in seq:
            seq_list.append(s['code'])
        print(seq_list)

        self.seq_lW.addItems(seq_list)

    def populate_task(self):
        self.task_treeWid.clear()
        proj_items = self.proj_lW.selectedItems()
        
        proj_name = [item.text() for item in proj_items]
        proj_name = str(proj_name[0])
        
        shot = sg_utils.list_shot(sg,proj_name)
        
        for s in shot:
            print(s)
            shot_list=[]
            for k,v in s.items():
                print(v)
                shot_list.append(v)
                
            print(shot_list)
            item = QtWidgets.QTreeWidgetItem(list(shot_list))
            self.task_treeWid.addTopLevelItem(item)
        # print(seq_list)

        



if __name__ == "__main__":
    app = QtWidgets.QApplication()
    applaunch = sg_main()
    applaunch.show()
    app.exec()
