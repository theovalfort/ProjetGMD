# -*- coding:utf-8 -*-

__nom_fichier__ = "interface"
__author__ = "Capucine"
__date__ = "mai 2018"

import PyQt5.QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GuiDisease(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        PyQt5.QtWidgets.QWidget.__init__(self)

        self.setWindowTitle("Search diseases from symptoms")

        self.label_symptoms_ = PyQt5.QtWidgets.QLabel("Which symptoms you have?", self)
        self.label_symptoms_.setAlignment(Qt.AlignCenter)
        self.edit_symptoms_ = PyQt5.QtWidgets.QLineEdit(self)
        self.edit_symptoms_.setText(" ")

        self.label_side_effect_ = PyQt5.QtWidgets.QLabel("Which side effect you have?", self)
        self.label_side_effect_.setAlignment(Qt.AlignCenter)
        self.edit_side_effect_ = PyQt5.QtWidgets.QLineEdit(self)
        self.edit_side_effect_.setText(" ")

        self.b_search_symptoms_ = self.create_button("Search diseases from symptoms only", self.search_disease)
        self.b_search_side_effect_ = self.create_button("Search diseases from side effect only", self.search_meds)
        self.b_search_both_ = self.create_button("If you don't know, click on this button", self.search_both)

        self.b_reset_ = self.create_button("Clear", self.reset)
        self.b_quit_ = self.create_button("Quit", PyQt5.QtWidgets.qApp.quit)

        mon_layout = PyQt5.QtWidgets.QGridLayout()

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
        @param libelle: libelle affiche sur le bouton
        @param method:  methode a lier au bouton
        @return:        le bouton auquel on a attache la méthode
        """
        button = PyQt5.QtWidgets.QPushButton(libelle, self)
        button.clicked.connect(method)
        return button

    def search_disease(self):
        res = 0
        PyQt5.QtWidgets.QMessageBox.information(GuiDisease(), "Résultat", "Test : " + str(res))

    def search_meds(self):
        res = 1
        PyQt5.QtWidgets.QMessageBox.information(GuiDisease(), "Résultat", "Test : " + str(res))

    def search_both(self):
        res = 2
        PyQt5.QtWidgets.QMessageBox.information(GuiDisease(), "Résultat", "Test : " + str(res))

    def reset(self):
        """
        @return: efface la scene de dessin
        """

        self.edit_symptoms_.clear()
        self.edit_side_effect_.clear()

    def quitter(self):
        """
        :return: fermer l'interface et réinitialiser le réseau
        """
        self.reinitialisation_reseau()
        PyQt5.QtWidgets.qApp.quit()


def main():
    app = PyQt5.QtWidgets.QApplication([])

    gui = GuiDisease()

    gui.show()

    r = app.exec_()

    return r


if __name__ == "__main__":
    main()
