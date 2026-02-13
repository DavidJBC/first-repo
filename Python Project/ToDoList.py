import time

#list of preset tasks
tasks = ['study', 'game']

#Function to add tasks
def Add():
    ResponseAdd = input('What task do you want to add? ')
    tasks.append(ResponseAdd)
    print('adding ' + ResponseAdd + '....')
    time.sleep(1)
    print(ResponseAdd + ' has been added')
    time.sleep(1)

#Function to remove tasks
def Remove():
    ResponseRemove = input('What task do you want to remove? ')
    tasks.remove(ResponseRemove)
    print('removing ' + ResponseRemove + '....')
    time.sleep(1)
    print(ResponseRemove + ' has been removed')
    time.sleep(1)

#Keeps the program running until the user choose to end it
while True:
    print('What do you want to do?')
    print('1.) View tasks\n2.) Add a tasks\n3.) Remove a tasks\n4.) Exit the program')
    response = input(":")

    if response == '1': #makes the user view the current tasks
        print(tasks)
        time.sleep(1.89)
    elif response == '2':
        Add()
    elif response == '3':
        Remove()
    elif response =='4':
        print('Exiting the program....')
        time.sleep(1.5)
        print('Program ended')
        break





    