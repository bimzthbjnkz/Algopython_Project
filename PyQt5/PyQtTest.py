#connecting the module with layouts
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout

#creating an application object
app = QApplication([])

# creating the main window object
my_win = QWidget()

# creating the name of the main window
my_win.setWindowTitle('NIGGER')
# setting the point where the window will show up on the computer screen
my_win.move(400, 80)
# setting the window size
my_win.resize(1080, 700)

# creating a horizontal layout
line = QVBoxLayout()
hor_line = QHBoxLayout()
# line = QVBoxLayout()
line.setAlignment(Qt.AlignCenter)

# creating a text object
mylabel = QLabel('NIGGER')
second_label = QLabel('NIGGER')
third_label = QLabel('NIGGER')

# set title size
mylabel.setStyleSheet("font-size: 30px; font-weight: bold; color: black;")
second_label.setStyleSheet("font-size: 30px; font-weight: bold; color: black;")
third_label.setStyleSheet("font-size: 30px; font-weight: bold; color: black;")

# putting the text on the center of the layout
line.addWidget(mylabel)
line.addWidget(second_label)
line.setSpacing(20)

hor_line.addWidget(third_label, alignment=Qt.AlignCenter)
line.addLayout(hor_line)

# adding the resulting line to the application window
my_win.setLayout(line)

# giving the window the command to show up
my_win.show()
app.exec()
