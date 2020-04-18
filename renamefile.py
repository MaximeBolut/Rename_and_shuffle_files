import os

#path of the file to be renamed
directory=input(print("give the folder path where you want your file to be renamed"))
os.chdir(directory)

#type of file you want to change
type_file=input(print("give the type of file you want to rename (Example, for jpg type: .jpg)"))

safety=0
while safety ==0:
      
    if type_file[0]!='.':
      print('invalid format, it need to be start with: . ')
      type_file=input(print("give the type of file you want to rename (Example, for jpg type: .jpg)"))
    
    else:
        safety=1

#New name you want to give to your files
name=input(print("give the new name you want for your files"))

#renaming the files of interest with the given name and the index of the created list (shuffled number from O to the number of file-1)
cpt=0 
for file in os.listdir():
    if type_file in file :                      #selecting only the file format we are interested in
      old_name=file                             #old name
      new_name=name+str(cpt)+type_file  #new name (keeping the file format extension)
      os.rename(old_name,new_name) 
      cpt+=1

#if a number of file>0 was renamed:
if cpt !=0:
  print(str(cpt)+" files in the "+str(type_file)+" format have been rename as "+ str(name)+ " from " + str(name)+"0 to "+str(name)+str((cpt-1)))

#otherwise if no file was renamed: 
else:
    print("there was no file with the mentioned format")
