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
  "Come on enter either \"y\" or \"n\"",
  "Come on you can do it. y/n",
  "Please just enter \"y\" or \"n\""

  ]
  
#Made two user-defined functions which would check that the correct data-type or response was entered.
def numinputchcker(usinput):
  while True:
    if usinput.isdigit(): #If/else conditionals
      break
    else:
      usinput = input(str(random.choice(answers) + " ")) #Choice() function from Random module used.
  return int(usinput)
  
def ynchk(ynn):
  while True:
    if ynn == "y" or ynn == "n":
      break
    else:
      ynn = input(str(random.choice(answers2) + " ")) #Choice() function again.
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
  elif wagecheck == "n":
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
  if extraitem == "y": #if/elif condtional chain. 
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
  print("Overspent by - " + "£{:.2f}").format(abs(difference)) #In built abs() function used to get rid of negative.
  
"""
This program is a simmple weekly budgeting program which requires the user to add all of their 
individual expenses, with prompting from some default expenses and room to add more. The program 
will then add up the expenses and deduct them from the wage the user has inputted to decided
whether the user has overspent or not. 

I first imported two in-built modules, time and random.  Random was to be used to keep the program 
feeling fun whenever the user entered an incorrect format response, so after this I created some
lists of responses to give the user whenever they did this.

Then as per the task, I created two user-defined functions to check the format of the user responses
as this would be recurrent throughout the program.  In the first I used isdigit(), to check the user
input was an integer, in a while loop which would stay in a loop unti the user entered a whole 
number.  In the second, I used the logical operator 'or' to check if the user enter 'y' or 'n',
similary in a while loop.

Then the main series of loops begins.  At first user input is taken to see how much the user earnt
that week.  I used my user-defined number checking function to check the format of the response.
This number was then assigned to a variable. The user was then asked to confirm the ammount, 
with my user-defined y/n checker function checking the format of the response.

Then the main thrust of the program begins. I created a dictionary with all the standard expenses
I could think of in it, with the values set to zero as default.  These were then run through with
a for loop asking the user for the amount spent on each.  A nested while loop then used my number
checking function to check the format of each response.  Each value added by the user-input was
then added to the dictionary of expenses. 

After this, a further while loop then check if the user has anymore expenses to add.  With my user
defined functions once again checking the formats of the input. In this while loop there was a 
nested conditional with a nested while loop within that if the input was 'y'.

Finally, when the user inputs 'n' for no more to add, the program breaks out of the while loop and
goes into the final stage of preparing and presenting the results.  I had used the format() built in 
function to present the results in the form '£0.00', simply for aesthetic purposes.  I also used the
sleep() function in the time module to create some fun suspense, by making the user wait 3 seconds
for the final result.  For the final presentation, I used a for loop to print() the key-value pairs
in the main dictionary.  As it was doing this, I used the in-built max() function on the dictionary
to see which was the largest value.  I used a if/else chain with non-equivalence comparison operator 
within the for loop to check each expense and change the presentation for the highest expense. I
also used the in built abs() function to convert the result if there was an overspend to a positive
number, again for aesthetic purposes.
"""


  

  

 

