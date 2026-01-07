import functions
import FreeSimpleGUI as sg
import time
import os

sg.theme('Black')

clock = sg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key='clock')

label = sg.Text("Type in a to-do")

input_box = sg.InputText(tooltip="Enter todo", key="todo")

img_path = os.path.join(os.path.dirname(__file__), "add.PNG")
if os.path.exists(img_path):
    add_button = sg.Button(size=3, image_source=img_path,
                           tooltip="Add Todo", mouseover_colors="red",
                           key="Add")
else:
    add_button = sg.Button("Add", size=3, tooltip="Add Todo", key="Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My ToDos', 
                   layout=[[label],
                           [clock],
                           [input_box, add_button], 
                           [list_box, edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 25))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:

        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 15))


        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 15))


        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])
        
        case sg.WIN_CLOSED:
            break

window.close()
