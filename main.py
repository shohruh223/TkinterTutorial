from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
import json

# colors
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#EB5D51"  # red

window = Tk()
window.geometry('300x320')
window.title('Converter')
window.configure(bg=cor0)
window.resizable(height=FALSE, width=FALSE)

# frames
top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

# https://rapidapi.com
# ushbu sayt kirganingizdan Currency Converter deb search berasiz
# chap tomondagi Convert bo'limiga o'tasiz
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'KZT':
        symbol = '₸'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'UZS':
        symbol = 'лв'

    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "28d0d114c8msh5b9ad1427ffbd16p1c86a9jsn15d5cd9c4ddc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result['text'] = formatted

    print(converted_amount, formatted)


# top frame

icon = Image.open('icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=5, padx=13, pady=30, anchor=CENTER,
                 font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_name.place(x=0, y=0)

# main frame
result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=cor0,
               fg=cor1)
result.place(x=50, y=10)

currency = ['KZT', 'UZS', 'EUR', 'USD']

from_label = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),
                   bg=cor0, fg=cor1)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),
                 bg=cor0, fg=cor1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=155)

button = Button(main, text="Converter", width=19, padx=5, height=1, bg=cor2, fg=cor0, font=("Ivy 12 bold"),
                command=convert)
button.place(x=50, y=210)

window.mainloop()