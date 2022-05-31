from conta import Conta

conta1 = Conta(26743, 'João Alves', 300)
conta2 = Conta(78412, 'Guilherme Silva', 130)

conta1.titular = 'Pedro'
conta1.extrato()
conta1.depositar(200)
conta1.extrato()
conta1.saca(150)
conta2.extrato()
conta1.transfere(conta2, 200)
conta2.extrato()
print(Conta.codigo_banco())