print("1.add task\n2.view tasks\n3.delete task\n4.exit")
list1 = []
while True:
    chooice = int(input("Enter your choice: "))
    if chooice == 1:
        
        task = input("Enter your name: ")
        list1.append(task)
        print("Task added successfully")
    elif chooice == 2:
        print("Your tasks are:")
        if not list1:
            print("No tasks available")
        else:
            for i in list1:
                print("-", i)
    elif chooice == 3:
        task=input("Enter task to delete: ")
        if task in list1:
            list1.remove(task)
            print("Task deleted successfully")
        else:
            print("Task not found")
            
    elif chooice == 4:
        break
    else:
        print("Invalid choice")
        print("exited")
        