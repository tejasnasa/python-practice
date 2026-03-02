class Train:
    ticketsLeft = 500

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    def bookTicket(self):
        print(f"Tickets booked for train {self.name}")
        print(f"Total amount: {self.fare}")
        self.ticketsLeft = self.ticketsLeft - 1

    def checkStatus(self):
        print(f"Tickets left: {self.ticketsLeft}")