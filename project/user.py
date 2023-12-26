import csv

class user:

    def __init__(self,u_name,u_gmail,u_number) -> None:
        self.name=u_name
        self.gmail=u_gmail
        self.number=u_number

    print("These are the doctors avilable at this time")
    def check(self):
        with open("forauthor.csv", "r") as file:
            reader= csv.reader(file)
            for rows in reader:
                print (f"""
                    Specealist={rows[0]}
                    doctor_name={rows[1]}
                    time={rows[2]}
            ..................................


                    """)
                
                
    def register(self):
        print("enter your information to book a apointment")
        self.name=input("enter patient name::>")
        self.gmail=input("enter a gmail")
        self.number=input("enter a number")
        with open("register.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.name, self.gmail, self.number])
                print("SUCESFULLY REGISTERD")
            
            
                
        
        
    
                
    
def call():
    u1= user("","","")
    u1.check()
    u1.register()
    exit(0)
        
if __name__=="__main__":
    call()
        





        
        

