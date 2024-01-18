# Class -> Blueprint
# PascalCase -> ClassName
# camelCase
# snake_case


class User:
    # pass  # null operation
    def __init__(self, user_id, username):
        # this function runs every time an object has been created by this User class & sets initial state
        # attributes -> a class has
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    #  Methods-> what a class does
    def follow_account(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "Manoj")
user_2 = User("002", "Monika")
print(user_1.followers)
user_1.follow_account(user_2)
print(user_1.following, user_2.followers)
