from functions import fetch_todo, write_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()
    if user_action.startswith("add"):
        todos = fetch_todo()

        todo = user_action[4:] + "\n"
        todos.append(todo)

        write_todo(todos)
    elif user_action.startswith("show"):
        todos = fetch_todo()
            
        for index, item in enumerate(todos):
            print(f"{index+1}-{(item.capitalize()).removesuffix("\n")}")

    elif user_action.startswith("edit"):
        try:
            todos = fetch_todo()

            n = int(user_action[5:])
            new_item = input("Enter new item: ") + "\n"
            todos[n-1] = new_item

            write_todo(todos)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = fetch_todo()

            n = int(user_action[9:])
            todos.pop(n-1)

            write_todo(todos)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Please enter a valid command.")

print("Bye!")