class Theatre:
    def __init__(self, screens,name):
        self.d = {i:[] for i in range(1,screens+1)}
        self.name=name
        self.screens = screens

    def AddShows(self, Movie,ScreenNo):
        if len(self.d[ScreenNo]) >=1:
            print(f"❌ Screen {ScreenNo} :   ' {Movie.title} '   Screen Limit Reached")
        else:
            self.d[ScreenNo].append(Movie.title)
            self.d[ScreenNo].append(Movie)
            print(f"✅ Screen {ScreenNo} :  Show '{Movie.title}' added successfully")
    def RemoveShow(self,Movie,ScreenNo):
        if self.d[ScreenNo] and Movie == self.d[ScreenNo][0]:
            self.d[ScreenNo].clear()
            print(f"✅ Screen {ScreenNo} :  Show '{Movie}' Removed Sucessfully")
        else:
            print(f"‼️ Show '{Movie}' Not Played In Current Screen")
    def CurrentlyRunning(self):
        print(" ............................Now Showing...............................")
        for i,j in self.d.items():
            if j:
                print(f"Screen {i} : {j[0]}")
