"""
================================================================================
Script para Remover Fundo Branco de uma Imagem e Torná-lo Transparente

Descrição:
    Este script processa uma imagem e remove todos os pixels brancos, tornando-os transparentes.
    O objetivo é facilitar a manipulação de imagens em projetos onde o fundo branco pode interferir.

Como funciona:
    - O usuário seleciona a imagem via janela de upload.
    - O script processa a imagem, removendo os pixels brancos.
    - Salva a imagem modificada no formato PNG para preservar a transparência.

Dependências:
    - Python 3.x
    - Pillow (PIL)
    - NumPy
    - Tkinter (nativo do Python)
    - tqdm (para a barra de progresso)

Criado por: Guilherme Vieira de Stéfani
Data de criação: 20/02/2025
Versão: 1.1
================================================================================
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np
import os
from tqdm import tqdm 

def remove_white_background(input_path):
    """Processa a imagem para remover o fundo branco e salva com transparência."""
    
    # Carregar a imagem
    img = Image.open(input_path).convert("RGBA")
    
    # Converter a imagem para um array NumPy
    img_array = np.array(img)
    
    # Definir o limite para considerar um pixel como branco
    threshold = 200  # Ajuste conforme necessário
    
    # Criar a barra de progresso
    print("\nProcessando a imagem...\n")
    for i in tqdm(range(img_array.shape[0]), desc="Removendo fundo", unit="linhas"):
        white_mask = (img_array[i, :, 0] > threshold) & \
                     (img_array[i, :, 1] > threshold) & \
                     (img_array[i, :, 2] > threshold)
        img_array[i, white_mask, 3] = 0  # Define a transparência para pixels brancos
    
    # Criar uma nova imagem com a modificação
    img_transparent = Image.fromarray(img_array)
    
    # Criar o nome do arquivo de saída automaticamente
    file_dir, file_name = os.path.split(input_path)  # Separa caminho e nome do arquivo
    name, ext = os.path.splitext(file_name)  # Separa nome e extensão
    output_path = os.path.join(file_dir, f"{name}_transparencia.png")  # Novo nome

    # Salvar a imagem processada
    img_transparent.save(output_path, format="PNG")

    print(f"\nImagem salva como: {output_path}")

    # Abrir automaticamente o arquivo no visualizador padrão
    os.startfile(output_path)

def selecionar_arquivo():
    """Abre uma janela para o usuário selecionar um arquivo de imagem."""
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    
    file_path = filedialog.askopenfilename(
        title="Selecione a imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    if file_path:
        remove_white_background(file_path)

# Executa a função de seleção de arquivo ao rodar o script
selecionar_arquivo()
