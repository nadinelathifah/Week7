
class WithdrawalLimitException(Exception):
    def __init__(self, message="★ Withdrawal Blocked ★ Unfortunately, you have reached the maximum withdrawal limit for this month.\nPlease refer to your checking account for future transactions."):
        super().__init__(message)
        # self.message = message
