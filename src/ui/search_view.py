
from tkinter import ttk, constants, StringVar
import re
import pandas as pd
import plotly.express as px
import os
from PIL import ImageTk,Image  
from services.transaction_service import transaction_service

class SearchView:
    def __init__(self, root, handle_return, handle_new_search, user):
        self._root = root
        self._handle_return = handle_return
        self._handle_new_search = handle_new_search
        self._frame = None
        self._entry = None
        self.user = user
        self._year_entry = None
        self._month_entry = None
        self._error_variable = None
        self._error_label = None
        self._canvas = None
        self._graph = None
        self._graph_label = None
        self.pie_inc_graph = None
        self.pie_inc_graph_label = None
        self.pie_exp_graph = None
        self.pie_exp_graph_label = None
        self._info_variable = None
        self._info_label = None
        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _search_all(self, user):
        results = transaction_service.find_transactions(user)
        if results == None:
                self._show_info("Ei tapahtumia.")
        else:
            self._hide_info()
            self._list_results(results)
            self._show_results(results)

    def _list_results(self, results):
        list_string = ""
        new_line = "\n"
        for item in results:
            item = f"id: {item[0]} {item[1]} {item[2]} {item[3]} {item[4]}"
            list_string = list_string+new_line+item
        self._show_info(list_string)

    def _show_results(self, results):
        dirname = os.path.dirname(__file__)
        pie_inc_path = os.path.join(dirname, "..", "..", "data", "pie_inc.png")
        pie_exp_path = os.path.join(dirname, "..", "..", "data", "pie_exp.png")
        graph_path = os.path.join(dirname, "..", "..", "data", "graph.png")
        self._make_graph(results)
        self._make_pie(results)
        results = self._print_search_results(results)
        self._graph = self._make_image(graph_path)
        self._graph_label = ttk.Label(master=self._frame, image = self._graph)
        self._graph_label.grid(row=1, rowspan=18, column=1, sticky=(constants.N))
        self._pie_inc = self._make_image(pie_inc_path)
        self._pie_inc_label = ttk.Label(master=self._frame, image = self._pie_inc)
        self._pie_inc_label.grid(row=1, rowspan=18, column=2, sticky=(constants.N))
        self._pie_exp = self._make_image(pie_exp_path)
        self._pie_exp_label = ttk.Label(master=self._frame, image = self._pie_exp)
        self._pie_exp_label.grid(row=1, rowspan=18, column=3, sticky=(constants.N))

    def _make_image(self, path):
        image = Image.open(path)
        image = image.resize((525, 375))
        image = ImageTk.PhotoImage(image)
        return image

    def _search_year(self, user):
        year = self._year_entry.get()
        if not year.strip():
            self._show_error("Et antanut vuosilukua.")
        elif not re.match("^\d{4}$", year.strip()):
            self._show_error("Virheellinen vuosiluku. Anna vuosiluku neljänä numerona.")
        else:
            self._hide_error()
            results = transaction_service.find_transaction_by_year(user, year = year.strip())
            if results == None:
                self._show_info("Ei tapahtumia.")
            else:
                self._hide_info()
                self._list_results(results)
                self._show_results(results)
                self._year_entry.delete(0, constants.END)

    def _search_month(self, user):
        year = self._year_entry.get()
        month = self._month_entry.get()
        if not year.strip():
            self._show_error("Et antanut vuosilukua.")
        elif not month.strip():
            self._show_error("Et antanut kuukautta.")
        elif not re.match("^\d{4}$", year.strip()):
            self._show_error("Virheellinen vuosiluku. Anna vuosiluku neljänä numerona.")
        elif not re.match("^\d{2}$", month.strip()):
            self._show_error("Virheellinen kuukausi. Anna kuukausi kahtena numerona.")
        else:
            self._hide_error()
            results = service.find_transaction_by_month(user, year.strip(), month.strip())
            if results == None:
                self._show_info("Ei tapahtumia.")
            else:
                self._hide_info()
                self._list_results(results)
                self._show_results(results)
                self._year_entry.delete(0, constants.END)
                self._month_entry.delete(0, constants.END)

    def _print_search_results(self, deposits):
        sum_transactions = 0
        new_deposits = []
        for item in deposits:
            item_string = f"id: {str(item[0])}, {item[1]}, {str(item[2])}, {item[3]}, {str(item[4])}"
            new_deposits.append(item_string)
            item = int(item[2])
            sum_transactions = sum_transactions+item
        final_sum = f"Saldo: {sum_transactions}"
        new_deposits.append(final_sum)
        return new_deposits

    def _make_graph(self, deposits):
        balance = []
        dates = []
        previous = 0
        for item in deposits:
            dep = previous + float(item[2])
            dep = round(dep, 2)
            balance.append(dep)
            previous = dep
            date = item[1]
            dates.append(date)
        fig = px.line(x=dates, y=balance, title="Tilin saldon muutos")
        fig.update_layout(xaxis_title="Ajankohta", yaxis_title="Saldo")
        dirname = os.path.dirname(__file__)
        new_path = os.path.join(dirname, "..", "..", "data", "graph.png")
        fig.write_image(new_path)

    def _make_pie(self, deposits):
        data_frame = self._make_dataframe(deposits)
        df_income = data_frame[data_frame.deposits > 0]
        df_expense = data_frame[data_frame.deposits < 0]
        df_expense.deposits = abs(df_expense.deposits)
        fig_inc = px.pie(df_income, values='deposits', names='category', title="Tulot",
        color_discrete_sequence=px.colors.sequential.RdBu)
        fig_exp = px.pie(df_expense, values='deposits', names='category', title="Menot",
        color_discrete_sequence=px.colors.sequential.RdBu)
        dirname = os.path.dirname(__file__)
        new_path = os.path.join(dirname, "..", "..", "data", "pie_inc.png")
        fig_inc.write_image(new_path)
        new_path = os.path.join(dirname, "..", "..", "data", "pie_exp.png")
        fig_exp.write_image(new_path)

    def _make_dataframe(self, deposits):
        data_frame = pd.DataFrame(deposits, columns=["id", "date", "deposits", "title", "category"])
        return data_frame

    def _remove_transaction(self):
        id_number = self._remove_entry.get()
        if not id_number.strip():
            self._show_error("Et antanut id-tunnusta.")
        elif not re.match("^\d+$", id_number.strip()):
            self._show_error("Virheellinen id-tunnus. Anna tunnus numerona.")
        else:
            self._hide_error()
            transaction_service.remove_transaction(id_number)
            self._remove_entry.delete(0, constants.END)
            self._show_info(f"Tapahtuma {id_number} on poistettu.")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=12, column=0, sticky=(constants.E, constants.W))

    def _hide_error(self):
        self._error_label.grid_remove()

    def _show_info(self, message):
        self._info_variable.set(message)
        self._info_label.grid(row=12, column=0, sticky=(constants.E, constants.W))

    def _hide_info(self):
        self._info_label.grid_remove()

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

        year_label = ttk.Label(master=self._frame, text="Anna vuosi (esim. 2021): ")
        self._year_entry = ttk.Entry(master=self._frame)
        month_label = ttk.Label(master=self._frame, text="Anna kuukausi numerona (esim. 12): ")
        self._month_entry = ttk.Entry(master=self._frame)

        button_search_all = ttk.Button(
            master=self._frame,
            text="Hae kaikki tapahtumat",
            command = lambda: self._search_all(self.user)
            )

        button_search_year = ttk.Button(
            master=self._frame,
            text="Hae yhden vuoden tapahtumat",
            command = lambda: self._search_year(self.user)
            )

        button_search_month = ttk.Button(
            master=self._frame,
            text="Hae yhden kuukauden tapahtumat",
            command = lambda: self._search_month(self.user)
            )

        remove_label = ttk.Label(
            master=self._frame, 
            text="""Anna poistettavan tapahtuman id-numero:
            (Jos et tiedä numeroa, hae tapahtumat hakutoiminnolla,
            niin saat tapahtuman id-numeron näkyviin.)""")
        self._remove_entry = ttk.Entry(master=self._frame)

        button_remove_transaction = ttk.Button(
            master=self._frame,
            text="Poista tapahtuma",
            command = self._remove_transaction
            )

        button_return = ttk.Button(
            master=self._frame,
            text="Palaa edelliseen valikkoon",
            command = lambda: self._handle_return(self.user)
            )

        year_label.grid(row=1, column=0, sticky=(constants.E, constants.W))
        self._year_entry.grid(row=2, column=0, sticky=(constants.E, constants.W))
        month_label.grid(row=3, column=0, sticky=(constants.E, constants.W))
        self._month_entry.grid(row=4, column=0, sticky=(constants.E, constants.W))
        button_search_all.grid(row=5, column=0, sticky=(constants.E, constants.W))
        button_search_year.grid(row=6, column=0, sticky=(constants.E, constants.W))
        button_search_month.grid(row=7, column=0, sticky=(constants.E, constants.W))
        remove_label.grid(row=8, column=0, sticky=(constants.E, constants.W))
        self._remove_entry.grid(row=9, column=0, sticky=(constants.E, constants.W))
        button_remove_transaction.grid(row=10, column=0, sticky=(constants.E, constants.W))
        button_return.grid(row=11, column=0, sticky=(constants.E, constants.W))
