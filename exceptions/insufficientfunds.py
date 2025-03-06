
#   Define a custom exception class to indicate the user of insufficient funds:
#   The custom exception inherits from built-in Exception class which enables errors to be raised.
class InsufficientFundsException(Exception):
#   Constructor __init__ initializes the exception with a custom message.
#   message= states that if no message is provided when raising the exception, it will automatically default to the string below:
#   the custom message overrides the message from Exception class.
    def __init__(self, message= "Invalid withdrawal amount. Unfortunately, you are unable to complete the transaction. Please ensure that you have sufficient funds in your account."):
#   Call the parent constructor to override the parameter "message"
        super().__init__(message)
        # self.message = message

# Add parameter for overdrawn funds