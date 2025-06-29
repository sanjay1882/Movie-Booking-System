from Theatre import Theatre

List=[Theatre(2,"INOX"),Theatre(3,"DIVYAM"),Theatre(6,"ROX"),Theatre(4,"SPR")]

def show_Theatres():
    j=0
    for i in List:
        print(j," : ",i.name)
        j+=1
