# Python3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

# Function to rename multiple files 
def main(): 
    #path of the file to be renamed
	os.chdir("C:\\Users\\images")

	i = 0						  #or 0 if you want your files numbering index to start at 0 
	
	for file in os.listdir():
		src=file                  #old name
		dst="image_new_name"+str(i)+".png"  #new name to be put here (with the type of file)
		os.rename(src,dst) 
		i+=1



if __name__ == '__main__': 
# Calling main() function 
	main()
