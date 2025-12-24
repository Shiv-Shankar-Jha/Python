while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # 1) This code that is written above takes the input from the user and removes the space from it.

    if user_action.startswith("add"):
        
        todo = user_action[4:]

    # 2) This code tells us that if user input is "add" then store everything from that text
    # 3) into a variable named todo and write the only text that is after 4 index in that word
    # 4) because we dont have to write "add" too.


        with open("todos.txt", 'r') as file:
            
            todos = file.readlines()

    # 5) This code opens a new text file in read mode and reads the things inside the variable of todos.

        todos.append(todo + "\n")

    # 6) This code adds the user input into that variable "todos" file with a break line.
     
        with open("todos.txt", "w") as file:
            
            file.writelines(todos)

    # 7) This code opens that text file again but with write mode, and writes the variable "todos".

    elif user_action.startswith("show"):
        
    # 8) This line tells us that if the "if condition" does not exexute then the condition written
    # 9) in "elif" will execute and this "elif" can be created infinity times.
        
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

    # 10) This line witll do as same as written in comment no 5.

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    # 11) this block of code conatains many things in it,
    # 12) first thing is for loop, = it iterates over the items in every types of data.
    # 13) here for loops iterates over the list todos with their index and item inside it.
    # 14) enumerate fn writes down the values stored in every index of the list in form of the 
    # 15) tuples, like('0: apple). in the third line of code there is a f string.
    # 16) f strings help us to write down normal strings, chracters and variable together.
    # 17) since in coding index starts from 0, therefore we added 1 in every index so that
    # 18) we can match with the index given by user.

    elif user_action.startswith('edit'):

    # 19) this code will be executed if user enters the condn "edit".

        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
     
    # 20) this will print the index of the todo that user have entered.
    # 21) and now we have to tell the computer to edit the new todo so we
    # 22) subtract 1 from the index.
     
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

    # 23) read the same text file. cause list are mutable that's why we can assign
    # 24) new values to them.so we assign a new value to a given index no. with a \n.
    # 25) then write down the new values in that text file using the writelines method. 

        except ValueError:
            print("Your command is invalid.")
            continue

    # 26) checks if there is any valueerror is there or nor .
    # 27) Then continues the loop again.

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

    # 28) this checks if the user action starts with complete.
    # 29) if yes then it will store that in the variable with sliced till 9 characters.

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)    

    # 30) this code subtracts 1 from users given index number.and then remove the break
    # 31) line with the help of strip method, then the pop method is used to remove that todo 
    # 32) with the help of modified index number.

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

    # 33) this code opens the text file in write mode. writes the thing that is inside the 
    # 34) todos variable.

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    # 35) this block first type a message first then prints it, then comes a "except" syntax which
    # 36) on the failure of Indexerror executes. and the loop continues.

    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid.")    