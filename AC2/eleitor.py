def eleitor(idade):
    if idade < 16:
        print("nao eleitor")
    elif 18 <= idade <= 65:
        print("eleitor obrigatorio")
    else:
        print("eleitor facultativo")


idade = int(input())
eleitor(idade)
