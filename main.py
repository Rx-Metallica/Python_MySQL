import os
from dbhelper import DB


def main():
    database=DB()
    while True:
        print("**********WELCOME***********")
        print()
        print("1: Press 1 to insert New User")
        print("2: Press 2 to Display All User User")
        print("3: Press 3 to Delete User")
        print("4: Press 4 to Update User")
        print("5: Press 5 to exit")
        print()
        try:
            choice=int(input())
            if choice==1:
                uid=int(input("Enter User Id"))
                username=input("Enter User Name")
                userphone=input("Enter User Phone")
                database.insert_user(uid,username,userphone)
            elif choice == 2:
                database.fetch_all()
            elif choice==3:
                userid=int(input("Enter Id to Delete User: "))
                database.delete_user(userid)
            elif choice == 4:
                database.update_user(uid,username,userphone)
                username=input("Enter New Name")
                userphone=input("Enter New Phone")
                #database.update_user(uid,username,userphone)
            elif choice == 5:
                break
            else:
                print("Invalid try again")
        except Exception as e:
            print(e)
            print("invalid Details")
if __name__== "__main__":
    main()