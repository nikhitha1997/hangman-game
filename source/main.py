from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from PIL import Image, ImageTk

from views import *
import random

LARGE_FONT=("Verdana",24)
MED_FONT=("Verdana",18)

class Hangman(Tk):

	def __init__(self,*args,**kwargs):#args is an arguement and kwargs key word argument

		Tk.__init__(self,*args,**kwargs)#pass the value to the tkinter,self is the instance of frame
		Tk.configure(self)
		
		self.container=Frame(self)
		self.container.grid()
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
			
		self.geometry("1024x768")
		self.show_frame(Main)

	def show_frame(self, cont):
		frame=cont(parent=self.container, controller=self)
		frame.grid(row=0,column=0,sticky="nsew")
		frame.tkraise()


class Main(Frame):#main frame

	def __init__(self, parent, controller):

		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="HANGMAN GAME", font=LARGE_FONT)
		start_btn = Button(self, text='Start',command=lambda:controller.show_frame(Game))
		add_word_btn = Button(self, text='Add New Word', command=lambda:controller.show_frame(AddWord))
		quit_btn = Button(self, text='Quit', command=self.controller.quit)

		heading_label.grid(row=2, column=6, padx=120,pady=30)
		start_btn.grid(row=6, column=6, padx=120, pady=10)
		add_word_btn.grid(row=7, column=6, padx=120, pady=10)
		quit_btn.grid(row=10, column=6, padx=120, pady=10)


class Game(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.guess_remaining = 7  #7 guessess are given
		self.controller = controller
		self.hint = Label(self, text="Hint",font=11)
		self.hint_box = Text(self,height=2,width=30)

		self.word_tobe_guessed = Label(self, text="Word to be Guessed",font=11)
		self.choose_letter = Label(self,text="Choose letter",font=11)
		
		self.letter=StringVar()

		self.show_word=Text(self,height=2, width=20)

		self.back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main))#back button
		self.back_btn.grid(row=9, column=5, padx=20, pady=20)

		# buttons
		self.button_0=Button(self,text='0',command=lambda:self.getText('0'))
		self.button_1=Button(self,text='1',command=lambda:self.getText('1'))
		self.button_2=Button(self,text='2',command=lambda:self.getText('2'))
		self.button_3=Button(self,text='3',command=lambda:self.getText('3'))
		self.button_4=Button(self,text='4',command=lambda:self.getText('4'))
		self.button_5=Button(self,text='5',command=lambda:self.getText('5'))
		self.button_6=Button(self,text='6',command=lambda:self.getText('6'))
		self.button_7=Button(self,text='7',command=lambda:self.getText('7'))
		self.button_8=Button(self,text='8',command=lambda:self.getText('8'))
		self.button_9=Button(self,text='9',command=lambda:self.getText('9'))

		self.button_A=Button(self,text='A',command=lambda:self.getText('A'))
		self.button_B=Button(self,text='B',command=lambda:self.getText('B'))
		self.button_C=Button(self,text='C',command=lambda:self.getText('C'))
		self.button_D=Button(self,text='D',command=lambda:self.getText('D'))
		self.button_E=Button(self,text='E',command=lambda:self.getText('E'))
		self.button_F=Button(self,text='F',command=lambda:self.getText('F'))
		self.button_G=Button(self,text='G',command=lambda:self.getText('G'))
		self.button_H=Button(self,text='H',command=lambda:self.getText('H'))
		self.button_I=Button(self,text='I',command=lambda:self.getText('I'))
		self.button_J=Button(self,text='J',command=lambda:self.getText('J'))

		self.button_K=Button(self,text='K',command=lambda:self.getText('K'))
		self.button_L=Button(self,text='L',command=lambda:self.getText('L'))
		self.button_M=Button(self,text='M',command=lambda:self.getText('M'))
		self.button_N=Button(self,text='N',command=lambda:self.getText('N'))
		self.button_O=Button(self,text='O',command=lambda:self.getText('O'))
		self.button_P=Button(self,text='P',command=lambda:self.getText('P'))
		self.button_Q=Button(self,text='Q',command=lambda:self.getText('Q'))
		self.button_R=Button(self,text='R',command=lambda:self.getText('R'))
		self.button_S=Button(self,text='S',command=lambda:self.getText('S'))
		self.button_T=Button(self,text='T',command=lambda:self.getText('T'))

		self.button_U=Button(self,text='U',command=lambda:self.getText('U'))
		self.button_V=Button(self,text='V',command=lambda:self.getText('V'))
		self.button_W=Button(self,text='W',command=lambda:self.getText('W'))
		self.button_X=Button(self,text='X',command=lambda:self.getText('X'))
		self.button_Y=Button(self,text='Y',command=lambda:self.getText('Y'))
		self.button_Z=Button(self,text='Z',command=lambda:self.getText('Z'))


	
		self.hint.grid(row=1, column=1, padx=5, pady=10)
		self.hint_box.grid(row=1,column=2,padx=10,columnspan=7)

		self.word_tobe_guessed.grid(row=2, column=1, padx=5, pady=10)
		self.choose_letter.grid(row=3, column=1, padx=5, pady=10)
		
		self.show_word.grid(row=2,column=2,columnspan=7)
		

		self.button_0.grid(row=4,column=2,sticky='nsew',padx=5,pady=5)
		self.button_1.grid(row=4,column=3,sticky='nsew',padx=5,pady=5)
		self.button_2.grid(row=4,column=4,sticky='nsew',padx=5,pady=5)
		self.button_3.grid(row=4,column=5,sticky='nsew',padx=5,pady=5)
		self.button_4.grid(row=4,column=6,sticky='nsew',padx=5,pady=5)
		self.button_5.grid(row=4,column=7,sticky='nsew',padx=5,pady=5)
		self.button_6.grid(row=4,column=8,sticky='nsew',padx=5,pady=5)
		self.button_7.grid(row=4,column=9,sticky='nsew',padx=5,pady=5)
		self.button_8.grid(row=4,column=10,sticky='nsew',padx=5,pady=5)
		self.button_9.grid(row=4,column=11,sticky='nsew',padx=5,pady=5)

		self.button_A.grid(row=5,column=2,sticky='nsew',padx=5,pady=5)
		self.button_B.grid(row=5,column=3,sticky='nsew',padx=5,pady=5)
		self.button_C.grid(row=5,column=4,sticky='nsew',padx=5,pady=5)
		self.button_D.grid(row=5,column=5,sticky='nsew',padx=5,pady=5)
		self.button_E.grid(row=5,column=6,sticky='nsew',padx=5,pady=5)
		self.button_F.grid(row=5,column=7,sticky='nsew',padx=5,pady=5)
		self.button_G.grid(row=5,column=8,sticky='nsew',padx=5,pady=5)
		self.button_H.grid(row=5,column=9,sticky='nsew',padx=5,pady=5)
		self.button_I.grid(row=5,column=10,sticky='nsew',padx=5,pady=5)
		self.button_J.grid(row=5,column=11,sticky='nsew',padx=5,pady=5)


		self.button_K.grid(row=6,column=2,sticky='nsew',padx=5,pady=5)
		self.button_L.grid(row=6,column=3,sticky='nsew',padx=5,pady=5)
		self.button_M.grid(row=6,column=4,sticky='nsew',padx=5,pady=5)
		self.button_N.grid(row=6,column=5,sticky='nsew',padx=5,pady=5)
		self.button_O.grid(row=6,column=6,sticky='nsew',padx=5,pady=5)
		self.button_P.grid(row=6,column=7,sticky='nsew',padx=5,pady=5)
		self.button_Q.grid(row=6,column=8,sticky='nsew',padx=5,pady=5)
		self.button_R.grid(row=6,column=9,sticky='nsew',padx=5,pady=5)
		self.button_S.grid(row=6,column=10,sticky='nsew',padx=5,pady=5)
		self.button_T.grid(row=6,column=11,sticky='nsew',padx=5,pady=5)

		self.button_U.grid(row=7,column=2,sticky='nsew',padx=5,pady=5)
		self.button_V.grid(row=7,column=3,sticky='nsew',padx=5,pady=5)
		self.button_W.grid(row=7,column=4,sticky='nsew',padx=5,pady=5)
		self.button_X.grid(row=7,column=5,sticky='nsew',padx=5,pady=5)
		self.button_Y.grid(row=7,column=6,sticky='nsew',padx=5,pady=5)
		self.button_Z.grid(row=7,column=7,sticky='nsew',padx=5,pady=5)
		

		data_list = load_data()
		self.word = "_ " * len(data_list[0][0])
		hint = data_list[0][1]

		self.letters=data_list[0][0]
		self.hint_box.insert('1.0', hint)
		self.show_word.insert('end-1c',self.word)
		self.word2 = list(self.word)


		#inserting the canvas  to draw the hangman 
		canvas_width = 500
		canvas_height = 500
		self.w = Canvas(self, bg="white",
		           width=canvas_width,
		           height=canvas_height,)
		self.w.grid(row=13,column=3,columnspan=7)
		
		
		
	def getText(self,val):#to get the text from the buttons
		self.val_from_button = val

		self.index_list=[]

		for i,value in enumerate(self.letters):
			if self.val_from_button == value:
				self.index_list.append(i)

		count = len(self.index_list)

		if count == 0:
			self.guess_remaining -= 1
			
			if self.guess_remaining==6:
				self.w.create_line(300, 50, 150, 50)        
				self.w.create_line(300,50,300,350)
				
			
			if self.guess_remaining==5:
				self.w.create_oval(100,50,200,100)
				 	         
			if self.guess_remaining==4:
				self.w.create_line(150, 100, 150, 300)


			if self.guess_remaining==3:
				self.w.create_line(150,150,75,200)

			if self.guess_remaining==2:
				self.w.create_line(150,270,75,350)

			if self.guess_remaining==1:
				self.w.create_line(150,150, 250, 200)	
		
		
		if self.guess_remaining == 0:
			self.w.create_line(150,270,250,350)	
			self.message = messagebox.showwarning('warning', 'You are out of guesses')#show the out of guessess
		
			self.controller.show_frame(Main)

		for i in range(len(self.word2)):
			if i/2 in self.index_list:
				self.word2[i]=self.val_from_button


		self.show_word.delete('1.0','end-1c')
		self.show_word.insert('end-1c', "".join(self.word2))
		
		if "_" not in self.word2:
			self.message = messagebox.showwarning('Yay!!', 'You\'ve guessed the word!')
			self.controller.show_frame(Main)


class AddWord(Frame):#frame to add the new word and hint
	def __init__(self, parent, controller):

		Frame.__init__(self,parent)

		self.controller=controller

		self.word=Label(self,text='word',font=11)
		self.hint=Label(self,text='hint',font=11)
		self.word_box=Text(self,height=1,width=30)
		self.hint_box=Text(self,height=1,width=30)


		self.word.grid(row=1,column=1)
		self.hint.grid(row=2,column=1)
		self.word_box.grid(row=1,column=2)
		self.hint_box.grid(row=2,column=2)

		self.save_btn=Button(self, text="Add Word", command=self.add_word)
		self.back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		
		self.save_btn.grid(row=9, column=4, padx=20, pady=20)
		self.back_btn.grid(row=9, column=5, padx=20, pady=20)

	def add_word(self):#function to add new word
		if len(self.word_box.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add Word')

		elif len(self.hint_box.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add Hint')

		else:
			word_1 = self.word_box.get("1.0", "end-1c")
			word_hint = self.hint_box.get("1.0", "end-1c")

			add_data(word=word_1, hint=word_hint)

FRAMES = (Main,Game,AddWord)


app = Hangman()
app.mainloop()	