import random

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def bookTicket(self, fromStation, toStation, passengerName):
        print(f"Ticket booked for {passengerName} on train number {self.trainNo} from {fromStation} to {toStation}.")
        
    def getStatus(self):
        print(f"Train number {self.trainNo} is on time.")
    
    def getFare(self, fromStation, toStation):
        print(f"Fare for train number {self.trainNo} from {fromStation} to {toStation} is {random.randint(100, 1000)}.")
        

lokShaktiExpress = Train(12345)
lokShaktiExpress.bookTicket("Mumbai", "Delhi", "Alice")
lokShaktiExpress.getStatus()
lokShaktiExpress.getFare("Mumbai", "Delhi")
