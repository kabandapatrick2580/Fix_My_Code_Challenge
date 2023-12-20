#!/usr/bin/python3
"""
User class for representing a user with an email attribute.
"""

class User:
    def __init__(self):
        """
        Initializes a User object with an email attribute set to None.
        """
        self.__email = None

    @property
    def email(self):
        """ 
        Getter method for the email attribute.

        Returns:
        Email of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """ 
        Setter method for the email attribute.

        Args:
        - value (str): The email to set.

        Raises:
        - TypeError: If the provided email is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")
        self.__email = value
 
if __name__ == "__main__":
    # Example usage
    u = User()
    u.email = "john@snow.com"
    print("User's Email:", u.email)
