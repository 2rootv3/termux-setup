import os

banner1 = '''
 #####                                     #####  
#     # #####   ####   ####  ##### #    # #     # 
      # #    # #    # #    #   #   #    #       # 
 #####  #    # #    # #    #   #   #    #  #####  
#       #####  #    # #    #   #   #    #       # 
#       #   #  #    # #    #   #    #  #  #     # 
####### #    #  ####   ####    #     ##    ##### 
                                                                                                                                               '''
banner2='''                                                                                                  
e   e eeeee eeeee eeeee eeeee eeee    e    e eeeee e   e    eeeee e    e eeeee eeeee eeee eeeeeee 
8   8 8   8 8   8 8   8   8   8       8    8 8  88 8   8    8   " 8    8 8   "   8   8    8  8  8 
8e  8 8eee8 8e  8 8eee8   8e  8eee    8eeee8 8   8 8e  8    8eeee 8eeee8 8eeee   8e  8eee 8e 8  8 
88  8 88    88  8 88  8   88  88        88   8   8 88  8       88   88      88   88  88   88 8  8 
88ee8 88    88ee8 88  8   88  88ee      88   8eee8 88ee8    8ee88   88   8ee88   88  88ee 88 8  8 
                                                                                                  '''

os.system('clear')
print(banner1)
#start program
print("1)update termux")
print("2)exit")
user = int(input("==>"))
if user == 1:
    print(banner2)
    os.system('pkg update -y')
    os.system('pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install python-pip -y')
    os.system('pkg install wget -y')
    os.system('pkg install fish -y')
    os.system('pkg install git -y')
    os.system('pkg install nmap -y')
    os.system('pkg install bash -y')
    os.system('pkg install nano -y')
    os.system('pkg install figlet -y')
    os.system('pkg install tor -y')
    os.system('pkg install openssl -y')
    os.system('pkg install openssl-tool -y')
    os.system('pkg install toilet -y')
    os.system('pkg install net-tools -y')
    os.system('pkg install goaccess -y')
    os.system('pkg install golang -y')
    os.system('pkg install tar -y')
    os.system('pip install requests ')
    os.system('pip install termcolor')
elif user==2:
    os.system('exit')
    print('exit the program.........')
print("Thanks for using thi's tools")
