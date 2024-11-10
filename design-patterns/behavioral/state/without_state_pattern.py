class OrderStatus:
    def __init__(self, status:str):
        self.status = status

    def get_status(self):
        return self.status
    
    def next_state(self):
        if self.status == "Order Placed":
            self.status = "Order Shipped"
        
        elif self.status == "Order Shipped":
            self.status = "Order Delivered"
        
        else:
            self.status = "Order Placed"

    def send_notification(self):
        print(f"Order Status: {self.status}")

"""
The current implementation of the OrderStatus class is not following the State Design Pattern.
It also violates the Open-Closed Principle, as we need to modify the class every time we add a new state.

For example:
    if we need to add a new state "Order Cancelled", 
    we need to modify the next_state() method.
"""
if __name__ == '__main__':
    order = OrderStatus("Order Placed")
    order.send_notification()

    order.next_state()
    order.send_notification()

    order.next_state()
    order.send_notification()