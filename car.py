run = True
while run:
    commend = input('> ')
    print(f' you said {commend}')
    if commend == 'help':
        print('to start the car press s')
    if commend == 's':
        print('car started')
    if commend == 'q':
        print('car stoped')
        run = False