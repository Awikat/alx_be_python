
class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount instance with an optional initial balance.
        The balance defaults to 0 if no initial balance is provided.
        """
        self.__account_balance = initial_balance  # Encapsulated balance attribute

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.
        Args:
            amount (float): The amount to withdraw.
        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Displays the current account balance in a formatted string.
        """
        print(f"Current balance: ${self.__account_balance:.2f}")
