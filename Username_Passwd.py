User={'Mrudula':'Mrudula123','Arpan':'Arpan123','Diganta':'Diganta123','Aliyas':'Aliyas123'}
print ("Enter your Username" )
Username= input()
print ("Enter your Password" )
Password= input()
if Username== 'Mrudula' and Password== User['Mrudula']:
    print('Your Login is Succesfull')
elif Username == 'Arpan' and Password == User['Arpan']:
        print('Your Login is Succesfull')
elif Username == 'Diganta' and Password == User['Diganta']:
            print('Your Login is Succesfull')
elif Username == 'Aliyas' and Password == User['Aliyas']:
                print('Your Login is Succesfull')
elif Username == 'Mrudula' and Password != User['Mrudula']:
                print('Incorrect Password')
elif Username == 'Arpan' and Password != User['Arpan']:
                print('Incorrect Password')
elif Username == 'Diganta' and Password != User['Diganta']:
             print('Incorrect Password')
elif Username == 'Aliyas' and Password != User['Aliyas']:
            print('Incorrect Password')
elif Username != 'Mrudula' and Password == User['Mrudula']:
                print('Incorrect Username')
elif Username != 'Arpan' and Password == User['Arpan']:
                print('Incorrect Username')
elif Username != 'Diganta' and Password == User['Diganta']:
             print('Incorrect Username')
elif Username != 'Aliyas' and Password == User['Aliyas']:
            print('Incorrect Username')
else:
    print('Invalid Credentials')