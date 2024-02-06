Datum:6 feb 2024 
Gebruikers gids/User guide:
SuperPy -project beschrijving:
Een grote supermarktketen heeft  gevraagd  opdrachtregelprogramma’s te schrijven die hun voorraad kan bij houden: ze willen het applicatie Superpy noemen. Dit project is een demo en bevat uitsluitend fruit producten. In een latere ontwikkelingsfase fase zullen andere producten zoals jam, pinda kaas toe gevoegd worden.
De kernfunctionaliteit gaat over het bijhouden en genereren van rapporten over verschillende soorten gegevens zoals bijvoorbeeld:
1)Welke producten de supermarkt aanbiedt;
2)Hoeveel van elk type product heeft de supermarkt momenteel in voorraad;
3)Voor hoeveel elk product is gekocht en wat de houdbaarheidsdatum is;
4)Voor hoeveel elk product is verkocht en of het is verlopen, het feit dat dit het geval is.
Alle gegevens moeten worden opgeslagen in CSV-bestanden. Indien er een uitzondering is dan wordt dat in de uitleg aangegeven.
De gebruiker maakt gebruik van opdrachtsregels (in het engels: commands) die in de terminal display van VS code wordt geplaats. Hieronder volgen de opdrachtregels die gebruikt kunnen worden en de bijbehorende uitleg eventueel inclusief een test data set om een idee krijgen hoe het werkt:
Opdrachtregel_1: buy
Uitleg van opdrachtregel_1:In onderstaande opdrachtregel wordt een product die is aangekocht met de naam: orange, prijs 0.8 euro, expiratie_datum 2024-01-01 via de terminal ingevoerd. Dus de gebruiker kan de opdrachtregel kopiëren en vervolgens plakken in de terminal. De applicatie Superpy zal zorgen dat de gegevens van de opdrachtregel in het bestand met de naam bought.csv wordt geplaatst.
De opdrachtregel is de input: python main.py buy –product_nam orange --price 0.8 –expiration_date 2024-01-01
Resultaat als output: in het bestand: bought.csv  te zien:
id,product_name,buy_date,buy_price,expiration_date
1,orange,2023-11-25,0.8,2024-01-01
Uitleg over regel met id 1: 
1)	De id wordt automatisch gegenereerd
2)	Buy_date : is afhankelijk wat er in het bestand met naam internal_date.csv is gezet als datum. In dit geval : 2023-11-25
Opdrachtregel_2  inventory –now
Uitleg van opdrachtregel_2:De opdrachtregel: python main.py report inventory –now laat zien in een schema wat de voorraad op dit moment is. Dit moment wordt bepaald wat er in het bestand internal_date.csv als datum staat. In dit geval is het :2023-12-31. In dit rapport komen alleen producten waarvan de houdbaarheidsdatum (expiration-date) nog niet verstreken zijn. Voorwaarde is er is minimaal 1 rij in bestand bought.csv.
De opdrachtregel is de input: python main.py report inventory –now

Voor de test zijn er hier enige test data voor het bestand bought.csv. Indien er producten zijn die dezelfde gegevens hebben dan worden deze 2 bij elkaar opgeteld en via kolom “ count” om aan te geven hoeveel ervan zijn.
Resultaat: hieronder is een voorbeeld van output schema in de terminal (hieronder alleen de data in de terminal zie je belijning van de bijbehorende tabel)
Product Name count Buy Price Expiration Date
Orange             1          0.8            2024-01-01

Opdrachtregel_3: advance-time 2
Uitleg van opdrachtregel_3:Er wordt gebruik gemaakt van het bestand met naam:internal_date.csv daarin staat de datum:2024-01-01 met de opdachtregel: python main.py --advance-time 2 wordt de datum in het bestand python main.py --advance-time 2, 2 dagen verder gezet. De wordt dus 2024-01-03
De opdrachtregel is de input: python main.py --advance-time 2
Resultaat: de datum in het  bestand  met naam: 2024-01-01 wordt 2024-01-03
Opdrachtregel 4: report inventory –yesterday
Uitleg van opdrachtregel_4: Er wordt gebruik gemaakt van het bestand met naam:internal_date.csv daarin staat de datum:2023-12-06. Omdat er “ yesterday” staat wordt de datum in internal_date.csv bewijzigd naar (1 dag terug): 2023-12-05. In dit rapport komen alleen producten waarvan de houdbaarheidsdatum (expiration-date) nog niet verstreken zijn.
De test dataset voor bought.csv is:
bought.csv
id,product_name,buy_date,buy_price,expiration_date
1,appel,2023-11-25,0.4,2023-12-06
2,appel,2023-11-25,0.4,2023-12-06
3,appel,2023-11-25,0.4,2023-12-05
4,appel,2023-11-25,0.4,2023-12-07
5,banana,2023-11-25,0.5,2023-12-06
6,banana,2023-11-25,0.5,2023-12-05
7,banana,2023-11-25,0.5,2023-12-07

De opdrachtregel is de input: python main.py report inventory –yesterday

Resultaat in Rich(Rich is een module die zorgt er voor dat de tabel mooi kan worden opgemaakt
Bijvoorbeeld met speciale kleuren):

product name count buy price expiration_date
appel         2     0.4      2023-12-06  
appel         1     0.4      2023-12-07 
banana        1     0.5      2023-12-06
banana        1     0.5      2023-12-07
Opdrachtregel 5:Sell
Uitleg: doel van deze opdrachtregel is : indien een product wordt verkocht dan wordt dit vastgelegd in het stand sold.csv. Dit bestand heeft diverse kolommen te weten:
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
Deze kolommen worden gevuld. Een opmerking hierbij is dat de waarde van kolom bought_id komt uit de gegevens van bestands bougt.csv en de sell_date komt van de datum uit het bestand .de internal_date. Tevens wordt in het bestand bought.csv waarvan het product is verkocht verwijderd
Hierbij heb je test data nodig om eerst klaar te wachten daarna kan je de opdrachtregel gebruiken om de resultaat te zien:
Test data:
bought.csv
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date

id,product_name,buy_date,buy_price,expiration_date
1,orange,2023-11-25,0.5,2023-12-5
2,appel,2023-11-23,0.4,2023-11-23 
3,appel,2023-11-25, 0.4,2023-12-6
4,banana,2023-11-24,0.6,2023-12-8
5,appel,2023-11-25,0.4,2023-12-9
6,orange,2023-11-25,0.5,2023-12-5
7,orange,2023-11-25,0.5,2023-12-5
8,appel,2023-11-23,0.4,2023-12-10


internal_date.csv:
internal_date
2023-12-07
Sold.csv
Geen rij

De opdrachtregel/input: python main.py sell --product_name appel --price 2

Resultaat/output: het bestand sold.csv zou zo behoren uit te zien, toegevoegd is regel 2 met id 2:
sold.csv
id,bought_id,sell_date,sell_price
1,5,2023-12-7,2.0
2,8,2023-12-7,2.0

Opdrachtregel 6: report inventory --now
Uitleg van opdracht_6 : De opdrachtregel: python main.py report inventory –now laat zien in een schema wat de voorraad op dit moment is. Dit moment wordt bepaald wat er in het bestand internal_date.csv als datum staat. In dit geval is het :2023-12-31. In dit rapport komen alleen producten waarvan de houdbaarheidsdatum (expiration-date) nog niet verstreken zijn. Voorwaarde is dat er 0 rij in bestand bought.csv. Ten gevolge hiervan krijg je alleen een leeg tabel te zien zonder rij.

De opdrachtregel is: python main.py report inventory --now 
Note: Er zijn GEEN rijen in bestand bought.csv
Resultaat/uitput, hier wordt de kolommen weer gegeven in de terminal display in csv code zie je een tabel met alleen kolom namen en 0 rijen:
Product Name count Buy_price Expiration_date

Opdrachtregel 7: report revenue --yesterday
Uitleg:doel van deze opdrachtregel: python main.py report revenue –yesterday, is de opbrengst (aantal verkochte producten x verkoopprijs) te berekenen van gisteren. De datum van gisteren is afhankelijk van de datum die staat in het bestand internal_date.csv. In de terminal display krijg he het resultaat te zien.
Voordat je de opdrachtregel invoert moet je eerst de test data klaar zetten van:
Internal_date.csv
internale_date 
2023-12-07
sold.csv :
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
1,5,2023-12-6,2.0,appel,2023-11-25,0.4,2023-12-31
2,4,2023-12-6,2.0,appel,2023-11-25,0.4,2023-12-31
3,3,2023-12-6,1.5,banan,2023-11-25,0.4,2023-12-31
4,2,2023-12-5,2.0,appel,2023-11-25,0.4,2023-12-31
5,1,2023-12-4,1.5,banan,2023-11-25,0.4,2023-12-31
6,6,2023-12-9,2.0,appel,2023-11-25,0.4,2023-12-31
7,7,2023-12-10,1.0,orange,2023-11-25,0.4,2023-12-31

De opdrachtregel/input: python main.py report revenue --yesterday
Resultaat als output is ALLEEN de laatste regel de rest is uitwerking:
expected result:
id 1,2,3
id sell_price
1  2.2
2  2.2
3  1.5
totaal:5.9

Opdrachtregel_8: report revenue --today 
Uitleg van deze opdachtregel is: python main.py report revenue --today, is de opbrengst (aantal verkochte producten x verkoopprijs) te berekenen van vandaag. De datum van vandaag is afhankelijk van de datum die staat in het bestand internal_date.csv. In de terminal display krijg he het resultaat te zien.
Voordat je de opdrachtregel invoert moet je eerst de test data klaar zetten van:
internale_date.csv:
internale_date 
2023-12-07
sold.csv :
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
1,5,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
2,4,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
3,3,2023-12-7,1.5,banan,2023-11-25,0.4,2023-12-31
4,2,2023-12-5,2.0,appel,2023-11-25,0.4,2023-12-31
5,1,2023-12-4,1.5,banan,2023-11-25,0.4,2023-12-31
6,6,2023-12-9,2.0,appel,2023-11-25,0.4,2023-12-31
7,7,2023-12-10,1.0,orange,2023-11-25,0.4,2023-12-31

De opdrachtregel: python main.py report revenue --today
Het resultaat/output, in de terminal display zie je alleen de laatste regel, totaal bedrag :
expected result:
id 1,2,3
id sell_price
1  2.0
2  2.0
3  1.5
totaal:5.5

Opdrachtregel_9: python report revenue --date 2023-12 --file_type_excel
Uitleg van deze opdachtregel: de gebruiker geeft via de opdrachtregel in de terminal en haalt op de totale omzet(verkoop) van de maand december 2023. Hier wordt totale omzet weg geschreven in een microsoft excel met de naam revenue_report.xlxs.
Voordat je de opdrachtregel invoert moet je eerst de test data klaar zetten van:
2)sold.csv :
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
1,5,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
2,4,2023-11-7,2.0,appel,2023-11-25,0.4,2023-12-31
3,3,2023-12-1,1.5,banan,2023-11-25,0.4,2023-12-31
4,2,2023-12-30,0.5,appel,2023-11-25,0.4,2023-12-31
5,1,2023-10-4,1.5,banan,2023-11-25,0.4,2023-12-31
6,6,2023-9-9,2.0,appel,2023-11-25,0.4,2023-12-31
7,7,2023-11-10,1.0,orange,2023-11-25,0.4,2023-12-31


De opdrachtregel_9: python main.py report revenue --date 2023-12 --file_type_excel
Resultaat /output:
expected result:
output:Revenue from December 2023: 4.0
Teven ook te vinden in bestand met de naam: revenue_report.xlxs. Deze is te vinden in de file manager en te openen met Microsoft Excel.

De opdrachtregel_10:python main.py report profit –today
Uitleg: De datum van “vandaag” is afhankelijk van wat in de internal_data.csv staat. Hier wordt de winst van “ vandaag” uitgerekend. De definitie van winst is totale verkoop minus de totale kosten.
Voordat je de opdrachtregel invoert moet je eerst de test data klaar zetten van:
Internal_date.csv:
Internal_date
2023-12-07
sold.csv
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
1,5,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
2,4,2023-12-7,2.0,appel,2023-11-25,0.4,2023-12-31
3,3,2023-12-6,1.5,banan,2023-11-25,0.4,2023-12-31
4,2,2023-12-5,2.0,appel,2023-11-25,0.4,2023-12-31
5,1,2023-12-10,1.5,banan,2023-11-25,0.4,2023-12-31
6,6,2023-12-9,2.0,appel,2023-11-25,0.4,2023-12-31
7,7,2023-12-7,1.0,orange,2023-11-25,0.3,2023-12-31

De opdrachtregel_10: python main.py report profit –today

Resultaat: profit of today=3,9
Op 4-2-2024 alles getest en werkt ook user guide afgerond
 Hierna 3x highlight schrijven en requirement uitleg.
Eisen/”Requirement” van project Superpy
Hieronder wordt uitleg gegeven hoe applicatie Superpy wordt voldaan aan de eisen/”requirement” van het project Superpy . Er zijn 2 type eisen:
1)eisen voor de programmeer code
2)eisen voor het rapport(report)
Ad1: eisen voor de programmeer code:
Hieronder worden de eisen voor de programmeer code eerst opgesomd en daarna nogmaals herhaald om uit te leggen hoe in de applicatie aan eisen wordt voldaan.
A)Goed gestructureerde en gedocumenteerde code, waaronder:
1)Duidelijke en effectieve namen van variabelen en functies;
2)Gebruik van commentaar waarbij de code niet voor zichzelf spreekt;
3)Duidelijke en effectieve scheiding van code in afzonderlijke functies en eventueel bestanden.

B)Gebruik van modules voor zover daaruit blijkt dat u zelfstandig de documentatie heeft kunnen lezen en begrijpen, en de technieken kunt toepassen binnen:
1)module :csv
2)module:argparse
3)module:datetime, inclusief in het bijzonder het date-object, strftime- en strptime-functies en datetime-berekeningen met behulp van timedelta

C)Gebruik van externe tekstbestanden (CSV) om gegevens te lezen en te schrijven.
D)Een goed gestructureerde en gebruiksvriendelijke opdrachtregelinterface met duidelijke beschrijvingen van elk argument in de --help-sectie.
E)Een tekstbestand met een gebruikshandleiding gericht op peers als doelgroep. De gebruikshandleiding moet voldoende voorbeelden bevatten.
F)De applicatie moet het volgende ondersteunen:
F1)Het instellen en vervroegen van de datum die de applicatie als 'vandaag' beschouwt;
F2)Vastleggen van de aan- en verkoop van producten op bepaalde data;
F3)Rapporteren van omzet en winst over bepaalde perioden;
F4)Selecties van gegevens exporteren naar CSV-bestanden;
F5)Twee andere aanvullende niet-triviale kenmerken naar keuze:
F5.1: Het gebruik van een externe module Rich(opent in een nieuw tabblad) om de applicatie te verbeteren.
F5.2: De mogelijkheid om rapporten te importeren/exporteren van/naar andere formaten dan CSV (naast CSV)
Hieronder volgt de uitwerking van de eisen : programmeer code , de eis zal volledigheidshalve worden herhaald:
A)Goed gestructureerde en gedocumenteerde code, waaronder:
1)Duidelijke en effectieve namen van variabelen(A1.1) en functies(A1.2);
Uitwerking A1.1: Duidelijke en effectieve namen van variabelen: add_buy_product(product_name,buy_price,expiration_date,)
wordt de variabel met de naam: id_int , gebruikt. Hiermee wordt aangeduid dat de id de type integer heeft en niet de type string. In dezelfde for- loop wordt de variabel : new_row_id gebruikt om aan te duiden dat dit de id is voor de nieuw aangekochte product.
Uitwerking A1.2: Duidelijke en effectieve namen van functies: A1.2  duidelijk naam voor de functies:Voor de aankoop van een nieuwe product is de fucntie met de naam:add_buy_product(product_name,buy_price,expiration_date,) en voor de verkoop van een product is een functie met de naam:add_sold_product(product_name,sell_price). Bij het lezen van de naam van de functie is het duidelijk wat de functionaliteit van de functie is.
2)Gebruik van commentaar waarbij de code niet voor zichzelf spreekt;
Uitwerking A2: Zie hiervoor de functie met de naam:add_buy_product(product_name,buy_price,expiration_date,),direct onder de definitie regel van functie staat volgende " comment" :#open en leest bestand:internal_date.csv. Deze comment geeft dus aan dat hieronder het bestand met de naam: internal_date.csv wordt geopend en de data worden uitgelezen.
3)Duidelijke en effectieve scheiding van code in afzonderlijke functies en eventueel bestanden.
Uitwerking A3: hiervoor is gebruik gemaakt van het bestand met de naam: main.py. In  bestand main.py wordt b.v. de functie met de naam:main() beschreven. In main wordt alle opdrachtregels beschreven. De functie die hoort bij bijvoorbeeld de opdrachtregel: python main.py buy –product_nam orange --price 0.8 –expiration_date 2024-01-01, kort genoemd: command buy,wordt in het bestand : functions.py aangeroepen in de functie:add_buy_product(product_name,buy_price,expiration_date,).
B)Gebruik van modules voor zover daaruit blijkt dat u zelfstandig de documentatie heeft kunnen lezen en begrijpen, en de technieken kunt toepassen binnen:
B1)module :csv
Uitwerking B1: als voorbeeld nemen we het bestand functions.py ,daarin lees je de functie:add_sold_product(product_name,sell_price) en statement:with open(internal_date_file_path,'r',newline='')as file:. Boven in functions.py lees je de statement:import csv.Dit is gedaan na het lezen van het document:https://docs.python.org/3/. Daarin staat dat je de module:csv moet gebruiken om bestanden met de extentie .csv b.v te openen, lezen of verwijderen.Na lezen ervan is  b.v.de statement:  with open(internal_date_file_path,'r',newline='')as file:,gebruikt om het bestand internal_date.csv te openen in python.
B2)module:argparse:
Uitwerking B2:Voor b.v. de opdrachtregel (command):python main.py buy –product_nam orange --price 0.8 –expiration_date 2024-01-01, lees je in google dat je gebruik moet maken van de module argparse. Om de uitleg van de module argarse te vinden moet je gaan naar de documentatie van python:https://docs.python.org/3/. Daarin staat beschreven een voorbeeld  hoe je met de module argparse kan gebruiken om een command te maken.
B3)module:datetime, inclusief in het bijzonder het date-object, strftime- en strptime-functies en datetime-berekeningen met behulp van timedelta
Uitwerking B3:module:datetime:Voor b.v. de opdrachtregel (command):python main.py buy –product_nam orange --price 0.8 –expiration_date 2024-01-01, zie je dat in de opdrachtregel een kolom is benoemd met de naam " expiration_date" in de command is dit de type: string welke geconverteerd moet worden naar de type datetime object. Aangezien je in b.v. de functie:add_sold_product(product_name,sell_price) berekening moet maken met de datum ,b.v. "gisteren"/"yesterday" of "2 dagen terug"/"advance_time 2" is het noodzakelijk de documentatie van python :https://docs.python.org/3/ en module datetime hiervoor te gebruiken. Verder lees je dat in de return statement van de functie:string_to_datetime(date_string, format='%Y-%m-%d') wordt datetime.strptime gebruikt. Voor de functie:datetime_to_string(date_object,format='%Y-%m-%d') wordt date_object.strftime(format) gebruikt. Voor de functie:advance_time(advance_time) wordt in de if-statement de timedelta() functie gebruikt.
C)Gebruik van externe tekstbestanden (CSV) om gegevens te lezen en te schrijven.
Uitwerking C: in de functie:advance_time(advance_time) zijn er 2 statements gebruikt. De eerste statement is:with open(internal_date_file_path,'r',newline='')as file:, de letter 'r' staat voor "read" , dit betekent dat de bestaande data uit het bestand internal_date wordt uitgelezen. De tweede statement is :with open(internal_date_file_path,'w', newline='') as file:, dit betekent dat met de letter 'w' de nieuwe waarde van de datum wordt weggeschreven naar de het bestand met de naam internal_date.
D)Een goed gestructureerde en gebruiksvriendelijke opdrachtregelinterface met duidelijke beschrijvingen van elk argument in de --help-sectie.
Uitwerking D: Zie hiervoor in main.py b.v. voor de command:sell. Hiervoor worden de volgende 2 statements gebruikt:sell_parser.add_argument("--product_name", type=str, help="give the name of the product choice:apple, banana, manderin")
sell_parser.add_argument("--price", type=float, help="give the price of the product for example: 0.7"). Voor de structuur zie je dat voor de noodzakelijke argument, die bij naam wordt genoemd, een aparte statement is gemaakt met daarin de bijbehorende "hulp" commentaar.
E)Een tekstbestand met een gebruikshandleiding gericht op peers als doelgroep. De gebruikshandleiding moet voldoende voorbeelden bevatten.
Uitwerking E:In de ReadMe file is de gebruikshandleiding(user guide) opgenomen daarin lees je de voorbeelden.
F)De applicatie moet het volgende ondersteunen:
F1)Het instellen en vervroegen van de datum die de applicatie als 'vandaag' beschouwt;
Uitwerking F1:zie hiervoor de functie:advance_time(advance_time). In deze functie wordt als uitgangspunt de datum van het bestand internal_date.csv gebruikt. Door middel van de command b.v.:--advance_time 2 wordt de functie :advance_time(advance_time) aangeroepen en  de datum 2 dagen vooruit gezet.
F2)Vastleggen van de aan- en verkoop van producten op bepaalde data;
Uitwerking F2: uitwerking F2:voor aankoop van producten zie de werking van de command:
python main.py buy –product_nam orange --price 0.8 –expiration_date 2024-01-01
voor verkoop van producten zie de werking van de command:
python main.py sell --product_name appel --price 2

F3)Rapporteren van omzet en winst over bepaalde perioden;
Uitwerking F3: zie voor rapport omzet command:
python main.py report revenue --today
zie voor rapport winst command:Er is geen rapport van winst wel berekening zie command die hierna komt. Het tabel vorm van het rapport van winst is vergelijkbaar met die van omzet maar dan andere gegevens: python main.py report profit –today
F4)Selecties van gegevens exporteren naar CSV-bestanden;
Uitwerking F4: zie uitwerking van command:python main.py sell --product_name appel --price 2
In de functie van de command:add_sold_product(product_name,sell_price) wordt zowel via module CSV ingelezen als weggeschreven d.m.v.de modes "r":read, "w":write.
F5)Twee andere aanvullende niet-triviale kenmerken naar keuze:
F5.1: Het gebruik van een externe module Rich(opent in een nieuw tabblad) om de applicatie te verbeteren.
Uitwerking F5.1: Uitwerking F.5.1)Rich is voor  de command:report inventory --now, in de functie: report_now(now)
F5.2: De mogelijkheid om rapporten te importeren/exporteren van/naar andere formaten dan CSV (naast CSV): de keuze is gevallen voor export naar microsoft excel.
Uitwerking F5.2: Uitwerking 5.1)de uitwerking is gemaakt voor de command:python report revenue --date 2023-12 --file_type_excel, in de functie:revenu_date(date,file_type_excel)
--the end 5 feb 2024--




Ad 2:eisen voor het rapport:
2.1Voeg een kort rapport van 300 woorden toe waarin drie technische elementen van uw implementatie worden belicht die u opmerkelijk vindt.
2.2 Leg uit welk probleem ze oplossen en waarom je ervoor hebt gekozen ze op deze manier te im plementeren
2.3	Neem dit op in uw repository als een report.md-bestand
Ad 2.1 en 2.2:Uitwerking van :2.1 en 2.2: Aangezien deze 2 eisen gerelateerd zijn aan elkaar wordt hieronder 3 tal technische elementen belicht die opmerkelijk zijn. Tevens wordt ook uitgelegd (ad 2.2) wat voor soort probleem wordt opgelost  en de rede van de keuze van de oplossing.
Technische_element_1:functions: string_to_datetime() en functie: datetime_to_string()
Door het geheel van de applicatie wordt regelmatig de datum geconverteerd van data type string naar data type datetime object en andersom. Vanwege de veelvuldigheid van dit gebruik zijn er twee tal functies gemaakt om dit op te lossen te weten:
1 functie: string_to_datetime()
2 functie: datetime_to_string()
De rede waarom voor de keuze van deze oplossing is omdat de beide functies herbruikbaar is en makkelijker is te onderhouden.
Technische_element_2:de id van functie: add_buy_product() van de opdrachtregel buy 
Voor de opdrachtregel : python main.py buy –product_nam orange --price 0.8 –expiration_date 2024-01-01, wordt in de bought.csv de kolom “ id”  aangehouden. De kolom “id” wordt automatisch door de applicatie Superpy opgehoogd indien er een nieuw product wordt toegevoegd. Om dit op te lossen is gekozen voor de volgende oplossing: voor elke iteratie van de rij in de bought.csv wordt een variabel bijgehouden b.v. id_bijhouden. Bij elke iteratie wordt de de variabel id_bijhouden opgehoogd met 1. Indien er een NIEUW product wordt toegevoegd dan wordt de variabel id_eenOphogen gebruikt daarbij wordt bewerkt dat id_bijhouden met 1 wordt opgehoogd. De waarde van id_eenOphogen is dan de waarde van de kolom ‘id’ van de nieuw toegevoegde rij. De naam van de variabelen die hierboven zijn genoemd zijn fictie gekozen om de functionaliteit te laten begrijpen voor de lezer. In de functie: add_buy_product() zie je de beschreven constructie terug.
Technische_element_3:door inzicht in fuctionaliteit van het proces kan je programmeren vergemakkelijken
In de opdracht van het project werd voor de bought.csv en sold.csv als voorstel gedaan de volgende kolommen:
id,product_name,buy_date,buy_price,expiration_date
Sold.csv, kolommen:
id,bought_id,sell_date,sell_price
Aangezien de opdrachtregel van b.v.  rapport: python main.py report profit --today  in de bought.csv van het verkochte product de rij wordt verwijderd is het handig de kolommen van sold.csv UIT TE BREIDEN met de volgende kolommen van bought.csv: product_name,buy_date,buy_price,expiration_date
Ten gevolge hiervan zien  de namen van de “ nieuwe”  kolommen van sold.csv als volgt uit:
id,bought_id,sell_date,sell_price,product_name,buy_date,buy_price,expiration_date
Door de ‘nieuwe’ kolommen van sold.csv aan te houden worden de bijbehorende data ook zodanig geplaatst. Ten gevolge hiervan is het relatief makkelijk om b.v. voor  de command: python main.py report profit –today, een functie te maken met de naam: report_profit_today(), om de winst(‘profit’) te berekenen.
Ad2.3 In de report.md zijn de 3 Technische_elementen opgenomen conform de opdracht.
Xx einde alle Eisen aan report xx 4-2-2024



















