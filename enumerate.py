#First i want to print position and and its value without using enumerate
pos=0
name=['google','amazon','Dell','nasa']
for x in name:
	print(pos,'is the index of:',name[pos])
	pos+=1

pos=0
for x in name:
	print(f" {pos}-------->{name[pos]}")
	pos+=1


#Now by using enumerate function

name=['google','amazon','Dell','nasa']
for pos,name in enumerate(name):
	print(pos,"----------->",name)