from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint

def update_base_label1(event):
    code = base_combobox1.get()
    name = currencies[code]
    base_currency_label1.config(text=name)

def update_base_label2(event):
    code = base_combobox2.get()
    name = currencies[code]
    base_currency_label2.config(text=name)

def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_currency_label.config(text=name)

def exchange():
    target_code = target_combobox.get().strip()
    base1_code = base_combobox1.get().strip()
    base2_code = base_combobox2.get().strip()
    if target_code and base1_code and base2_code:
        try:
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{base1_code}')
            response1.raise_for_status()
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')
            response2.raise_for_status()
            data1 = response1.json()
            data2 = response2.json()
            if target_code in data1['rates'] and data2['rates']:
                exchange_rate1 = data1['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                base1 = currencies[base1_code]
                base2 = currencies[base2_code]
                target = currencies[target_code]
                mb.showinfo('Курс обмена', f'Курс : {exchange_rate1:.2f} {target} за 1 {base1},\n {exchange_rate2:.2f} {target} за 1 {base2}')
            else:
                mb.showerror('Ошибка', f'Валюта не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)
    else:
        mb.showwarning('Внимание', 'Введите код валюты')


currencies = {
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'RUB': 'Рубли',
    'JPY': 'Японская иена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'}



root = Tk()
root.configure(bg='lightblue')
root.title('Курс обмена валют')
root.geometry('360x350')

Label(root, text='Базовая валюта', bg='purple1').pack(pady=10, padx=10)
base_combobox1 = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox1.pack(pady=10, padx=10)
base_combobox1.bind('<<ComboboxSelected>>', update_base_label1)
base_currency_label1 = ttk.Label(root)
base_currency_label1.pack()

Label(root, text='Вторая базовая валюта', bg='purple1').pack(pady=10, padx=10)
base_combobox2 = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox2.pack(pady=10, padx=10)
base_combobox2.bind('<<ComboboxSelected>>', update_base_label2)
base_currency_label2 = ttk.Label(root)
base_currency_label2.pack()

Label(root, text='Целевая валюта', bg='purple1').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=10, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_currency_label = ttk.Label(root)
target_currency_label.pack()

Button(text='Получить курс обмена', bg='blue', font="bold",
       command=exchange).pack(pady=10, padx=10)


root.mainloop()
