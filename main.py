
message = """ 1 - add tasks to a list 
 2 - mark task as complete
 3 - view tasks
 4 - Quit  """

tasks = []

def add_tasks():
    nomber_tasks = int(input("Enter nomber tasks :"))
    c= 0
    while c < nomber_tasks :
        c+=1
        task = input(f"Enter The tasks {c} to list : ")
        tasks.append(task)
        
    
def mark_tasks():
    mark = int(input("Enter le nombre as mark :"))
    if tasks[mark] not in tasks :
        print("Invalid choice, please enter in tasks :")
    del tasks[mark-1]

    

def view_tasks():
    for task in tasks:
        print(task ,'\n')

while True:
    print(message)
    choice = input("Enter your choice : ")

    if choice == "1" :
        add_tasks()
    elif choice == "2" :
        mark_tasks()
    elif choice == "3" :
        view_tasks()
    elif choice == "4" :
        break
    else:
       print('Invalid choice, please enter a number between 1 and 4 ')
