import FreeSimpleGUI as fg
from Function_for_zip import extract_zip


layout1 = fg.Text("Select Zip file")
input_box1 = fg.InputText(tooltip = "choose a ZIP file", key = "zipfile")
button1 = fg.FileBrowse("choose", tooltip = "choose a zip file to extract")

layout2 = fg.Text("Select Extract Folder")
input_box2 = fg.InputText(tooltip = "choose a folder to extract to", key = "extractfolder")
button2 = fg.FolderBrowse("choose", tooltip = "choose a folder to extract to")

window = fg.Window("ZIP Extractor",
                   layout = [[layout1, input_box1, button1],
                             [layout2, input_box2, button2],
                             [fg.Button("Extract"), fg.Button("Exit")]])

while True:
    event, values = window.read()
    zip_path = values["zipfile"]
    extract_to = values["extractfolder"]
    extract_zip(zip_path, extract_to)
    fg.popup("Extraction Completed!")


window.close()