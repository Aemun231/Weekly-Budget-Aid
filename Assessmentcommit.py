#This is a householed weekly budgeting program asking for user input to calculate spending.

#Imported built-in modules.
import random
import time

#Created lists with different wrong-format replies that would be used by the checking functions.
answers = [
  "Can you please enter a whole number!",
  "Try again, enter a number!",
  "Stop being daft and enter a whole number!",
  "Sigh. Enter a whole number!"
  ]

answers2 = [
  "Come on enter either \"y\" or \"n\""
  "Come on you can do it. y/n"
  "Please just enter \"y\" or \"n\""

  ]
  
#Made two user-defined functions which would check that the correct data-type or response was entered.
def numinputchcker(usinput):
  while True:
    if usinput.isdigit():
      break
    else:
      usinput = input(str(random.choice(answers) + " ")) #Choice() function from Random module used.
  return int(usinput)
  
def ynchk(ynn):
  while True:
    if ynn == "y" or "n":
      break
    else:
      ynn = input(str(random.choice(answers2))) #Choice() function again.
  return ynn

#Began inital loop to ask for wage.    
while True:
  
  wage = input("How much did you earn this week? ")
  wage = numinputchcker(wage) #User-defined checker function used.
  break

#Another loop to check wage input was ok, utilising yes no checker function (ynchk()).  
while True:
  
  print("Ok, so you earned £" + "{:.2f}".format(wage)) #In-built format() function used to add decimals for presentation.
  wagecheck = input("Is this correct, y/n? ")
  wagecheck = ynchk(wagecheck) #Yes no checker function.
  if wagecheck == "y":
    print("Ok!")
    break
  if wagecheck == "n":
    print("Well, I'd restart this program then if I were you!")
    exit()

#Create dictionary of default items to be checked in budget with values set to zero.
accountsdict = {"Rent": 0, "Bills": 0, "Food Costs": 0, "Travel": 0, "Toiletries": 0}

#Used a for loop to cycle through keys in above items dictionary.
for item in accountsdict:
  #With a nested while loop, which checks value entered is correct format.
  while True:
    cost = input("How much are you going to spend on " + str(item) + "? ") 
    accountsdict[item] = numinputchcker(cost) #User-defined checking function
    break

#Another while loop after dictionary items to see if there are extra costs.   
while True:
  extraitem = input("Is there another cost not mentioned, y/n?")
  extraitem = ynchk(extraitem) # Yes no checker function.
  #A nested conditional to find out what the cost is.
  if extraitem == "y":
    newkey = input("What is the name of this cost? ")
    
    #Then a nested while loop to check input.
    while True:
      newvalue = input("And how much will you spend on this? ")
      newvalue = numinputchcker(newvalue) #User defined checker function.
      break
      
    accountsdict[newkey] = float(newvalue) #New item is added to expense dictionary.
    
  elif extraitem == "n":
    break

#Then results are presented.  With empty lines added for spacing.  
print("")
print("\033[1mThis is the itemised lists of your weekly budget:\033[0m") #Bold format.
print("")

#A for loop to loop through the dictionary and present each key-value pair to the user.
for item, cost in accountsdict.items():
  if cost != max(accountsdict.values()): #In-built max() function used to separate biggest expense/s
    print(str(item) + " - " + "£{:.2f}").format(cost) #In-built format() function to add zeros.
  else:
   print(str(item) + " - " + "£{:.2f}" + "  (*highest)").format(cost) 
    
print("_____________________")
#Sleep() function used from time module to add suspense to final budget result of final balance.
print("...And wait for it... you have...")
time.sleep(3)

#Final balance calculated. 
totalcosts = sum(accountsdict.values())
difference = wage - totalcosts
if wage - totalcosts >= 0:
  print("Spare Cash - " + "£{:.2f}").format(difference) #In-built format() function used to add decimal places.
else:
  print("Overspent by - " + "£{:.2f}").format(difference)
  



  

  

 

