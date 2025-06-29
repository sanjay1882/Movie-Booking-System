
class Show:
    def __init__(self,title,totalseats,availableseats):
            self.title=title
            self.totalseats=totalseats
            self.availableseats=availableseats

    def showDetails(self):
          print("Title :",self.title)
          print("Total Seats :",self.totalseats)
          print("Avaliable Seats :",self.availableseats)

          return "---Book The Show---"
    def BookTickets(self,num):
            Flag=""
            if num>self.availableseats:
                Flag=f"Sorry Only {self.availableseats} Tickets are available"
            elif num>self.totalseats:
                Flag=f" ❕Tickets are Unavailable "
            else:
                self.availableseats-=num
                Flag=f"✅  Tickets are Booked...'\n ---Enjoy the Show---"

            return Flag
    def CancelTickets(self,num):
            if num+self.availableseats>self.totalseats:
                return " ⚠️ Too Many Tickets Can't Cancel"
            elif num<=0:
                return "You Must Select Atleast One Ticket"
            else:
                self.availableseats+=num
                return " ✅ Cancelled The Ticket"
          
                
                
