
class User:
    def __init__(self,name,email):
        self.Booking=[]
        self.Booking_history=[]
        self.name=name
        self.email=email

    def Book(self,Show):
        self.Booking.append(Show)
        self.Booking_history.append(Show)

