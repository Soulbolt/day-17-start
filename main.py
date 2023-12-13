# Creating a custom Class, class name always use Pascal Case ex: HelloWorld()
class User:
    # special function: __init__(self) calls on its class(User)
    def __init__(self, user_id, username):
        # Initialise attributes when class is called/initialise
        self.id = user_id


# Initialise object, when attributes are added into the class, we can pass on the respective arguments
user_1 = User("001", "Cesar")
# Create attributes
# user_1.id = "001"
# user_1.username = "Cesar"
user_2 = User("002", "Joan")

print(user_1.id)
