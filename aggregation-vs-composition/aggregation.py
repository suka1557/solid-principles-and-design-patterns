class DeliveryPartner:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def deliver(self):
        print(f"{self.name} is delivering the package using {self.vehicle}")

class Zomato:
    def __init__(self, partners = None):
        self.delivery_partners = partners

    def add_delivery_partner(self, partner):
        if self.delivery_partners is None:
            self.delivery_partners = []
        self.delivery_partners.append(partner)

    def show_delivery_partners(self):
        for partner in self.delivery_partners:
            print(partner.name)

    def make_delivery(self, partner: DeliveryPartner):
        partner.deliver()

if __name__ == '__main__':
    dp1 = DeliveryPartner("John", "Bike")
    dp2 = DeliveryPartner("Doe", "Car")

    zomato = Zomato()
    zomato.add_delivery_partner(dp1)
    zomato.add_delivery_partner(dp2)

    zomato.show_delivery_partners()
    zomato.make_delivery(dp1)
    zomato.make_delivery(dp2)