from tkinter.constants import N
import requests
import base64
import tkinter
from tkinter import messagebox

def message(x):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo('Test', x)

class Request:

    def peticion(url):
        r = requests.get(url, verify=False)
        json_code = r.json()
        flag = json_code['data']
        return flag

    def decrypt(flag):
        flag_bytes = base64.b64decode(flag)
        flag_decode = flag_bytes.decode('ascii')
        message(flag_decode)

Request.decrypt(Request.peticion('URL'))



