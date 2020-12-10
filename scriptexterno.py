# -*- coding: utf:8 -*-
import sys
import datetime
import time

#Checando os argumentos de linha de comando
if __name__ == "__main__":
  print(f'Quantos argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")

#Identificar os argumentos de entrada e de saída
try:
  entrada = sys.argv[1]
  saida = sys.argv[2]
  # Gerar um arquivo txt como saída
  fileOutput = open(saida, 'w+')
  fileOutput.write('Voce digitou: ')
  fileOutput.write(str(entrada))
  fileOutput.write('\n')
  data = datetime.datetime.now()
  dia = data.day
  mes = data.month
  ano = data.year
  hora = data.hour
  minuto = data.minute
  segundos = data.second
  fileOutput.write('Ituiutaba, ' + str(dia) + '/' + str(mes) + '/' + str(ano))
  fileOutput.write('\n')
  fileOutput.write(str(hora) + ':' + str(minuto) + ':' + str(segundos))
  fileOutput.close()
except Exception as e:
  print(str(e))
finally:
  # Demorar para encerrar o programa
  time.sleep(5)
  print("Finished!")