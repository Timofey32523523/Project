#coding=1251
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import webbrowser

def get_recipes():
    products = products_entry.get()
    products_list = products.split(',')
    query = '������+��+' + '+'.join(products_list)
    
    url = f'https://www.google.com/search?q={query}'

    response = requests.get(url)    

    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = soup.find_all('a')
    
    recipe_links = []
    for link in results:
        href = link.get('href')
        if href.startswith('/url?q='):
            recipe_links.append(href[7:])  # ������� "/url?q=" �� ������ ������
    
    if recipe_links:
        recipes_text.delete(1.0, tk.END)
        for i in range(min(5, len(recipe_links))):
            recipe_link = recipe_links[i]
            recipes_text.insert(tk.END, f'������ {i+1}:\n')
            recipes_text.insert(tk.END, recipe_link, f'link_{i+1}')
            recipes_text.tag_bind(f'link_{i+1}', '<Button-1>', lambda e, link=recipe_link: webbrowser.open(link))
            recipes_text.insert(tk.END, '\n\n')
    else:
        recipes_text.insert(tk.END, "�� �������")


root = tk.Tk()
root.title("Interactive Cookbook")

products_label = tk.Label(root, text="������� ���� ��������")
products_label.pack()
products_entry = tk.Entry(root)
products_entry.pack()

get_recipes_button = tk.Button(root, text="�������� �������", command=get_recipes)
get_recipes_button.pack()

recipes_text = tk.Text(root, width=50, height=20)
recipes_text.pack()

root.mainloop()