# -*- coding:utf-8 -*-

__nom_fichier__ = "interface"
__author__ = "Capucine"
__date__ = "mai 2018"

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from searchBySymptom import *
from searchBySE import *

class GuiDisease(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Search diseases from symptoms")

        self.label_symptoms_ = QLabel("Which symptoms you have?", self)
        self.label_symptoms_.setAlignment(Qt.AlignCenter)
        self.edit_symptoms_ = QLineEdit(self)
        self.edit_symptoms_.setText("")

        self.label_side_effect_ = QLabel("Which side effect you have?", self)
        self.label_side_effect_.setAlignment(Qt.AlignCenter)
        self.edit_side_effect_ = QLineEdit(self)
        self.edit_side_effect_.setText("")

        self.b_search_symptoms_ = self.create_button("Search diseases from symptoms only", self.search_disease)
        self.b_search_side_effect_ = self.create_button("Search diseases from side effect only", self.search_meds)
        self.b_search_both_ = self.create_button("If you don't know, click on this button", self.search_both)

        self.b_reset_ = self.create_button("Clear", self.reset)
        self.b_quit_ = self.create_button("Quit", qApp.quit)

        mon_layout = QGridLayout()

        mon_layout.addWidget(self.label_symptoms_, 0, 0)
        mon_layout.addWidget(self.edit_symptoms_, 0, 1)
        mon_layout.addWidget(self.label_side_effect_, 1, 0)
        mon_layout.addWidget(self.edit_side_effect_, 1, 1)

        mon_layout.addWidget(self.b_search_symptoms_, 2, 0)
        mon_layout.addWidget(self.b_search_side_effect_, 2, 1)
        mon_layout.addWidget(self.b_search_both_, 3, 0, 1, 2)

        mon_layout.addWidget(self.b_reset_, 4, 0)
        mon_layout.addWidget(self.b_quit_, 4, 1)

        self.setLayout(mon_layout)

    def create_button(self, libelle, method):
        """
        @param libelle: libelle print on the buttom
        @param method:  methode to link a buttom
        @return:        the linked buttom
        """
        button = QPushButton(libelle, self)
        button.clicked.connect(method)
        return button

    def search_disease(self):
        res = searchDisease(self.edit_symptoms_.text())
        QMessageBox.information(GuiDisease(), "Results", "Overview of the results, please look at the result.csv file for more information : " + str(res[0]))

    def search_meds(self):
        res = searchSE(self.edit_side_effect_.text())
        QMessageBox.information(GuiDisease(), "Résultat", "Overview of the results, please look at the resultSE.csv file for more information :  " + str(res[0]))

    def search_both(self):
        res_symptome = searchDisease(self.edit_symptoms_.text())
        res_SE = searchSE(self.edit_side_effect_.text())
        QMessageBox.information(GuiDisease(), "Results", "Overview of the results, please look at the csv files for more information : " + str(res_symptome[0]) + "\n" + str(res_SE[0]))

    def reset(self):
        """
        @return: deleted the scene
        """

        self.edit_symptoms_.clear()
        self.edit_side_effect_.clear()

    def quitter(self):
        """
        :return: close the window
        """
        self.reinitialisation_reseau()
        qApp.quit()


def main():
    app = QApplication([])

    gui = GuiDisease()

    gui.show()

    r = app.exec_()

    return r


if __name__ == "__main__":
    main()
