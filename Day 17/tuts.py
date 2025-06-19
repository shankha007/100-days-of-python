class User:
    # Constructor
    def __init__(self, user_id, username):
        # Adding Attributes to the created object
        self.id = user_id
        self.username = username
        self.followers = 0 # default value
        self.following = 0

    # Method
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "ShankhaD")
print(user_1.username)

user_2 = User("002", "JohnD")
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)