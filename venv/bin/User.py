class User:
    def __init__(self, first_name, last_name, password, position, projects=0):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.position = position
        self. projects = projects

    def change_password(self, old_password, repeat_password, new_password):
        if old_password == repeat_password:
            self.password = new_password
            return self.password
        else:
            return 'Sorry, the passwords don\'t match. Please try again.'

    def change_first_name(self, new_first_name):
        self.first_name = new_first_name
        return f'You have changed your first name to {new_first_name}.'

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name
        return f'You have changed your last name to {new_last_name}.'

    def change_position(self, new_position):
        self.position = new_position
        return f'You have changed your position to {new_position}.'






