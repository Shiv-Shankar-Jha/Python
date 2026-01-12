import FreeSimpleGUI as fg
from Function_for_zip import extract_zip


layout1 = fg.Text("Select Zip file")
input_box1 = fg.InputText(tooltip = "choose a ZIP file", key = "zipfile")
button1 = fg.FileBrowse("choose", tooltip = "choose a zip file to extract")

layout2 = fg.Text("Select Extract Folder")
input_box2 = fg.InputText(tooltip = "choose a folder to extract to", key = "extractfolder")
button2 = fg.FolderBrowse("choose", tooltip = "choose a folder to extract to")

extract_button = fg.Button("Extract")
output_label = fg.Text(key="output", text_color="green")

column1 = fg.Column([[layout1, input_box1, button1]])
column2 = fg.Column([[layout2, input_box2, button2]])
column3 = fg.Column([[button1], [button2]])

window = fg.Window("ZIP Extractor",
                   layout = [[column1],
                             [column2],
                             [column3]),
                             [extract_button, output_label]]

while True:
    event, values = window.read()
    zip_path = values["zipfile"]
    extract_to = values["extractfolder"]
    extract_zip(zip_path, extract_to)
    fg.popup("Extraction Completed!")


window.close()