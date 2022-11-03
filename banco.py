from datetime import datetime  
from os import system
f = open("extracto.txt", "w")
f.close()

def fechaActual():
  f = datetime.now()
  f = f.strftime('%Y/%m/%d %H:%M:%S')
  return f

def guardarReg(reg):
  f = open("extracto.txt", "a")
  f.write(reg)
  f.close()

class CuentaBanco:
  def __init__(self, cuenta, saldoInicial):
    self.cuenta = cuenta
    self.saldo = saldoInicial
    guardarReg(fechaActual() + ';' + str(cuenta) + ';' + 'ini' + ';' + str(saldoInicial) + ';\n')

  def consultarSaldo(self):
    return self.saldo
  def depositar(self, valor):
    self.saldo += valor
    guardarReg(fechaActual() + ';' + str(self.cuenta) + ';' + 'dep' + ';' + str(valor) + ';\n')

  def retirar(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      guardarReg(fechaActual() + ';' + str(self.cuenta) + ';' + 'ret' + ';' + str(valor) + ';\n')
      return True
    else:
      print('Saldo insuficiente: ${:,.2f}'.format(self.saldo))
      return False
  
  def transferir(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      guardarReg(fechaActual() + ';' + str(self.cuenta) + ';' + 'ret' + ';' + str(valor) + ';\n')
      return True
    
    else: 
      print('*Fondos insuficientes: $ ', self.saldo)
      print('*Transferencia rechazada!')

  def extracto(self):
    f = open('extracto.txt')
    print('\n*Extracto {} | '.format(self.cuenta))
    print(f.read())
    f.close()


  def menu(self):   
    op = 1
    while op != 0:
      system('clear')
      print('--- Banco JesusArango | Cuenta: {} ---\n'.format(self.cuenta))
      op = int(input('1. Consultar Saldo\n' +
                     '2. Depositar\n' +
                     '3. Retirar\n' +
                     '4. Transferir\n' +
                     '5. Extracto\n' +
                     '0. Salir\n\n' +
                     'Opción: '))
      if op == 1:
        print('\nSaldo Actual: ${:,.2f} | {}'.format(self.consultarSaldo(), fechaActual()))
      if op == 2:
        v = float(input('\nValor a Depositar $ '))
        if v > 0: self.depositar(v)
      if op == 3:
        v = float(input('\nValor a Retirar $ '))
        if v > 0: self.retirar(v)
      if op == 4:
        v = int(input('Transferir a cuenta:   '))
        x = float(input('Transferir Valor:  $ '))
        if v > 0 and x > 0: self.transferir(v, x)
      if op == 5:
        self.extracto()
      if op == 0:
        print(arrayCuentas)
        arrayCuentas[self.cuenta-1][1] = self.saldo
        f = open('Cuentas.txt' , 'w')
        for linea in arrayCuentas:
          reg = str(linea[0]) + ',' + str(linea[1]) + ',' + linea[2]
          f.write(reg)
        f.close()

      if op != 0: input('\nContinuar...')  

with open('Cuentas.txt') as f:
  arrayCuentas = []
  i = 0
  for linea in f:
    reg = linea.split(',')
    arrayCuentas.append([])
    arrayCuentas[i].append(int(reg[0]))
    arrayCuentas[i].append(float(reg[1]))
    arrayCuentas[i].append(reg[2])
    i + 1

cuenta = int(input('Cuenta: '))
saldo = arrayCuentas[cuenta-1][1]
c = CuentaBanco(cuenta, saldo)
c.menu()
print('\nHasta pronto...')
