import PySimpleGUI as user_interface
from zipCreator import make_archives

label1 = user_interface.Text("Select files to compress")
user_input1 = user_interface.Input(key="file_display")
choose_btn1 = user_interface.FilesBrowse("Choose", key="filepath")

label2 = user_interface.Text("Select destination folder")
user_input2 = user_interface.Input(key="folder_dis")
choose_btn2 = user_interface.FolderBrowse("Choose", key="folder_path")

compress_btn = user_interface.Button("Compress")
output = user_interface.Text(key="dis")

layout = [[label1, user_input1, choose_btn1], [label2, user_input2, choose_btn2], [compress_btn, output]]

windows = user_interface.Window("File Compressor", layout, font=("Helvetica", 16))

while True:
    event, value = windows.read()
    print(event)
    print(value)

    filepath = value['filepath'].split(";")
    folderPath = value['folder_path']
    make_archives(filepath, folderPath)
    windows['dis'].update(value="Compression Successful")



windows.close()
