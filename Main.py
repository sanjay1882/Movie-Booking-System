import Show
import Theatre

from Show import Show
from Theatre import Theatre
import TheatresList 

if __name__ =="__main__":

    while True:
        
        print("1. Book tickets")
        print("2. Show Theatre")
        print("3. Show Movies")
        v=int(input())
        if v==1:
           print(TheatresList.show_Theatres())
