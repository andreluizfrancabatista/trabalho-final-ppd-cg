# PyQt5 - Criando interfaces gráficas com Python
import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QLineEdit
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow, self).__init__()
    self.setup_main_window()
    self.initUI()
  
  def setup_main_window(self):
    self.x = 640
    self.y = 480
    self.setMinimumSize(QSize(self.x, self.y))
    self.setWindowTitle("Hello World")
    self.wid = QWidget(self)
    self.setCentralWidget(self.wid)
    self.layout = QGridLayout()
    self.wid.setLayout(self.layout)

  def initUI(self):
    #Criar os widgets (Label, Button, Text, Image)

    #Criando um QLabel para texto
    self.texto = QLabel("Hello World from PyQt5 - IFTM", self)
    self.texto.adjustSize()
    self.largura = self.texto.frameGeometry().width()
    self.altura = self.texto.frameGeometry().height()
    self.texto.setAlignment(QtCore.Qt.AlignCenter)

    #Criando os botões
    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("Run me!")
    self.b1.clicked.connect(self.run_me)
    self.b2 = QtWidgets.QPushButton(self)
    self.b2.setText("Run me too!")
    self.b2.clicked.connect(self.run_me_too)

    # Texto QLabel
    self.texto1 = QLabel("Insira código hash:", self)
    self.texto1.adjustSize()
    self.texto1.setAlignment(QtCore.Qt.AlignCenter)
    
    self.resposta = QLabel("Respostas", self)
    self.resposta.adjustSize()
    self.resposta.setAlignment(QtCore.Qt.AlignCenter)

    # QLineEdit
    self.codigoacao = QLineEdit()

    # Organizando os widgets dentro da GridLayout
    self.layout.addWidget(self.texto, 0, 0, 1, 4)

    self.layout.addWidget(self.texto1, 1, 0, 1, 1)
    self.layout.addWidget(self.codigoacao, 1, 1, 1, 1)
    self.layout.addWidget(self.resposta, 1, 2, 1, 2)

    self.layout.addWidget(self.b1, 3, 0, 1, 2)
    self.layout.addWidget(self.b2, 3, 2, 1, 2)
    
    for i in range(4):
      self.layout.setRowStretch(i, 1)
      self.layout.setColumnStretch(i, 1)

  #Métodos para ações dos botões
  def run_me(self):
    self.entrada = self.codigoacao.text()
    self.saida = 'respostas.txt'
    self.script = '.\scriptexterno.py'
    self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
    print(self.program)
    self.result = subprocess.run(self.program, shell=True)
 
  def run_me_too(self):
    try:
      self.entrada = open('respostas.txt', 'r+')
      self.conteudo = self.entrada.readlines()
      self.resposta.setText(' '.join(self.conteudo))
      self.entrada.close()
    except Exception as e:
      self.resposta.setText('Arquivo não encontrado.\n' + str(e))

  
def window():
  app = QApplication(sys.argv)
  win = MyWindow()
  win.show()
  sys.exit(app.exec_())

window()
  