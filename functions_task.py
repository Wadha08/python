from datetime import datetime

yearOfbirth = input("Enter year of birth: ")
MonthOfbirth = input("Enter month of birth: ")
DayOfbirth = input("Enter day of birth: ")


def check_birthdate(yearOfbirth ,MonthOfbirth,DayOfbirth):#check if the dateBirth valid or not
    Date = (yearOfbirth+"-"+MonthOfbirth+"-"+DayOfbirth) #convert the string to date format
    DateBirth = datetime.strptime(Date, "%Y-%m-%d") #convert the string to datetime object
    currentDate = datetime.now()
    if currentDate.date() > DateBirth.date():
        return calculate_age(yearOfbirth,MonthOfbirth,DayOfbirth)
    else:
        return print("the birthdate is invalid.")

def calculate_age(yearOfbirth ,MonthOfbirth,DayOfbirth):
    Date = (yearOfbirth+"-"+MonthOfbirth+"-"+DayOfbirth) #convert the string to date format
    DateBirth = datetime.strptime(Date, "%Y-%m-%d") #convert the string to datetime object
    currentDate = datetime.now()

    #Calculate Days seperatly 
    Daybirth = DateBirth.day
    Daycurrent = currentDate.day

    #Calculate Month seperatly 
    MonthOfbirth = DateBirth.month
    Monthcurrent = currentDate.month

    #Calculate Years seperatly 
    yearOfbirth = DateBirth.year
    yearcurrent = currentDate.year


    #Days left
    if Daycurrent < Daybirth: 
        Daycurrent = Daycurrent+30
        Dayleft = Daycurrent-Daybirth
        Monthcurrent = Monthcurrent-1

    else:
        Dayleft = Daycurrent-Daybirth

 

    #Month left
    if Monthcurrent < MonthOfbirth:
        Monthcurrent =  Monthcurrent+12
        MonthLeft = Monthcurrent - MonthOfbirth
        yearcurrent = yearcurrent-1
        Monthleft = Monthcurrent - MonthOfbirth
    

    else:
        Monthleft = Monthcurrent - MonthOfbirth
        #print(Monthleft)


        #years left 
    yearsleft =yearcurrent-yearOfbirth
    print("You are "+str(yearsleft)+" years, "+str(Monthleft)+" months, and "+str(Dayleft)+" days")
    #print(yearsleft)

check_birthdate(yearOfbirth,MonthOfbirth,DayOfbirth)
