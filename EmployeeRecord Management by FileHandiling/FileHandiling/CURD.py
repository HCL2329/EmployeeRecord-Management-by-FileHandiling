import os
z=1
while(True):
    print("\n 1.Add Record")
    print("\n 2.Display All Record")
    print("\n 3.Search Employee  Record by name")
    print("\n 4.Search Employee Record by Id")
    print("\n 5.Delete Employee  Record by name")
    print("\n 6.Update Employee Record ")
    print("\n 7.Exit")
    print()
    n=int(input("Enter your choice :"))
    if(n==7):
        break
    elif(n==1):
        print("\nEnter Employee Details :\n")
        n=input("Enter Employee name :")
        id=input("Enter Employee id number :")
        d=input("Enter Employee Department :")
        sal=input("enter Employee Salary :")
        f=open("Employee.txt","a")
        f.write(n+"-"+id+"-"+d+"-"+sal+"\n")
        f.close()
    elif(n==2):
        print("\n List of Present Record \n")
        print("NAME-ID-Department-Salary")
        f=open("Employee.txt","r")
        while(True):
            d=f.readline()
            l=len(d)
            if(l==0):
                break
            print(d.strip())
        f.close()
    elif(n==3):
        name=input("Enter employee Name :")
        f=open("Employee.txt","r")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
               break
            g=t.split("-")
            if(g[0]==name):
                print("\n Record Found")
                print("Employee Name  is :",g[0])
                print("Employee id is :",g[1])
                print("Employee Department is :",g[2])
                print("Employee Salary is :",g[3])
                flag=1
                break
        if(flag==0):
            print("Record not found")
        f.close()
    elif(n==4):
        id=input("Enter employee ID :")
        f=open("Employee.txt", "r")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split("-")
            if(g[1]==id):
                print("\n Record Found")
                print("Employee Name  is :",g[0])
                print("Employee id is :",g[1])
                print("Employee Department is :",g[2])
                print("Employee Salary is :",g[3])
                flag=1
                break
        if(flag==0):
            print("Record not found")
        f.close()

    elif(n==5):
        empname=input("Enter Employee name to Delete :")
        f=open("Employee.txt","r")
        tt=open("temp.txt","w")
        h=0
        flag=0
        while(True):
            d=f.readline()
            l=len(d)
            if(l==0):
                break
            g=d.split("-")
            if(g[0]!=empname):
                tt.write(d)
            if(g[0]==empname):
                h=1
        f.close()
        tt.close()

        if(h==1):
            print("Record delete succesfully ")
            os.remove("Employee.txt")
            os.rename("temp.txt", "Employee.txt")
        elif(h==0):
            print("Record not found ! Deletion Unsuccesful")
    elif(n==6):
        h=0
        empName=input("Enter employee name to update :")
        f=open("Employee.txt","r")
        tt=open("temp.txt","w")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split("-")
            if(g[0]==empName):
                print("Current Details of Employee is :",t)
                print("---------------------------------------")
                newName = input("Want to change Change name ? Enter new details or Press enter to continue ")
                newid=input("Want to change id ? Enter new details or Press enter to continue ")
                newDept=input("Want to change DepartMent ? Enter new details or Press enter to continue ")
                newSal=input("Want to change  Salary ? Enter new details or Press enter to continue ")
                if(len(newName)==0):
                    newName=g[0]
                if(len(newid)==0):
                   newid=g[1]
                if(len(newDept)==0):
                    newDept=g[2]
                if(len(newSal)==0):
                    newSal=g[3]
                tt.write("\n"+newName+"-"+newid+"-"+newDept+"-"+newSal)
                h=1
            else:
                 tt.write(t)

        f.close()
        tt.close()
        if(h==1):
            print("Record Updated Succesfully")
            os.remove("Employee.txt")
            os.rename("temp.txt", "Employee.txt")
        elif(h==0):
             print("No Such Record Exist : for updation process ")
















