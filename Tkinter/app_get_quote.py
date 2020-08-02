import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from random import shuffle
import requests

root = tk.Tk()
root.title('Цитата дня')

def generate_quote(*args):
    response = requests.get('https://ru.citaty.net/')
    html_data = BeautifulSoup(response.text)
    quotes = html_data.find_all(class_='blockquote')

    quotes_of_the_day = []
    for quote in quotes:        
        quotes_of_the_day.append(quote.find().get_text())
    shuffle(quotes_of_the_day)
    label_quote.set(quotes_of_the_day[1])


label_quote = tk.StringVar(value='Тут будет цитата')

label_frame = ttk.Frame(root, padding=(20,20,10,10))
label_frame.grid(row=0, column=0)

button_frame = ttk.Frame(root, padding=(20, 20, 10, 10))
button_frame.grid()

label_name_quote = ttk.Label(label_frame, text='Цитата дня: ')
label_name_quote.grid()

label_quote_display = ttk.Label(label_frame, textvariable=label_quote)
label_quote_display.grid(row=0, column=1)

button_random_quote = ttk.Button(button_frame, text='Generate quote', command=generate_quote)
button_random_quote.grid(pady=20)

root.mainloop()
