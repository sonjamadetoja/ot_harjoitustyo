
from tkinter import Tk
from ui.ui import UI
from initialize_database import DataBase
from database_connection import get_database_connection
from repositories.user_repository import user_repository

def main():

    database = DataBase(get_database_connection(), user_repository)
    database.initialize_database()

    window = Tk()
    window.title("Menoseuranta")

    user_interface = UI(window)
    user_interface.start()

    window.mainloop()

if __name__ == '__main__':
    main()
