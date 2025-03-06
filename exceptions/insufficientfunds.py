
#   Define a custom exception class for insufficient funds:
class InsufficientFundsException(Exception):
#   Constructor to initialize the exception with a custom message.
    def __init__(self, message= "Invalid withdrawal amount. Unfortunately, you are unable to complete the transaction. Please ensure that you have sufficient funds in your account."):
#   Call the parent constructor to set the message
        super().__init__(message)
        self.message = message


