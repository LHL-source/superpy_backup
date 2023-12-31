# Imports
import argparse
import csv
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from functions import *

from functions import date_type

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
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
    inventory_group.add_argument("--now", nargs='?', const=None, help="Report inventory for today")

    #hieronder definieer argument groups voor (report) revenue w? yes 
    revenue_group=revenue_parser.add_argument_group("Revenue options")
    #voeg de argumenten toe aan revenue_group
    revenue_group.add_argument("--yesterday", type=str, help="Report revenue for yesterday")
    revenue_group.add_argument("--today",type=str, help="Report revenue for today")
    revenue_group.add_argument("--date",type=str, help="Report revenue for specific date(e.g.'2019-12')")

    #definieer argument-groups voor (report) profit works?yes
    profit_group=profit_parser.add_argument_group("Profit options")
    #voeg de argumenten toe aan profit_group
    profit_group.add_argument("--today", type=str, help="Profit of today")

    args = parser.parse_args()
    
    
    mainPy_get_internal_date=get_internal_date()#w?y
    #print('r17 mainPy_get_internal_date()',mainPy_get_internal_date)#w?y
    #print('r18 type(mainPy_get_internal_date)',type(mainPy_get_internal_date))#w?y

    if args.advance_time :
         mainPy_args_advance_time=advance_time(args.advance_time)
         #print(' mainPy_args_advance_time', mainPy_args_advance_time)
         #print('type(mainPy_args_advance_time)',type(mainPy_args_advance_time))
    else:
         pass
         
    if args.command =='buy':#w?yes
        pass
        #print('go to def add_buy_product()')
        add_buy_product(args.product_name,args.price,args.expiration_date)#w?y
        #print('oke (of buy)')

           #add_buy_product(args.product_name,args.price)#uitgehaald:,args.expiration_date
    elif args.command =='sell':#works? yes
           
           add_sold_product(args.product_name,args.price)
    elif args.command =='report':#works? yes
           print('into report')

           if args.report_command=='inventory':#w?
              print('into main.py/report_inventory')#w?y
              report_now(args.now)
              if args.yesterday:#w?y
                    print('go to def report_yesterday()')
              elif args.now:#works?y
                    #print('main.py:go to def report_now()')
                    report_now(args.now)

                

           elif args.report_command=='revenue':#w?y
               print('into report_revenue')
               if args.yesterday:#w?y
                   print('go to def revenu_yesterday()')
               elif args.date:#w?y
                   print('go to def revenu_date()')   

           elif args.report_command=='profit':#w?y
               print('into report_profit')#w?y
               print('go to def profit_today()')#w?y
            

if __name__ == "__main__":
    main()
