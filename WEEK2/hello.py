class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if (len(self.passengers)) == self.capacity:
            print(f"sorry {name}, the flight is full")
            return False
        else:
            self.passengers.append(name)
            print(f"welcome {name}, you have been added")
            return True


flynas9 = Flight(4)

flynas9.add_passenger("Khaled")
flynas9.add_passenger("Mohammed")
flynas9.add_passenger("Saad")
flynas9.add_passenger("Jaffarr")
flynas9.add_passenger("Soso")
