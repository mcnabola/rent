from datetime import datetime
from datetime import timedelta



dateFormat = "%d/%m/%Y"

class period(object):
    
    def __init__(self, month, year):
        ##this is all the information I am given to create a period
        self.month = month
        self.year = year

        #ternary conditional, I need the month value to be zero-padded. (7) -> (07)
        self.monthFormatted = str(self.month) if (len(str(self.month)) > 1) else "0"+str(self.month)

        #these could be in getters and setters
        #the period date is always the 28th of the month
        self.dateFormatted = "28/"+self.monthFormatted+"/"+str(self.year)
        self.date = datetime.strptime(self.dateFormatted,dateFormat)
        ## The start date and end date of a period are 10 days either side of the 'date'
        self.dateEnd = self.date + timedelta(days=10)
        self.dateStart = self.date - timedelta(days=10)
        #have to also store the balances for each period



def messageCleanUp(unedited):
    edited = unedited.replace("365","")
    edited = edited.replace("Online", "")
    return edited


class data(object):

    def __init__(self, date, message,debit,credit,balance):
        self.date = datetime.strptime(date,dateFormat)
        self.message = message ##messageCleanUp(self.message)
        self.debit = debit
        self.credit = credit
        self.balance = balance




class user(object):
    aliases = []

    def __init__(self, name):
        self.name = name

    def addAlias(self,alias):
        aliases.append(alias)
        #will have to be careful with aliases and how you search and add them. As you dont want people with short names and long names to show up for both (AM) -> (PAM)


#HARDCODING FOR NOW
a = [data("26/07/2019","ted","2600","","188"), data("26/08/2019","tedis","2600","","188"), data("25/08/2019","Jam","2600","","188"), data("29/09/2019","Roly","2600","","188"), data("29/09/2019","Poly","2600","","188")]
#assumption that this data will always be in order
# creating list of messages - in future read in from csv


periods = []

for i in a:
    month = i.date.month
    year = i.date.year
    if len(periods) > 0:
        found = False
        for x in periods:
            if (x.month == month and x.year == year):
                #print("Period already created: " + str(x.month) + ":"+str(month) + " : " + str(x.year) +":"+ str(year))
                found = True
        if(found==False):
            periods.append(period(month, year))
        found = False
    else:
        periods.append(period(month, year))


print(":::"+str(len(periods))+"::")


####Creating the users, keep this seperate to periods atm if its easier to get working on its own
userAccounts = []

for i in a:
    details = i.message
    if len(userAccounts) > 0:
        found = False
        for x in userAccounts:
            if (x.name in details): # this will never ever be true - will have to be a contains()
                print(x.name +":"+ details)
                found = True
        if(found==False):
            print("New user to be created; Message:: "+details)
            name = input("Enter the main name for this user: ")
            userAccounts.append(user(name))
            aliasAddittions = input("Do you want to add an alias for this user: (y) (n)")
            monthFormatted = True if aliasAddittions=="y" else False
            
        found = False
    else:
        # Have to print out the message , ask them for the main name of the user , add aliases , second name , initials , store and do all searching in lowercase
        print("New user to be created; Message:: "+details)
        name = input("Enter the main name for this user: ")
        userAccounts.append(user(name))
        #this same procedure will also be in use higher up when you also have to create a new user there
    
    





#testing the period object
#a = period(7,2019)
#print(str(a.month) + " : " + str(a.year))
#print(  (a.dateStart).strftime(dateFormat) + " : "+ (a.date).strftime(dateFormat) +" : "+ (a.dateEnd).strftime(dateFormat) )



        
        
        
        
        
