
#from rich.console import Console
from rich.table import Table
from rich import print
from rich.console import Console

#print("[italic red]Hello[/italic red] World!", locals())
table=Table(title='Star Wars Movies')#w?y

table.add_column("Release", justify="right",style="cyan", no_wrap=True)#no_wrap=True
table.add_column("Title", style="magenta")
table.add_column("Box Office",justify="right",style="green")

table.add_row("Dec 20 2019", "Star Wars: The Rise of Skywalker","$952,110,690")
table.add_row("May 25 2018","Solo:A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# Create a Console object
console = Console()
# Set soft_wrap property of the Console object
console.soft_wrap = True
#print(table, )#soft_wrap=True

#count now may time apple appears:#w?y 11 dec 2023
#fruits=['apple','banana','orange','apple','banana','apple']
#fruit_counts={}

#for fruit in fruits:
    #print('fruit',fruit)#w?y
    #if fruit in fruit_counts:
        #fruit_counts[fruit]+=1
    #else:
        #fruit_counts[fruit]=1

#for fruit in fruit_counts:
    #print('fruit_counts',fruit_counts)

#here under the concept of count in a DYNAMIC (not static) way for report/invetory/--now
#goal is to make a count, to count the double roll with critera:the same is :name and and color 
#and than put it in Rich 
#the data in a LIST of dictionary:
fruits = [
    {'name': 'apple', 'color': 'red', 'type': 'fruit'},
    {'name': 'banana', 'color': 'yellow', 'type': 'fruit'},
    {'name': 'orange', 'color': 'orange', 'type': 'fruit'},
    {'name': 'carrot', 'color': 'orange', 'type': 'vegetable'},
    {'name': 'grape', 'color': 'purple', 'type': 'fruit'},
    {'name': 'apple', 'color': 'green', 'type': 'fruit'},
    {'name': 'banana', 'color': 'yellow', 'type': 'fruit'},
    {'name': 'carrot', 'color': 'orange', 'type': 'vegetable'},
]

#initialize an empty dictionary called "fruit_counts" to store the dynamic counts.
fruit_counts={}
#we start a loop to iterate through each dictionary in the 'fruits' list
for fruit in fruits:
    #for each fruit dictionary, we extract the relevant criteria(name and color) and 
    #create a tuple called 'criteria'.This tuple will be used as a key in our 'fruit_counts'
    criteria=(fruit['name'],fruit['color'])

    #we check if the 'criteria' tuple is already in the 'ruit_counts'dictionary:
    #if NOT, we add it to the dictionary with an initial count of 1
    #if it is already in the dicionary, we increment the count by 1
    if criteria not in fruit_counts:
        fruit_counts[criteria]=1
    else:
        fruit_counts[criteria] +=1
    #after processing all fruits, we iterate through the items(key-value pairs) in the 
    #'fruit_counts' dictionary
    # we print a message for each criteria tuple, indicating the number of occurences
for criteria, count in fruit_counts.items():
    print(f"For{criteria}:{count} occurrences")
    
    #After processing all fruits, we iterate the items(key-value pairs)in the 'fruit_counts'
    #dictionary.
    #we print a message for each criteria tuple, indicating the number of occurences
    # here is an example output:
    #For ('apple', 'red'): 1 occurrences.
    #For ('banana', 'yellow'): 2 occurrences.
    #For ('orange', 'orange'): 1 occurrences.
    #For ('carrot', 'orange'): 2 occurrences.
    #For ('grape', 'purple'): 1 occurrences.
    #For ('apple', 'green'): 1 occurrences.

#this code dynamically counts the occurrences of fruitsbased on their name and color,
#and you can adapt it for your scenario with products and attributes
        
#now the dynamic 'fruit_counts' how to use in Rich?
#from rich.console import Console
#from rich.table import Table
#assume fruit_counts is the dynamically generated data
#fruit_counts={
    #('apple', 'red'): 1,
    #('banana', 'yellow'): 2,
    #('orange', 'orange'): 1,
    #('carrot', 'orange'): 2,
    #('grape', 'purple'): 1,
    #('apple', 'green'): 1,
#}

#console=Console()
#create a Rich Table
#table=Table(title="Fruit Counts")
#table.add_column('Fruit Name', justify="center")
#table.add_column("Color",justify="center")
#table.add_column("Occurences",justify="center")

#polulate the table with dynamic data
#for (fruit_name, color), occurences in fruit_counts.items():#w?y
    #table.add_row(fruit_name, color, str(occurences))#w?y

#print the table
#console.print(table)#w?y
    
#iterate through a list of dictionary:
fruit_counts={'apple':3,'banana':2,'orange':5}
for soepkip, muizendrol in fruit_counts.items():
    print ('L119 ',soepkip)

#of course it is the same logic as:

fruit=['appel','banana','mango']
for eachFruitOfIteration in fruit:
    print('print for variabel eachFruitOfIteration  the value of each iteration:',eachFruitOfIteration)