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
┏━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Product Name ┃ Count ┃ Buy Price ┃ Expiration Date ┃
┡━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│    appel     │   2   │    0.4    │   2023-12-06    │
│    appel     │   1   │    0.4    │   2023-12-07    │
│    banana    │   1   │    0.5    │   2023-12-06    │
│    banana    │   1   │    0.5    │   2023-12-07    │
└──────────────┴───────┴───────────┴─────────────────┘


