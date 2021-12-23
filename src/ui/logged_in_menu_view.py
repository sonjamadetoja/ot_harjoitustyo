from tkinter import ttk, constants
from services.user_service import user_service

class MenuView:
    def __init__(self, root, handle_logout, handle_search, handle_add, user):
        self._root = root
        self._frame = None
        self._entry = None
        self._handle_logout = handle_logout
        self._handle_search = handle_search
        self._handle_add = handle_add
        self.user = user

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _search_handler(self, user):
        self._handle_search(user)

    def _add_handler(self, user):
        self._handle_add(user)
    
    def _logout_handler(self):
        user_service.logout(self.user)
        self._handle_logout()

    def _delete_username_handler(self):
        user_service.delete_user(self.user)
        self._handle_logout()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        button_add_transaction = ttk.Button(
            master=self._frame,
            text="Lisää tapahtumia yksittäin tai tiedostosta",
            command = lambda: self. _add_handler(self.user)
            )

        button_search = ttk.Button(
            master=self._frame,
            text="Katso tai poista tapahtumia",
            command = lambda: self._search_handler(self.user)
            )

        button_remove_username = ttk.Button(
            master=self._frame,
            text="Poista käyttäjätunnus",
            command = self._delete_username_handler
            )

        button_logout = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command = self._logout_handler
            )

        button_add_transaction.pack(fill=constants.X)
        button_search.pack(fill=constants.X)
        button_remove_username.pack(fill=constants.X)
        button_logout.pack(fill=constants.X)
