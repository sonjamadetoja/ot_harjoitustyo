from tkinter import ttk, constants, StringVar
from services.service import service

class LoginView:
    def __init__(self, root, handle_register, handle_login):
        self._root = root
        self._handle_register = handle_register
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._error_variable = None
        self._error_label = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        user = service.login(username)
        if not user==None:
            self._handle_login(user)
        else:
            self._show_error("Virheellinen käyttäjätunnus")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.pack()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )

        username_label = ttk.Label(master=self._frame, text="Käyttäjänimesi: ")
        self._username_entry = ttk.Entry(master=self._frame)

        button_login = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command = self._login_handler
            )

        button_register = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command = self._handle_register
            )

        button_exit = ttk.Button(
            master=self._frame,
            text="Lopeta ohjelma",
            command = self._root.quit
            )

        username_label.pack(fill=constants.X)
        self._username_entry.pack(fill=constants.X)
        button_login.pack(fill=constants.X)
        button_register.pack(fill=constants.X)
        button_exit.pack(fill=constants.X)
