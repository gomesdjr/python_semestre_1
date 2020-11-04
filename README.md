### Atividades realizadas durante o primeiro semestre da faculdade na disciplina de Linguagem de Programação.

# AC 01
**1. Construa um programa que calcula a distância entre dois pontos A = (xA; yA) e B = (xB; yB) noR2 (isto é, no espaço bidimensional)**<br>
dAB = √(xB − xA)2 + (yB − yA)2
Ordem das intruções:
- Leia xA.
- Leia yA.
- Leia xB.
- Leia yB.
- Calcule e imprima dAB<br>

**2. Um objeto é lançado a um ângulo θ  em relação ao solo, com uma velocidade inicial v (em m/s), num planeta com gravidade g. Construa um programa que leia θ (em graus), v e g e calcule a altura máxima h em metros alcançada pelo  objeto, e em seguida exiba (imprima) o resultado h na saída do programa.**<br>

**3. Desenvolva um programa que leia o nome de 5 pessoas e suas respectivas idades. Para tornar o programa mais robusto contra erros, as idades podem ser negativas,  portanto  você terá que garantir que seus valores sempre serão convertidos para valores positivos (dica: use a função fabs() do módulo math). Outra  restrição é que  as idades devem obrigatoriamente ser valores inteiros. Caso o usúario informe um número decimal, ele deverá ser convertido (truncado) para o tipo int. Em seguida:**
- Imprima os nomes e as idades das 5 pessoas no formato do exemplo a seguir (Atenção: utilize exatamente a mesma saída, com a mesma quantidade de espaços, pontuação, etc)<br>
Pessoa: Nome Completo da Pessoa , 20<br>
Pessoa: Fulano de Tal , 7<br>
Pessoa: Ciclano , 78<br>
Pessoa: Outro Nome Completo , 43<br>
Pessoa: Algum Nome Completo , 35<br>
- Calcule e exiba em uma única linha na saída do programa a soma das idades.
- Calcule e exiba em linhas separadas na saída do programa a média aritméetica e a médiageomêtrica das idades. Somente para o caso da méedia geométrica, o valor deverá ser truncad.

# AC 02
**1. Escreva um programa que leia dois valores inteiros e informe qual é o maior. Se os números forem iguais, imprima qualquer um deles.**<br>
<br>
**2. Faça um programa que leia a idade (valor inteiro) de uma pessoa e informe sua classe eleitoral. O programa deve imprimir as seguintes mensagens:**
- não eleitor, se a idade é abaixo de 16 anos.
- eleitor obrigatorio, se a idade é maior e igual a 18 ou menor e igual a 65 anos.
- eleitor facultativo, se a idade está entre 16 e 18 anos ou acima dos 65 anos.

**3. Crie um programa para calcular o IMC (índice de massa corporal). Seu programa deve ler a altura(em metros) e o peso (em kg) de uma pessoa. O programa deve exibir o IMC arredondado em duas casas decimais, e em outra linha exibir um status dependendo do valor do IMC. Para arredondar em duas casas decimais, utilize a função round(IMC, 2), onde IMC é a variável que armazena o valor do IMC.**
- Muito abaixo do peso, se IMC < 17,0.
- Abaixo do peso, se 17:0 <= IMC < 18,50.
- Peso normal, se 18:50 <= IMC < 25,00.
- Acima do peso, se 25:0 <= IMC < 30,00.
- Obesidade grau I, se 30:0 <= IMC < 35,00.
- Obesidade grau II, se 35:0 <= IMC < 40,00.
- Obesidade grau III, se IMC >= 40,0.

# AC 03
**1. Escreva um programa que exiba na saída padrão os 100 primeiros números naturais (inteiros positivos incluindo o zero).**<br>
   - OBS: O programa não lê entrada, apenas exibe os 100 primeiros números naturais, cada um em uma linha diferente.
   
 **2. Faça um programa que imprima todos os números ímpares entre dois números dados (n e m).**
Ordem das intruções:<br>
- Leia n (inteiro).
- Leia m (inteiro).
- Imprima todos os números ímpares maiores ou iguais a n e menores ou iguais a m.<br>
- Dica: para testar se um número x é ímpar, o resto da divisãoo entre x e 2 deve ser igual a 1.

**3. Escreva um programa para somar os n primeiros termos da seguinte série:**

Dica: Aqui todas as frações são somadas, mas como calcular o denominador? Tente primeiro fazer a exibição apenas dos denominadores.<br>
Os denominadores são: 1; 4; 9; 16; 25; 36;..., qual a relação entre eles e a posição dos némeros?<br>
Compare com a posição dos termos: 1; 2; 3; 4; 5; 6;....<br>
<br>
**Ordem das intruções:**
- Leia n > 0.
- A saída deve ser uma única linha contendo apenas o resultado da somatóoria formatado para exibir 6 casas de precisão. Neste caso, para fazer o arredondamento utilize o comando print("f0:.6fg".format(S)) para exibir a saída na tela, onde S é a variável que armazenao somatóorio da série.

# AC 04
**1. Escreva a função juros simples(c, i, t) que recebe 3 parâmetros:** <br>
- o capital inicial c, a taxa de jurosi (de 0 a 1, representando 0 a 100%), e o tempo t. Construa a lóggica que calcula o capital inicial acrescido de juros simples, e devolva (retorne) este valor. A fórmula para calcular o montante final com juros simples é a seguinte: M = c + (c * i * t)<br>
- Em seguida, escreva a funçãojuros compostos(c, i, t) que recebe 3 parâmetros: o capital inicial c,a taxa de juros i (de 0 a 1, representando 0 a 100%), e o tempo t. Construa a lógica que calcula o capital inicial acrescido de juros compostos (montante final), e devolva (retorne) este valor. A fórmula para calcular o montante final com juros compostos é a seguinte: M = c * (1 + i)^t

**2. Escreva a função checa quantidade divisores(n, qtd) que dado um inteiro positivo n e a quantidade de divisores qtd, devolva (retorne) True caso n possua qtd divisores, ou False caso contrário.**
- Dica: você deve testar se todos os números de 1 atén são divisíveis por n.
- Dica: para testar se um número n é divisíel por outro número i, verifique se o resto da divisão entre eles é igual a 0 (zero).
