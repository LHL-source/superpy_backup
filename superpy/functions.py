
from datetime import date
from datetime import datetime
from datetime import timedelta
import csv
import os


import argparse

def date_type(date_string,):#w?y
    try:
        date_object=datetime.strptime(date_string,'%Y-%m-%d')
        formated_date_object=date_object.strftime('%Y-%m-%d')
        return formated_date_object
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Use 'year-month-day' (e.g.,'2023-10-15).")

#hieronder test result of date_type w?? yes good job
#result_date_type=date_type("2023-01-02")
#print("In function.py:result_date_type",result_date_type )

#current_day=date.today()#w?y
#print(current_day)#w?y

#
def advance_time(advance_time):#w?yes
    print('into function advance_time,advance_time: ',advance_time)#w?y
    current_day=date.today()
    future_date=current_day + timedelta(advance_time)
    
    print('future_date', future_date)

    return  future_date #w?y

#advance_time(2)#w?y
#test input:python main.py buy --product_name apple --price 0.5 --expiration_date 2023-4-2  #w?yes well done
#define file_path
file_path=os.path.join('data','bought.csv')
def add_buy_product(product_name,buy_price,expiration_date):
  with open (file_path,'r') as file:
    reader=csv.DictReader(file)
    rows=list(reader)
    #print('r36 rows',rows)#w?y

    maximum=0
    for eachRow in rows:
        #print(' r 48 eachRows',eachRow)#w?y 
        print("eachRow['id']",eachRow['id'])#w?yes
        #de waarde/value van id is een string conver naar een integer 
        id_int=int(eachRow['id'])
        #print('id_int',id_int)#wy
        #print('type(id_int)',type(id_int))#w?y
        if id_int > maximum:
            maximum =id_int
            #print('r48 maximum', maximum)# w? yes good job
    new_row_id=maximum + 1

    new_row ={
    'id':new_row_id,
    'product_name':product_name,
    'buy_date':date.today(),
    'buy_price':buy_price,
    'expiration_date':expiration_date,
    
    }
   
    rows.append(new_row)#w?y
    print('r 69 rows ', rows)#w?y good job

    # add to the file: bought.csv:test_file_with_Id.csv

    
  with open (file_path,'w', newline='') as file:#w?yes wel done
      writer=csv.DictWriter(file,fieldnames=reader.fieldnames)
      writer.writeheader()
      writer.writerows(rows)
  return

#print_add_buy_product=add_buy_product('apple', '0.5', '2023-4-2')#works?yes
#print('print_add_buy_product',print_add_buy_product)

#here under the function for "add_sold_product"#w?
sold_file_path=os.path.join('data', 'sold.csv')
bought_file_path=os.path.join('data', 'bought.csv')
def add_sold_product(product_name,sell_price):
      print("function:add_sold_product/product_name:",product_name)#w?y
      print('function:add_sold_product/sell_price:',sell_price)#w?y      
      #open sold.csv
      with open (sold_file_path,'r') as sold_file:#w?y
           sold_reader= csv.DictReader(sold_file)#w?y
           sold_rows=list(sold_reader)#w?y
           #print('sold_rows',sold_rows)#w/y
     #open bought.csv
      #with open (file_path,'r')as bought_file:#w?y
           #bought_reader=csv.DictReader(bought_file)#w?y
           #bought_rows=list(bought_reader)#w?y
           #print('bought_rows',bought_rows)#w/y
        
           # made for sold.csv id which will cumulate automatically
           maximum = 0
           for each_sold_Row in sold_rows:#w?yes
               #print('r104 each_sold_Row',each_sold_Row)#w?
               #print only here under the VALUE of sold_Row_ (not the key)
               #print(" r 106 value:",each_sold_Row['id'])
               #print here under only the KEY with name: id of each_sold_Row
               #print(" r 107 only the name of the key with name id:",'id')
               #convert sold id to integer
               sold_id_convert_to_integer=int(each_sold_Row['id'])
               #print('sold_id_convert_to_integer',sold_id_convert_to_integer)#w?y
               #print('sold_id_convert_to_integer',type(sold_id_convert_to_integer))#w?y
               if sold_id_convert_to_integer >  maximum:
                  maximum= sold_id_convert_to_integer#w?y
                  #print('maximum',maximum)#w?y
                  new_sold_row_id= maximum + 1#w?y
                  #('new_sold_row_id',new_sold_row_id)#w?y
      
      #stap 1 :open the bought.csv file #w? yes 
      with open (bought_file_path, 'r') as bought_file:#w?y
           bought_reader=csv.DictReader(bought_file)
           bought_rows=list(bought_reader)
           #print('bought_rows',bought_rows)#w?y

           #stap 2:put the input :product_name into a variabel
           product_name_1=product_name
           #print('r 126 product_name_1:',product_name_1)#w?yes
           expiration_date_min=datetime.max
           print('r 141  expiration_date_min',expiration_date_min)#w?y
           #stap 3:go through the hole bought.csv and make a selection of items only with product_name=appel
           appel_list=[]
           for eachItem_appel_list in bought_rows:
               if eachItem_appel_list ['product_name']==product_name_1:#w?t
                   #print('r 132 product_name_1==product_name TRUE ')#wYes
                   appel_list.append(eachItem_appel_list)#w?y
                   #print('r134 appel_list_add_item',appel_list)#w?y

                   #stap 4: loop met de for/loop door the appel_list en haalt op de laatste:expiratation_date
                   #date_str="2010-12-31"
                   date_format="%Y-%m-%d"
                   
                   #expiration_date_min=datetime.max
                   #print('r 141  expiration_date_min',expiration_date_min)#w?y
                   #expiration_date_min=datetime.strptime( date_str,date_format)
                   #print('r 141 expiration_date_min:',expiration_date_min)#w? almost because it also include hours
                   #print('r142 expiration_date_min:',type(expiration_date_min))#y
                   #formatted_time=expiration_date_min.strftime("%Y-%m-%d")
                   #print('r 144 formatted_time:',formatted_time)
                   #print('r 145 formatted_time ',type(formatted_time))

                   for eachItem_appel_list_1 in appel_list:
                       print("r150 eachItem_appel_list_1['expiration_date'] ",eachItem_appel_list_1['expiration_date'])#w?y
                       #print("r149 eachItem_appel_list_1['expiration_date']",type(eachItem_appel_list_1['expiration_date']) ) #let op type is string so convert into type datetime                  
                       eachItem_appel_list_1_convert=datetime.strptime(eachItem_appel_list_1['expiration_date'],date_format)
                       print('r 153 (waarde) eachItem_appel_list_1_convert:', eachItem_appel_list_1_convert)#w?y
                       print('r 154  type(eachItem_appel_list_1_convert):', type(eachItem_appel_list_1_convert))#w?y
                       #if eachItem_appel_list_1_convert < expiration_date_min:
                            #expiration_date_min=eachItem_appel_list_1_convert 
                            
                       #print('155 expiration_date_min' ,expiration_date_min)
                       #print the expiration_date of the FIRST row of the list

                       #print('expiration_date_min', expiration_date_min)
                       #if eachItem_appel_list_1 ['expiration_date']

           #



           return