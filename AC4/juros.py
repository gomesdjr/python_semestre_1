def juros_simples(c, i, t):
    montante_final = capital + (capital * taxa * tempo)
    return montante_final


def juros_compostos(c, i, t):
    montante_final = capital * (1 + taxa) ** tempo
    return montante_final


# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input('Escolha a opção "simples" ou "composto": ')
capital = float(input('Informe o capital: '))
taxa = float(input('Insira a taxa: '))
tempo = float(input('Informe o tempo: '))
if taxa > 0.99:
    taxa = taxa / 100
if opcao == 'simples':
    montante_final = juros_simples(capital, taxa, tempo)
elif opcao == 'composto':
    montante_final = juros_compostos(capital, taxa, tempo)

print("{0:.2f}".format(montante_final))
