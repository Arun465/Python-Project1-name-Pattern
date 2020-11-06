#v3.0
#Please Read Readme Note Before Run Code
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
from tkinter import scrolledtext
import time

root=Tk()
root.title("Words to Pattern by Python")
### to convert exe comment line no's 13 and 19    to run py file comment line no 14 and 20 then uncomment 13 and 19
root.iconbitmap('man.ico')
#root.iconbitmap('.icon\\man.ico')

root.configure(bg="#CBCBA9",width=500,height=300)


img = ImageTk.PhotoImage(Image.open("man2.jpg"))
#img = ImageTk.PhotoImage(Image.open(".img\\man2.jpg"))
imagep= Label(root, image = img)
imagep.place(x=170,y=0)

'''
def run():
	a= e.get()
	t.delete(1.0, END)

	t.insert(END,a)
	t.insert(END,"\n")
	t.insert(END,a)
	return


'''



#code For A
A=[[" " for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if((col!=0 and row+col==3)or (row>2 and (col==1 or col==5))or((row==1 or row==2) and col-row==3)or(row==4 and (col >1 and col<5))):
			A[row][col]="*"
#code For B
B=[[" " for i in range(5)]for j in range(8)]
for row in range(8):
	for col in range(5):
		if((col==1) or ((row>0 and row<4 )and row+col==5) or ((row==0 or row==4 or row==7) and (col==2 or col==3))or (col==4 and(row==5 or row==6))):
			B[row][col]="*"
			
#code For C
C=[[" "for i in range(6)]for j in range (8)]
for row in range(8):
	for col in range(6):
		if (col==1 and row!=0 and row!=7)or((row==0 or row==7)and (col>1 and col<5))or (col==5 and (row==1 or row==6)):
			C[row][col]="*"


#code For D
D=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1) or(row<3 and col-row==3)or((col>1 and col<4)and (row==0 or row==7))or(col==5 and (row>1 and row<6))or(col==4 and(row==1 or row ==6)):
			D[row][col]="*"
#code For E
E=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1)or ((row==0 or row==7)and (col>1 and col<6))or(row==3 and (col>1 and col<4)):
			E[row][col]="*"


#code For F
F=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1)or(row==0 and (col>1 and col<6))or (row ==3 and(col>1 and col<5)):
			F[row][col]="*"

#code For G
G=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1 and(row>0 and row<7))or ((row==0 or row==7)and (col>1 and col<5))or(col==5 and row==1)or(row==5 and col==3)or (row==4 and (col>2 and col<6))or (col==5 and(row>3 and row<7)):
			G[row][col]="*"

			
#code For H
H=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1 or col==5)or (row==3 and (col>1 and col<5)):
			H[row][col]="*"

#code For I
I=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if ((row==0 or row==7)and(col>0 and col<6))or(col==3 and(row>0 and row<7)):
			I[row][col]="*"	

			
#code For J
J=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (row==0 and (col>0 and col<6))or (col==3 and row<7)or (col==2 and row==7)or(col==1 and (row>4 and row<7)):
			J[row][col]="*"	
			
			
#code For K
K=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1)or(col>1 and row+col==5)or(col>1 and row-col==2):
			K[row][col]="*"	
			
#code For L
L=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1)or (row==7 and(col>1 and col<6)):
			L[row][col]="*"	

#code For M
M=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if ((col==1 or col==5)and row!=0)or (col<4 and col-row==1)or(col>3 and row+col==5):
			M[row][col]="*"	
#code For N
N=[[" "for i in range(8)]for j in range(8)]
for row in range(8):
	for col in range(8):
		if (col==0 or col==7)or row==col:
			N[row][col]="*"	
			
#code For O
O=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if ((col==1 or col==5)and (row>0 and row<7))or ((row==0 or row==7)and(col>1 and col<5)):
			O[row][col]="*"	
			
			
#code For P
P=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1)or(col==5 and (row>0 and row<4))or((col>1 and col<5) and (row==0 or row==4)):
			P[row][col]="*"	

#code For Q
Q=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if ((col==1 or col==5)and (row>0 and row<6))or ((row==0 or row==6)and(col>1 and col<5))or(col==3 and row==5)or((col==5 or col==4) and row==7):
			Q[row][col]="*"

#code For R
R=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if (col==1)or(col==5 and(row>0 and row<4))or((row==0 or row==4)and (col>1 and col<5))or(row>4 and row-col==2):
			R[row][col]="*"	
			
			
#code For S
S=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if ((col>1 and col<5)and (row==0 or row==4 or row==7))or (col==1 and ((row>0 and row<4)or(row==6)))or(col==5 and ((row==1)or(row>4 and row<7))):
			S[row][col]="*"	
			
#code For T
T=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if ((col>0 and col<6) and row==0)or (row!=0 and col==3):
			T[row][col]="*"	

			
#code For U
U=[[" "for i in range(6)]for j in range(8)]
for row in range(8):
	for col in range(6):
		if ((col==1 or col==5)and row!=7)or(row==7 and (col>1 and col<5)):
			U[row][col]="*"	

#code For V
V=[[" "for i in range(8)]for j in range(8)]
for row in range(8):
	for col in range(8):
		if ((col==1 or col==7)and row==1)or((col==2 or col==6)and row==3)or((col==3 or col==5)and row==5)or (col==4 and row==7):
			V[row][col]="*"	

#code For W
W=[[" "for i in range(8)]for j in range(8)]
for row in range(8):
	for col in range(8):
		if (col==1 or col==7)or ((row>3 and row<7) and (row+col==8))or((row>4 and row<7) and (row==col)):
			W[row][col]="*"	
			
			
#code For X
X=[[" "for i in range(8)]for j in range(8)]
for row in range(8):
	for col in range(8):
		if (col-row==1)or(col+row==7 and (row<7)):
			X[row][col]="*"	
			

#code For Y
Y=[[" "for i in range(8)]for j in range(8)]
for row in range(8):
	for col in range(8):
		if (col-row==1 and row<3)or(col+row==7 and row<3)or(col==4 and row>2):
			Y[row][col]="*"

#code For Z
Z=[[" "for i in range(8)]for j in range(8)]
for row in range(8):
	for col in range(8):
		if ((row==0 or row==6)and col!=0)or(row!=7 and(row+col==7)):
			Z[row][col]="*"

#code for space
sp=[[" "for i in range(5)]for j in range(8)]
for row in range(8):
	for col in range(5):
		if (col==1) or (col==2) or (col==3) or (col==4):
			sp[row][col]=" "
						
#code for full stop
fs=[[" "for i in range(4)]for j in range(8)]
for row in range(8):
	for col in range(4):
		if (row==5 and (col==1 or col==3))or ((row>3 and row<7)and col==2):
			fs[row][col]="."

			
TO=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,sp,fs]
global ToActivateStopButton
ToActivateStopButton=False

def run():
	global ToActivateStopButton
	if e.get()=="":
		return
	ToActivateStopButton = True
	word=""

	word=e.get()
	word1=word.upper()
	li=[sp]
	
	for letter in word1:
		for l in range(28):
			if chr(65+l)==letter:
				li.append(TO[l])
		if letter==" ":
			li.append(sp)
		if letter==".":
			li.append(fs)
	li.append(sp)
	if len(li)<9:
		dif=9-len(li)
		for i in range(dif+1):
			li.append(sp)


	al = ""

	for i in range(8):
		for k in range(len(li)):
			for j in range(len(li[k][0])):
				al = al + (li[k][i][j])
			al = al + " "
		al = al + '\n'
	global lenn

	lenn=int(len(al)/8)
	lenn2=int(lenn*2)-1
	lenn3 = int(lenn * 3) - 1
	lenn4 = int(lenn * 4) - 1
	lenn5 = int(lenn * 5) - 1
	lenn6 = int(lenn * 6) - 1
	lenn7 = int(lenn * 7) - 1
	lenn8=int(lenn*8)-1

	global al1,al2,al3,al4,al5,al6,al7,al8

	al1=al[0:lenn-1]
	al2=al[lenn:lenn2]
	al3=al[(lenn*2):lenn3]
	al4 = al[(lenn * 3):lenn4]
	al5 = al[(lenn * 4):lenn5]
	al6 = al[(lenn * 5):lenn6]
	al7= al[(lenn * 6):lenn7]
	al8= al[(lenn * 7 ):lenn8]

	# t.delete(1.0,END)
	# t.insert(END,al)
	# print(len(al))
	t.delete(1.0,END)
	# t.insert(END,al)


	tsl=56     #56 character avaialable in single line in text box t...
	alll=""
	for i in range(tsl+1):
		alll=alll+" "

	t.insert(END,alll[0:56])
	t.insert(END, "\n")
	t.insert(END, alll[0:56])
	t.insert(END, "\n")
	t.insert(END, alll[0:56])
	t.insert(END, "\n")
	t.insert(END,  alll[0:56])
	t.insert(END, "\n")
	t.insert(END, alll[0:56])
	t.insert(END, "\n")
	t.insert(END, alll[0:56])
	t.insert(END, "\n")
	t.insert(END, alll[0:56])
	t.insert(END, "\n")
	t.insert(END, alll[0:56])
	#print(lenn)

	# for o in range(lenn-57):
	global onu
	onu=0
	global flow
	flow = True
	runn(onu=0)
	return


def runn(onu=0):
	while flow==True:
		t.delete('1.0')
		t.delete("2.0")
		t.delete("3.0")
		t.delete("4.0")
		t.delete("5.0")
		t.delete("6.0")
		t.delete("7.0")
		t.delete("8.0")

		t.insert(1.55, al1[onu])
		t.insert(2.55, al2[onu])
		t.insert(3.55, al3[onu])
		t.insert(4.55, al4[onu])
		t.insert(5.55, al5[onu])
		t.insert(6.55, al6[onu])
		t.insert(7.55, al7[onu])
		t.insert(8.55, al8[onu])
		#print(o)
		if onu==(lenn-2):
			onu=0
		onu=onu+1

		time.sleep(0.1)
		t.update()
		if flow==False:
			global gh
			gh = onu
			break
	return
def Stop():
	global ToActivateStopButton
	if ToActivateStopButton==False:
		return
	global b1title
	global flow
	#FG=b1.cget("text")
	#print(FG)
	if b1.cget("text")=="Stop":

		flow=False
		b1title.set("Resume")

	elif b1.cget("text")=="Resume":
		flow=True
		b1title.set("Stop")
		runn(onu=gh)
	return



	
#scroll=Scrollbar(root)
#scroll.place(x=10,y=260,width=480,height=150)
alart=Label(root,text="!!!Don't Close When Text Scroll\n Please Stop the running by \nClick Below the Button \nThen Close it.!!!")
alart.place(x=300,y=10)
l=Label(root,text="WELCOME TO PATTERN \n Enter your Name",bg="#7FE5F0",fg="#000000")
l.place(x=10,y=0,width=150)
e=Entry(root)
e.place(x=10,y=50,width=150)
b=Button(root,text="Show Pattern",command=run)
b.place(x=10,y=80,width=150)
t=Text(root,bg="#c9df8a",width=10,fg="#234d20",wrap=WORD)
t.place(x=10,y=120,width=480,height=150)
global b1title
b1title=StringVar()
b1title.set("Stop")
b1=Button(root,textvariable=b1title,command=Stop)
b1.place(x=300,y=80,width=50)


root.mainloop()











	
'''	
		for i in range(8):
			for k in range(len(li)):
				for j in range(len(li[k][0])):
					print(li[k][i][j],end="")
				print(end=" ")
			print("/n")
'''