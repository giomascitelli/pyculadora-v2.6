import tkinter as tk
import math
import random
from graphsgenbr import generate_graph # Importar o gerador de gráficos com matplotlib
from numinfobr import * # Importar as informações sobre os números que são usadas nos resultados das operações
from tkinter import ttk
from PIL import Image, ImageTk



# Função da operação fatorial
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

# Função da sequência de Fibonacci
def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


# Definindo as funções das operações que ocorrerão após o clique do botão correspondente

# Função do botão de adição
def option1():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} + {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('addition', result, num1, num2, root)
    
# Função do botão de subtração    
def option2():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} - {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('subtraction', result, num1, num2, root)
    
# Função do botão de multiplicação    
def option3():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} * {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('multiplication', result, num1, num2, root)

# Função do botão de divisão    
def option4():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 / num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} / {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('division', result, num1, num2, root)

# Função do botão de potenciação   
def option5():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1**num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1} ^ {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('exponentiation', result, num1, num2, root)
        
# Função do botão de raiz quadrada
def option6():
    num1 = float(entry1.get())
    result = math.sqrt(num1)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\na raiz quadrada de ({num1}) = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')    
    
# Função do botão de porcentagem
def option7():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = (num1 * num2) / 100
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num2}% de {num1} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled') 
    generate_graph('percentage', result, num1, num2, root)

# Função do botão de resto de divisão
def option8():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 % num2
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\no resto da divisão {num1} / {num2} = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    generate_graph('modulus', result, num1, num2, root)
 
# Função do botão da sequência de Fibonacci
def option9():
    num1 = int(entry1.get())
    result = fibonacci(num1)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\na sequência de fibonacci com o número {num1} como limite = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')
    
# Função do botão da operação fatorial   
def option10():
    num1 = int(entry1.get())
    result = factorial(num1)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{num1}! = {result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')

     
# Função do botão de gerar um número aleatório
def option11():
    result = random.randint(0, 500)
    even_odd_info = evenOdd(result)
    prime_comp_info = isPrime(result)
    divisible_info = divisible(result)
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('end', f"\n{result}" + even_odd_info + prime_comp_info + divisible_info, "center")
    text.config(state='disabled')



# Interface gráfica da pyculadora
root = tk.Tk()
root.title("pyculadora")
root.geometry("500x535")
root.config(bg="#E6E6E6")
root.resizable(False, False)

frame = tk.Frame(root)
frame.grid(row=8, column=0, padx=20, pady=10, sticky="ew")

# Carregar imagem
image = Image.open("pyculadora\logobr.png")
image = image.resize((330, 80), Image.Resampling.LANCZOS)  # Redimensão da imagem
photo = ImageTk.PhotoImage(image)

# Criação de uma label para alocar a imagem
image_label = tk.Label(root, image=photo, bg="#E6E6E6")
image_label.image = photo 
image_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Criação das labels principais
label1 = tk.Label(root, text="", bg="#E6E6E6")
label1.grid(row=0, column=0, columnspan=4, padx=20, pady=(70,10))

# Criação das funções de texto placeholder nos campos de entrada
def on_entry_click(event):
    """Função para lidar com o evento do clique do mouse"""
    widget = event.widget
    if widget.get() == 'primeiro número' or widget.get() == 'segundo número':
        widget.delete(0, "end")
        widget.config(fg='black')

def on_focus_out(event):
    """Função para lidar quando o usuário clica fora da caixa de input"""
    widget = event.widget
    if widget.get() == '':
        widget.insert(0, 'primeiro número' if widget == entry1 else 'segundo número')
        widget.config(fg='gray')

# Criação dos campos de entrada do usuário
entry1 = tk.Entry(root, fg='gray')
entry1.insert(0, 'primeiro número')
entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focus_out)
entry1.grid(row=1, column=0, columnspan=4, padx=20, pady=5)

entry2 = tk.Entry(root, fg='gray')
entry2.insert(0, 'segundo número')
entry2.bind("<FocusIn>", on_entry_click)
entry2.bind("<FocusOut>", on_focus_out)
entry2.grid(row=2, column=0, columnspan=4, padx=20, pady=5)


# Criação dos botões que realizam as operações
button1 = tk.Button(root, text="adição", command=option1, bg="#F2F2F2", width=10)
button1.grid(row=3, column=0, padx=20, pady=10)

button2 = tk.Button(root, text="subtração", command=option2, bg="#F2F2F2", width=10)
button2.grid(row=3, column=1, padx=20, pady=10)

button3 = tk.Button(root, text="multiplicação", command=option3, bg="#F2F2F2", width=10)
button3.grid(row=3, column=2, padx=20, pady=10)

button4 = tk.Button(root, text="divisão", command=option4, bg="#F2F2F2", width=10)
button4.grid(row=3, column=3, padx=20, pady=10)

button5 = tk.Button(root, text="potência", command=option5, bg="#F2F2F2", width=10)
button5.grid(row=4, column=0, padx=20, pady=10)

button6 = tk.Button(root, text="raiz quadrada", command=option6, bg="#F2F2F2", width=10)
button6.grid(row=4, column=1, padx=20, pady=10)

button7 = tk.Button(root, text="porcentagem", command=option7, bg="#F2F2F2", width=10)
button7.grid(row=4, column=2, padx=20, pady=10)

button8 = tk.Button(root, text="resto", command=option8, bg="#F2F2F2", width=10)
button8.grid(row=4, column=3, padx=20, pady=10)

button9 = tk.Button(root, text="fibonacci", command=option9, bg="#F2F2F2", width=10)
button9.grid(row=5, column=1, padx=20, pady=10)

button10 = tk.Button(root, text="fatorial", command=option10, bg="#F2F2F2", width=10)
button10.grid(row=5, column=2, padx=20, pady=10)

button11 = tk.Button(root, text="número aleatório", command=option11, bg="#F2F2F2", width=15)
button11.grid(row=6, column=0, padx=20, pady=10, sticky="ew", columnspan=4)


# Criação da área que exibe o resultado e as informações dele
text = tk.Text(root, height=10, wrap='word',state='disabled', bg='#dedede')
text.grid(row=9, column=0, sticky="nsew", columnspan=4)

# Criação da barra de scroll
vsb = ttk.Scrollbar(root, orient="vertical", command=text.yview)
vsb.grid(row=9, column=4, sticky="ns")

text.configure(width=50, yscrollcommand=vsb.set)

text.tag_configure("center", justify="center") # Centralizar o texto

text.bind_all("<MouseWheel>", lambda event: text.yview_scroll(-1 * int(event.delta/120), "units")) # Permitir que o usuário utilize a roda do mouse para utilizar a barra de scroll

# Loop principal da interface gráfica
root.mainloop()

