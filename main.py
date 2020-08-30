#Importing necessary modules


from tkinter import *
from tkinter.font import Font
import random
from PIL import Image, ImageTk
import PIL
from tkinter import simpledialog
#Main Window class
class MainWindow:
    def __init__(self, master):
        #Constructor to initialize the window size and background properties
        self.master = master
        self.master.geometry('900x600')
        self.master.config(bg = "black")
        self.computerScore = 0
        self.userScore = 0
        self.chances = 5
        self.widgets()
        #Asking the user name by using simpledialog
        self.name = simpledialog.askstring(title="Names", prompt="First Player")
    def widgets(self):
        #Widget function to place the widgets on the screen
        self.score = 0 #Score variable to store the score information
        #Top frame
        frame = Frame(self.master, bg = "#47a2f8")
        self.label = Label(frame, text = "RESULT WINDOW", font = Font(family="Gotham",size=20,weight="bold"),fg = "white", bg = "#47a2f8")
        frame.place(x = 100, y = 5, height = 70, width = 700)
        self.label.place(x = 350, y = 35, anchor = "center")
        #Second frame on which the buttons are placed
        frame2 = Frame(self.master, bg="black")
        #Adding buttons to second frame and formatting them
        img = PIL.Image.open("userRock.png")
        UserRocktkimg = ImageTk.PhotoImage(img)
        self.btn1 = Button(frame2, image = UserRocktkimg, text = "1",font = Font(family="Gotham",size=20), bg = "#47a2f8",fg = "white")
        self.btn1.image = UserRocktkimg
        
        self.btn1.config(command = self.user1 )
        self.btn1.pack(side = LEFT,padx = 20)

        img = PIL.Image.open("userScissor.png")
        UserRocktkimg = ImageTk.PhotoImage(img)
        
        self.btn3 = Button(frame2,image = UserRocktkimg ,text="3", font=Font(family="Gotham", size=20), bg = "#47a2f8",fg = "white")
        self.btn3.config(command = self.user3)
        self.btn3.pack(side=RIGHT, padx=20)
        self.btn3.image = UserRocktkimg

        img = PIL.Image.open("paperUser.png")
        UserRocktkimg = ImageTk.PhotoImage(img)
        self.btn2 = Button(frame2,image = UserRocktkimg, text="2", font=Font(family="Gotham", size=20), bg = "#47a2f8",fg = "white")
        self.btn2.config(command = self.user2)
        self.btn2.image= UserRocktkimg
        self.btn2.pack(side=TOP, pady=5)
        frame2.place(x=250, y=90, height=70, width=400)
        

        #Third frame that has the labels like the game status
        frame3 = Frame(self.master, bg="black")
        #Game status label
        self.label1 = Label(frame3, text="User BEATS Computer", font=Font(family="Gotham", size=20, weight="bold"), fg="white",bg="black")
        #Player move label on which the player image is placed
        self.playerLabel = Label(frame3,fg = "white", font=Font(family="Gotham", size=10, weight="bold"), text = "USER INPUT", height = 10, width = 20, bg="#47a2f8")
        self.playerLabel.pack(side = LEFT)
        #Computer move label
        self.computerLabel = Label(frame3,fg = "white", font=Font(family="Gotham", size=10, weight="bold"), text="COMPUTER INPUT", height=10, width=20, bg="#47a2f8")
        self.computerLabel.pack(side=RIGHT)
        frame3.place(x=75, y=170, height=300, width=750)
        self.label1.place(x=375, y=160, anchor="center")

        #Last frame to show the score record
        frame4 = Frame(self.master, bg="#47a2f8")
        self.scoreLabel = Label(frame4, text="SCORE: "+str(self.score), fg = "white", bg = "#47a2f8", font=Font(family="Gotham", size=15, weight="bold"))
        self.scoreLabel.place(x=240,y=20)
        frame4.place(x = 150, y = 480, height = 70, width = 600)
        self.labelChances = Label(self.master, text = "Chances : "+str(self.chances),font=Font(family="Gotham", size=12,weight = "bold"),bg = "#47a2f8",fg = "white")
        self.labelChances.place(x = 420, y = 200)

        
    #Button 1 funtion
    def user1(self):
        if(self.chances != 0):
            computer = random.randrange(1, 4)
            if(computer == 1):
                #If computer move is one
                #Pick the image userRock because user move is also one
                img = PIL.Image.open("userRock.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("computerRock.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text = "ROCK",height = 160, width = 160, image = computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                #Open the images and place on the labels
                self.playerLabel.config(text = "ROCK",height = 160, width = 160, image = UserRocktkimg)
                self.playerLabel.image = UserRocktkimg
                #Configuring the status label and score label
                self.label1.config(text = "TIE")
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
            elif (computer == 2):
                #Doing the same thing as mentioned above
                img = PIL.Image.open("userRock.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("paperComputer.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                self.playerLabel.image = UserRocktkimg

                self.computerLabel.config(text="PAPER")
                self.playerLabel.config(text="ROCK")
                self.label1.config(text=self.name+ " BEATS Computer")
                self.score += 1
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
            elif (computer == 3):
                #Doing the same thing as mentioned above
                img = PIL.Image.open("userRock.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("computerScissor.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                self.playerLabel.image = UserRocktkimg

                self.computerLabel.config(text="SCISSOR")
                self.playerLabel.config(text="ROCK")
                self.label1.config(text=self.name+" BEATS Computer")
                self.score += 1
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
        else:
            #If the chances are down to zero
            print(self.score)
            print(self.computerScore)
            #Disable the buttons
            self.btn1['state'] = DISABLED
            self.btn2['state'] = DISABLED
            self.btn3['state'] = DISABLED
            #If user score are greater than computer score
            if(self.score > self.computerScore):
                #Change the text that the user wins
                self.label.config(text = self.name+" WINS")
            if(self.computerScore > self.score):
                #Else computer wins
                self.label.config(text = "COMPUTER WINS")
            if(self.computerScore == self.score):
                #OR tie
                self.label.config(text = "TIE")
 
        #Button 2 function
    def user2(self):
        if(self.chances != 0):
            computer = random.randrange(1, 4)
            if (computer == 1):
                #If computer move is one
                #Pick the image userRock because user move is also one
                
                img = PIL.Image.open("paperUser.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("computerRock.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                #Open the images and place on the labels
                self.playerLabel.image = UserRocktkimg

                self.computerScore += 1
                self.label1.config(text="Computer BEATS "+self.name)
                self.chances -= 1
                self.labelChances.config(text = "Chances : "+str(self.chances))
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
            if (computer == 2):
                #Doing the same things as mentioned above
                img = PIL.Image.open("paperUser.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("paperComputer.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                self.playerLabel.image = UserRocktkimg


                self.label1.config(text="TIE")
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
            if (computer == 3):
                #Doing the same things as mentioned above
                img = PIL.Image.open("paperUser.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("computerScissor.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                self.playerLabel.image = UserRocktkimg

                self.label1.config(text="Computer BEATS "+self.name)
                self.chances -= 1
                self.labelChances.config(text = "Chances : "+str(self.chances))
                self.computerScore += 1
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
        else:
            #If the chances are down to zero
            print(self.score)
            print(self.computerScore)
            #Disable the buttons
            self.btn1['state'] = DISABLED
            self.btn2['state'] = DISABLED
            self.btn3['state'] = DISABLED
            #If user score are greater than computer score
            if(self.score > self.computerScore):
                #Change the text that the user wins
                self.label.config(text = self.name+" WINS")
            if(self.computerScore > self.score):
                #Else computer wins
                self.label.config(text = "COMPUTER WINS")
            if(self.computerScore == self.score):
                #OR tie
                self.label.config(text = "TIE")
        #Button 3 function
    def user3(self):
        if(self.chances != 0):
            computer = random.randrange(1, 3)
            
            if (computer == 1):
                #Doing the same things as mentioned above
                img = PIL.Image.open("userScissor.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("computerRock.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                self.playerLabel.image = UserRocktkimg

                self.computerLabel.config(text="ROCK")
                self.playerLabel.config(text="SCISSOR")
                self.label1.config(text="Computer BEATS "+self.name)
                self.chances -= 1
                self.labelChances.config(text = "Chances : "+str(self.chances))
                self.computerScore += 1
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
            if (computer == 2):
                #Doing the same things as mentioned above
                img = PIL.Image.open("userScissor.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("paperComputer.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                self.playerLabel.image = UserRocktkimg

                self.computerLabel.config(text="PAPER")
                self.playerLabel.config(text="SCISSOR")
                self.label1.config(text=self.name+" BEATS Computer")
                self.score += 1
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
            if (computer == 3):
                #Doing the same things as mentioned above
                img = PIL.Image.open("userScissor.png")
                UserRocktkimg = ImageTk.PhotoImage(img)
                img = PIL.Image.open("computerScissor.png")
                computerRocktkimg = ImageTk.PhotoImage(img)
                self.computerLabel.config(text="ROCK", height=160, width=160, image=computerRocktkimg)
                self.computerLabel.image = computerRocktkimg
                self.playerLabel.config(text="ROCK", height=160, width=160, image=UserRocktkimg)
                self.playerLabel.image = UserRocktkimg

                self.computerLabel.config(text="SCISSOR")
                self.playerLabel.config(text="SCISSOR")
                self.label1.config(text="TIE")
                self.scoreLabel.config(text=self.name+" " + str(self.score) + " : "+str(self.computerScore)+" Computer")
        else:
            #If the chances are down to zero
            print(self.score)
            print(self.computerScore)
            #Disable the buttons
            self.btn1['state'] = DISABLED
            self.btn2['state'] = DISABLED
            self.btn3['state'] = DISABLED
            #If user score are greater than computer score
            if(self.score > self.computerScore):
                #Change the text that the user wins
                self.label.config(text = self.name+" WINS")
            if(self.computerScore > self.score):
                #Else computer wins
                self.label.config(text = "COMPUTER WINS")
            if(self.computerScore == self.score):
                #OR tie
                self.label.config(text = "TIE")

root = Tk()
MainWindow(root)
root.mainloop()
