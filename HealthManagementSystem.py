

def getDateTime():
    import datetime
    return datetime.datetime.now()

while True:


    print("=====WELCOME TO HEALTH MANAGEMENT SYSTEM=====")
    print("Enter the Client Number\n1. for Harry\n2. for Rohan\n3. for Hammad\n4. Exit")
    clientnum=int(input())
    #CLIENT IS HARRY
    if clientnum==1:
        print("Do you want to log data retrieve data?\n1.Log Data\n2. Retrieve Data")
        datachoice=int(input())
        if datachoice==1:
            print("What do you want to log?\n1. Exercise\n2. Diet")
            logchoice=int(input())
            if logchoice==1:
                with open("harryexercise.txt","a") as f:
                    s=input("Enter what you want to save:\n")
                    print(getDateTime())
                    f.write(str(getDateTime()))
                    f.write(s)
            elif logchoice==2:
                with open("harrydiet.txt","a") as f:
                    s=input("Enter what you want to save:\n")
                    print(getDateTime())
                    f.write(str(getDateTime()))
                    f.write(s)
        elif datachoice==2:
             print("What do you want to retrive?\n1. Exercise\n2. Diet")
             logchoice=int(input())
             if logchoice==1:
                with open("harryexercise.txt","r") as f:
                    s=int(input("Enter the starting adress from where you want to retrive:\n"))
                    print(f.readline(s))
                    print(getDateTime())
             elif logchoice==2:
                with open("harrydiet.txt","r") as f:
                    s=int(input("Enter the starting adress from where you want to retrive:\n"))
                    print(f.readline(s))
                    print(getDateTime())

    #CLIENT IS ROHAN

    elif clientnum==2:
        print("Do you want to log data retrieve data?\n1.Log Data\n2. Retrieve Data")
        datachoice=int(input())
        if datachoice==1:
            print("What do you want to log?\n1. Exercise\n2. Diet")
            logchoice=int(input())
            if logchoice==1:
                with open("rohanexercise.txt","a") as f:
                    s=input("Enter what you want to save:\n")
                    print(getDateTime())
                    f.write(str(getDateTime()))
                    f.write(s)
            elif logchoice==2:
                with open("rohandiet.txt","a") as f:
                    s=input("Enter what you want to save:\n")
                    print(getDateTime())
                    f.write(str(getDateTime()))
                    f.write(s)
        elif datachoice==2:
             print("What do you want to retrive?\n1. Exercise\n2. Diet")
             logchoice=int(input())
             if logchoice==1:
                with open("rohanexercise.txt","r") as f:
                    s=int(input("Enter the starting adress from where you want to retrive:\n"))
                    print(f.readline(s))
                    print(getDateTime())
             elif logchoice==2:
                with open("rohan.txt","r") as f:
                    s=int(input("Enter the starting adress from where you want to retrive:\n"))
                    print(f.readline(s))
                    print(getDateTime())
    #CLIENT IS HAMMAD
    elif clientnum==3:
        print("Do you want to log data retrieve data?\n1.Log Data\n2. Retrieve Data")
        datachoice=int(input())
        if datachoice==1:
            print("What do you want to log?\n1. Exercise\n2. Diet")
            logchoice=int(input())
            if logchoice==1:
                with open("hammadexercise.txt","a") as f:
                    s=input("Enter what you want to save:\n")
                    print(getDateTime())
                    f.write(str(getDateTime()))
                    f.write(s)
            elif logchoice==2:
                with open("hammaddiet.txt","a") as f:
                    s=input("Enter what you want to save:\n")
                    print(getDateTime())
                    f.write(str(getDateTime()))
                    f.write(s)
        elif datachoice==2:
             print("What do you want to retrive?\n1. Exercise\n2. Diet")
             logchoice=int(input())
             if logchoice==1:
                with open("hammadexercise.txt","r") as f:
                    s=int(input("Enter the starting adress from where you want to retrive:\n"))
                    print(f.readline(s))
                    print(getDateTime())
             elif logchoice==2:
                with open("hammaddiet.txt","r") as f:
                    s=int(input("Enter the starting adress from where you want to retrive:\n"))
                    print(f.readline(s))
                    print(getDateTime())
    elif clientnum==4:
        print("Program Ended")
        break 
    
    else :
            print("Invalid Client Number! Please try again.")   
        


               

