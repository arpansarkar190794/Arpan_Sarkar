D1={'User':'Arpan','Password':1234}
Username = input("Enter your Username: ")
Password = input("Enter your password: ")
while Username != 'Arpan' and Password != 1234:
    print('Invalid Username and Password')
    break
else:
    if Username== D1['User'] and D1['Password']== 1234:
        print('Login Succesful')



