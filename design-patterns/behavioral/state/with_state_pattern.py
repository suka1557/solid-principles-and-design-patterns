"""
To implement the State Pattern, we need the following:
Key Components:

    Context: The class that maintains an instance of a ConcreteState subclass, 
                which defines the current state.

    State: An interface that declares the state-specific behavior.

    ConcreteState: Subclasses that implement the state-specific behavior.
"""

from abc import ABC, abstractmethod


class OrderStatusInterface(ABC):
    """This is the Order Status Interface that declares the state-specific behavior.
        All the concrete states will implement this interface.
    """
    @abstractmethod
    def next_state(self):
        pass

    def send_notification(self):
        pass

class OrderPlaced(OrderStatusInterface):
    def next_state(self):
        return OrderShipped()

    def send_notification(self):
        print("Order Placed")

class OrderShipped(OrderStatusInterface):
    def next_state(self):
        return OrderDelivered()

    def send_notification(self):
        print("Order Shipped")

class OrderDelivered(OrderStatusInterface):
    def next_state(self):
        pass

    def send_notification(self):
        return print("Order Delivered")
    
"""Now its time to implement the main Context Class that will make use of the Concrete States"""
class OrderStatus:
    def __init__(self):
        self.status = OrderPlaced()

    def next_state(self):
        self.status = self.status.next_state()

    def send_notification(self):
        self.status.send_notification()

"""
In the current implementation, we have separated the states into different classes.
If we need to add a new state, we can easily create a new class that implements the OrderStatusInterface.
"""

if __name__ == '__main__':
    order = OrderStatus()
    order.send_notification()

    order.next_state()
    order.send_notification()

    order.next_state()
    order.send_notification()