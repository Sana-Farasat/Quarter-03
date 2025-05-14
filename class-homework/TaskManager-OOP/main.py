from termcolor import colored

class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, new_task):
        self.tasks.append(new_task)

    def remove_task(self, remove_task):
        if remove_task in self.tasks:
            self.tasks.remove(remove_task)
        else:
            print(colored("Task not found", "red"))

    def update_task(self, index, updated_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = updated_task
        else:
            print(colored("Invalid index.", "red"))

    def view(self):
        return self.tasks


class Task_Manager(Task):
    def __init__(self):
        super().__init__()

    def start_app(self):
        while True:
            print(colored("\n\t\t_______________ Task Manager ________________\n", "yellow"))
            print(colored("1. Add Task", "green"))
            print(colored("2. Remove Task", "green"))
            print(colored("3. Update Task", "green"))
            print(colored("4. View Tasks", "green"))
            print(colored("5. Exit", "green"))

            choice = input(colored("\n Enter your choice: ","blue"))

            if choice == "1":
                new_task = input(colored("Enter new task: ","blue"))
                self.add_task(new_task)

            elif choice == "2":
                remove_task = input(colored("Remove task: ","blue")) 
                self.remove_task(remove_task)

            elif choice == "3":
                index = int(input(colored("Enter index number of task to update: ","blue")))  
                updated_task = input(colored("Enter new task: ","blue"))
                self.update_task(index - 1, updated_task)

            elif choice == "4":
                tasks = self.view()
                if tasks:
                 for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                else:
                   print(colored("No tasks added yet.","red"))

            elif choice == "5":
                print(colored("Exit....","magenta"))
                break
            else:
                print(colored("Invalid choice. Try again!","red"))

task = Task_Manager()
task.start_app()