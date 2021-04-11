# class User:
#     def __init__(self, first_name, last_name, password, position, projects):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.password = password
#         self.position = position
#         self.projects = projects
#
#     def change_password(self, old_password, repeat_password, new_password):
#         if old_password == repeat_password:
#             self.password = new_password
#             return self.password
#         else:
#             return 'Sorry, the passwords don\'t match. Please try again.'
#
#     def change_first_name(self, new_first_name):
#         self.first_name = new_first_name
#         return f'You have changed your first name to {new_first_name}.'
#
#     def change_last_name(self, new_last_name):
#         self.last_name = new_last_name
#         return f'You have changed your last name to {new_last_name}.'
#
#     def change_position(self, new_position):
#         self.position = new_position
#         return f'You have changed your position to {new_position}.'
#
# class Project:
#     def __init__(self, project_name, project_status, tasks_list, users_list):
#         self.project_name = project_name
#         self.project_status = project_status
#         self.tasks_list = tasks_list
#         self.users_list = users_list
#
#
# class Task:
#     def __init__(self, task_name, task_description, deadline, priority, for_whom):
#         self.task_name = task_name
#         self.task_description = task_description
#         self.deadline = deadline
#         self.priority = priority
#         self.for_whom = for_whom
#
#
# Katya = User('Katya', 'Hirhenson', '12345', 'junior', 'MyFirstProject')
# print(Katya.first_name())
