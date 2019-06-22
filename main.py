# Greg's Branch

from pytube import YouTube as yt
import os
import time
import numpy as np
import pickle
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem

# Gets the current working directory before the program runs
cwd = os.getcwd()


# -------------------- Function definitions --------------------
# Creates data folder, and subfolders
def create_data_folder():
    data_folder = cwd + "/data"
    if not os.path.isdir(data_folder):
        os.makedirs(data_folder)

    img_folder = data_folder + "/img"
    if not os.path.isdir(img_folder):
        os.makedirs(img_folder)

    audio_folder = data_folder + "/audio"
    if not os.path.isdir(audio_folder):
        os.makedirs(audio_folder)


# Saves dictionary passed
def save_dict(temp_dict):
    with open(cwd + '/data/data.dat', 'wb') as fp:
        pickle.dump(temp_dict, fp)


# Loads dictionary passed
def load_dict():
    with open(cwd + '/data/data.dat', 'rb') as f:
        out_dict = pickle.load(f)
        return out_dict


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeRowsToContents()
        self.resizeColumnsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(n, m, newitem)
        self.setHorizontalHeaderLabels(horHeaders)


# Displays the GUI
def app():
    main_app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Testing this mug")
    # layout = QVBoxLayout()
    # layout.addWidget(QPushButton('Top'))
    # layout.addWidget(QPushButton('Bottom'))
    # window.setLayout(layout)
    window.show()
    main_app.exec_()


# -------------------- Start of main program --------------------
create_data_folder()
# app()
# my_dict = {
#     'Name1': {'Name': 'Nightcore - Destiny', 'URL': 'https://www.youtube.com/watch?v=3caAitEusSw'},
#     'Name2': {'Name': 'Nightcore - BLACKOUT', 'URL': 'https://www.youtube.com/watch?v=HZYihvoBBGw'}
# }
# my_dict = {
#     'ID1': ['Nightcore - Destiny', 'https://www.youtube.com/watch?v=3caAitEusSw'],
#     'ID2': ['Nightcore - BLACKOUT', 'https://www.youtube.com/watch?v=HZYihvoBBGw']
# }



save_dict("")
try:
    my_dict_2 = load_dict()

except TypeError:
    print("No file or data in file")

app = QApplication(sys.argv)
table = TableView(my_dict_2, 2, 2)
table.show()
sys.exit(app.exec_())

# # File name for text file with YouTube links to download
# infile_name = "YouTube Download Audio.txt"
#
# if os.path.exists(infile_name) == True:
#     # Gets Current Working Directory
#     cwd = os.getcwd()
#     file_object = open(infile_name, "r")
#
#     # Reads first line for save directory
#     line = file_object.readline()
#     line = line.rstrip()
#
#     # Checks for new subdirectory in cwd
#     if ((line[0] == "\\") or (line[0] == "/")):
#         temp_dir = cwd + line
#         # If user input directory doesn't exist, it will be created
#         if (os.path.isdir(temp_dir) == False):
#             print("Folder does not exist. Created:\n" + os.path.normpath(temp_dir))
#             # Can make multiple subdirectories
#             os.makedirs(temp_dir)
#
#         print("Sub Directory")
#         working_dir = temp_dir
#     elif (os.path.isdir(line) == True):
#         print("Custom Directory")
#         working_dir = line
#     else:
#         # Creates default working directory
#         default_dir = cwd + "\Downloads"
#         print("No download directory specified.")
#         # If default directory doesn't exist, create it
#         if (os.path.isdir(default_dir) == False):
#             print("Creating default directory:\n" + default_dir)
#             os.mkdir(default_dir)
#         else:
#             print("Using default directory.")
#         working_dir = default_dir
#         file_object.close()
#         file_object = open(infile_name, "r")
#
#     # Loop spanning the number of lines in the text file
#     for line in file_object:
#         line = line.rstrip()  # Removes newline character from line
#         test_title = yt(line).title
#         temp = False
#         # Gets number of files in the working directory
#         num_dir_files = len(next(os.walk(working_dir))[2])
#         # Loop checing every filename in directory
#         for j in range(0, num_dir_files):
#             # Resets temp value
#             temp = True
#             # print(test_title[j], next(os.walk(working_dir))[2][j])
#             # Loop checking spanning the length of the videoname
#             for k in range(0, len(test_title)):
#                 # print(test_title[k], next(os.walk(working_dir))[2][j][k])
#                 if (test_title[k] != next(os.walk(working_dir))[2][j][k]):
#                     temp = False
#                     break
#             # If Youtube video name is found in file name
#             if (temp == True):
#                 print(test_title)
#                 print("Already Exists!")
#                 break
#         # Downlaods audio if not found
#         if (temp == False):
#             print(test_title)
#             print("Downloading...")
#             start = time.time()
#             # print(yt(line).streams.filter(only_audio = True, ).order_by('abr').desc().all())
#             yt(line).streams.filter(only_audio=True).order_by('abr').desc().first().download(working_dir)
#             end = time.time()
#             print("Downloaded! (took " + "{0:.2f}".format(round(end - start, 2)) + "s)")
#
#     file_object.close()
#
#     start = time.time()
#
#
#
# else:
#     file_object = open(infile_name, "w+")
#     print("Input Text File Created.")
#     file_object.close()
