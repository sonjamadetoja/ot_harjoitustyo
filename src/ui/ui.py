from ui.login_view import LoginView
from ui.logged_in_menu_view import MenuView
from entities.user import User
from ui.search_view import SearchView

class UI:
    def __init__(self):
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        self._current_view = LoginView()
        action = self._current_view.show()
        if action == "no_username":
            print("Tämännimistä käyttäjää ei ole.")
            self._show_login_view()
        if action == "register":
            print("Käyttäjänimi on rekisteröity. Voit kirjautua. ")
            self._show_login_view()
        if action == False:
            print("Tämä käyttäjänimi on jo olemassa, on liian pitkä tai et kirjoittanut sitä. Kokeile uudestaan. ")
            self._show_login_view()
        if isinstance(action, User) :
            self._show_menu_view(action)

    def _show_menu_view(self, user):
        self._current_view = MenuView()
        action = self._current_view.show_menu(user)
        if action == "logout":
            self._show_login_view()
        if action == "again":
            self._show_menu_view(user)
        if action == "search":
            self._show_search_view(user)

    def _show_search_view(self, user):
        self._current_view = SearchView()
        action = self._current_view.show_search_options(user)
        if action == "return":
            self._show_menu_view(user)
        if action == "again":
            self._show_search_view(user)
