import Conta

print(Conta.Conta.codigo_banco())
cont = Conta.Conta(113,"30226-2",120.0,"diego Pimentel")
cont2 = Conta.Conta(111,"1111-3",150.0,"joao")
cont._Conta__conta = 1


cont.transferir(cont2,250)

cont.extrato_conta()
cont2.extrato_conta()


