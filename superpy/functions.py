
from datetime import date
from datetime import datetime
from datetime import timedelta
import csv
import os
import argparse


#initiate 'current_day' and 'choosen_date_byUser'
current_day=datetime.today()
print('r11 current_day:',current_day)
print('r12 type(current_day)', current_day)
#choosen_date_byUser=current_day
#print('14 choosen_date_byUser:',choosen_date_byUser)
#print('r15 type(choosen_date_byUser)',choosen_date_byUser )

#check if --advance_date is provided
#if args.advance_time:
     #choosen_date_byUser=advance_time(args.advance_time)

def date_type(date_string,):#w?y
    try:
        date_object=datetime.strptime(date_string,'%Y-%m-%d')
        formated_date_object=date_object.strftime('%Y-%m-%d')
        return formated_date_object
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Use 'year-month-day' (e.g.,'2023-10-15).")


def advance_time(advance_time):#w?yes
    current_day=date.today()
    future_date=current_day + timedelta(advance_time)
    return  future_date #w?y


#advance_time(2)#w?y
#define file_path
file_path=os.path.join('data','bought.csv')
def add_buy_product(product_name,buy_date,buy_price,expiration_date,):
  print('r 41 product_name',product_name)
  print('r 42 buy_date',buy_date)# was buy_date.strftime('%Y-%m-%d')
  print('r 41 buy_price ',buy_price)
  print('r 41 expiration_date ',expiration_date)
  
  if buy_date is None:
        buy_date = datetime.today()
  
  with open (file_path,'r') as file:
    reader=csv.DictReader(file)
    rows=list(reader)
    

    maximum=0
    for eachRow in rows:#works? y
        #de waarde/value van id is een string conver naar een integer 
        id_int=int(eachRow['id'])#works?y
        if id_int > maximum:
            maximum =id_int
    new_row_id=maximum + 1
    
    current_day=date.today()# niet nodig in test fase wel in productie fase
    print('r 60 current_day:',current_day)
    print('r 61 type(current_day):',type(current_day))
    formated_currentday_object=current_day.strftime('%Y-%m-%d')
    print('r61 formated_currentday_object:',formated_currentday_object)
    print('r62 type(formated_currentday_object):',type(formated_currentday_object))
    #test_day = datetime.strptime('2020-01-01', '%Y-%m-%d')
   
    
    new_row ={
    'id':new_row_id,
    'product_name':product_name,
    'buy_date':date_type(buy_date.strftime('%Y-%m-%d')),#date_type(formated_currentday_object),oude gegeven:date_type(buy_date.strftime('%Y-%m-%d'))
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


#here under the function for "add_sold_product"#w?
sold_file_path=os.path.join('data', 'sold.csv')
bought_file_path=os.path.join('data', 'bought.csv')
def add_sold_product(product_name,sell_price):
      print("function:add_sold_product/product_name:",product_name)#w?y
      print('function:add_sold_product/sell_price:',sell_price)#w?y 
      current_day=date.today()

      #step 1:open file sold.csv and read it
      with open (sold_file_path,'r') as sold_file:#w?y
           sold_reader= csv.DictReader(sold_file)#w?y
           sold_rows=list(sold_reader)#w?y
           
        
           #step 2: made for sold.csv id which will cumulate automatically
           maximum = 0
           for each_sold_Row in sold_rows:#w?yes
               #convert sold id to integer
               sold_id_convert_to_integer=int(each_sold_Row['id'])
               if sold_id_convert_to_integer >  maximum:
                  maximum= sold_id_convert_to_integer#w?y
           new_sold_row_id= maximum + 1#w?y
              
      #stap 3 :open the bought.csv file #w? yes 
      with open (bought_file_path, 'r') as bought_file:#w?y
           bought_reader=csv.DictReader(bought_file)
           bought_rows=list(bought_reader)
           #stap 3.1:put the input :product_name into a variabel
           product_name_1=product_name
           #step:3.2 make a minimum date
           expiration_date_min=datetime.max
           #stap 3.3:go through the hole bought.csv and make a selection of items only with product_name=appel
           appel_list=[]
           for eachItem_appel_list in bought_rows:
               if eachItem_appel_list ['product_name']==product_name_1:#w?t
                   appel_list.append(eachItem_appel_list)#w?y
                   #stap 3.4: loop met de for/loop door the appel_list en haalt op de laatste:expiratation_date
                   #date_str="2010-12-31"
                   date_format="%Y-%m-%d"
                   for eachItem_appel_list_1 in appel_list:
                       #print("r143 eachItem_appel_list_1['expiration_date']",type(eachItem_appel_list_1['expiration_date']) ) #let op type is string so convert into type datetime                  
                       eachItem_appel_list_1_convert=datetime.strptime(eachItem_appel_list_1['expiration_date'],date_format)
                       if eachItem_appel_list_1_convert < expiration_date_min:
                            expiration_date_min=eachItem_appel_list_1_convert 
                            #step 3.5 find the buy_id and put in variabel:buy_id_min_expDate
                            buy_id_min_expDate= eachItem_appel_list_1['id']                     
                            print('157 expiration_date_min' ,expiration_date_min)#wy
                            print('158 buy_id_min_expDate:', buy_id_min_expDate)#w/y
                      
                       # step 3.6 make a new row and append to sold.csv
           new_row={
                          'id': new_sold_row_id,
                          'bought_id': buy_id_min_expDate,
                          'sell_date': current_day.strftime('%Y-%m-%d'),
                          'sell_price':sell_price
                    }        
           sold_rows.append(new_row)#w?y
           print('r 176 rows ', sold_rows)#w?y good job
           #
      with open (sold_file_path,'w', newline='') as file:#w?yes wel done
                        writer=csv.DictWriter(file,fieldnames=sold_reader.fieldnames)
                        writer.writeheader()
                        writer.writerows(sold_rows)


      return