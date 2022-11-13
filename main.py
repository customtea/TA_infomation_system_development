from core.book_mgr import BookManager
from core.user_mgr import UserManager

from ui.ui_user import UserInterface

from getpass import getpass
from hashlib import sha256

book_man = BookManager()
user_man = UserManager()

book_man.load_file()
user_man.load_file()

# user_man.add_user("test")
# user_man.add_user("admin")
# ue = user_man.search_user4name("admin")
# ue.set_user_type(3000)
# book_man.add_book("a","a",0)
# book_man.add_book("b","b",0)


def main():
    print("""
        __        __   _                            _     _ _
        \ \      / /__| | ___ ___  _ __ ___   ___  | |   (_) |__  _ __ __ _ _ __ _   _
         \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |   | | '_ \| '__/ _` | '__| | | |
          \ V  V /  __/ | (_| (_) | | | | | |  __/ | |___| | |_) | | | (_| | |  | |_| |
           \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_____|_|_.__/|_|  \__,_|_|   \__, |
                                                                                 |___/
    """)
    try:
        while True:
            user_name = input("login: ")
            if user_name == "exit":
                break
            passwd_text = getpass("password: ")

            passwd_hash = sha256(passwd_text.encode()).digest()
            user = user_man.search_user4name(user_name)
            if user != None and user.auth(passwd_hash):
                print(f"Welcom back {user.name()}")
                ui = UserInterface(user)
                ui.shell()
            else:
                print("\nLogin incorrect")
    except KeyboardInterrupt:
        print(" Bye")
    finally:
        print("Saveing File ... ", end="")
        book_man.save_file()
        user_man.save_file()
        print("Done")




if __name__ == '__main__':
    main()