class Room:
    def __init__(self, name):
        self.name = name

    def get_room_name(self):
        return self.name

class House:
    def __init__(self, address: str, rooms = None):
        self.address = address
        self.rooms = rooms

    def add_room(self, room):
        room_object = Room(room)
        """
        This is the key part.
        The Room object is created inside the House class.
        So when the House object is deleted, the Room object is also deleted.
        """
        if self.rooms is None:
            self.rooms = []
        self.rooms.append(room_object)


if __name__ == '__main__':
    # Usage 
    house = House("123 Main St") 
    house.add_room("Living Room") 
    house.add_room("Bedroom") 
    
    # Accessing rooms via the house 
    for room in house.rooms: 
        print(room.get_room_name())