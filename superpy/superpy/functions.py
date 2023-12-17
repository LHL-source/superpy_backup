
from datetime import date
from datetime import datetime
from datetime import timedelta
import csv
import os
import argparse

from rich.table import Table
from rich import print
from rich.console import Console


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
              #print('existing_content',existing_content)

    #update the content
    if existing_content:
              #print('existing_content is trufy')
              #get the existing internalt_date
              existing_internal_date=string_to_datetime(existing_content[0]['internal_date'])
              #calculate the future date based on the existing date
              future_date=existing_internal_date+timedelta(advance_time)
              #update the internal_date value
              existing_content[0]['internal_date']=datetime_to_string(future_date)
              #print('datetime_to_string(future_date)',datetime_to_string(future_date))
              #print('existing_content[0][''internal_date'']',existing_content[0]['internal_date'])
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
    #print('r 69 rows ', rows)#w?y good job

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
           add_product_name=None
           for row in relevant_rows:
               
               try:
                  # Try converting the date string to datetime objects
                   expiration_date_convert_date = string_to_datetime(row['expiration_date'], format='%Y-%m-%d')#w?y,object datetime
                   internal_date_value_convert_toDate = string_to_datetime(internal_date_value, format='%Y-%m-%d')#w?y object datetime

               except ValueError as e:
                   print(f"Error converting date string: {e}")
                   print(f"Problematic date string: {row['expiration_date']}") 

               #get the expiration_date in bought.csv which is earlier than the internal_date  
               #  min_exp_date_row=None  
               if expiration_date_convert_date >=internal_date_value_convert_toDate:
                     min_exp_date_row=row
                     min_exp_date_row['id']
                     
                     #add bought.csv coloms:product_name,buy_date,buy_price,expiration_date
                     # to sold.csv 
                     add_product_name=row['product_name']#w?y type:string                  
                     add_buy_date=row['buy_date']#w?y type:string
                     add_buy_price=row['buy_price']#w?y type:string
                     add_expiration_date=row['expiration_date']#w?y type:string
                     
           new_row={
                          'id': new_sold_row_id,
                          'bought_id': min_exp_date_row['id'],
                          'sell_date': internal_date_value,
                          'sell_price':sell_price,
                          'product_name':add_product_name,
                          'buy_date':add_buy_date,
                          'buy_price':add_buy_price,
                          'expiration_date':add_expiration_date
                    }        
           sold_rows.append(new_row)#w?y
           print('L257 rows ', sold_rows)#w?y good job
           #
      with open (sold_file_path,'w', newline='') as file:#w?yes wel done
                        writer=csv.DictWriter(file,fieldnames=sold_reader.fieldnames)
                        writer.writeheader()
                        writer.writerows(sold_rows)

      #after write down in sold.csv, in bought.csv delete the same id because it is sold(gone) 
      # this to prevent to sell the same product twice which is not possible
      with open (bought_file_path, 'r') as bought_file:#w?y
           bought_reader=csv.DictReader(bought_file)
           bought_rows_list=list(bought_reader)#list
           print(' L 234 type(bought_rows_list)',type(bought_rows_list))
           
           #define an empty list to store the rows we want to keep
           new_bought_rows=[]
           #iterate through each row in bought_rows_list 
           for row in bought_rows_list:
              # Check if the 'id' of the current row is not equal to the 'id' we want to remove
               if row['id'] != min_exp_date_row['id']:
               # If the condition is true, add the row to the new_bought_rows list
                  new_bought_rows.append(row)

      with open(bought_file_path, 'w', newline='') as bought_file:
                writer = csv.DictWriter(bought_file, fieldnames=bought_reader.fieldnames)
                writer.writeheader()
                writer.writerows(new_bought_rows)

      return

# make a function to make report
bought_file_path=os.path.join('data', 'bought.csv')
internal_date_file_path=os.path.join('data', 'internal_date.csv')
def  report_now(now):#w? y type:string
     #print("into function.py, function report_now(now)")#w?y
     #print('into functions.py_report_now():')
     #print( 'L 270 now:',now)#w?y
     #print('L271 type(now):',type(now))#w?y

     

     #add rows in the table:but first open sold.csv and read the row(s)
     with open(internal_date_file_path,'r',newline='')as file:
              reader=csv.DictReader(file)
              existing_content=list(reader)#w?y
              internal_date= existing_content[0]['internal_date']#w?y type:string
              #print('L283 internal_date',internal_date)#w?y
              #print('L284 type(internal_date)',type(internal_date))#w?y type string

     with open (bought_file_path, 'r') as bought_file:#w?y
           bought_reader=csv.DictReader(bought_file)
           bought_rows=list(bought_reader)#w?y type:list of dictionary
           
     #print('L 290 bought_rows',bought_rows)#w? y
     #print('L 291 type(bought_rows)',type(bought_rows))#w?y type class:list

     for row in bought_rows:
          #print(f"Processing row:{row}")#w?y
          #define a new list (of dictionary) ALL products with expiration_date >= internal_date
          all_product_expDate_QualOrLargerThan_internalDate=[]
          #convert expiration_date to a datetime also for internaldate
          exp_date_in_datetime=string_to_datetime(row['expiration_date'])#type datetime object
          #print('L 299 exp_date_in_datetime',exp_date_in_datetime)#w?y
          #print('L 300 type(exp_date_in_datetime)',type(exp_date_in_datetime))#w?y
          
          internalDate_in_datetime=string_to_datetime(internal_date)
          #print('internalDate_in_datetime',internalDate_in_datetime)#w?y
          #print('L304 type(internalDate_in_datetime)',type(internalDate_in_datetime))#w?y type datetime object
          
          #select only the items which expiration_date >= internal_date
          if  exp_date_in_datetime>= internalDate_in_datetime:#w?y
               all_product_expDate_QualOrLargerThan_internalDate.append(row)#w?y
     
          for row in all_product_expDate_QualOrLargerThan_internalDate:#w?y
                  
                  #print('L300 row',row)#w?y
                  #print('row',type(row))#w?y type:class 'dict'
          
          #For each product (e.g., apple, banana, orange):
          #Create a sublist containing only rows for that product here is product_name='appel'
                   appel_expDate_QualOrLargerThan_internalDate=[]#type class list
                   print('appel_expDate_QualOrLargerThan_internalDate',type(appel_expDate_QualOrLargerThan_internalDate))
          if  all_product_expDate_QualOrLargerThan_internalDate['product_name']=='appel':
                  appel_expDate_QualOrLargerThan_internalDate.append(row)
          
          #controle the  appel_expDate_QualOrLargerThan_internalDate 
          #for row in appel_expDate_QualOrLargerThan_internalDate :
               #print('L 322 row',row)
               #print('L 323type(row)',type(row))
          
     return    
#hoi 17-12-2023



           