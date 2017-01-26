import numpy as np
puz = [[0,6,0,2,7,0,1,0,0],[0,0,9,8,0,0,0,0,6],[0,3,7,0,0,0,4,0,0],[0,0,0,4,2,0,9,7,0],[0,0,0,6,0,1,0,0,0],[0,8,2,0,3,9,0,0,0],[0,0,5,0,0,0,3,9,0],[7,0,0,0,0,5,2,0,0],[0,0,3,0,8,2,0,1,0]]
[0,6,0,2,7,0,1,0,0]
#a=[3,4,5,8,9]
b=[0,2,5,7,8]
puzzle=np.array(puz)
#to check if a number missing in the row can be in a grid
def check_grid(p,i,j):

	ctr=0
	for y in range(0,10,3):
		for x in range(0,10,3):
			ctr=ctr+1
			if i in range(y,y+3) and j in range(x,x+3): 
				dict={'box':ctr,'l1':y, 'l2':y+3, 'u1':x, 'u2':x+3}
	lo1=dict['l1']
	lo2=dict['l2']
	up1= dict['u1']
	up2= dict['u2']
	grid=np.array(puz)[lo1:lo2:,up1:up2]
			
	print grid
	
	
	if not p in grid:
		return 1
	else:
		return 0



#to find all perms for a list

def perm(a,k=0):
	global l
	l=[]
	if(k==len(a)):
		temp=[]
		for val in a:
			temp.append(val)
		l.append(temp)
		
		
			
	else:
		for i in xrange(k,len(a)):
			a[k],a[i] = a[i],a[k]
			perm(a,k+1)
			a[k],a[i] = a[i],a[k]


	

def check_col(p):
	j=a.index(p)
	if p in puzzle[:,j]:
		print p
		return 0
	return 1
	
def check(a,x):
	j=0
	for p in a:
		print p
		print(check_grid(p,x,j) and check_col(p))
		j=j+1



	
	
