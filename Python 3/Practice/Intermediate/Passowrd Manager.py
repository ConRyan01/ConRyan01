master_pwd = input('what is the master password? ')


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split ("|")
            print(f'user: {user}. password: {passw}.')

def add():
    name = input ('Account Name: ')
    pwd = input ('password: ')

    with open('passwords.txt', 'a') as f:
        f.write(f'{name} | {pwd}\n')

while True:
    mode = input('would you like to add a new password or view existing passwords (view, add)? ').lower()
    if mode == 'q':
        break
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()