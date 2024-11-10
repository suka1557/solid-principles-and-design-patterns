"""
State is a behavioral design pattern that lets an object alter its behavior 
when its internal state changes. It appears as if the object changed its class.

Key Components:

    Context: The class that maintains an instance of a ConcreteState subclass, which defines the current state.

    State: An interface that declares the state-specific behavior.

    ConcreteState: Subclasses that implement the state-specific behavior.

Example use case:
Suppose you are designing the Order Status for an E-Commerce Platform. 
The Order can have multiple states: 
    - Order Placed
    - Order Shipped
    - Order Delivered

Based on the current status of the Order,
Notifications need to be sent to the Customer.
FOR SIMPLICITY, we will only send a simple text message that just prints the status of the Order.
"""