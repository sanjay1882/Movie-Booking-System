from Show import Show
from Theatre import Theatre



if __name__=="__main__":
    Inox=Theatre(7)
    Inox.AddShows(Show("Tenet",140,120),1)
    Inox.AddShows(Show("Godzilla X Kong",150,120),7)
    Inox.AddShows(Show("Avengers",180,120),6)
    Inox.AddShows(Show("X Man",150,120),5)
    Inox.AddShows(Show("Godzilla X Kong -Tamil",150,120),4)
    Inox.RemoveShow("Tenet",1)

    print('')
    print('')
    Inox.CurrentlyRunning()
