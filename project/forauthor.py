import csv
from user import *
class author:

    def __init__(self,d_sector,d_name,d_time) -> None:
        self.sector=d_sector
        self.name=d_name
        self.time=d_time


    def avilabledoc_(self):
        print("Give doctors information..\n")
        self.sector=input("enter a sector:>>")
        self.name=input("enter a name of doctor:>>")
        self.time=input("enter a time::>")
        with open("forauthor.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.sector, self.name, self.time])
                print("These are the abilable doctors in certain time")
                exit(0)

    def checkregister(self):
         with open("register.csv", "r",) as file:
                reader = csv.reader(file)
                for rows in reader:
                     print(f"""
                    :::::::::::::::::::::::::::::::
                        patient_name={rows[0]}
                        registerd_gmail={rows[1]}
                        registerd_num={rows[2]}
                    ::::::::::::::::::::::::::::::::
                     

                            """)
                     
                exit(0)
          

    


def meneu():
    d1=author(" "," "," ")
    print(f"""
        1) Enter '1' to add doc_details.
        2) Enter '2' to check register.
        3) enter '3' to exit the program.
      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            """)
    choice=int (input("Enter your choice::>"))
    if choice==1:
         d1.avilabledoc_()
    
    elif choice==2:
        d1.checkregister()
     
    elif choice==3:
         exit()

    else:
         print("please enter valid choice..")
         exit()
    
    
   # u1=user

meneu()




        
    