## LIBRARY MANAGEMENT SYSTEM PROJECT



#                                     GROUP MEMBERS

#       HASSAAN ABDULLAH       2022-UAM-1951
#       ABDUL-BASIT            2022-UAM-1935
#       SYED HAIDER ABBAS      2022-UAM-1939
#       MAZHAR GHAFFAR         2022-UAM-1916
#       ZAIN-UL-ABIDEEN AZAM   2022-UAM-1928

#                      A PROGRAM THAT ALLOW THE USER TO DISPLAY INFORMATION ABOUT LIBRARY
#              IT CONTAIN MULTIPLE FEATURE     (ADD_BOOKS)--(DISPLAY_BOOKS)--(DELETE ANY BOOK TAHT YOU WANT) 
#                  WE ALSO ADD THOSE FEATURE THAT WAS GIVEN MEAN INHERITANCE, EXCEPTION HANDLING
#                        AND WE ADD ADDITIONALL TASK THAT IS FILE HANDLING TO STORE BOOKS DATA





#class of book
class Books:
    def init (self,BK_name,BK_Author,BK_ISBN):
        self.BK_name=BK_name
        self.BK_Author=BK_Author
        self.BK_ISBN=BK_ISBN
class Fiction(Books):
    def write_Fiction_File(self):
        file=open("Fiction Books.txt","a")
        BK_name=file.write(f"BOOK_NAME           :   { self.BK_name } \n")
        BK_Author=file.write(f"Author Of Book      :   { self.BK_Author } \n")
        BK_ISBN=file.write(f"BOOK_ISBN           :   { self.BK_ISBN } \n")
        file.write("\n")
        file.close()
    def read_Fiction_File(self):
        file=open("Fiction Books.txt","r")
        print(file.read())
        file.close()
    # polymorphyism  method  <delete_book
    def delete_book(self):
        with open ('Fiction Books.txt','r') as f:
            lines=f.readlines()
        try:
            num=input('Enter your Book Name which you want to delete  :  ')
        except:
            print("Wrong input \ Enter correct Book name")
        with open ('Fiction Books.txt','w') as f:
            i=0
            while i<len(lines):
                if num in lines[i]:
                    i+=4
                else:
                    f.write(lines[i])
                    i+=1


    
    
class NON_Fiction(Books):
    def NON_Fiction_Display(self):
        print("NON FICTION BOOKS")
    def write_NON_Fiction_File(self):
        file=open("Non Fiction Books.txt","a")
        BK_name=file.write(f"BOOK_NAME           :   { self.BK_name } \n")
        BK_Author=file.write(f"Author Of Book      :   { self.BK_Author } \n")
        BK_ISBN=file.write(f"BOOK_ISBN           :   { self.BK_ISBN } \n")
        file.write("\n")
        file.close()
    def read_NON_Fiction_File(self):
        file=open("NON Fiction Books.txt","r")
        print(file.read())
        file.close()
    # polymorphyism  method  <delete_book
    def delete_book(self):
        with open ('NON Fiction Books.txt','r') as f:
            lines=f.readlines()
        try:
            num=input('Enter your Book Name which you want to delete  :  ')
        except:
            print("Wrong input \ Enter correct Book name")
        with open ('NON Fiction Books.txt','w') as f:
            i=0
            while i<len(lines):
                if num in lines[i]:
                    i+=4
                else:
                    f.write(lines[i])
                    i+=1

    
        
        
class Textbook(Books):
    def Textbook_Display():
        print("Textbook ")
    def write_Textbook_File(self):
        file=open("textbooks.txt","a")
        BK_name=file.write(f"BOOK_NAME            :   { self.BK_name } \n")
        BK_Author=file.write(f"Author Of Book       :   { self.BK_Author } \n")
        BK_ISBN=file.write(f"BOOK_ISBN            :   { self.BK_ISBN } \n")
        file.write("\n")
        file.close()
    def read_Textbook_File(self):
        file=open("textbooks.txt","r")
        print(file.read())
        file.close()
    # polymorphyism  method  <delete_book
    def delete_book(self):
        with open ('textbooks.txt','r') as f:
            lines=f.readlines()
        try:
            num=input('Enter your Book Name which you want to delete  :  ')
        except:
            print("Wrong input \ Enter correct Book name")
        with open ('textbooks.txt','w') as f:
            i=0
            while i<len(lines):
                if num in lines[i]:
                    i+=4
                else:
                    f.write(lines[i])
                    i+=1

    
        
        
#class of library 
class library:
    def __init__(self,name,location,num_of_books,opening_time,closing_time):
        self.name=name
        self.location=location
        self.num_of_books=num_of_books
        self.opening_time=opening_time
        self.closing_time=closing_time
         
    # encapsulation << data of owner >>
    def __owner_details (self):
        self.name="Mujahid"
        self.ph_no="03018100088"
        print(f"OWNER NAME            :  {self.name}")
        print(f"OWNER PHONE NUMBER    :  {self.ph_no}")
    
    def get_owner_details(self):
        return self.__owner_details()
        
    def display_Library(self):
        print("WELL COME TO                 : ",self.name)
        print("LOCATION                     : ",self.location)
        print("NUMBER OF BOOKS IN LIBRARY   : ",self.num_of_books)
        print("OPENING TIME                 : ",self.opening_time)
        print("CLOSING TIME                 : ",self.closing_time)
obj1=library('BOGGY WOGGy LIBRARY ','CENTRAL MULTAN','50','10 AM','10 PM')

i=1
while i==1:
    
    #main menu
    print("       ____________________________________________________________")
    print("      |              WELL-COME TO BOGGY WOGGY LIBRARY              |")
    print("      |____________________________________________________________|")
    print("      |                         MAIN--MENU                         |")
    print("      |___________________________________________________________ |")
    print("      |             PRESS 1 FOR DETAILS OF LIBRARY                 |")
    print("      |             PRESS 2 FOR ADD BOOKS                          |")
    print("      |             PREEs 3 FOR VIEW BOOKS IN LIBRARY              |")
    print("      |             PRESS 4 FOR DELETING BOOKS                     |")
    print("      |             PRESS 5 FOR EXIT                               |")
    print("      |____________________________________________________________|")
    try:
        a=int(input("ENTER YOUR CHOICE : "))
    except:
        print("PLEASE ENTER INTEGER AS A CHOICE")
    if a == 1:
        print("******************( LIBRARY  )**********************")
        obj1.display_Library()
        print(" IF YOU WANT TO NOW ABOUT OWNER PRESS 'y' else 'n'  :  " )
        ch=input("ENTER YOUR CHOICE  :  ")
        if ch == 'y':
            print(obj1.get_owner_details())
        elif ch =='n':
            print(" AS YOU WISH ")
        else:
            print("WRONG INPUT")
              
              
        print("________________________________________________________")
    elif a == 2:
        loop=0
        while loop==0:
            print("       ____________________________________________________________")
            print("      |                  ADD BOOK INTERFACE                        |")
            print("      |____________________________________________________________|")
            print("      |                         MENU                               |")
            print("      |___________________________________________________________ |")
            print("      |             PRESS 1 TO ADD FICTION BOOKS                   |")
            print("      |             PRESS 2 TO ADD NON-FICTION BOOKS               |")
            print("      |             PREEs 3 TO ADD TEXTBOOKS                       |")
            print("      |             PRESS 4 FOR EXIT                               |")
            print("      |____________________________________________________________|")
            try:
                choice=int(input("ENTER YOUR CHOICE : "))
            except:
                print("PLEASE ENTER ONLY INTEGER AS CHOICE")
            if choice == 1:
                print("\n\n******************( ADD FICTION BOOK INFORMATION )*******************\n")
                try:
                    BK_name=input("ENTER NAME OF THE BOOK : ") 
                except:
                    print("Invalid Input")
                try:   
                    BK_Author=input("ENTER AUTHOR OF BOOK : ")
                except:
                     print("Invalid Input")
                try:
                    BK_ISBN=int(input("ENTER ISBN OF BOOK : "))
                except:
                    print("Invalid Input")
                
                obj=Fiction()
                obj.init(BK_name,BK_Author,BK_ISBN)
                obj.write_Fiction_File()
                print("\n***************( FICTION BOOK ADDED SUCCESSFULLY )********************")
                print("\n \n")
            elif choice == 2:
                print("\n\n******************( ADD NON_FICTION BOOK INFORMATION )*******************\n")
                try:
                    BK_name=input("ENTER NAME OF THE BOOK : ") 
                except:
                    print("Invalid Input")
                try:   
                    BK_Author=input("ENTER AUTHOR OF BOOK : ")
                except:
                     print("Invalid Input")
                try:
                    BK_ISBN=int(input("ENTER ISBN OF BOOK : "))
                except:
                    print("Invalid Input")
                    
                obj=NON_Fiction()
                obj.init(BK_name,BK_Author,BK_ISBN)
                obj.write_NON_Fiction_File()
                print("\n*******************( NON-FICTION ADDED SUCCESSFULLY )*******************")
                print("\n \n")
            elif choice == 3:
                print("\n\n******************( ADD TEXT BOOK INFORMATION )*******************\n")
                try:
                    BK_name=input("ENTER NAME OF THE BOOK : ") 
                except:
                    print("Invalid Input")
                try:   
                    BK_Author=input("ENTER AUTHOR OF BOOK : ")
                except:
                     print("Invalid Input")
                try:
                    BK_ISBN=int(input("ENTER ISBN OF BOOK : "))
                except:
                    print("Invalid Input")
                
                    
                obj=Textbook()
                obj.init(BK_name,BK_Author,BK_ISBN)
                obj.write_Textbook_File()
                print("\n**********************( TEXT BOOK ADDED SUCCESSFULLY )***********************")
                print("\n \n")
            elif choice == 4:
                loop=1
            else :
                print("WRONG INPUT")
                loop=1
            

    elif a == 3:
        print("       ____________________________________________________________")
        print("      |                     SHOW BOOK INTERFACE                    |")
        print("      |____________________________________________________________|")
        print("      |                         MENU                               |")
        print("      |____________________________________________________________|")
        print("      |             PRESS 1 TO SHOW FICTION BOOKS                  |")
        print("      |             PRESS 2 TO SHOW NON-FICTION BOOKS              |")
        print("      |             PREEs 3 TO SHOW TEXTBOOKS                      |")
        print("      |             PRESS 4 FOR EXIT                               |")
        print("      |____________________________________________________________|")
        loop=0
        while loop==0:
            try:
                chose=int(input("ENTER YOUR CHOICE : "))
            except:
                print("PLEASE ENTER ONLY INTEGER ")
            if chose == 1:
                print("******************( THE FICTION BOOKS IN LIBRARY IS )*********************")
                print("__________________________________________________________________________")
                obj=Fiction()
                obj.read_Fiction_File()
                print("***********************************************************************")
            elif chose ==2:
                print("***********************( THE NON FICTION BOOK IS )***********************")
                print("_________________________________________________________________________")
                obj=NON_Fiction()
                obj.read_NON_Fiction_File()
                print("***********************************************************************")
            elif chose ==3:
                print("****************************(  TEXT BOOKS  )******************************")
                print("__________________________________________________________________________")
                obj=Textbook()
                obj.read_Textbook_File()
                print("*************************************************************************")
            elif chose==4:
                loop=1
            else :
                print(" WRONG INPUT ")
    elif a == 4:
        print("       ____________________________________________________________")
        print("      |                     DELETING BOOKS                         |")
        print("      |____________________________________________________________|")
        print("      |                         MENU                               |")
        print("      |___________________________________________________________ |")
        print("      |             PRESS 1 TO DELETE FICTION BOOKS                |")
        print("      |             PRESS 2 TO DELETE NON-FICTION BOOKS            |")
        print("      |             PREEs 3 TO DELETE TEXTBOOKS                    |")
        print("      |             PRESS 4 FOR EXIT                               |")
        print("      |____________________________________________________________|")
        loop=0
        while loop==0:
            try:
                chose=int(input("ENTER YOUR CHOICE : "))
            except:
                print("PLEASE ENTER ONLY  INTEGER")
            if chose == 1:
                print("***************************************************************************")
                obj=Fiction()
                obj.delete_book()
                print("**********************( THE FICTION BOOK HAS BEEN DElETED )************************")
                
        
            elif chose ==2:
                print("***************************************************************************")
                obj=NON_Fiction()
                obj.delete_book()
                print("*******************( THE NON-FICTION BOOK HAS BEEN DElETED )**********************")
                                
            elif chose ==3:
                print("***************************************************************************")
                obj=Textbook()
                obj.delete_book()
                print("********************( THE TEXT-BOOK HAS BEEN DElETED )***************************")
                                
            elif chose==4:
                loop=1
            else :
                print(" WRONG INPUT ")

    elif a == 5:
        print("***********************( THANKS FOR VISITING )*****************************")
        break
    else :
        print("invalid Input")
