import datetime
import re
from tkinter import ttk, constants, StringVar
from services.service import service
from entities.user import User

class AddTransactionView:
    def __init__(self, root, handle_return, user):
        self._root = root
        self._handle_return = handle_return
        self._frame = None
        self.user = user
        self._date_entry = None
        self._amount_entry = None
        self._title_entry = None
        self._category_entry = None
        self._file_name_entry = None
        self._added_label = None
        self._error_variable = None
        self._error_label = None
        self._info_variable = None
        self._info_label = None
        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_transaction(self):
        self._hide_info()
        date = self._date_entry.get()
        if not date.strip():
            date = datetime.datetime.now()
            date = date.strftime("%Y-%m-%d")
        else:
            date = date.strip()
        amount = self._amount_entry.get()
        title = self._title_entry.get()
        category = self._category_entry.get()
        if not re.match("^\d{4}-\d{2}-\d{2}$", date):
            self._show_error("Virheellinen päivämäärä. Tapahtumaa ei lisätty.")
        elif not re.match("^(-|\+)*[0-9]+$", amount):
            self._show_error("Virheellinen summa. Tapahtumaa ei lisätty.")
        else:
            self._hide_error()
            service.add_transaction(date, amount, self.user, title, category)
            self._show_info("Tapahtuma lisätty.")
            self._date_entry.delete(0, constants.END)
            self._amount_entry.delete(0, constants.END)
            self._title_entry.delete(0, constants.END)
            self._category_entry.delete(0, constants.END)

    def _add_file(self):
        self._hide_info()
        filename = self._file_name_entry.get()
        if not filename.strip():
            self._show_error("Tiedostonnimi-kenttä on tyhjä. Kirjoita nimi.")
        else:
            filename = filename.strip()
            result = service.add_file(self.user, filename)
            if result == False:
                self._show_error("Tiedostoa ei löydy tällä nimellä.")
            else:
                self._hide_error()
                self._show_info("Tiedoston tapahtumat lisätty.")
                self._file_name_entry.delete(0, constants.END)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.pack()

    def _hide_error(self):
        self._error_label.pack_forget()

    def _show_info(self, message):
        self._info_variable.set(message)
        self._info_label.pack()

    def _hide_info(self):
        self._info_label.pack_forget()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._info_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )

        self._info_label = ttk.Label(
            master=self._frame,
            textvariable=self._info_variable
        )

        date_label = ttk.Label(master=self._frame, text="Anna päivämäärä muodossa yyyy-mm-dd (esim. 2021-12-01): ")
        self._date_entry = ttk.Entry(master=self._frame)
        amount_label = ttk.Label(master=self._frame, text="Anna summa (+/-): ")
        self._amount_entry = ttk.Entry(master=self._frame)
        title_label = ttk.Label(master=self._frame, text="Anna otsikko: ")
        self._title_entry = ttk.Entry(master=self._frame)
        category_label = ttk.Label(master=self._frame, text="Luokittele tapahtuma: ")
        self._category_entry = ttk.Entry(master=self._frame)

        button_add = ttk.Button(
            master=self._frame,
            text="Lisää tapahtuma",
            command = self._add_transaction
            )

        file_name_label = ttk.Label(master=self._frame, text="Anna tiedoston nimi: ")
        self._file_name_entry = ttk.Entry(master=self._frame)
        dir_label = ttk.Label(master=self._frame, text="Huomaa, että tiedoston tulee sijaita data-nimisessä hakemistossa.")

        button_file = ttk.Button(
            master=self._frame,
            text="Lisää tapahtumia csv-tiedostosta",
            command = self._add_file
            )

        button_return = ttk.Button(
            master=self._frame,
            text="Palaa edelliseen valikkoon",
            command = lambda: self._handle_return(self.user)
            )

        date_label.pack(fill=constants.X)
        self._date_entry.pack(fill=constants.X)
        amount_label.pack(fill=constants.X)
        self._amount_entry.pack(fill=constants.X)
        title_label.pack(fill=constants.X)
        self._title_entry.pack(fill=constants.X)
        category_label.pack(fill=constants.X)
        self._category_entry.pack(fill=constants.X)
        button_add.pack(fill=constants.X)
        file_name_label.pack(fill=constants.X)
        self._file_name_entry.pack(fill=constants.X)
        dir_label.pack(fill=constants.X)
        button_file.pack(fill=constants.X)
        button_return.pack(fill=constants.X)
