from cryptography.fernet import Fernet

'''
def write_key():
    key=fernet.generate_key()
    with open ("key.key","wb")as key_file:
        key_file.write(key)'''

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

key=load_key()
fer=Fernet(key)


def view():
    with open('pwds.text','r')as f:
        for line in f.readlines():
            data=(line.rstrip())
            user,pssw=data.split("|")
            print("User : ",user, "| Password : ",fer.decrypt(pssw.encode()).decode())


def add():
    name = (input("enter account number : "))
    pwd=(input("enter password : "))

    with open("pwds.text","a")as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode=input("add a password or view a password : (view/add) or press q to quit : ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("you have entered a wrong mode !!")