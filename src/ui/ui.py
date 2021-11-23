from ui.login_view import LoginView
from ui.logged_in_menu_view import MenuView

class UI:
    def __init__(self):
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        self._current_view = LoginView()
        action = self._current_view.show()
        if action == "login":
            self._show_menu_view()
        if action == "register":
            print("Rekisteröiminen ei vielä valmis")
            
    def _show_menu_view(self):
        self._current_view = MenuView()
        self._current_view.show_menu()