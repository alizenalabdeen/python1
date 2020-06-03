triesnumber = 0
while triesnumber != 2:
    usrnm= input('enter your name: ')
    if usrnm == 'ali':
        print('good gob')
        triesnumber = 0
        exit()
    else:
        print ('bad job')
        triesnumber +=1 
        print ('you have' + str(2 - triesnumber) + 'tries')