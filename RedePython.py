import scipy.io as sio
import torch
import numpy as np

# 1. Carregar as matrizes salvas do MATLAB
data = sio.loadmat('RedePrecisao85.mat')

# Extrair pesos e bias
W1 = torch.tensor(data['W1'], dtype=torch.float32)  # Pesos da primeira camada
b1 = torch.tensor(data['b1'], dtype=torch.float32)  # Bias da primeira camada
W2 = torch.tensor(data['W2'], dtype=torch.float32)  # Pesos da segunda camada
b2 = torch.tensor(data['b2'], dtype=torch.float32)  # Bias da segunda camada
W3 = torch.tensor(data['W3'], dtype=torch.float32)  # Pesos da terceira camada
b3 = torch.tensor(data['b3'], dtype=torch.float32)  # Bias da terceira camada


#x = torch.tensor([[14],[145],[65],[54],[18],[92],[37.3]], dtype=torch.float32) # Entrada de exemplo (converta para tensor PyTorch)

# maximo e minimo usado para normalizar a rede 
#max_train = torch.tensor([[100], [200], [120], [150], [40], [100], [41]], dtype=torch.float32)
#min_train = torch.tensor([[0], [90], [60], [50], [10], [70], [35]], dtype=torch.float32)


#x_norm = torch.div(x-min_train,max_train-min_train)

# Funções de ativação
def logsig(x):
    return 1 / (1 + torch.exp(-x))  # Versão compatível com PyTorch

def purelin(x):
    return x

# Forward Pass na Rede
#a1 = logsig(torch.mm(W1, x_norm) + b1)  # Primeira camada
#a2 = logsig(torch.mm(W2, a1) + b2)# Segunda camada
#a3 = purelin(torch.mm(W3, a2) + b3)# terceira camada (saída)
# Exibir a saída
#print("Saída da Rede:", a3)
#
# [vermelho; laranja ; amarelo; verde ; azul]
