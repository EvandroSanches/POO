class Conta:

    def __init__(self, conta, titular, saldo):
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo

    def extrato(self):
        print( f'Titular:{self.titular} \nSaldo:{self.saldo} ')

    def depositar(self, valor):
        self.__saldo += valor
        print('Valor depositado com sucesso')

    def __pode__sacar(self, valor_a_sacar):
        if self.__saldo > 0 and self.__saldo >= valor_a_sacar:
            return True
        else:
            return False

    def saca(self, valor):
        if self.__pode__sacar(valor):
            self.__saldo -= valor
            print('saque bem sucedido')
        else:
            print('saldo insuficiente')

    def transfere(self, destinatario, valor):
        self.saca(valor)
        destinatario.depositar(valor)
        print('Transferencia feita')

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular


    @staticmethod
    def codigo_banco():
        return 'Caixa: 103'
