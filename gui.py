import PySimpleGUI as user_interface

label1 = user_interface.Text("Select files to compress")
user_input1 = user_interface.Input()
choose_btn1 = user_interface.FilesBrowse("Choose")

label2 = user_interface.Text("Select destination folder")
user_input2 = user_interface.Input()
choose_btn2 = user_interface.FilesBrowse("Choose")

compress_btn = user_interface.Button("Compress")

layout = [[label1, user_input1, choose_btn1], [label2, user_input2, choose_btn2], [compress_btn]]

windows = user_interface.Window("File Compressor", layout)

windows.read()
windows.close()
