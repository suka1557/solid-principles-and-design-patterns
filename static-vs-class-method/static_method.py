"""
A static method in Python is a method that belongs to a class 
but 
doesn't access or modify the class state or instance-specific data. 

Static methods are used when you want to group related utility functions together within a class, 
without requiring an instance of the class.

A good example of practical use case might be Payment Gateway Integration in a web application.
You can have a class called PaymentGateway that has a static method called process_payment.
This method can be used to process payment transactions without requiring an instance of the PaymentGateway class.
Because you don't need to access or modify the class state or instance-specific data.

And you don't need the object of this class to live beyond the method call.
"""

class PaymentGateway:
    @staticmethod
    def process_payment(amount, card_number):
        # Code to process payment
        print(f'Processing payment of ${amount} using card number {card_number}')

if __name__ == '__main__':
    PaymentGateway.process_payment(100, '1234 5678 9012 3456')
    PaymentGateway.process_payment(200, '9876 5432 1098 7654')
    PaymentGateway.process_payment(300, '5678 1234 9876 5432')