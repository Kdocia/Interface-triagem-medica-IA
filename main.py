import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QLCDNumber
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from interface import Ui_MainWindow
from RedePython import logsig, purelin, W1, b1, W2, b2, W3, b3  # Importa os componentes necessários da rede neural
import torch
from queue_system import CustomQueue


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Instancia a fila
        self.fila = CustomQueue()

        # Conecta o botão "Run" ao método de execução da rede neural
        self.ui.pushButton.clicked.connect(self.run_network)

    def normalize_input(self, inputs):
        """Normaliza os inputs com base nos valores máximos e mínimos."""
        max_train = torch.tensor([[100], [200], [120], [150], [40], [100], [41]], dtype=torch.float32)
        min_train = torch.tensor([[0], [90], [60], [50], [10], [70], [35]], dtype=torch.float32)
        return torch.div(inputs - min_train, max_train - min_train)

    def run_network(self):
        # Coletar os inputs do usuário a partir dos LineEdits
        try:
            inputs = torch.tensor([
                [float(self.ui.age_input.text())],     # Idade
                [float(self.ui.ps_input.text())],   # Pressão Sistólica
                [float(self.ui.pd_input.text())],   # Pressão Diastólica
                [float(self.ui.fc_input.text())],   # Frequência Cardíaca
                [float(self.ui.fr_input.text())],   # Frequência Respiratória
                [float(self.ui.so2_input.text())],   # Saturação de O2
                [float(self.ui.tc_input.text())],   # Temperatura Corporal
            ], dtype=torch.float32)

            nome = self.ui.name_input.text() # Coletar o nome do paciente
            
            # Normalizar os inputs
            x_norm = self.normalize_input(inputs)

            # Passar pela rede neural
            a1 = logsig(torch.mm(W1, x_norm) + b1)
            a2 = logsig(torch.mm(W2, a1) + b2)
            a3 = purelin(torch.mm(W3, a2) + b3)
            print(a3)
            # Interpretar a saída da rede (simula a imagem da pulseira)
            #print("Saída da Rede:", a3)
            # Exibir a imagem correspondente na GraphicsView
            for i in range(0,5):
                if a3[i]>0.5:
                    pos = i
                    print(pos)
                    break
            
            pos_fila = self.fila.insert(nome,pos) # Insere o paciente na fila
            
            self.update_lcd(pos_fila) # Atualiza o LCD com a posição na fila
                    
            image_path = self.get_image_path(pos)
            self.display_image(image_path)

        except ValueError:
            print("Por favor, insira valores numéricos válidos.")

    def get_image_path(self, pos):
        """Retorna o caminho da imagem baseado na saída da rede."""
        # Simulação: você pode ajustar para carregar imagens reais.
        print(pos)
        if pos == 0:
            return "./imagens/vermelho.jpg"
        elif pos == 1:
            return "./imagens/laranja.jpg"
        elif pos == 2:
            return "./imagens/amarelo.jpg"
        elif pos == 3:
            return "./imagens/verde.jpg"
        return "./imagens/azul.jpg"

    def display_image(self, image_path):
        """Exibe a imagem no GraphicsView."""
        scene = QGraphicsScene()
        pixmap = QPixmap(image_path)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        pixmap_item.setTransformationMode(Qt.SmoothTransformation)
        scene.addItem(pixmap_item)

        # Ajustar a cena ao GraphicsView
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)
    
    def update_lcd(self, pos_fila):
        """Define um valor no display LCD."""
        self.ui.lcdNumber.display(pos_fila)  # Atualiza o valor no display 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())