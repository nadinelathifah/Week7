

#   Define a custom exception class for insufficient funds:
class InsufficientFundsException(Exception):
#   Constructor to initialize the exception with a custom message.
    def __init__(self, message):
#   Call the parent constructor to set the message
        super().__init__(message)


