class User:

    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id