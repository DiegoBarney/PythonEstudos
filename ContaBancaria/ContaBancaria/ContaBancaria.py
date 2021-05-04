import Conta


cont = Conta.Conta(113,"30226-2",120.0,"Diego Pimentel")
cont2 = Conta.Conta(111,"1111-3",150.0,"Joao")
cont._Conta__conta = 1

cont.transferir(cont2,50)

cont.extrato_conta()
cont2.extrato_conta()
