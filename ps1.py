###### this is the first .py file ###########

####### write your code here ##########

s=raw_input('')    #input from user

i=s.count('1')    # counts the no of 1's 


if i%2==0 :       # check whether even no of ones or odd if even then add 1 
	s=s+"1"
	print(s)
	k=s.replace('010','0100',s.count('010')) # insert 0 when 010 is found
	
	if s[-2:]=="01":   #if last two bit are 01 then replace with 010 and and insert flag also
		k=k[:-2]+"0100101"
		print(k)
	else : 
		k=k+"0101"
		print(k)
	

 	



else  :
	print(s)
	s.replace('010','0100',s.count('010'))
	if s[-2:]=="01":
		k=s[:-2]+"0100101"
		print(k)
	else : 
		k=k+"0101"
		print(k)
