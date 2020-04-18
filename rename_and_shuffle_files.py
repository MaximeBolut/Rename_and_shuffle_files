# Pythono3 code to rename multiple files (here png) in a directory or folder 
# importing os module 

import os 
import random


# Function to rename multiple files 
def main(): 
    #path of the file to be renamed
	os.chdir("C:\\Users\\images")

	mylist =[str(j) for j in range(len(os.listdir()))]
	random.shuffle(mylist)
	
	i = 0
	for file in os.listdir():
		src=file                           #old name
		dst="image"+str(mylist[i])+".png"  #new name to be put here (with the type of file)
		os.rename(src,dst) 
		i+=1


if __name__ == '__main__': 
# Calling main() function 
	main()
