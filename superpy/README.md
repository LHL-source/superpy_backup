for command: python main.py report inventory --now (with min 1 row)
test data:
bought.csv:id,product_name,buy_date,buy_price,expiration_date
1,orange,2023-11-25,0.5,2023-12-5
2,appel,2023-11-23,0.4,2023-11-8
3,appel,2023-11-25,0.4,2023-12-6
4,banana,2023-11-24,0.6,2023-12-8
5,appel,2023-11-25,0.4,2023-12-9
6,orange,2023-11-25,0.5,2023-12-10
7,orange,2023-11-25,0.5,2023-12-11
8,appel,2023-11-25,0.4,2023-12-9
9,appel,2023-11-23,0.4,2023-12-7
10,orange,2023-11-25,0.5,2023-12-10

expected result: totally 7 rows
product name  count  buy price  expiration date
appel         2      0.4        2023-12-9
appel         1      0.4        2023-12-7
orange        2      0.5        2023-12-10
orange        1      0.5        2023-12-11
banana        1      0.6        2023-12-8

for command:python main.py report inventory --now (with no row in bought.csv)
The tabel of the assignment has no row, in my application there is a empty row.
I think it is better to keep one empty row so the user conclude there is nog row 
because the first row is empty. Have ask on 29 dec 2023 in the chat and mentor Christiaan Verlaan
said it is oke.

29-12-2023
command: python main.py report inventory --yesterday
test data set:
internal_date.csv
internal_date
2023-12-06

bought.csv
id,product_name,buy_date,buy_price,expiration_date
1,appel,2023-11-25,0.4,2023-12-06
2,appel,2023-11-25,0.4,2023-12-06
3,appel,2023-11-25,0.4,2023-12-05
4,appel,2023-11-25,0.4,2023-12-07
5,banana,2023-11-25,0.5,2023-12-06
6,banana,2023-11-25,0.5,2023-12-05
7,banana,2023-11-25,0.5,2023-12-07

expected result in Rich:
product name count buy price expiration_date
appel         2     0.4      2023-12-06  
appel         1     0.4      2023-12-07 
banana        1     0.5      2023-12-06
banana        1     0.5      2023-12-07


datum 30-12-2023
definitie van revenu volgens wikipedia:https://nl.wikipedia.org/wiki/Omzet
Omzet is een bedrijfseconomische term die duidt op het totaalbedrag van verkopen van een bedrijf in een bepaalde periode. De omzet is opgebouwd uit twee componenten, prijs en afzet. De bijdrage van één bepaald product aan de omzet is: prijs × afzet. Wikipedia

dtum 30-12-2023
comman:python main.py report revenue --today
starting point:
1) today is mean the value of internal_date which is displayed in the internal_date.csv
2) in sold.csv each row has only 1 item (of product)
3)revenue is the sold_price of products in a certain periode in formule:
revenue=[(sold_price x product)of certain periode], example follow


Description: in the sold.csv are colomns. Calculate the revenu of today. 

1)Today: is the value of the variabel internale_date in internale_date.csv:
internale_date 
2023-12-07

2)revenue=sold_price x product, in certain periode

id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
1,5,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-9

xxx xxx
test scenario:
internal_date= 2023-12-07
1)sell_date = internal_date
2)sell_date < internal_date
3)sell_date > internal_date

uitwerking van:
1)sell_date = internal_date
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
1,5,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
2,4,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
3,3,2023-12-7,1.5,banan,2023-11-25,0.4,2023-12-31

2)sell_date < internal_date
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
4,2,2023-12-5,2.0,appel,2023-11-25,0.4,2023-12-31
5,1,2023-12-4,1.5,banan,2023-11-25,0.4,2023-12-31

3)sell_date > internal_date
6,6,2023-12-9,2.0,appel,2023-11-25,0.4,2023-12-31
7,7,2023-12-10,1.0,orange,2023-11-25,0.4,2023-12-31

sold.csv :
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
1,5,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
2,4,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
3,3,2023-12-7,1.5,banan,2023-11-25,0.4,2023-12-31
4,2,2023-12-5,2.0,appel,2023-11-25,0.4,2023-12-31
5,1,2023-12-4,1.5,banan,2023-11-25,0.4,2023-12-31
6,6,2023-12-9,2.0,appel,2023-11-25,0.4,2023-12-31
7,7,2023-12-10,1.0,orange,2023-11-25,0.4,2023-12-31

expected result:
id 1,2,3
id sell_price
1  2.0
2  2.0
3  1.5
totaal:5.5
xx end xxx