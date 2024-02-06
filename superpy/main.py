# Imports
import argparse
import csv
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from functions import *

from functions import date_type

__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
#hieronder :sub-parse:report 
    parser=argparse.ArgumentParser(description="Superpy Supermarket Inventory")
    #voeg argument toe waar aan?(er is GEEN command en sub-command (b.v. report_command))
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

    #hieronder DEFINEER argument groups for inventory 
    inventory_group=inventory_parser.add_argument_group("Inventory options")
    #voeg de argumenten toe aan inventory_group
    inventory_group.add_argument("--yesterday", nargs='?',const="yesterday", help="Report inventory for yesterday")
    inventory_group.add_argument("--now", nargs='?', const="now", help="Report inventory for today")

    #hieronder definieer argument groups voor (report) revenue 
    revenue_group=revenue_parser.add_argument_group("Revenue options")
    #voeg de argumenten toe aan revenue_group
    revenue_group.add_argument("--yesterday", nargs='?',const="yesterday", help="Report revenue for yesterday")
    revenue_group.add_argument("--today",nargs='?',const="today", help="Report revenue for today")
    revenue_group.add_argument("--date", nargs='?', const="2023-12", help="Report revenue for a specific date (e.g., '2023-12')")
    revenue_group.add_argument("--file_type_excel", nargs='?', const="xlsx", help="Specify the file type for the report (default is CSV)")
    
    #definieer argument-groups voor (report) profit 
    profit_group=profit_parser.add_argument_group("Profit options")
    #voeg de argumenten toe aan profit_group
    profit_group.add_argument("--today",nargs='?',const="today", help="Profit of today")

    args = parser.parse_args()
    
    
    mainPy_get_internal_date=get_internal_date()
    

    if args.advance_time :
         mainPy_args_advance_time=advance_time(args.advance_time)
         
    else:
         pass
         
    if args.command =='buy':
        pass
        add_buy_product(args.product_name,args.price,args.expiration_date)
           
    elif args.command =='sell':
           add_sold_product(args.product_name,args.price)
    elif args.command =='report':

           if args.report_command=='inventory':
             
              if args.yesterday:
                    print('go to def report_yesterday()')
                    report_yesterday(args.yesterday)
                    
              elif args.now:
                    report_now(args.now)                

           elif args.report_command=='revenue':
               if args.today:
                    revenue_today(args.today)

               elif args.yesterday:
                   revenu_yesterday(args.yesterday)
               elif args.date:
                   revenu_date(args.date, args.file_type_excel)
                   
           elif args.report_command=='profit':
               report_profit_today(args.today)

if __name__ == "__main__":
    main()
#6 feb 2024 12.46 u einde