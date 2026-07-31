#atm machine

menu = input(""" 
Hi ! how can i help you .
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for Withdrawl
4. Enter 4 for exit
""")

if menu == '1':
    print('pin change')
elif menu == '2':
    print('balance update')
elif menu == '3':
    print('withdrawl')
else :
    print('exit')