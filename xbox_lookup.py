#ip database
import time, sys #imports time feature so there is spaces in between prints. And sys function.

#Special feature that gives the python script the typewriting effect
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush() 
    time.sleep(0.01)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  value = input()  
  return value 

#varible
yes_no = ["yes", "no"]

print('''
 ██▓ ███▄    █   █████▒▒█████  ▄▄▄█████▓ ▄▄▄       ██ ▄█▀▓█████  ██▀███  
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒▓  ██▒ ▓▒▒████▄     ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒▒ ▓██░ ▒░▒██  ▀█▄  ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░░ ▓██▓ ░ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░  ▒██▒ ░  ▓█   ▓██▒▒██▒ █▄░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░   ▒ ░░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░     ░      ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒    ░        ░   ▒   ░ ░░ ░    ░     ░░   ░ 
 ░           ░            ░ ░                 ░  ░░  ░      ░  ░   ░     
                                
                                By: 123xboxlookup''')

time.sleep(1)

typingPrint("DISCLAIMER!, Before you use this tool we, the creators, are not responsible for any actions performed with the use of this tool and should only be used for educational purposes. Futhermore, there is nothing illegal with scraping for information as proven in court many times, including in the United Kingdom. ")
print("")

time.sleep(2)#sleep feature that dictates how long the program waits for. In this case 3 seconds

response = ''
while response not in yes_no:
    response = typingInput("if you understand and have just read through the previous message please enter either yes or no: ")

if response == 'no':
	typingPrint("ok exiting now.")
	quit()
else:
	if response == 'yes':
		typingPrint("ok continuing please wait... ")
print("")

time.sleep(1)

IP = input("Enter gamertag (case sensitive): ")

typingPrint("tracking, " + IP )
print("")

time.sleep(2)

#cool symbol
typingPrint('''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
''')
print("")

time.sleep(1)

typingPrint("Almost done finalizing results.")
print("")

time.sleep(1)

#information about people
if IP == 'Deathscar3081':
    typingPrint('''IP = 86.182.42.234
ISP = BT
Country = UK
Currency = GBP''')

else:
    if IP == 'Baldmartin6793':
        typingPrint('''IP = 151.227.241.210
ISP = Sky
Country = UK
Currency = GBP''')

    else:
        if IP == 'Classicchaos666':
            typingPrint('''IP = 109.156.228.27
ISP = BT
Country = UK
County = Derbyshire
Town = barlow
Road = Valley Road
Currency = GBP
Connection type = Cable/DSL
Coordinates = 53.27421043264742, -1.493140634474341
Post code = S18 7SN
                     ''')

        else:
            if IP == 'DylanDOGE894':
                typingPrint('''IP = 90.203.192.89
ISP = BT
Country = UK
City = Bolton
                         ''')

            else:
                if IP =='Elite Ramiz7':
                    typingPrint('''IP = 212.159.86.90
ISP = Plusnet
Country = UK
                             ''')

                else:
                    if IP =='Superdarken10':
                        typingPrint('''IP = 151.231.214.15
ISP = Sky
Country = UK
                                 ''')

                    else:
                        if IP =='Mossybird101':
                            typingPrint('''IP = 46.64.175.60
ISP = Sky
Country = UK
County = Derbyshire
Town = Dronfield
Address = 7 Egerton Rd, Dronfield S18 2LG
Post code = S18 2LG
Currency = GBP
Connection type = Cable/DSL
Coordinates = 53.30467310278891, -1.4682198677700666
Name = Alex Moss
Date of birth = 2006/2007
                                     ''')

                        else:
                            if IP =='Cheese boi9769':
                                typingPrint('''IP = 92.17.160.25
ISP = TalkTalk
Country = UK
County = Derbyshire
Town = Dronfield
Post code = S18 2LN
Currency = GBP
Address = 70 Green Ln, Dronfield S18 2LN
Coordinates = 53.30657029830694, -1.465228582627336
Date of birth = 2006/2007
Related phone numbers = +44 0789 4275809
Name = Joe Bracken
Connection type = Cable/DSL

                                         ''')

                            else:
                                if IP =='Beanreborn':
                                    typingPrint('''IP = 86.179.255.229                                             
ISP = BT
Country = UK
                                             ''')

                                else:
                                    if IP =='Gta Layered':
                                        typingPrint('''IP = 5.71.248.76                                               
ISP = Sky
Country = UK
                                                 ''')
                                    else:
                                        if IP =='SlickPup8934571':
                                            typingPrint('''IP = 64.237.228.180
ISP =  Puerto Rico Telephone Company
Country = Puerto Rico
                                                     ''')

                                        else:
                                            if IP =='Deep Merge':
                                                print('''IP = 75.9.86.140                                               
ISP = Sky
Country = UK
                                                         ''')

                                            else:
                                                if IP == 'andreasBRHUE66':
                                                    typingPrint('''IP = 152.250.132.234                                               
ISP = Telefonica Brasil S.A
Country = brasil
                                                             ''')
                                                else:
                                                    if IP == 'Thee Greg':
                                                        typingPrint('''IP = 104.0.65.126                                               
ISP = AT&T Corp
Country = United States
                                                                 ''')

                                                    else:
                                                        if IP == 'Laggy1exe':
                                                            typingPrint('''IP = 147.147.86.219                                              
ISP = Plusnet
Country = UK
                                                                     ''')

                                                        else:
                                                            if IP == 'electromaniac15':
                                                                typingPrint('''IP = 5.65.236.247                                             
ISP = Sky
Country = UK
                                                                         ''')

                                                            else:
                                                                if IP == 'Harley james985':
                                                                    typingPrint('''IP = 151.227.240.13                                            
ISP = Sky
Country = UK''')
                                                                else:
                                                                    if IP == 'X LEO X RNG':
                                                                        typingPrint('''IP = 45.186.249.20
ISP = Glfibra Servicos De Telecomunicacoes Ltda
Country = Brasil''')                                                
                                                                    else:
                                                                        if IP == 'ProSpartan303':
                                                                            typingPrint('''IP = 5.69.36.89
ISP = Sky
Country = UK
Currency = GBP''')
                                                                        else:
                                                                            if IP == 'redbear269':
                                                                                typingPrint('''IP = 86.13.34.10
ISP = Virgin Media Limited
Country = UK''')                                                            
                                                                            else:
                                                                                if IP == 'pulchra9737':
                                                                                    typingPrint('''IP = 5.64.5.16
ISP = Sky
Country = UK ''')

                                                                                else:
                                                                                    if IP == 'udc spectre':
                                                                                        typingPrint('''IP = 150.143.89.5
ISP = BT Americas Inc
Country = UK''')

                                                                                    else:
                                                                                        if IP == 'marineward01':
                                                                                            typingPrint('''IP = 90.206.218.68
ISP = Sky
Country = UK''')

                                                                                        else:
                                                                                            if IP == 'n0ahB1476':
                                                                                                typingPrint('''IP = 94.13.180.27
ISP = Sky
Country = UK''')

                                                                                            else:
                                                                                                if IP == 'DerekDaftLad':
                                                                                                    typingPrint('''IP = 81.111.123.246
ISP = Virgin Media Limited
Country = UK''')

                                                                                                else:
                                                                                                    if IP == 'focalcheese5464':
                                                                                                        typingPrint('''IP = 92.13.177.117
ISP = Carphone Warehouse
Country = UK''')

                                                                                                    else:
                                                                                                        if IP == 'xxrevliinxx':
                                                                                                            typingPrint('''IP = 90.248.194.126
ISP = Vodafone
Country = UK''')

                                                                                                        else:
                                                                                                            if IP == 'JammyJP3936':
                                                                                                                typingPrint('''IP = 86.13.88.156
ISP = Virgin
Country = UK
County = Derbyshire
Town = dronfield
address = 69-71 Holmesdale Rd, Dronfield S18 2FA
Post code = S18 2FA
coordinates = 53.30674319087971, -1.4575017285546672
Currency = GBP
Connection type = Cable/DSL
Name = John Plummer
Date of birth = 2007
Email address = Jp12340987565@gmail.com
Facebook = John Plummer
Instagram = johnplum420
Phone number: +44 7480 772003''')

                                                                                                            else:
                                                                                                                if IP == 'jefff9990':
                                                                                                                    typingPrint('''STOP! Resolving this person is banned and your IP has subsequently been logged.''')
                                                                                                                else:
                                                                                                                    if IP == 'III Xvq III':
                                                                                                                        typingPrint('''IP = 86.13.91.53
ISP = Virgin
Country = UK''')

                                                                                                                    else:
                                                                                                                        if IP == 'GazaCR24':
                                                                                                                            typingPrint('''IP = 186.159.163.180
ISP = Cable Tica
Country = Costa rica''')

                                                                                                                        else:
                                                                                                                            if IP == 'AngryPerson3012':
                                                                                                                                typingPrint('''IP = 46.64.146.21
ISP = Sky
Country = UK''')

                                                                                                                            else:
                                                                                                                                if IP == 'Was Good Breh':
                                                                                                                                    typingPrint('''IP = 76.214.244.189
ISP = AT&T Services, Inc.
Country = USA''')

                                                                                                                                else:
                                                                                                                                    if IP == 'Jake5111':
                                                                                                                                        typingPrint('''IP = 82.12.161.51
ISP = Virgin Media Limited
Country = UK''')

                                                                                                                                    else:
                                                                                                                                        if IP == 'Daniellocochow4':
                                                                                                                                            typingPrint('''IP = 187.236.125.211
ISP = Uninet S.A. de C.V.
Country = Mexico''')

                                                                                                                                        else:
                                                                                                                                            if IP == 'R2D24977':
                                                                                                                                                typingPrint('''IP = 92.232.204.28
ISP = Virgin
Country = UK
County = Derbyshire
City = Sheffield''')

                                                                                                                                            else:
                                                                                                                                                if IP == 'jsmd37079727':
                                                                                                                                                    typingPrint('''ISP = Virgin
Country = UK
County = Derbyshire
Town = Dronfield
Address = 86 Cecil Rd, Dronfield S18 2GX
Coordinates = 53.307666382003646, -1.471073303803803
Post code = S18 2GX
Currency = GBP
Connection type = Cable/DSL
Date of birth = 2007 (May 17) Maybe wrong about the number in brackets
Name = Jacob Dyson
Age = 15
Phone number = +44 7751 225581 
Discord name = JSMD3707#8008
Sex = man
Instagram (username) = jsmd3707
instagram (name) = Jacob Dyson
Facebook = Jacon Dyson
Steam (name) = jsmd
Phone provider = O2
Extra notes = Supports LGBTQ, Identifys as pansexual, non-binary and genderflux, pet lover 
''')

                                                                                                                                                else:
                                                                                                                                                    if IP == 'NuclearGaming39':
                                                                                                                                                        typingPrint('''IP = 176.254.176.237
ISP = Sky
Country = UK
County = Derbyshire
City = Sheffield
Town = Eckington
Coordinates = 53.30770215356089, -1.3579917742872472
Post code = S21 4HL
Currency = GBP
Age = 15
Name = Leo Revill
Sex = Male
instagram = mr king
Connection type = Cable/DSL''')

                                                                                                                                                    else:
                                                                                                                                                        if IP == 'jaedonx':
                                                                                                                                                            typingPrint('''IP = 2.121.148.244
ISP = Sky
Country = UK
''')

                                                                                                                                                        else:
                                                                                                                                                            if IP == 'BabyOd1n':
                                                                                                                                                                typingPrint('''Country = UK
County = Derbyshire
Town = Dronfield
Address = 3 Cecil Rd, Dronfield S18 2GW
Post code = S18 2GW
Coordinates = 53.305168510670974, -1.4694284241390239
Currency = GBP''')

                                                                                                                                                            else:
                                                                                                                                                                if IP == 'BigKahuna010':
                                                                                                                                                                    typingPrint('''Country = UK
County = Derbyshire
Town = Barlow
Currency = GBP''')

                                                                                                                                                                else:
                                                                                                                                                                    if IP == 'HomeBoyMeek':
                                                                                                                                                                        typingPrint('''IP = 162.193.214.216
ISP = AT&T Services, Inc.
Country = USA
State = Georgia
Town = DeKalb
Connection type = Cable/DSL
Currency = USD''')

                                                                                                                                                                    else:
                                                                                                                                                                        if IP == 'MeoowHM':
                                                                                                                                                                            typingPrint('''IP = 173.50.97.144
ISP = Verizon Business
Country = USA
State = New York
Connection type = Corporate
Currency = USD''')

                                                                                                                                                                        else:
                                                                                                                                                                            if IP == 'RetroWaif866':
                                                                                                                                                                                typingPrint('''IP == 31.49.248.217
ISP = BT
Country = UK
City = Stockton-on-Tees
Post code = TS16
Currency = GBP
Connection type = Corporate
Name = Luke Kitching''')

                                                                                                                                                                            else:
                                                                                                                                                                                if IP == 'steelclown4':
                                                                                                                                                                                    typingPrint('''IP == 107.208.213.156
ISP = AT&T Services, Inc.
Country = USA
State = Washington
District = King
Connection type = Corporate
Currency = USD''')

                                                                                                                                                                                else:
                                                                                                                                                                                    if IP == 'DerekDaftLad':
                                                                                                                                                                                        typingPrint('''IP = 81.111.123.246
ISP = Virgin
Country = UK''')

                                                                                                                                                                                    else:
                                                                                                                                                                                        if IP == 'clynxyy':
                                                                                                                                                                                            typingPrint('''IP = 94.1.153.212
ISP = Sky
Country = UK''')

                                                                                                                                                                                        else:
                                                                                                                                                                                            if IP == 'IRONHAND5523':
                                                                                                                                                                                                typingPrint('''IP = 94.195.227.21
ISP = Sky
Country = UK''')

                                                                                                                                                                                            else:
                                                                                                                                                                                                if IP == 'Hendog98443':
                                                                                                                                                                                                    typingPrint('''IP = 90.220.125.19
ISP = Sky
Country = UK''')

                                                                                                                                                                                                else:
                                                                                                                                                                                                    if IP == 'Alfmeister07':
                                                                                                                                                                                                            typingPrint('''IP = 82.33.54.131
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if IP == 'Blanksy4509':
                                                                                                                                                                                                            typingPrint('''IP = 92.14.194.153
ISP = TalkTalk
Country = UK''')

                                                                                                                                                                                                        else:
                                                                                                                                                                                                            if IP == 'E06 13':
                                                                                                                                                                                                                typingPrint('''IP = 81.154.114.248
ISP = BT
Country = UK''')

                                                                                                                                                                                                            else:
                                                                                                                                                                                                                if IP == 'iSpectate1768':
                                                                                                                                                                                                                    typingPrint('''IP = 90.205.64.77
ISP = Sky
Country = UK''')

                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    if IP == 'Kieran2gud':
                                                                                                                                                                                                                        typingPrint('''IP = 86.185.32.183
ISP = BT
Country = UK''')

                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        if IP == 'UnwornMarrow325':
                                                                                                                                                                                                                            typingPrint('''IP = 86.6.145.207
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            if IP == 'I cant kill6087':
                                                                                                                                                                                                                                typingPrint('''STOP! Resolving this person is banned and your IP has subsequently been logged.''')

                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                if IP == 'Timeguide638795':
                                                                                                                                                                                                                                    typingPrint('''STOP! Resolving this person is banned and your IP has subsequently been logged.''')

                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                    if IP == 'Cruzian Chika':
                                                                                                                                                                                                                                        typingPrint('''IP = Cruzian Chika
ISP = Comcast Cable Communications, LLC
Country = USA''')

                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                        if IP == 'Fatneek774':
                                                                                                                                                                                                                                            typingPrint('''IP = 86.13.91.53
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                            if IP == 'IDRAGXNFLYI':
                                                                                                                                                                                                                                                typingPrint('''IP = 86.153.247.4
ISP = BT
Country = UK/Scotland''')

                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                if IP == 'PDE4L':
                                                                                                                                                                                                                                                    typingPrint('''IP = 97.106.73.187
ISP = Charter Communications Inc
Country = USA''')

                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                    if IP == 'Seuxy':
                                                                                                                                                                                                                                                        typingPrint('''IP = 213.64.57.253
ISP = Telia Company AB
Country = Sweden''')

                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                        if IP == 'txics':
                                                                                                                                                                                                                                                            typingPrint('''IP = 73.172.226.87
ISP = Comcast Cable Communications
Country = USA''')

                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                            if IP == 'vPROXv':
                                                                                                                                                                                                                                                                        typingPrint('''IP = 68.147.240.9
ISP = Shaw Communications Inc.
Country = Canada
Region = Alberta
City = Calgary
Currency = Canadian Dollar
Connection type = Cable/DSL''')

                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                if IP == 'dancing wretch':
                                                                                                                                                                                                                                                                    typingPrint('''IP = 107.220.210.241
ISP = AT&T Services, Inc.
Country = USA''')

                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                    if IP == 'Rixvty':
                                                                                                                                                                                                                                                                        typingPrint('''IP = 5.68.200.170
ISP = Sky
Country = UK''')

                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                        if IP == 'Allxuh':
                                                                                                                                                                                                                                                                            typingPrint('''IP = 189.160.185.34
ISP = Uninet S.A. de C.V
Country = Mexico''')

                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                            if IP == 'CoinPenguin8639':
                                                                                                                                                                                                                                                                                typingPrint('''IP = 94.15.161.18
ISP = Sky
Country = UK''')

                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                if IP == 'Defcon1122':
                                                                                                                                                                                                                                                                                    typingPrint('''Country = UK
County = Derbyshire
Town = Dronfield
Address = 3 Cecil Rd, Dronfield S18 2GW
Post code = S18 2GW
Coordinates = 53.305168510670974, -1.4694284241390239
Currency = GBP''')

                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                    if IP == 'IIIlIIlIIlI9221':
                                                                                                                                                                                                                                                                                        typingPrint('''IP = 86.13.88.156
ISP = Virgin
Country = UK
County = Derbyshire
Town = dronfield
address = 69-71 Holmesdale Rd, Dronfield S18 2FA
Post code = S18 2FA
coordinates = 53.30674319087971, -1.4575017285546672
Currency = GBP
Connection type = Cable/DSL
Name = John Plummer
Date of birth = 2007
Email address = Jp12340987565@gmail.com
Facebook = John Plummer
Instagram = johnplum420
Phone number: +44 7480 772003''')

                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                        if IP == 'MissBlxssed':
                                                                                                                                                                                                                                                                                            typingPrint('''IP = 2.121.148.244
ISP = Sky
Country = UK''')

                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                            if IP == 'IRONFIST2042':
                                                                                                                                                                                                                                                                                                typingPrint('''IP = 94.195.227.21
ISP = Sky
Country = UK''')

                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                if IP == 'ron boxed u':
                                                                                                                                                                                                                                                                                                    typingPrint('''IP = 82.46.205.211
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                    if IP == 'IRONHAND9577':
                                                                                                                                                                                                                                                                                                        typingPrint('''IP = 94.195.227.21
ISP = Sky
Country = UK''')

                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                        if IP == 'RXGEZZ':
                                                                                                                                                                                                                                                                                                            typingPrint('''IP = 80.7.13.242
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                            if IP == 'ItsJustJames888':
                                                                                                                                                                                                                                                                                                                typingPrint('''IP = 86.19.205.253
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                if IP == 'FocalCheese5464':
                                                                                                                                                                                                                                                                                                                    typingPrint('''IP = 92.14.194.153
ISP = TalkTalk
Country = UK''')

                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                    if IP == 'End3r M4n':
                                                                                                                                                                                                                                                                                                                        typingPrint('''IP = 109.156.246.190
ISP = BT
Country = UK''')

                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                        if IP == 'XxBlueSwapxX':
                                                                                                                                                                                                                                                                                                                            typingPrint('''Country = UK
County = Derbyshire
Town = Dronfield
Address = 3 Cecil Rd, Dronfield S18 2GW
Post code = S18 2GW
Coordinates = 53.305168510670974, -1.4694284241390239
Currency = GBP''')

                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                            if IP == 'l Jinyx l':
                                                                                                                                                                                                                                                                                                                                typingPrint('''IP = 97.82.66.119
ISP = Charter Communications
Country = USA''')

                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                if IP == 'REDNECK2589':
                                                                                                                                                                                                                                                                                                                                    typingPrint('''IP = 68.191.107.102
ISP = Charter Communications
Country = USA
State = Alabama
District = Morgan
City = Decatur
Coordinates = 34.60173226806904, -86.98184180048416
Connection type = Corperate
Currency = USD
Name = Jason Heflin''')

                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                    if IP == 'ExprdLactaid':
                                                                                                                                                                                                                                                                                                                                        typingPrint('''IP = 71.195.182.144
ISP = Comcast Cable Communications, LLC
Country = USA''')

                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                        if IP == 'aflopcea':
                                                                                                                                                                                                                                                                                                                                            typingPrint('''IP = 88.106.202.28
ISP = TalkTalk
Country = UK/Scotland''')

                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                            if IP == 'ITZ 1BBY':
                                                                                                                                                                                                                                                                                                                                                typingPrint('''IP = 82.31.29.63
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                if IP == 'LucidxKiller346':
                                                                                                                                                                                                                                                                                                                                                    typingPrint('''IP = 74.83.201.125
ISP = Fuse Internet Access
Country = USA''')

                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                    if IP == 'Monroy7':
                                                                                                                                                                                                                                                                                                                                                        typingPrint('''IP = 108.18.96.50
ISP = Verizon Communications
Country = USA''')

                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                        if IP == 'Nitrix Warlord':
                                                                                                                                                                                                                                                                                                                                                            typingPrint('''IP = 67.170.161.60
ISP = Comcast Cable Communications, LLC
Country = USA
State = Oregon
District = Multnomah
City = Troutdale
Coordinates = 45.528828217770915, -122.3980663083856
Connection type = Cable/DSL
Currency = USD
ASN = AS7922 - Comcast Cable Communications, LLC
Timezone = America/Los_Angeles
''')

                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                            if IP == 'dekk98':
                                                                                                                                                                                                                                                                                                                                                                typingPrint('''IP = 96.46.94.48
ISP = The Junction Internet, LLC
Country = USA''')

                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                if IP == 'O P P X V':
                                                                                                                                                                                                                                                                                                                                                                    typingPrint('''IP = 50.207.104.66
ISP = Comcast Cable Communications, LLC
Country = USA
State = Minnesota
District = Hennepin
City = New Hope
Coordinates = 45.03373000456205, -93.38729712737707
Connection type = Cable/DSL
Currency = USD
ASN = AS7922 - Comcast Cable Communications, LLC
Timezone = America/Chicago
Youtube = OPPXV
Tiktok = Oppxv''')

                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                    if IP == 'Whisperbeau':
                                                                                                                                                                                                                                                                                                                                                                        typingPrint('''IP = 80.3.95.97
ISP = Virgin
Country = UK''')

                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                        if IP == 'D4NSTRK07':
                                                                                                                                                                                                                                                                                                                                                                            typingPrint('''IP = 90.196.154.186
ISP = Sky
Country = UK''')
                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                            typingPrint("sorry target not found please run the script again")
time.sleep(7)

                                                                                                            
                                                                                                    