"""
	Aluno: Diego Junior Gomes
	RA: 1904172

"""
import math

nome = str(input())
idade = float(input())
nome1 = str(input())
idade1 = float(input())
nome2 = str(input())
idade2 = float(input())
nome3 = str(input())
idade3 = float(input())
nome4 = str(input())
idade4 = float(input())

idade = math.fabs(idade)
idade = math.floor(idade)
idade1 = math.fabs(idade1)
idade1 = math.floor(idade1)
idade2 = math.fabs(idade2)
idade2 = math.floor(idade2)
idade3 = math.fabs(idade3)
idade3 = math.floor(idade3)
idade4 = math.fabs(idade4)
idade4 = math.floor(idade4)

soma_idade = (idade + idade1 + idade2 + idade3 + idade4)
media_aritmetica = ((idade + idade1 + idade2 + idade3 + idade4) / 5)
media_geometrica = (idade * idade1 * idade2 * idade3 * idade4) ** (1/5)
media_geometrica = math.floor(media_geometrica)

print ("Pessoa:",nome,"," ,"%.0f"% idade,)
print ("Pessoa:",nome1,"," ,"%.0f"% idade1,)
print ("Pessoa:",nome2,"," ,"%.0f"% idade2,)
print ("Pessoa:",nome3,"," ,"%.0f"% idade3,)
print ("Pessoa:",nome4,"," ,"%.0f"% idade4,)
print (soma_idade)
print (media_aritmetica)
print (media_geometrica)
