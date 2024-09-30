import random
import tkinter as tk

def gerar_informacoes_corredores():
    corredores = ['Corredor 1', 'Corredor 2', 'Corredor 3', 'Corredor 4']
    temperaturas = gerar_temperaturas_aleatorias()
    distancias = gerar_distancias_aleatorias_m()
    niveis_bateria = gerar_niveis_bateria_aleatorios()
    return corredores, distancias, temperaturas, niveis_bateria

def gerar_temperaturas_aleatorias(num_temperaturas=4):
    return [random.uniform(1, 100) for _ in range(num_temperaturas)]

def gerar_distancias_aleatorias_m(num_distancias=4):
    return [random.uniform(0, 100) for _ in range(num_distancias)]

def gerar_niveis_bateria_aleatorios(num_niveis=4):
    return [random.uniform(0, 100) for _ in range(num_niveis)]

def atualizar_info():
    corredores, distancias, temperaturas, niveis_bateria = gerar_informacoes_corredores()
    posicoes = sorted(zip(corredores, distancias), key=lambda x: x[1], reverse=True)
    
    info_text = ""
    for i, (corredor, distancia) in enumerate(posicoes):
        info_text += f'{corredor} (Posição {i + 1}):\n'
        if i != 0:
            info_text += f'  Distância: {distancia:.2f} m\n'
        info_text += f'  Temperatura: {temperaturas[corredores.index(corredor)]:.2f}°C\n'
        info_text += f'  Nível de Bateria: {niveis_bateria[corredores.index(corredor)]:.2f}%\n\n'

    info_label.config(text=info_text)
    root.after(5000, atualizar_info)

root = tk.Tk()
root.title("Informações dos Corredores da Fórmula E")
root.geometry("500x400")
root.configure(bg='#2E2E2E')

info_label = tk.Label(root, text="", justify="left", padx=10, pady=10, bg='#2E2E2E', fg='white', font=('Helvetica', 12))
info_label.pack(expand=True, fill="both")

atualizar_info()
root.mainloop()
