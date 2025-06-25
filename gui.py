import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass


sg.theme("black")
time_label = sg.Text(key="time")
label = sg.Text("Type a todo: ")
input_box = sg.InputText(tooltip="Enter a to-do", font="Courier 20", key="todo")
list_box = sg.Listbox(values=functions.fetch_todo(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

add_button = sg.Button('Add')

complete_button = sg.Button('Complete')

exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[time_label],
                            [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font="Helvetica 20")

while True:
    try:
        event, values = window.read(timeout=200)

        match event:
            case "Add":
                todos = functions.fetch_todo()
                new_todo = values["todo"] + "\n"
                todos.append(new_todo)
                functions.write_todo(todos)
                window['todos'].update(values=todos)

            case "Edit":
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.fetch_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window['todos'].update(values=todos)

            case "Complete":
                todo_to_complete = values["todos"][0]
                todos = functions.fetch_todo()

                todos.remove(todo_to_complete)
                functions.write_todo(todos)

                window['todos'].update(values=todos)


            case 'todos':
                window['todo'].update(value=values['todos'][0])

            case "Exit":
                break

            case sg.WIN_CLOSED:
                break

        current_time = time.strftime("%b %d, %Y %H:%M:%S")
        window["time"].update(value=f"{current_time}")

    except IndexError:
        continue


window.close()