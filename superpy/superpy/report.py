
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
fruits=['apple','banana','orange','apple','banana','apple']
fruit_counts={}

for fruit in fruits:
    #print('fruit',fruit)#w?y
    if fruit in fruit_counts:
        fruit_counts[fruit]+=1
    else:
        fruit_counts[fruit]=1

for fruit in fruit_counts:
    print('fruit_counts',fruit_counts)
