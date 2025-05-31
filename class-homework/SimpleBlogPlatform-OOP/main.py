import json
from termcolor import colored

class Blog():
    def __init__(self):
        self.blog_list = []              # Empty blog list declared
        self.blog_storage = "blogs.json" # Json file initialized
        self.blog_reading()              # Called method in constructor

    def blog_reading(self):
        """Reads the blogs from the storage file."""
        try:
            with open(self.blog_storage, "r") as file:
                self.blog_list = json.load(file)
        except FileNotFoundError:
            print(colored("Blog storage file not found. Starting with an empty blog list.", "yellow"))
        except json.JSONDecodeError:
            print(colored("Error reading the blog data. The file may be corrupted.", "red"))
            self.blog_list = []  # Start with an empty list if the file is corrupted
   
    def blog_saving(self):
        """Writes the current blog list to the storage file."""
        try:
            with open(self.blog_storage, "w") as file:
                json.dump(self.blog_list, file, indent=4)
        except Exception as e:
            print(colored(f"Error writing to file: {e}", "red"))

    def add_blog(self):
        author_name = input(colored("Enter blog author: ", "blue"))
        blog_name = input(colored("Enter blog name: ", "blue"))

        blog = {
            "author_name" : author_name,
            "blog_name" : blog_name
        }
        self.blog_list.append(blog)
        self.blog_saving()
        print(colored("Blog saved successfully!","green"))
        return
    
    def delete_blog(self):
        author_name = input(colored("Enter blog author: ","blue"))
        blog_name = input(colored("Enter blog name: ", "blue"))

        blog = {
            "author_name" : author_name,
            "blog_name" : blog_name
        }
        self.blog_list.remove(blog)
        self.blog_saving()
        print(colored("Blog removed successfully!", "green"))
        return
    
    def update_blog(self):
        old_author = input(colored("Enter current blog author: ", "blue"))
        old_title = input(colored("Enter current blog name: ", "blue"))

        for blog in self.blog_list:
            if blog["author_name"] == old_author and blog["blog_name"] == old_title:
                new_author = input(colored("Enter new author name (leave blank to keep unchanged): ","blue"))
                new_title = input(colored("Enter new blog name (leave blank to keep unchanged): ","blue"))

                if new_author:
                    blog["blog_author"] = new_author

                if new_title:
                    blog["blog_name"] = new_title

                self.blog_saving()
                print(colored("Blog updated successfully!","green"))
                return
            
            print(colored("Blog not found. No update made.", "red"))

    def find_blog(self):
        author_name = input(colored("Enter blog author: ","blue"))
        blog_name = input(colored("Enter blog name: ","blue"))

        for blog in self.blog_list:
            if blog["author_name"] == author_name and blog["blog_name"] == blog_name:
                print(colored("Blog found!", "green"))
                return blog
        
        print(colored("Blog not found.", "red"))
        return None
    
    def view_blogs(self):
        if not self.blog_list:
            print(colored("No blogs to display.","red"))
            return

        print("List of Blogs:")
        for idx, blog in enumerate(self.blog_list, start=1):
            print(colored(f"{idx}. Author: {blog['author_name']} | Title: {blog['blog_name']}","yellow"))

class Blog_Manager(Blog):

    def __init__(self):
        super().__init__()

blog_manager = Blog_Manager()

while True:
    print(colored("\n ________Welcome to Blogs App_________", "yellow"))
    print(colored("1. Add Blogs", "green"))
    print(colored("2. Delete Blogs", "green"))
    print(colored("3. Update Blogs", "green"))
    print(colored("4. Find Blogs", "green"))
    print(colored("5. View Blogs", "green"))
    print(colored("6. Exit", "green"))

    choice = input(colored("\nEnter your choice: ", "blue"))

    if choice == "1":
        blog_manager.add_blog()
    elif choice == "2":
        blog_manager.delete_blog()
    elif choice == "3":
        blog_manager.update_blog()
    elif choice == "4":
        blog_manager.find_blog()
    elif choice == "5":
        blog_manager.view_blogs()
    elif choice == "6":
        print(colored("\n Exiting...", "magenta"))
        break
    else:
        print(colored("Invalid choice","red"))

print(colored("\n ________Thanks For Using My App_________", "yellow"))



        

