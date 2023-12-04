
from datetime import date
from datetime import datetime
from datetime import timedelta
import csv
import os
import argparse

def string_to_datetime(date_string, format='%Y-%m-%d'):#w?y
     

     """
     Convert a string to a datetime object.
     Parameters:
     -date_string(str):The input date string.
     -format(str):The format of the date string(default is '%Y-%m-%d')
     Returns:
     -datetime objects:The converted datetime object.
     """
     return datetime.strptime(date_string, format)

def datetime_to_string(date_object,format='%Y-%m-%d'):#w?y
     """
     Convert a datetime object to a string
     Parameters:
     -date_object (datetime):The input datetime object.
     -format(str):The format of the output date string(default is '%Y-%m-%d')
     Return:
     -str: The formattewd date string.
     """
     return date_object.strftime(format)
# make function:internal_date()
#internal_date_file_path=os.path.join('data', 'internal_date.csv')
def get_internal_date ():#w?y
    internal_date_file_path=os.path.join('data', 'internal_date.csv')
    #check if the file exists
    if os.path.exists(internal_date_file_path):#w?y
         with open(internal_date_file_path,'r',) as file:
              reader=csv.DictReader(file)
              row=next(reader, None)
              if row and 'internal_date' in row:
                    internal_date =string_to_datetime(row['internal_date'])
                    return internal_date
              
              else:            
                   with open (internal_date_file_path,'w',newline='') as file:  
                        writer=csv.DictWriter(file,fieldnames=['internal_date'])
                        writer.writeheader()
                        writer.writerow({'internal_date': datetime_to_string(date.today())})
              return datetime_to_string(date.today())  

func_py_get_internal_date=get_internal_date()
#print('func.py_get_internal_date',func_py_get_internal_date)
#print(type(func_py_get_internal_date))
#print("func_py_get_internal_date['internal_date']",func_py_get_internal_date['internal_date'])
#print('',type(func_py_get_internal_date['internal_date']))
      
    #internal_date=date.today()
    #return #internal_date


#function date_type convert:a string into datetime object into string (again)
def date_type(date_string,):#w?y
    try:
        date_object=datetime.strptime(date_string,'%Y-%m-%d')#object datetime
        formated_date_object=date_object.strftime('%Y-%m-%d')#convert object datetime into string
        
        return formated_date_object
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Use 'year-month-day' (e.g.,'2023-10-15).")

def advance_time(advance_time):#w?yes
    #current_day=date.today()
    #future_date=current_day + timedelta(advance_time)

    # # Update the internal date in the CSV file
    internal_date_file_path=os.path.join('data', 'internal_date.csv')
    #print('r70/funcPY internal_date_file_path:', os.path.abspath(internal_date_file_path))  # Add this line
    existing_content=[]
    #Read the existing content
    if os.path.exists(internal_date_file_path):
         with open(internal_date_file_path,'r',newline='')as file:
              reader=csv.DictReader(file)
              existing_content=list(reader)
              print('existing_content',existing_content)

    #update the content
    if existing_content:
              print('existing_content is trufy')
              #get the existing internalt_date
              existing_internal_date=string_to_datetime(existing_content[0]['internal_date'])
              #calculate the future date based on the existing date
              future_date=existing_internal_date+timedelta(advance_time)
              #update the internal_date value
              existing_content[0]['internal_date']=datetime_to_string(future_date)
              print('datetime_to_string(future_date)',datetime_to_string(future_date))
              print('existing_content[0][''internal_date'']',existing_content[0]['internal_date'])
             #existing_content[0]['internal_date']=datetime_to_string(future_date)
    
    #write the updated content back to the file
    with open(internal_date_file_path,'w', newline='') as file:
         writer=csv.DictWriter(file,fieldnames=['internal_date'])
         writer.writeheader()
         writer.writerows(existing_content)
    return future_date #w?y
    #else:
         #pass
         #return None


#define file_path
file_path=os.path.join('data','bought.csv')
internal_date_file_path=os.path.join('data', 'internal_date.csv')
def add_buy_product(product_name,buy_price,expiration_date,):#w?yes
  
  with open(internal_date_file_path,'r',newline='')as file:
              reader=csv.DictReader(file)
              existing_content=list(reader)#w?y
              buy_date_value= existing_content[0]['internal_date']
              
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
    
    new_row ={
    'id':new_row_id,
    'product_name':product_name,
    'buy_date':buy_date_value,
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
internal_date_file_path=os.path.join('data', 'internal_date.csv')

def add_sold_product(product_name,sell_price):
      #print("function:add_sold_product/product_name:",product_name)#w?y
      #print('function:add_sold_product/sell_price:',sell_price)#w?y 
      
      #open internal_date.csv
      with open(internal_date_file_path,'r',newline='')as file:
              reader=csv.DictReader(file)
              existing_content=list(reader)#w?y
              internal_date_value= existing_content[0]['internal_date']#w?y string
              
      #step 1:open file sold.csv and read it
      with open (sold_file_path,'r') as sold_file:#w?y
           sold_reader= csv.DictReader(sold_file)#w?y
           sold_rows=list(sold_reader)#w?y
           
        
           #step 2: made for sold.csv value of id which will cumulate automatically
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
         
           #Find relevant_rows[] in bought.csv
           relevant_rows=[]
           for row in bought_rows:
               if row ['product_name']==product_name:#w?t
                   relevant_rows.append(row)#w?y
          
           #Print each row in relevant_rows
           for eachRow in relevant_rows:
               eachRow_expiration_date=eachRow['expiration_date'].strip()                 
                   
           #Find the row with minimum expiration date not exceeding internal_date
           min_exp_date_row=None
           for row in relevant_rows:
               
               try:
                  # Try converting the date string to datetime objects
                   expiration_date_convert_date = string_to_datetime(row['expiration_date'], format='%Y-%m-%d')#w?y,object datetime
                   internal_date_value_convert_toDate = string_to_datetime(internal_date_value, format='%Y-%m-%d')#w?y object datetime

               except ValueError as e:
                   print(f"Error converting date string: {e}")
                   print(f"Problematic date string: {row['expiration_date']}") 
                   
               #get the expiration_date in bought.csv which is earlier than the internal_date    
               if expiration_date_convert_date <=internal_date_value_convert_toDate:
                     print('L232 min_exp_date_row',min_exp_date_row)
                     print('L233 type(min_exp_date_row)',type(min_exp_date_row))#type dict
                     if min_exp_date_row is None or expiration_date_convert_date >string_to_datetime(min_exp_date_row):
                         min_exp_date_row=row
                         print('min_exp_date_row',min_exp_date_row)
               
                   #buy_id_min_expDate=None
                   #print('buy_id_min_expDate',buy_id_min_expDate)
                   #print('Before loop, buy_id_min_expDate:', buy_id_min_expDate)
                   #for eachItem_appel_list_1 in appel_list:
                       #print("r143 eachItem_appel_list_1['expiration_date']",type(eachItem_appel_list_1['expiration_date']) ) #let op type is string so convert into type datetime                  
                       #eachItem_appel_list_1_convert=string_to_datetime(eachItem_appel_list_1['expiration_date'])#was datetime.strptime(eachItem_appel_list_1['expiration_date']
                       #print('eachItem_appel_list_1_convert',eachItem_appel_list_1_convert)
                       #print('type(eachItem_appel_list_1_convert)',type(eachItem_appel_list_1_convert))
                       #if buy_id_min_expDate is None or eachItem_appel_list_1_convert < expiration_date_min:
                            #expiration_date_find=eachItem_appel_list_1_convert #was  expiration_date_min=eachItem_appel_list_1_convert
                            #print('expiration_date_find',expiration_date_find)
                            #print('type(expiration_date_find',type(expiration_date_find))
                            #step 3.5 find the buy_id and put in variabel:buy_id_min_expDate
                            #update buy_id_min_expDate in all iterations
                            #buy_id_min_expDate= eachItem_appel_list_1['id']                     
                            #print('expiration_date_min' ,expiration_date_find)#wy
                            #print('type(expiration_date_min)' ,type(expiration_date_find))
                            #print('buy_id_min_expDate:', buy_id_min_expDate)#w/y

                   #print('After loop, buy_id_min_expDate:', buy_id_min_expDate) 
                       # step 3.6 make a new row and append to sold.csv
           #new_row={
                          #'id': new_sold_row_id,
                          #'bought_id': buy_id_min_expDate,
                          #'sell_date': sell_date_value,
                          #'sell_price':sell_price
                    #}        
           #sold_rows.append(new_row)#w?y
           #print('r 176 rows ', sold_rows)#w?y good job
           #
      #with open (sold_file_path,'w', newline='') as file:#w?yes wel done
                        #writer=csv.DictWriter(file,fieldnames=sold_reader.fieldnames)
                        #writer.writeheader()
                        #writer.writerows(sold_rows)


      return