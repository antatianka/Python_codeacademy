#User calendar which is accessible from comand line
from time import sleep, strftime
USER_FIRST_NAME = "Tatyana"
calendar = {}
def welcome():
    print "Welcome, " + USER_FIRST_NAME + "."
    print "Calendar starting..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "The time is: " + strftime("%H:%M:%S")
    print "What would you like to do?"





def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V': 
            if len(calendar.keys()) < 1:
                print "Calendar empty."
            else:
                print calendar 
        elif user_choice == 'U':
            date = raw_input("What date? ")
            update = raw_input("Enter the update: ")   
            calendar[date] = update
            print "The update being successful."
            print "The calendar %s" % (calendar)   
        elif user_choice == 'A':
            date = raw_input("Enter date (MM/DD/YYYY):")
            event = raw_input("Enter your event:")
            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print "Invalid date was entered."  
                try_again = raw_input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print "The event was successfully added."
        elif user_choice == "D":
            if len(calendar.keys())<1:
                print "The calendar is empty." 
            else:
                event = raw_input("What is your event?")
                for date in calendar.keys():
                    if calendar[date] == event:
                        del calendar[date]
                        print "The event was successfully deleted."
                    else:
                        print "Incorect event was specified."  
        elif user_choice == "X":
            start = False  
        else:
            print "This is a gabage."
            
start_calendar()                        
                        
                        
                        
                        
                      
                  
                  
              
          
                    
                    

