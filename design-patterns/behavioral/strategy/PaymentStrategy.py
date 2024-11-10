from abc import ABC, abstractmethod

# Step 1: Define the strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Implement concrete strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder, expiry_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Processing credit card payment of ${amount} for card holder {self.card_holder}")

class PaypalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount} for account {self.email}")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Processing Bitcoin payment of ${amount} to wallet {self.wallet_address}")

# Step 3: Context class that uses the payment strategy
class ShoppingCart:
    def __init__(self):
        self.payment_strategy = None

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        if self.payment_strategy is None:
            raise ValueError("Payment strategy not set!")
        self.payment_strategy.pay(amount)

# Client code
cart = ShoppingCart()

# Choose payment strategy based on user choice
cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "John Doe", "12/25", "123"))
cart.checkout(100)

cart.set_payment_strategy(PaypalPayment("john.doe@example.com"))
cart.checkout(200)

cart.set_payment_strategy(BitcoinPayment("1A2b3C4d5E6f7G8h9I"))
cart.checkout(300)
