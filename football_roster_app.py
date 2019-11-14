import sys
import re
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from arrange_team import Player, OFFENSE, DEFENSE, ST

COLLEGES_FOR_TEAM = "Colleges for Team"
GRADE_FOR_TEAM = "Grade for Team"
PLAYERS_FOR_COLLEGE = "Players for College"

QB = "QB"

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Football Roster")

        self.mode_box = QComboBox()
        self.mode_box.addItems([COLLEGES_FOR_TEAM, GRADE_FOR_TEAM, PLAYERS_FOR_COLLEGE])
        # self.mode_box.currentIndexChanged.connect(self.mode_changed)

        self.team_box = QComboBox()
        self.team_box.addItems(get_teams())
        # self.team_box.currentIndexChanged.connect(self.team_changed)

        self.go_button = QPushButton('Go')
        self.go_button.clicked.connect(self.pushed_button)

        self.label = QLabel('')
        self.label.setAlignment(Qt.AlignCenter)

        main_widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.mode_box)
        layout.addWidget(self.team_box)
        layout.addWidget(self.go_button)
        layout.addWidget(self.label)

        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)
        self.show()

    def pushed_button(self):
        team_name = self.team_box.currentText().split()[-1]
        team_file = team_name + ".p"
        team = pickle.load(open(team_file, "rb"))

        # self.label.setText(self.team_box.currentText())
        self.label.setText(team[OFFENSE][QB][0].name)
        self.label.repaint()


def get_teams():
    teams = []
    with open("teams.txt", "r") as file:
        teams = [t.rstrip() for t in file.readlines()]
    return teams


def football_app():
    app = QApplication([])
    window = MainWindow()

    app.exec_()


if __name__ == '__main__':
    football_app()
