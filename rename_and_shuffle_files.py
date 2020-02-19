# Pythono3 code to rename multiple 
# files in a directory or folder 
# importing os module 

import os 
import random
import numpy as np

# Function to rename multiple files 
def main(): 
    #path of the file to be renamed
	os.chdir("C:\\Users\\images")

	i = 0						  #or 0 if you want your files numbering index to start at 0 
	mylist =[]
	j=1
	itemnuber= len(os.listdir())

	for j in range(itemnuber):
		mylist.append(str(j))
		j+=1


	random.shuffle(mylist)
	#print(mylist)

	for file in os.listdir():
		src=file                  #old name
		dst="image"+str(mylist[i])+".png"  #new name to be put here (with the type of file)
		os.rename(src,dst) 
		i+=1


if __name__ == '__main__': 
# Calling main() function 
	main()
