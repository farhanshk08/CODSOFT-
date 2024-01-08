class To_Do_List:
    def __init__(self):
        self.works = []

    def add_work(self, activity):
        self.works.append(activity)
        print(f"Task '{activity}' added.")

    def rem_work(self, activity):
        if activity in self.works:
            self.works.remove(activity)
            print(f"Task '{activity}' removed.")
        else:
            print(f"Task '{activity}' not found.")

    def disp_work(self):
        if not self.works:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index in range(len(self.works)):
                print(str(index+1) + ". " + self.works[index])

def main():
    todo_list = To_Do_List()

    while True:
        print("\n ********** TO-DO LIST APPLICATION ********** \n ")
        print("1. Add Task to To-Do List")
        print("2. Remove Task from To- Do List")
        print("3. Display Tasks from To-Do List")
        print("4. Exitttttt")

        choice = input("Enter your choice from (1-4): ")

        if choice == '1':
            activity = input("Enter the task to add it into the To-Do List: ")
            todo_list.add_work(activity) # add_work() is a method to add task into the To-doList
        elif choice == '2':
            activity = input("Enter the task to remove from the To-Do List: ")
            todo_list.rem_work(activity) #rem_work() is a method to remove task from the To-doList
        elif choice == '3':
            todo_list.disp_work() #disp_work() is a method to display tasks from the To-doList
        elif choice == '4':
            print("Terminating the program. GOOD GOOODBYEEE!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()