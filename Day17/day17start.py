class User:
    # Constructors and Initializing
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # when we don't need to always create an attribute set the value to '0'
        self.following = 0
        print("new user being created...")

    # Methods are Functions within a Class
    # Always requires a 'self' parameter as the 1st param
    # When this method is called, it knows the object that called it
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Adding an Attribute to our Class
# Attributes are like variables for Objects

user_1 = User("001", "Ali")
print(f"user.followers = {user_1.followers}")
print(user_1.id, user_1.username)
user_2 = User("002", "Aazam")
print(user_2.id, user_2.username)

user_1.follow(user_2)
# user_1 to follow user_2
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)