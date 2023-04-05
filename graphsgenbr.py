import matplotlib.pyplot as plt

def generate_graph(operation, result, num1, num2, root):
    if operation == 'addition':
        x = ['primeiro número', 'segundo número', 'resultado']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('resultado da adição')
        ax.set_xlabel('valores')
        ax.set_ylabel('soma')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
    
    if operation == 'subtraction':
        x = ['primeiro número', 'segundo número', 'resultado']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('resultado da subtração')
        ax.set_xlabel('valores')
        ax.set_ylabel('subtração')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
        
    if operation == 'multiplication':
        x = ['primeiro número', 'segundo número', 'resultado']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('resultado da multiplicação')
        ax.set_xlabel('valores')
        ax.set_ylabel('multiplicação')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()

    if operation == 'division':
        x = ['primeiro número', 'segundo número', 'resultado']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('resultado da divisão')
        ax.set_xlabel('valores')
        ax.set_ylabel('divisão')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()

    if operation == 'exponentiation':
        x = ['primeiro número', 'segundo número', 'resultado']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('resultado da potenciação')
        ax.set_xlabel('valores')
        ax.set_ylabel('potência')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
    
    if operation == 'percentage':
        x = ['primeiro número', 'segundo número', 'resultado']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('resultado da porcentagem')
        ax.set_xlabel('valores')
        ax.set_ylabel('porcentagem')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
        
    if operation == 'modulus':
        x = ['primeiro número', 'segundo número', 'resultado']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('resultado do resto')
        ax.set_xlabel('valores')
        ax.set_ylabel('resto')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
    
    