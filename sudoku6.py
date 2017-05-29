import sudomodule6 as sm
import numpy as np
import time
puz = [[0,0,0,0,0,0,5,0,0],[0,0,0,6,0,9,0,3,0],[0,0,9,1,5,0,0,2,6],[3,0,0,0,0,8,0,5,7],[0,0,7,0,0,0,2,0,0],[8,6,0,3,0,0,0,0,4],[7,4,0,0,6,5,9,0,0],[0,5,0,4,0,3,0,0,0],[0,0,8,0,0,0,0,0,0]]
#puz = [[0,6,0,2,7,0,1,0,0],[0,0,9,8,0,0,0,0,6],[0,3,7,0,0,0,4,0,0],[0,0,0,4,2,0,9,7,0],[0,0,0,6,0,1,0,0,0],[0,8,2,0,3,9,0,0,0],[0,0,5,0,0,0,3,9,0],[7,0,0,0,0,5,2,0,0],[0,0,3,0,8,2,0,1,0]]

missing_indices=[]
missing_values=[]

for row in puz:
	sm.l = []
	row_missing=[]
	for item in range(1,10):
		if item not in row:
			row_missing.append(item)
	missing_values.append(sm.perm(row_missing))
	"""
	for item in sm.perm(row_missing):
		print(len(row_missing), len(item))
	"""

	indices_missing = []
	for i in range(0,9):
		if row[i] == 0:
			indices_missing.append(i)
	missing_indices.append(indices_missing)

"""
for row in missing_values[0]:
	print(row)
"""


def inplace(puz, x):
	#print('Going to next level', x)
	for row in missing_values[x]:
		if(sm.check(puz,row,missing_indices[x],x)):
			sm.place(puz[x], missing_indices[x], row)
			if(x==8):
				print puz
				
				return
			inplace(puz,x+1)
			#print puz
			#print x
		else:
			for i in missing_indices[x]:
				puz[x][i]=0
		

	
			
	#print puz
	
		
	
inplace(puz,0)
#print(puz)

