from tkinter import*

root= Tk()
root.title("wugduiw")
root.geometry("200x250")

labelgrd4 = Label(root)
labelgrd6 = Label(root)
labelgrd8 = Label(root)

class grd4():
    def __init__(self, sub1,sub2):
        self.sub1 = sub1
        self.sub2 = sub2
        
    def perc(self):
        totmk = self.sub2 + self.sub1
        totmk100 = totmk*100
        print(totmk, totmk100)
        gr4perc = totmk/200
        labelgrd4['text'] = str(gr4perc)
        print(gr4perc)
        
class grd6():
    def __init__(self, sub1,sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        
    def perc(self):
        totmk = self.sub2 + self.sub1 + self.sub3
        totmk100 = totmk*100
        print(totmk, totmk100)
        gr6perc = totmk/300
        labelgrd6['text'] = str(gr6perc)
        print(gr6perc)
        
class grd8():
    def __init__(self, sub1,sub2,sub3,sub4):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        
    def perc(self):
        totmk = self.sub2 + self.sub1 + self.sub3 + self.sub4
        totmk100 = totmk*100
        print(totmk, totmk100)
        gr8perc = totmk/400
        labelgrd8['text'] = str(gr8perc)
        print(gr8perc)
        
grd4obj = grd4(90,100)
grd6obj = grd6(99,85,89)
grd8obj = grd8(100,63,90,100)

grd4btn = Button(root, text="Grade 4 percentage",command= grd4obj.perc)
grd6btn = Button(root, text="Grade 6 percentage",command= grd6obj.perc)
grd8btn = Button(root, text="Grade 8 percentage",command= grd8obj.perc)

grd4btn.pack()
labelgrd4.pack()
grd6btn.pack()
labelgrd6.pack()
grd8btn.pack()
labelgrd8.pack()

root.mainloop()

