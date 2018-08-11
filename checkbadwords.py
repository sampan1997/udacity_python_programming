from urllib.request import urlopen
def readfile():

   file= open(r"C:/Users/DELL/Desktop/mlexx/ML6-SVM/machine-learning-ex6/ex6/emailSample2.txt")
   contents=file.read()
   print(contents)
   file.close()
   checkprofanity(contents)
def checkprofanity(text):
   connection=urlopen("http://www.wdyl.com/profanity?q="+text)
   output=connection.read()
   print(output)
   connection.close()
   

readfile()
