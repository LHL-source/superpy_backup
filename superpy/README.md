Datum:22-1-2024 (ma)
ReadMe van project Superpy:
Het doel van project Superpy
Project Superpy heeft 3 leer doelen:
1)Begrijpen wat CLI inhoud
2)Het zelfstandig ontwerpen van een logische stroom op basis van een beschrijving van wat het programma zou moeten doen
3) Leren over een nieuwe module en deze in uw applicatie implementeren
Beschrijving van Superpy project:
Er zijn drie belangrijke modules uit de standaardbibliotheek die worden gebruikt voor deze opdracht :
1)	csv: CSV File Reading and Writing
2)	argparse: Parser for command-line options, arguments, and subcommands
3)	Datetime: basic date and time types
SuperPy
Een grote supermarktketen heeft  gevraagd  opdrachtregelprogramma’s te schrijven die hun voorraad kan bijhouden:,ze willen het applicatie Superpy noemen.
De kernfunctionaliteit gaat over het bijhouden en genereren van rapporten over verschillende soorten gegevens:
1)Welke producten de supermarkt aanbiedt;
2)Hoeveel van elk type product heeft de supermarkt momenteel in voorraad;
3)Voor hoeveel elk product is gekocht en wat de houdbaarheidsdatum is;
4)Voor hoeveel elk product is verkocht en of het is verlopen, het feit dat dit het geval is.
Alle gegevens moeten worden opgeslagen in CSV-bestanden. 

De programmeertaal die wordt gebruikt is Python. De modules die daarvoor worden gebruikt zijn:
1)module argparse
2)module datetime
3)module OS
4)module CSV
5)module rich
6)module panda
De opdracht:
Voor de opdracht zullen onderstaande opgaven worden gemaakt dus in de programmeer taal Python:
Opdr_1)De programma zou een “intern datum” moeten hebben van welke dag het is (misschien opgeslagen in een eenvoudig tekstbestand) zodat je de tijd twee dagen vooruit kunt zetten door een commando te gebruiken als bijvoorbeeld de gebruikers opgave (in engels genoemd command): python super.py --advance-time 2
Opdr_2)Interactie met uw programma moet via de opdrachtregel verlopen b.v.:
Opdr_2a)python main.py buy --product-name orange --price 0.8 --expiration-date 2024-01-01
OK
Opdr_2b)python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+
Opdr_2c)python super.py --advance-time 2
OK
Opdr_2d)python super.py report inventory --yesterday
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+

Opdr_2e)python super.py sell --product-name orange --price 2
OK
Opdr_2f)python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+

Opdr_2g)python super.py report revenue --yesterday
Yesterday's revenue: 0

Opdr_2h)python super.py report revenue --today
Today's revenue so far: 2

Opdr_2i)python super.py report revenue --date 2019-12
Revenue from December 2019: 0

Opdr_2j)python super.py report profit --today
1.2
Opdr_2k)python super.py sell --product-name orange --price 2
ERROR: Product not in stock.

Vereisten
Vereisten aan de applicatie Superpy zijn:
A)Goed gestructureerde en gedocumenteerde code, waaronder:
1)Duidelijke en effectieve namen van variabelen en functies;
2)Gebruik van commentaar waarbij de code niet voor zichzelf spreekt;
3)Duidelijke en effectieve scheiding van code in afzonderlijke functies en eventueel bestanden.

B)Gebruik van modules voor zover daaruit blijkt dat u zelfstandig de documentatie heeft kunnen lezen en begrijpen, en de technieken kunt toepassen binnen:
1)module :csv
2)module:argparse
3)module:datetime, inclusief in het bijzonder het date-object, strftime- en strptime-functies en datetime-berekeningen met behulp van timedelta

C)Gebruik van externe tekstbestanden (CSV) om gegevens te lezen en te schrijven.
D)Een goed gestructureerde en gebruiksvriendelijke opdrachtregel interface met duidelijke beschrijvingen van elk argument in de --help-sectie.
E)Een tekstbestand met een gebruikshandleiding gericht op doelgroep. De gebruikshandleiding moet voldoende voorbeelden bevatten.
F)De applicatie moet het volgende ondersteunen:
F1)Het instellen en vervroegen van de datum die de applicatie als 'vandaag' beschouwt;
F2)Vastleggen van de aan- en verkoop van producten op bepaalde data;
F3)Rapporteren van omzet en winst over bepaalde perioden;
F4)Selecties van gegevens exporteren naar CSV-bestanden;
F5)Twee andere aanvullende niet-triviale kenmerken  gekozen  zijn:
F5.1: Het gebruik van een externe module Rich(opent in een nieuw tabblad) om de applicatie te verbeteren.
F5.2: De mogelijkheid om rapporten te importeren/exporteren van/naar andere formaten dan CSV (naast CSV)
Report eisen:
1)	Voeg een kort rapport van 300 woorden toe waarin drie technische elementen van uw implementatie worden belicht die u opmerkelijk vindt
2)	Leg uit welk probleem ze oplossen en waarom je ervoor hebt gekozen ze op deze manier te implementeren.
3)	Neem dit op in uw repository als een report.md-bestand

--einde--
Hieronder wordt  de uitwerking van genoemde opdracht. Volledigheidshalve wordt de opdracht nog een keer genoemd:
Opdr_1:interne datum
Opdr_1)De programma zou een “intern datum” moeten hebben van welke dag het is (misschien opgeslagen in een eenvoudig tekstbestand) zodat je de tijd twee dagen vooruit kunt zetten door een commando te gebruiken als bijvoorbeeld de gebruikers opgave (in engels genoemd command): python super.py --advance-time 2
Uitwerking van Opdr_1:
Ten behoeve van deze opdracht is een speciale .csv gemaakt met de naam:internal_date.csv. Voor de internal_date.csv is de volgende functie gemaakt: get_internal_date ().De taak van deze functie is gebruik maken van de module csv zodat de in de internal_date.csv genoemde datum wordt uitgelezen. Indien in de internal_date.csv geen datum staat dan wordt de dag van vandaag geplaatst en uitgelezen. Voor de test uitwerking zie Opdr_2c)python super.py --advance-time 2
Opdr_2:opdrachtregel: python main.py buy –product_name orange --price 0.8 –expiration_date 2023-01-01
Opdr_2)Interactie met uw programma moet via de opdrachtregel verlopen b.v.:
Opdr_2a)python main.py buy –product_name orange --price 0.8 –expiration_date 2023-01-01
Output:OK
Uitwerking van Opdr_2a:Voor deze opdracht klaarzetten in VS code:
Doel : van deze opdrachtregel is om een aangekocht product toe te voegen in document met naam bought.csv
Klaarzetten van gegevens voordat je de opdrachtregel kan gebruiken in de terminal display:
-bought.csv met daarin met kolommen en 1 rij: id,product_name,buy_date,buy_price,expiration_date 
1, appel,2023-11-25,0.4, 2024-1-1
-internal_date.csv:kolom naam:internal_date, waarde: 2023-11-1

-opdrachtregel(command): python main.py buy –product_name orange --price 0.8 –expiration_date 2024-01-01
Extra informatie: 
1)De kolom met de naam id in bought.csv wordt automatisch op volgorde ingevuld in de functie:
add_buy_product(product_name,buy_price,expiration_date,)
2)De kolom met de naam buy_date wordt gevuld met de waarde wat er staat voor de kolom met de naam internal_date in internal_date.csv , b.v. internal_date=2023-11-01
Resultaat: de verwachte resultaat zal zijn: in bought.csv wordt rij 2 toegevoegd, met id 2:
id,product_name,buy_date,buy_price,expiration_date 
1, appel,2023-11-25,0.4, 2024-1-1
2, orange, 2023-11-01,0.8,2024-01-01

Opdr_2b)python main.py report inventory --now	
Output:
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+
Uitwerking van : Opdr_2b)python super.py report inventory --now
Doel: van deze opdracht is het maken van een tabel zoals te zien in de output. Alle producten met dezelfde :Product Name EN Buy Price EN Expiration Date ,zullen worden samengevoegd en uitgebeeld als 1 regel.  In de kolom Count wordt vermeld hoeveel ervan zijn. Voor het woord “now” wordt gekeken naar de waarde van internal_date in the internal_date.csv
Klaarzetten van data voor de test:
0)internal_date.csv
Internal_date
internal_date:2023-12-5

1)Bought.csv:

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
2)opdrachtregel(command): python main.py report inventory –now
Extra informatie: Expiration_date betekent dat de houdbaarheid van het product  is verstreken en dus niet meer verkoopbaar is. Bijvoorbeeld expiration_date=2023-12-01 en vandaag =2023-12-01 dit betekent dat het product met expiration_date=2023-12-01 NIET verkoopbaar is.
Resultaat is:totaal 6 rijen, waarvan appel en orange :2 rijen hebben die dezelfde waardes hebben en de kolom Count op 2 wordt gezet.
Product Name Count Buy Price Expiration Date
appel        1         0.4   2023-12-06 
banana       1         0.6   2023-12-08
appel        2         0.4   2023-12-09
orange       2         0.5   2023-12-10
orange       1         0.5   2023-12-11
appel        1         0.4   2023-12-07
Xx xx
Opdr_2c)python main.py --advance_time 2
Output:OK
Uitwerking Opdr_2c)python main.py --advance_time 2:
Doel: het doel van deze opdracht is dat in de internal_date.csv in de kolom internal_date de waarde 2023-11-01 door de opdrachtregel: python main.py --advance_time 2 , 2 dagen verder wordt gezet wordt dus: 2023-11-03.
Klaarzetten van gegevens voor de test:
1)internal_date.csv
Internal_date
2023-11-01
2)opdrachtregel: python main.py --advance_time 2
Resultaat: de verwachte resultaat is de waarde van internal_date wordt :2023-11-03
internal_date.csv
Internal_date
2023-11-03

Opdr_2d)python mainpy report inventory –yesterday
Output:
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+
Uitwerking:
Doel: deze opdracht heeft de zelfde uitwerking als opdrachtregel:python.py report inventory –now, met 1 uitzondering in plaats van “now” is het “yesterday” dus de voorraad van gisteren.Uitgangspunt is de datum in de kolom van internal_date van internal_date.csv
De naam van de bijbehorende functie is: report_yesterday(yesterday)
Klaarzetten van gegevens voor de test:
1)internal_date.csv
Internal_date
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
8,appel,2023-11-25,0.4,2023-12-04
Opdrachtregel: python mainpy report inventory –yesterday
Resultaat:
Product Name Count Buy Price Expiration Date
appel        2     0.4       2023-12-06
appel        1     0.4       2023-12-07
banana       1     0.5       2023-12-06
banana       1     0.5       2023-12-07
Xx ende xx
Opdr_2e)python main.py sell --product-name orange --price 2
Output:OK
Gebruikte functie naam: add_sold_product(product_name,sell_price)



Opdr_2f)python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+

Opdr_2g)python super.py report revenue --yesterday
Yesterday's revenue: 0

Opdr_2h)python super.py report revenue --today
Today's revenue so far: 2

Opdr_2i)python super.py report revenue --date 2019-12
Revenue from December 2019: 0

Opdr_2j)python super.py report profit --today
1.2
Opdr_2k)python super.py sell --product-name orange --price 2
ERROR: Product not in stock.




