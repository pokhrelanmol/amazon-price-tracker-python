# car game
command= ""
started = False
while True:
    command = input("command> ").lower()
    
    if(command == "start"):
        if(started):
            print("Car is already started")
        else:
           started = True
           print("car started ...")
    elif(command == "stop"):
        if(not started):
          print("Car is already stopped") 
        else:
           started = False  
           print("car stopped ..." )
    elif(command == "help"):
        print('''
start -> to start a car
stop -> to stop a car
quit -> to quit this program
          ''')
    elif(command == "quit"):
        break
    else:
        print("sorry, I don't understand that command")
#function
def add(numbersToAdd):
    sum = 0
    for i in numbersToAdd:
        sum+=i
    return sum
   