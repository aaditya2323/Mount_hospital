import csv
class author:
    authorname=" "
    password=" "

    def __init__(self,a_name,a_password) -> None:
        self.authorname=a_name
        self.password=a_password

    def creatauthor(self):
        self.authorname=input("create username::>")
        self.password=input("create password::>")
        confirm_password=input("please confirm your password ::>  ")
        if self.password==confirm_password:
            with open("author.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.authorname, self.password])
        else :
            print("Something Went Wrong :( !")

    def __str__(self) -> str:
        return f"{self.authorname} was created"
    
    def loginauthor(self):
        self.authorname=input("enter author name::>")
        self.password=input("enter password::>")
        with open("author.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if self.authorname==row[0] and self.password==row[1]:
                    print("login sucessfully...")
                    return True
                else:
                    print("something went wrong!!!!")
                    return False
    

def meneu():
    a1=author(" "," ")
   # a1.creatauthor()
    a1.loginauthor()
    if __name__=="__main__":
        meneu()




    


        


        
    