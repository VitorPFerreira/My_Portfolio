import tkinter as tk
from sql import *
from main import *
from tkinter import *

cor01 = "#F0FFFF"
cor02 = "#FFFFFF"
cor03 = "#FF0000"
cor04 = "#000000"
cor05 = "#6d706e"
cor06 = "#4284f5"

def submitact():
    user = Username.get()
    passw = password.get()
    logintodb(user, passw)


def logintodb(user, passw):
    if passw:
        db = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='01020304',
                                     database='autopecasbd', )
        cursor = db.cursor()

    else:
        db = mysql.connector.connect(host="localhost",
                                     user='user',
                                     database='autopecasbd')
        cursor = db.cursor()
    savequery = mostrar()
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")
    except:
        db.rollback()
        print("Error occured")


root = tk.Tk()
root.geometry("900x600")
root.resizable(width=False, height=False)
root.title("Login")
BannerBemvindo = tk.Label(root, text="Bem-vindo à Auto Peças BD", font=30)
BannerBemvindo.place(x=200, y=10)
lblfrstrow = tk.Label(root, text="Código de Usuário", font=30)
lblfrstrow.place(x=200, y=60)
Username = tk.Entry(root, width=35)
Username.place(x=200, y=90, width=200)
lblsecrow = tk.Label(root, text="Senha", font=30)
lblsecrow.place(x=200, y=120)
password = tk.Entry(root, width=200)
password.place(x=200, y=150, width=200)
submitbtn = tk.Button(root, pady=10, text="Login", bg=cor06, font=30, command=submitact)
submitbtn.place(x=220, y=190, width=150)
root.mainloop()
