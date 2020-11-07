#v1.0
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
root=Tk()
root.title("Words to Pattern by Python")
root.iconbitmap('.icon\man.ico')
root.configure(bg="#CBCBA9",width=320,height=300)



img = ImageTk.PhotoImage(Image.open(".img\man2.jpg"))
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
def run():	
	word=""

	word=e.get()
	word1=word.upper()
	li=[]
	
	for letter in word1:
		for l in range(28):
			if chr(65+l)==letter:
				li.append(TO[l])
		if letter==" ":
			li.append(sp)
		if letter==".":
			li.append(fs)
	

	t.delete(1.0,END)
	t.place(x=10,y=120,width=(len(li)*60),height=150)
	if len(li)<=5:
		root.configure(bg="#CBCBA9",width=320,height=300)
	elif len(li)>5:
		root.configure(bg="#CBCBA9",width=(50+(len(li)*60)),height=300)
	
	for i in range(8):
		for k in range(len(li)):
			for j in range(len(li[k][0])):
				a=li[k][i][j]
				t.insert(END,a)
			t.insert(END," ")
		t.insert(END,"\n")

	return

l=Label(root,text="WELCOME TO PATTERN \n Enter your Name",bg="#7FE5F0",fg="#000000")
l.place(x=10,y=0,width=150)
e=Entry(root)
e.place(x=10,y=50,width=150)
b=Button(root,text="Show Pattern",command=run)
b.place(x=10,y=80,width=150)
t=Text(root,bg="#c9df8a",width=10,fg="#234d20")
t.place(x=10,y=120,width=150,height=150)

root.mainloop()











	
'''	
		for i in range(8):
			for k in range(len(li)):
				for j in range(len(li[k][0])):
					print(li[k][i][j],end="")
				print(end=" ")
			print("/n")
'''