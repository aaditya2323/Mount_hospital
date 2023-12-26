import os
from subprocess import call
import login
print("\n")
print("Welcome to the mounthospital app...\n")
print("Are you a author or user..\n")
print("""
           Enter '1' if you are author
           Enter '2' if you are user
           Enter '3' to exit

      .................................
      """)

def myfun():
      option=int (input("Enter\n::> "))
      if option==1:
            print ("Executing the forauthorfile..")
            a1=login.author
            if a1.loginauthor(a1):
             call("python ./forauthor.py")
            else:
                 print("!!!WRONG author name or password!!!")
      elif option==2:
            call("python ./user.py")
      else:
           exit(0)

      if __name__=="__main__":
           myfun()
      



            
    

myfun()
    
    



      
