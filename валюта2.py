from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint


def update_currency_label1(event):
    code1 = combobox1.get()
    name1 = currencies[code1]
    currency_label1.config(text=name1)

def update_currency_label2(event):
    code2 = combobox2.get()
    name2 = currencies[code2]
    currency_label2.config(text=name2)

def update_currency_label3(event):
    code3 = combobox3.get()
    name3 = currencies[code3]
    currency_label3.config(text=name3)

def exchange():
    code1 = combobox1.get()
    code2 = combobox2.get()
    code3 = combobox3.get()
    if code3:
        try:
            response1 = requests.get('https://open.er-api.com/v6/latest/USD')
            response1.raise_for_status()
            response2 = requests.get('https://open.er-api.com/v6/latest/USD')
            response2.raise_for_status()
            response3 = requests.get('https://open.er-api.com/v6/latest/USD')
            response3.raise_for_status()
            data1 = response1.json()
            data2 = response2.json()
            data3 = response3.json()
            if code1 in data1['rates'] and code2 in data2['rates'] and code3 in data3['rates']:
                exchange_rate1 = data1['rates'][code1]/data3['rates'][code3]
                exchange_rate2 = data2['rates'][code2]/data3['rates'][code3]
                currency_name1 = currencies[code1]
                currency_name2 = currencies[code2]
                mb.showinfo('Курс обмена', f'Курс валют: {exchange_rate1:.4f} {code1} за 1 {code3},\n {exchange_rate2:.4f} {code2} за 1 {code3}')
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
root.title('Курс обмена валют')
root.geometry('360x350')

l1 = Label(root, text='Базовая валюта').pack(pady=10, padx=10)
popular_currencies = ['USD', 'EUR', 'RUB', 'JPY', 'GBP', 'AUD',
                      'CAD', 'CHF', 'CNY', 'KZT', 'UZS']
combobox1 = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox1.pack(pady=10, padx=10)
combobox1.bind('<<ComboboxSelected>>', update_currency_label1)

currency_label1 = ttk.Label(root)
currency_label1.pack()

l2 = Label(root, text='Вторая базовая валюта').pack(pady=10, padx=10)
popular_currencies = ['USD', 'EUR', 'RUB', 'JPY', 'GBP', 'AUD',
                      'CAD', 'CHF', 'CNY', 'KZT', 'UZS']
combobox2 = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox2.pack(pady=10, padx=10)
combobox2.bind('<<ComboboxSelected>>', update_currency_label2)

currency_label2 = ttk.Label(root)
currency_label2.pack()

l3 = Label(root, text='Целевая валюта').pack(pady=10, padx=10)
popular_currencies = ['USD', 'EUR', 'RUB', 'JPY', 'GBP', 'AUD',
                      'CAD', 'CHF', 'CNY', 'KZT', 'UZS']
combobox3 = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox3.pack(pady=10, padx=10)
combobox3.bind('<<ComboboxSelected>>', update_currency_label3)

currency_label3 = ttk.Label(root)
currency_label3.pack()

Button(text='Получить курс обмена',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()
