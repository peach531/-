def Login(id,password):
    if id == 'Cube' and password == 1234:
        return 1
    elif id == 'Cube':
        return 2
    elif password == 1234:
        return 3
    else :
        return 4

def Say(a):
    if a == 1:
        return 'Login Success.'
    if a == 2:
        return 'Please check your PW.'
    if a == 3:
        return 'Please check your ID.'
    if a == 4:
        return 'please check your ID and PW.'

id = input('ID :')
password = input('PW: ')
a = Login(id,password)
print(Say(a))
