from ui.login_view import LoginView
from ui.logged_in_menu_view import MenuView
from ui.search_view import SearchView
from ui.register_view import RegisterView
from ui.add_transaction_view import AddTransactionView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._show_register_view,
            self._show_menu_view
            )
        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(
            self._root,
            self._show_login_view
            )
        self._current_view.pack()

    def _show_menu_view(self, user):
        self._hide_current_view()
        self._current_view = MenuView(
            self._root,
            self._show_login_view,
            self._show_search_view,
            self._show_add_transaction_view,
            user
            )
        self._current_view.pack()

    def _show_search_view(self, user):
        self._hide_current_view()
        self._current_view = SearchView(
            self._root,
            self._show_menu_view,
            self._show_search_view,
            user
            )
        self._current_view.pack()

    def _show_add_transaction_view(self, user):
        self._hide_current_view()
        self._current_view = AddTransactionView(
            self._root,
            self._show_menu_view,
            user
            )
        self._current_view.pack()
