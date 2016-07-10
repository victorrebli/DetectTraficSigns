# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

# o codigo abaixo é responsável por colocar as classes para as imagens no arquivo de treinamento: 0 para positivo e 1 para negativo
data = pd.read_csv('path/to/dataset/exemplos_train.txt', header=None)
data['label'] = 0
data['label'][29436:59127] = 1
data.to_csv('interme.txt', header=False, index=False)
data = pd.read_csv('interm.txt', header=None)
data = data.iloc[np.random.permutation(len(data))]
data.to_csv('path/to/placas5_preto/exemplos_train.txt', index=False, header=False, sep=" ")

# O código abaixo é responsável por colocar as classes para as imagems no arquivo de teste: 0 para positivo e 1 para negativo
data = pd.read_csv('path/to/exemplos_teste.txt', header=None)
data['label'] = 0
data['label'][8281:18051] = 1
data.to_csv('interme.txt', header=False, index=False)
data = pd.read_csv('interm.txt', header=None)
data = data.iloc[np.random.permutation(len(data))]
data.to_csv('path/to/placas5_preto/exemplos_teste.txt', index=False, header=False, sep=" ")
