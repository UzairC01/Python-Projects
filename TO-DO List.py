#To do list program

tasks = []



while(True): #this while loop will run if the input is true
    user_option = input("Would you like add, remove, view, or quit to or the to-do list: ") # asking the user to add, remove, or see the to do list
    if user_option == "add": #if user adds then it will asks what to add then it will add it to the list
        what_add = input("what would you like to add: ")
        tasks.append(what_add)
    elif user_option == "remove":#if user removes then it will asks what to remove then it will remove it from the list
        what_remove = input("What would you like to remove: ")
        tasks.remove(what_remove)
    elif user_option == "view":# if the user asks to view the to do list, it will print the list
        print(tasks)
    elif user_option == "quit": #if the user asks to quit the program will stop
        break
    else:
        print("Invalid Command")# if the user mistypes something thats not in the following option then it will make it run again with a error message

