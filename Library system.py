import pickle
import os


def addbook(): #will create file if not existing else read and add the records
    try:
        f=open('Book_module',"ab+")
        print(f.tell())
        if f.tell()>0:
            f.seek(0)
            Rec1=pickle.load(f)
        else:
            Rec1=[]
        while True:
            bname=input("Enter book name:")
            ath=input("Enter author:")
            genre=input("Enter genre:")
            price=float(input("Enter price:"))
            in_copies=int(input("Enter initial copies:"))
            rem_copies=int(input("Enter remaining compies:"))
            Rec=[bname.upper(),ath.upper(),genre.upper(),price,in_copies,rem_copies]
            Rec1.append(Rec)
            ch=input("Want to enter more records?:")
            if ch=='n' or ch=='N':
                break
        print(Rec1)
        f.close()
        with open("Book_module","wb")as f:
            pickle.dump(Rec1,f)
    except ValueError:
         print("Invalid values entered")
addbook()
            

    
def showbooks():  #display the added books
    try:
        with open("Book_module","rb") as f:
            print("="*75)
            print("BOOKNAME","AUTHOR","GENRE","PRICE","IN_COPIES","REM_COPIES",sep='      ')
            print("="*75)
            Rec=pickle.load(f)
            c=len(Rec)
            for i in Rec:
                for j in i:
                    print(j,end='\t')
                print()
            print("*"*75)
            print("Records read:",c)
            print("*"*75)
    except EOFError:
        print("="*75)
        print("Records read:",c)
    except FileNotFoundError:
            print(Book_module,"File not found")
showbooks()



def edit():  #make changes in the current information about books
    try:
        with open("Book_module","rb+") as f:
                  Rec1=pickle.load(f)
                  found=-1
                  A=input("Enter book whose details to be changed:")
                  for i in Rec1:
                      if i[0]==A:
                          found=0
                          ch=input("Change Book name(Y/N):")
                          if ch=='y' or ch=='Y':
                              i[1]=input("Enter name:")
                              i[1]=i[1].upper()

                          ch=input("Change author name(Y/N):")
                          if ch=='y' or ch=='Y':
                              i[2]=input("Enter author:")
                              i[2]=i[2].upper()

                          ch=input("Change genre(Y/N):")
                          if ch=='y' or ch=='Y':
                              i[3]=input("Enter genre")
                              i[3]=i[3].upper()

                          ch=input("Change price(Y/N):")
                          if ch=='y' or ch=='Y':
                              i[4]=float(input("Enter new price:"))

                          ch=input("Change no of initial copies(Y/N):")
                          if ch=='y' or ch=='Y':
                              i[5]=input("Enter new no of copies:")

                          ch=input("Change no of remaing copies(Y/N):")
                          if ch=='y' or ch=='Y':
                              i[6]=input("Enter remaining copies:")
                        
                  if found==-1:
                      print("Record not found..")
                  else:
                      f.seek(0)
                      pickle.dump(Rec1,f)
    except EOFError:
        print("Records Read:",c)
    except FileNotFoundError:
        print(Book_module,"File doesn't exist")
edit()


def searchname():  #will search the book by its name in uppercase
    try:
        with open("Book_module","rb")as f:
            Rec=pickle.load(f)
            ch=input("Enter book name to be searched:")
            for i in range(0,len(Rec)):
                if Rec[i][0]==ch.upper():
                    print("="*75)
                    print("BOOKNAME","GENRE","AUTHOR","PRICE","IN_COPIES","REM_COPIES")
                    print("="*75)
                    for j in Rec[i]:
                        print(j,end='\t')
                    print()
                    break
            else:
                print("Record not found")
    except FileNotFoundError:
        print(Book_module,"File not found")
searchname()


def delete():  #delete the required book
    try:
        with open("Book_module","rb+") as f:
            Rec=pickle.load(f)
            ch=input("Enter the book name to be deleted:")
            for i in range(0,len(Rec)):
                if Rec[i][0]==ch:
                    print(Rec.pop(i))
                    print("Record deleted")
                    break
            else:
                print("Record not found")

            f.seek(0)
            pickle.dump(Rec,f)

    except FileNotFoundError:
        print(Book_module,"File does not exist")
    except KeyError:
        print(Book_module,"Record not found")
    except IndexError:
        print(Book_module,"Record not found")
delete()

def main():
    while (True):
        print("Enter your choice\n1. Book Details\n2. Member Details\n3. Transaction\n4. Report\n5. Exit")
        choice=int(input())
        if choice==1:
            while(True):
                print("Enter Your Choice\n1. Add Book Details\n2. Show Book Details\
                     \n3. Edit book\n4. Search a book\n5. Delete book\n6.Back to main menu")
                ch=int(input())
                if ch==1:
                    print("1")
                elif ch==2:
                    print("2")
                elif ch==3:
                    print ("3")
                elif ch==4:
                    print("4")
                elif ch==5:
                    print("5")
                elif ch==6:
                    break
main()
