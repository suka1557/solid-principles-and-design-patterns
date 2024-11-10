"""
The Strategy Design Pattern is a behavioral design pattern that enables 
selecting an algorithm's behavior at runtime. 

It defines a family of algorithms, 
encapsulates each one, 
and makes them interchangeable. 

The pattern lets the algorithm vary independently from clients that use it.

Use Case:

Consider an e-commerce platform like Amazon that offers various payment methods. 
The payment method can be selected at runtime based on user preference. 
The Strategy Pattern allows defining different payment strategies (like Credit Card, PayPal, Cryptocurrency) 
and switching between them without altering the client code.
Key Components:

    Strategy Interface: Defines a common interface for all supported algorithms.

    Concrete Strategies: Implement the algorithms defined in the Strategy Interface.

    Context: Maintains a reference to the current strategy and delegates execution to it.

"""