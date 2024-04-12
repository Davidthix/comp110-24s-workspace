"""Practive writing classes!"""

class Profile: 

    username: str
    private: bool

    def __init__(self, username_input: str) -> None:
        """Create a new Profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """If profile is public, print message."""
        if not self.private:
            print(msg)

user1: Profile = Profile("110_rulez")
user1.private = False
user1.tweet("OOP is cool!")