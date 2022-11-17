class User:
    # Constructors and Initializing
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # when we don't need to always create an attribute set the value to '0'
        print("new user being created...")

# Adding an Attribute to our Class
# Attributes are like variables for Objects

user1 = User("001", "Ali")
print(f"user.followers = {user1.followers}")
print(user1.id, user1.username)
user2 = User("002", "Aazam")
print(user2.id, user2.username)


