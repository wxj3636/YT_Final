from pytube import YouTube as yt
import os
import time

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def app():
    main_app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Testing this mug")
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()
    main_app.exec_()


app()
print("TEST")


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
