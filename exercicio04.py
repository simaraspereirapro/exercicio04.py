primeiroNome = input("Digite seu primeiro nome: ")
dia = input("Dia do nascimento: ")
mes = input("Mês do nascimento: ")
ano = input("Ano do nascimento: ")

primeiraLetra = primeiroNome[0:1].upper()
restanteNome = primeiroNome[1:].lower()

primeiroNome = primeiraLetra + restanteNome


print ("{} nasceu no dia {}/{}/{}".format(primeiroNome.capitalize(), dia, mes, ano))

