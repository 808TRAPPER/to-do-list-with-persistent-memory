import os

todolist = ["smoke","learn_python",]

if os.path.exists("todolist.txt"):
   file = open("todolist.txt","r")
   contents = file.read()
   todolist = contents.split()

else:
    file = open("todolist.txt","w")
    for contents in todolist:
        file.write(contents + "\n")

def add_task():
    task=input("new task: ")
    todolist.append(task)

    file = open("todolist.txt","a")
    file.write(task + "\n")
    file.close()

def show_tasks():
    for tasks in todolist:
        print(tasks)

def rem_task():
    task=input("which task?: ")

    if task in todolist:
     todolist.remove(task)

     file=open("todolist.txt","r")
     contents=file.read()
     file.close()

     if task in contents:
        file=open("todolist.txt","w")
        contents = contents.replace(task + "\n","")
        file.write(contents)
        file.close()

    else:
        print("Task not found")

while True:

 os.system("cls")

 print("")
 print("1:Show tasks")
 print("2:Add task")
 print("3:Remove task")
 print("4:Exit")
 print("")

 choice = input("Choose an option: ")
 print("")

 if choice==("1"):
    show_tasks()
    print("")
    input("Press enter...")
 elif choice==("2"):
    add_task()
 elif choice==("3"):
    rem_task()
 elif choice==("4"):
     exit()
