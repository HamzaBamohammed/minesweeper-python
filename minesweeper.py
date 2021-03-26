def makeBoard(lvl):
	import random
	#the grid
	board=[]
	#the first and last line of the grid
	st=list()
	for i in range(lvl+2):
		st.append(["-","-"])
	board.append(st)
	#the body of the grid
	minesNum=0
	for i in range(lvl):
		L=list()
		ind=0
		L.append(["|","|"])
		for j in range(lvl):
			a=random.choice("@-")
			if a=="@" : ind+=1
			L.append([a,"+"])
		L.append([ind,"|"])
		board.append(L)
		minesNum+=ind
	#the last line of the grid
	board.append(st)
	#remplacing safe cells with number of adjacent mines 
	for i in range(1,lvl+1):
		for j in range(1,lvl+1):
			if board[j][i][0]=='-':
				board[j][i][0]=0
				if board[j][i+1][0]=="@": board[j][i][0]+=1
				if board[j][i-1][0]=="@": board[j][i][0]+=1
				if board[j+1][i+1][0]=="@": board[j][i][0]+=1
				if board[j+1][i-1][0]=="@": board[j][i][0]+=1
				if board[j+1][i][0]=="@": board[j][i][0]+=1
				if board[j-1][i+1][0]=="@": board[j][i][0]+=1
				if board[j-1][i-1][0]=="@": board[j][i][0]+=1
				if board[j-1][i][0]=="@": board[j][i][0]+=1
	ind=0
	while ind<(lvl*2):
		a=random.randrange(1,lvl-1)
		b=random.randrange(1,lvl-1)
		if board[a][b][0]!="@":
			ind+=1
			step(board,a,b)
	return board,minesNum

def showBoard(A):
	for i in range(len(A)):
		for j in range(len(A[0])):
			print(A[i][j][1],end=" ")
			if i==0 and j==len(A)-1 : print("x",end="")
		print()
	print("y")
	return

def step(A,x,y):
	A[x][y][1]=A[x][y][0]
	return

def flag(A,x,y):
	A[x][y][1]="#"
	return
	
#program start
print('MINESWEEPER GAME LITE 2021')
Q=1
lvl=4
while Q :
	Q=1
	print("LEVEL :", lvl-3)
	grid,minesNum=makeBoard(lvl)
	showBoard(grid)
	print()
	while True:
		tot=lvl*lvl
		print("enter coordinates x and y and action (step or flag) :")
		a,b,action=map(str,input().split())
		a,b,=int(a),int(b)
		if action=="flag" : 
			flag(grid,a,b)
			showBoard(grid)
		elif action=="step":
			step(grid,a,b)
			if grid[a][b][1]=="@":
				print("BOOM ! You died x_x ")
				showBoard(grid)
				print("Press 1 to restart, 0 to exit :",end=" ")
				Q=int(input())
				lvl=1
				break
			elif grid[a][b][1]!="+":
				print("This case is already chosen. Please try another one.")
				continue
			else :
				showBoard(grid)
				tot-=1
		else :
			print("False input ! please enter the command correctly (x y flag/step)")
			continue
		if tot==minesNum :
			lvl+=1
			print("Party won ! Upgrade to level >>>>>", lvl-3)
			break


