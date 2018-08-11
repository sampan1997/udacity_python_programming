import os
def rename_files():
    Filelist= os.listdir(r"C:\Users\DELL\Desktop\kunal chawla python programming\prank")
    print(Filelist)
    saved=os.getcwd();
    print(os.getcwd())
    os.chdir(r"C:\Users\DELL\Desktop\kunal chawla python programming\prank")
    
    for f in Filelist:
        #os.rename(f,f.translate(none,'0123456789'))
        print("file name"+f)
        os.rename(f,f.translate(f.maketrans('', '', '1234567890')))
        
    os.chdir(saved)



rename_files()
  

