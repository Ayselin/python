class User:

    def __init__(self,first_name,last_name,email):
        self.first_name = first_name
        self.last_name = last_name
        self.email =email
        self.login_attempts = 5

    def describe_user(self):
        print(f"Name: {self.first_name},\nLast Name: {self.last_name}, \nEmail: {self.email}")

    def greet_user(self):
        print(f"Dear {self.first_name} {self.last_name}, Welcome on board!")

    def increment_login(self, users):
        self.login_attempts += users

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Boris','Johnson','borisjohnson@email.com')
user2 = User('Vladimir','Putin','vladputin@email.com')


user1.describe_user()
user1.greet_user()
user1.increment_login(3)
print(f"{user1.first_name} attended to log in {user1.login_attempts} times!")

user1.reset_login_attempts()
print(f"{user1.first_name} resetting login attends to the {user1.login_attempts}")
