import typing as tp

from core.user_entry import UserEntry, UserType
from core.user_mgr import UserManager
from core.book_mgr import BookManager

class AdminInterface():
    func_table = {}
    
    def __init__(self, user) -> None:
        self.user_e: UserEntry = user
        self.book_man = BookManager()
        self.user_man = UserManager()
    
    def shell(self) -> None:
        print("Administrator Mode")
        while True:
            cmd_text = input("% ").lower().split(" ")
            if cmd_text[0] == "":
                continue
            fn_cmd = self.func_table.get(cmd_text[0])
            if fn_cmd != None:
                fn_cmd(self, cmd_text)
            elif cmd_text[0] == "exit":
                break
            else:
                print(f"Library Command '{cmd_text[0]}' not found")
        print("Exit Administrator Mode")
    
    def ui_help(self, cmd_text) -> None:
        print("====ADMIN HELP====")
        for cmd in self.func_table:
            print(f"{cmd} ", end="")
        print()
    
    def ui_addbook(self, cmd_text) -> None:
        if len(cmd_text) < 4:
            print("Not enough arguments")
            return
        else:
            title = cmd_text[1]
            author = cmd_text[2]
            if not cmd_text[3].isdecimal():
                print("ISBN is numeric only")
                return 
            isbn = int(cmd_text[3])
            if len(cmd_text) > 5:
                note = cmd_text[4:]
            else:
                note =None
            self.book_man.add_book(title, author, isbn, note)
            print("Add Book is Successful")
    
    def ui_booklist(self, cmd_text) -> None:
        for book in self.book_man.get_list():
            print(book)
    
    def ui_adduser(self, cmd_text) -> None:
        if len(cmd_text) < 2:
            print("Not enough arguments")
            return
        else:
            name = cmd_text[1]
            if len(cmd_text) > 3:
                note = cmd_text[3:]
            else:
                note = None
            self.user_man.add_user(name, note)
            print("Add User is Successful")
    
    def ui_search_user(self, cmd_text):
        if len(cmd_text) < 2:
            print("Not enough arguments")
            return
        else:
            name = cmd_text[1]
            user = self.user_man.search_user4name(name)
            if user == None:
                print("Not Found User")
            else:
                print(user)
    
    def ui_user_update(self, cmd_text):
        if len(cmd_text) < 3:
            print("Not enough arguments")
            return
        else:
            uid = cmd_text[1]
            utype = int(cmd_text[2])
            user = self.user_man.search_user4id(uid)
            if user == None:
                print("Not Found User")
            else:
                print(user)
                user.set_user_type = UserType(utype)
            print("UserType Upgrade is Successful")

    
    def ui_userlist(self, cmd_text) -> None:
        for user in self.user_man.get_list():
            print(user)
    

    func_table["help"] = ui_help
    func_table["addbook"] = ui_addbook
    func_table["booklist"] = ui_booklist
    func_table["adduser"] = ui_adduser
    func_table["userlist"] = ui_userlist
    func_table["finduser"] = ui_search_user
