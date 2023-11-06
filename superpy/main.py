# Imports
import argparse
import csv
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from functions import *

from functions import date_type
#import datetime

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

#hieronder :sub-parse:report #w?????
parser=argparse.ArgumentParser(description="Superpy Supermarket Inventory")
#voeg argument toe waar aan?(er is GEEN command en sub-command (b.v. report_command))#works?
parser.add_argument("--advance_time",type=int, help="for advanced time 2 days ,please type:2")
#wat de gebruiker als sumcommand heeft ingevulde keuze:buy, sell , report komt als value in attribute command
subparser=parser.add_subparsers(dest="command")
#hieronder maak een sub-parser voor "buy","sell" and "report"
buy_parser=subparser.add_parser("buy")
sell_parser=subparser.add_parser("sell")
report_parser=subparser.add_parser("report")

#Voor "buy" en "sell" subcommands, definieer specifieke argumenten voor elk
buy_parser.add_argument("--product_name", type=str, help="give the name of the product choice:apple, banana, manderin")
buy_parser.add_argument("--price", type=float, help="give the price of the product for example: 0.5")
buy_parser.add_argument("--expiration_date", type=date_type, help="Enter the expiredate in 'year-month-day'format")

sell_parser.add_argument("--product_name", type=str, help="give the name of the product choice:apple, banana, manderin")
sell_parser.add_argument("--price", type=float, help="give the price of the product for example: 0.7")


#hieronder voor "report" DEFINIEER the subcommands voor "inventory","revenue" en "profit"
report_subparsers=report_parser.add_subparsers(dest="report_command") 
inventory_parser = report_subparsers.add_parser("inventory")
revenue_parser = report_subparsers.add_parser("revenue")
profit_parser=report_subparsers.add_parser("profit") 

#hieronder DEFINIEER argument groups voor "report"
report_group=report_parser.add_argument_group("Report options")

#hieronder DEFINEER argument groups for inventory w?yes 
inventory_group=inventory_parser.add_argument_group("Inventory options")
#voeg de argumenten toe aan inventory_group
inventory_group.add_argument("--yesterday",type=str, help="Report inventory for yesterday")
inventory_group.add_argument("--now", type=str, help="Report inventory for today")

#hieronder definieer argument groups voor (report) revenue w? yes 
revenue_group=revenue_parser.add_argument_group("Revenue options")
#voeg de argumenten toe aan revenue_group
revenue_group.add_argument("--yesterday", type=str, help="Report revenue for yesterday")
revenue_group.add_argument("--today",type=str, help="Report revenue for today")
revenue_group.add_argument("--date",type=str, help="Report revenue for specific date(e.g.'2019-12')")

#definieer argument-groups voor (report) profit w? not yet
profit_group=profit_parser.add_argument_group("Profit options")
#voeg de argumenten toe aan profit_group
profit_group.add_argument("--today", type=str, help="Profit of today")

args = parser.parse_args() 
#test input:python main.py --advance_time 6 #w?y
#test input:python main.py buy --product_name apple --price 0.5 --expiration_date 2023-4-2  #w?yes
#test input:python main.py sell --product_name peer --price 0.1#  #w?y

#test input:python main.py report inventory --now now #w?yes
#test input:python main.py report inventory --yesterday yesterday  #w?y

#test input:python main.py report revenue --yesterday yesterday  #w?
#test input:python main.py report revenue --today today  #w?
#test input:python main.py report revenue --date 2020-2-5  #w?
#test input:python main.py report profit --today today  #w?

#test input:python main.py  --product_name peer --price 0.1#  #w?y

print("args.command",args.command)#w?
#print("args.report_command:",args.report_command)#w?y let op geen report_command PRINT by sell and buy want daar is geen report_command
#print("args.product_name",args.product_name)#w?
#print("args.price",args.price)#w?
#print("args.expiration_date",args.expiration_date)#w?
#print("args.advance_time:",args.advance_time )#w?y

if args.advance_time:#w?y
       print('go to def advance_time() and print args.advance_time: ',args.advance_time)#w?y
       advance_time(args.advance_time)
elif args.command =='buy':#w?yes
       print('go to def add_buy_product()')
       add_buy_product(args.product_name,args.price,args.expiration_date)#w?y
       print('oke (of buy)')


       #add_buy_product(args.product_name,args.price)#uitgehaald:,args.expiration_date
elif args.command =='sell':#works? yes
       #print('go to def add_sold_product()')
       #print('command',args.command)#w?yes
       #print("into main.py/sell")#w?yes
       #print("args.product_name",args.product_name)#w?yes
       #print("arg.price",args.price)#w?yes
       add_sold_product(args.product_name,args.price)
elif args.command =='report':#works? yes
       print('into report')

       if args.report_command=='inventory':#w?
          print('into report_inventory')
          if args.yesterday:#w?y
                print('go to def report_yesterday()')
          elif args.now:#works?y
                print('go to def report_now()')
                

       elif args.report_command=='revenue':#w?y
           print('into report_revenue')
           if args.yesterday:#w?y
               print('go to def revenu_yesterday()')
           elif args.date:#w?y
               print('go to def revenu_date()')   

       elif args.report_command=='profit':#w?y
               print('into report_profit')#w?y
               print('go to def profit_today()')#w?y
        


def main():
    pass


if __name__ == "__main__":
    main()
