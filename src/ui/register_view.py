from tkinter import ttk, constants, StringVar
from services.user_service import user_service

class RegisterView:
    def __init__(self, root, handle_reg):
        self._root = root
        self._frame = None
        self._entry = None
        self.handle_reg = handle_reg
        self._error_variable = None
        self._error_label = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _register_handler(self):
        username = self._entry.get()
        result = user_service.register(username)
        if result == False:
            self._show_error("""Rekisteröityminen epäonnistui.
            Joko antamasi käyttäjätunnus on jo olemassa,
            se on liian pitkä, tai kenttä jäi kokonaan tyhjäksi.""")
        else:
            self.handle_reg()

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

        username_label = ttk.Label(
            master=self._frame,
            text="Anna haluamasi käyttäjänimi."
            )
        instruction_label = ttk.Label(
            master=self._frame,
            text="Käyttäjänimi voi olla korkeintaan 20 merkkiä pitkä."
            )
        self._entry = ttk.Entry(master=self._frame)
        button_save_username = ttk.Button(
            master=self._frame,
            text="Tallenna käyttäjätunnus",
            command = self._register_handler
            )
        button_return = ttk.Button(
            master=self._frame,
            text="Palaa kirjautumisnäkymään",
            command = self.handle_reg
            )

        username_label.pack(fill=constants.X)
        instruction_label.pack(fill=constants.X)
        self._entry.pack(fill=constants.X)
        button_save_username.pack(fill=constants.X)
        button_return.pack(fill=constants.X)
