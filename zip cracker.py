import zipfile 
a=input("Enter the filename:") #enter the file name without the extension
a+=".zip"                          #the file must be in the same folder as the code
l1=["Ayush","ayush","gci","task","brute","force","cracking", "fedora",
      "project","good","password","string","strong","apple","fortnite",
      "python","zipfile","cracker","panda","windows","google","alphabet",
      "youtube","tree","cyber","security","19","winner","loud","winters"]
password = None 
open1= zipfile.ZipFile(a) 
for i in l1: 
    try:
        open1.extractall(pwd=bytes(i,'utf-8')) 
        password = "Password of the given zip file is: " + i 
        print(password) 
    except:
        pass