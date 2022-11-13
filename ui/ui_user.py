import typing as tp

from core.user_entry import UserEntry, UserType
from core.book_mgr import BookManager

from ui.ui_admin import AdminInterface

class UserInterface():
    func_table = {}
    
    def __init__(self, user) -> None:
        self.user_e: UserEntry = user
        self.book_man = BookManager()
    
    def shell(self) -> None:
        while True:
            cmd_text = input("> ").lower().split(" ")
            if cmd_text[0] == "":
                continue
            fn_cmd = self.func_table.get(cmd_text[0])
            if fn_cmd != None:
                fn_cmd(self, cmd_text)
            elif cmd_text[0] == "exit":
                break
            elif cmd_text[0] == "admin":
                if self.user_e.user_type() == UserType.ADMIN:
                    admin_ui = AdminInterface(self.user_e)
                    admin_ui.shell()
            else:
                print(f"Library Command '{cmd_text[0]}' not found")
    
    def ui_help(self, cmd_text) -> None:
        print("====HELP====")
        for cmd in self.func_table:
            print(f"{cmd} ", end="")
        print()

    
    def ui_name(self, cmd_text) -> None:
        print(self.user_e.name())
    
    def ui_list(self, cmd_text) -> None:
        blist = self.user_e.get_lendinglist()
        if blist != None:
            print("Not Lending books")
        for bookid in blist:
            book = self.book_man.search_book4id(bookid)
            print(f"{book.bookid():>6} {book.title()}")
    
    def ui_searchbook(self, cmd_text):
        if len(cmd_text) < 2:
            print("Few Arguments")
            return
        else:
            title = cmd_text[1]
        booklist = self.book_man.search_book4title(title)
        if booklist == None:
            print(f"Not Find '{title}' in library")
            return 
        for book in booklist:
            print(f"{book.bookid():>6} {book.title()} {book.state()}")
    

    func_table["help"] = ui_help
    func_table["name"] = ui_name
    func_table["list"] = ui_list
    func_table["search"] = ui_searchbook