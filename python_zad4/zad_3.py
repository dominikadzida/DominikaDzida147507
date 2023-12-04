class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.address}, {self.rooms} rooms, " \
               f"{self.area} sq. meters, ${self.price}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.address}, {self.rooms} rooms, " \
               f"{self.area} sq. meters, ${self.price}, " \
               f"Plot: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.address}, {self.rooms} rooms, " \
               f"{self.area} sq. meters," \
               f"${self.price}, Floor: {self.floor}"


house = House(area=150, rooms=4, price=200000,
              address="123 Main Street", plot=500)

flat = Flat(area=80, rooms=2, price=120000, address="456 Elm Street", floor=3)

print(house)
print(flat)
