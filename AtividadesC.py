# Curso de Python
import math
import random
import pygame
import os
from time import sleep
from datetime import date

cores = {'vermelho': '\033[1;31m',
         'azul': '\033[1;36m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'limpar': '\033[m'}


def desafio_01():
    nome = input('Qual é seu nome?')
    print('Olá', nome + '! Prazer em te conhecer')


def desafio_02():
    dia = input('Em qual dia você nasceu?')
    mes = input('Em qual mês?')
    ano = input('E em que ano?')
    print('Então você nasceu no dia', dia, 'de', mes, 'de', ano, '! Estou correto? ^^')


def desafio_03():
    n1 = int(input('Diga um valor:'))
    n2 = int(input('Diga outro valor:'))
    print('Então o resultado dessa soma equivale a: {}'.format(n1 + n2))


def desafio_04():
    z = input('Digite algo: ')
    print('Considere TRUE = para verdadeiro e FALSE = para falso.'
          '\nO tipo primitivo da sua palavra/número é:', type(z),
          '\nTem espaços: ', z.isspace(),
          '\nÉ um número: ', z.isnumeric(),
          '\nÉ uma letra: ', z.isalpha(),
          '\nÉ uma letra ou um número: ', z.isalnum())


def desafio_05():
    x = int(input('Type a random value: '))
    print(f'The predecessor and successor is: {x - 1}, {x + 1}')


def desafio_06():
    x = int(input('Type a random value: '))
    print(f' The double this result is: {x * 2}'
          f'\n The triple this result is: {x * 3}'
          f'\n While the square root is: {x ** (1 / 2)}')


def desafio_07():
    x = int(input('Um certo aluno, fez uma prova X de um determinado professor, e ele obteu a seguinte nota: '))
    x1 = int(input('Esse aluno na seguinte prova conseguiu outra nota: '))
    print(f'No final do periodo ele obteve o seguinte resultado. \nPROVA 1: {x} \nPROVA 2: {x1}'
          f'\nA média desse aluno foi: {(x + x1) / 2}')


def desafio_08():
    print('We will convert into (M, CM and MM) the value you want:')
    valor = int(input('First choose a random value: '))
    print(f'\nIts value in Meters: {valor}'
          f'\nIts value in Centimeters: {valor / 100}'
          f'\nIts value in Millimeters: {valor / 1000}')


def desafio_09():
    x = int(input('Choose a random value: '))
    print(f'This was the number chosen:{x}'
          '\nHere is the table: '
          f'\n1*{x}: {1 * x}'
          f'\n2*{x}: {2 * x}'
          f'\n3*{x}: {3 * x}'
          f'\n4*{x}: {4 * x}'
          f'\n5*{x}: {5 * x}'
          f'\n6*{x}: {6 * x}'
          f'\n7*{x}: {7 * x}'
          f'\n8*{x}: {8 * x}'
          f'\n9*{x}: {9 * x}'
          f'\n10*{x}: {10 * x}')


def desafio_10():
    x = int(input('How much money do you have in your wallet? \nDigit here R$: '))
    print(f'You have in your wallet: {x}'
          f' \nConverting this value into dollar you have: {0.18 * x} US$')


def desafio_11():
    print('How much paint is nedded to paint your wall, lets calculate?')
    x = int(input('Width in Meters: '))
    y = int(input('Height in Meters: '))
    print(f'Its wall is {x}m wide/width and {y}m wide/height. Its total area: {x * y}m²')
    print(f'You need {(x * y) / 2}L to paint the whole wall')


def desafio_12():
    x = float(input('Qual valor do produto escolhido por você: '))
    print('Pegando a vista você tem um desconto de 5%'
          f' \nTotal do desconto: {x * 0.05}'
          f' \nValor após o desconto: {x - (x * 0.05)}'
          f' \nAgradeço a preferencia!')

    y = float(input('Digite o valor do produto escolhido por você: '))
    print('Levando o produto a vista recebe um desconto de 10%, e caso vá dividir esse valor recebe um acréscimo de 8%'
          f'\nCaso escolha a vista o valor fica: {y - (0.1 * y)}'
          f'\nCaso vá dividir, o valor fica: {(0.08 * y) + y}')


def desafio_13():
    x = int(input('Qual é seu salario trabalhando como Dev naquela empresa? '))
    print('Na nossa empresa você recebe esse valor, com um acrescimo de  +15%'
          f'\nOu seja, seu salario irá ficar em R$:{(x * 0.15) + x}')


def desafio_14():
    x = float(input('Informe a temperatura ambiente de sua cidade: '))
    print(f'Sua temperatura é: {x}°C, convertendo esse valor para Fahrenheit: {(x * 9 / 5) + 32}°F'
          f'\nE em Kelvin fica: {x + 273.15} K')


def desafio_15():
    x = int(input('Quantos dias você passou com o carro? '))
    y = float(input('Quantos KM você rodou com o mesmo? '))
    print(f'O total a pagar pelo veiculo Alugado é: R${(x * 60) + (y * 0.15)}')


def desafio_16():
    y = float(input('Digite um valor qualquer: '))
    x = math.floor(y)
    print(f'A parte inteira desse valor é: {x}')


def desafio_17():
    y = int(input('Digite o valor do seu cateto oposto: '))
    x = int(input('Digite o valor de seu cateto adjacente: '))
    print(f'O valor de sua hiptenusa é: {math.hypot(y, x)}')


def desafio_18():
    aluno = str(input('Você deseja seno, cosseno ou tangente: '))
    x = float(input('Digite o seu ângulo: '))
    seno = round(math.sin(math.radians(x)), 2)
    cosseno = round(math.cos(math.radians(x)), 2)
    tangente = round(math.tan(math.radians(x)), 2)
    if aluno == 'seno':
        print(f'Seno: {seno}')
    elif aluno == 'cosseno':
        print(f'Cosseno {cosseno}')
    elif aluno == 'tangente':
        print(f'Tangente: {tangente}')
    else:
        print('Você digitou errado')


def desafio_19():
    roll = []
    print('Bem vindo a sala de aula virtual, meu nome é Prof. Onion.')
    aluno = str(input('Qual é seu nome? '))
    print(f'Prazer, {aluno}, bem vindo a sala de aula virtual.')
    print('Irei sortear um aluno para apagar o quadro. Cada aluno irá receber um número.')
    for c in range(1, 5):
        c = random.randint(1, 4)
        while c in roll:
            c = random.randint(1, 4)
        roll.append(c)
    a1 = roll[0]
    a2 = roll[1]
    a3 = roll[2]
    a4 = roll[3]
    print(f'N° {a1} - {aluno}, N°{a2} - João, N°{a3} - Clairo, N°{a4} - Pam')
    x = random.randrange(1, 4)
    print(f'O número sorteado foi {x}')


def desafio_20():
    import random
    roll = []
    print('Bem vindo a sala de aula virtual, meu nome é Prof. Onion.')
    aluno = str(input('Qual é seu nome? '))
    print(f'Prazer, {aluno}, bem vindo a sala de aula virtual.')
    print('Irei sortear todos aluno para apresentar um trabalho na frente do quadro. Cada aluno irá receber um número'
          '\nque será sua ordem.')
    for c in range(1, 5):
        c = random.randint(1, 4)
        while c in roll:
            c = random.randint(1, 4)
        roll.append(c)
    a1 = roll[0]
    a2 = roll[1]
    a3 = roll[2]
    a4 = roll[3]
    print(f'N° {a1} - {aluno}, N°{a2} - João, N°{a3} - Clairo, N°{a4} - Pam.')


def desafio_21():
    pygame.init()
    if os.path.exists('beatles.wav'):
        pygame.mixer.music.load('beatles.wav')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


def desafio_22():
    nome = str(input('Olá, qual é seu nome completo?: ')).strip()
    name_dividido = nome.split()
    print(f'Seu nome com todas letras maisculas é: {nome.upper()}')
    print(f'Seu nome com todas letras minusculas é: {nome.lower()}')
    print('Seu nome completo possui:', len(nome) - nome.count(' '), 'caracteres')
    print(f'Seu primeiro nome é: {name_dividido[0]}, e tem {len(name_dividido[0])} caracteres')


def desafio_23():
    numero = int(input('Digite um valor númerico (0 a 9999): '))
    u = numero // 1 % 10
    d = numero // 10 % 10
    c = numero // 100 % 10
    m = numero // 1000 % 10
    print(f'Separando esse número, ficará: Milhar: {m}, Centena: {c}, Dezena: {d}, Unidade: {u}')


def desafio_24():
    cidade = input('Bom dia, qual é o nome da sua cidade?: ').strip()
    cidaded = cidade.startswith('Santos')

    if cidaded:
        print('Sua cidade começa com Santos!')
    else:
        print('Sua cidade não começa com Santos!')


def desafio_25():
    name = input('Olá, qual é seu nome?: ')
    named = name.split()

    if 'Silva' or 'silva' in name:
        print(f'Olá, {named[0]}, você pertence a linhagem dos Santos.')
    else:
        print(f'Olá, {named[0]}, você não pertence a linhagem dos Santos.')


def desafio_26():
    frase = str(input('Olá digite uma frase qualquer para analisarmos: ')).strip().lower()

    frase_inic = frase.find('a')
    frase_fin = frase.rfind('a')
    frase_contag = frase.count('a')

    print(
        f'Nessa frase contém {frase_contag} "a", o primeiro aparece na posição {frase_inic + 1}, '
        f'e o ultimo na posição {frase_fin + 1}')


def desafio_27():
    name = input('Digite seu nome completo aqui: ')
    name_sep = name.split()

    print(f'Seu primeiro nome é: {name_sep[0]}, e seu último nome é: {name_sep[-1]}')


def desafio_28():
    print(cores['azul'], '*-' * 35, cores['limpar'])
    print(cores['vermelho'], 'O computador sorteou um número de 0~5. Adivinhe qual é esse número', cores['limpar'])
    print(cores['azul'] + '*-' * 35 + cores['limpar'])
    computador = random.randrange(0, 5)
    jogador = int(input('Qual foi o número?: '))

    if jogador == computador:
        print('Parabéns!!!! Você acertou o numero')
        print('O número escolhido pelo computador foi: {}'.format(
            computador))
    else:
        print('Tente novamente!')
        print('O número escolhido pelo computador foi: {}'.format(
            computador))


def desafio_29():
    print('Boa tarde! você foi parado por excesso de velocidade. Essa via é até 80km')
    vel = int(input('digite o valor: '))

    if vel >= 80:
        print(f'O dispositivo acusou uma velocidade de {vel} Km/h. A cada Km acima, é adicionado 7 Reais na multa')
        multa = ((vel - 80) * 7) + 80
        print(f'O valor da multa está custando R$: {multa}. Sua velocidade foi {vel}Km')
        print(f'O valor a pagar é R$: {multa}')

    else:
        print(
            'Sua velocidade está abaixo do limite. Perdão senhor, o dispositivo está com defeito. Iremos trocar e '
            'desculpa o incoviniente. Pode seguir!!')


def desafio_30():
    print('Quer saber se seu número é par ou impar?')
    num = float(input('Digite o número: '))

    num_div = num % 2

    if num_div == 0:
        print('seu número é PAR')
    else:
        print('seu número é impar')


def desafio_31():
    print('Bom dia, para onde você quer ir?')
    print('As tarifas varia a partir da distância R$ 0,50 por Km no máximo 200 Km e R$ 0,'
          '45 para viagens mais longas')
    distancia = int(input('Coloque a distancia em Km para onde você quer ir: '))

    if distancia <= 200:
        valor = (distancia * 0.5)
        print(f'A distância é de {distancia} e o valor da passagem ficará: R$ {valor}')
    elif distancia >= 200:
        valor = (distancia * 0.45)
        print(f'A distância é de {distancia}Km e o valor da passagem ficará: R$ {valor}')


def desafio_32():
    print('Olá, aqui vamos analisar se o ano é Bissexto ou não')
    ano = int(input('Digite o ano aqui: '))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('Ano bissexto')
    else:
        print('Ano normal')


def desafio_33():
    print('Quer saber qual número é maior do que o outro?')
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))
    num_3 = int(input('Digite o terceiro número: '))

    if num_1 > num_2 > num_3:
        print(f'Esse número {num_1} é maior que {num_2}, que é maior que {num_3}')
    elif num_3 > num_2 > num_1:
        print(f'Esse número {num_3} é maior que {num_2}, que é maior que {num_1}')
    elif num_2 > num_3 > num_1:
        print(f'Esse número {num_2} é maior que o numero {num_3}, que é maior que {num_1}')
    elif num_2 > num_1 > num_3:
        print(f'Esse número {num_2} é maior que o numero {num_1}, que é maior que {num_3}')
    elif num_3 > num_1 > num_2:
        print(f'Esse número {num_3} é maior que o numero {num_1}, que é maior que {num_2}')
    elif num_1 > num_3 > num_2:
        print(f'Esse número {num_1} é maior que o numero {num_3}, que é maior que {num_2}')


def desafio_34():
    print('Vamos dar um aumento para os funcionarios da loja')
    func_1 = float(input('Qual é seu salário atual?: '))

    if func_1 >= 1250:
        valor = (func_1 * 0.10) + func_1
        print('Você recebeu um aumento de 10% por apresentar o salário acima de R$: 1.250,00')
        print(f'O seu novo salário é de: R$ {valor}')
    elif func_1 <= 1250:
        valor = (func_1 * 0.15) + func_1
        print('Você recebeu um aumento de 15% por apresentar o salário abaixo de R$: 1.250,00')
        print(f'O seu novo salário é de: R$ {valor}')

    print('Espero que isso motivem vocês a trabalhar mais!!!')


def desafio_35():
    print('Olá! Agora vamos ver se com os dados informados há a existência de um triângulo')  # apresentação

    # Valores
    var_a = float(input('Digite o primeiro valor: '))
    var_b = float(input('Digite o segundo valor: '))
    var_c = float(input('Digite o terceiro valor: '))

    # Condição
    if (var_b - var_c) < var_a < var_b + var_c and (var_a - var_c) < var_b < var_a + var_c and (
            var_a - var_b) < var_c < var_a + var_b:
        print('Com os dados informados, há a presença de um triângulo!!!')
    else:
        print(
            'Infelizmente, os dados informados não obedece a regra, sendo assim, não é possível existir um triângulo.')


def desafio_36():
    # boas vindas - pergunta se o cliente quer
    print(cores['azul'] + 'Olá senhor, deseja tirar um emprestimo?' + cores['limpar'])
    # sleep(1)
    resp = str(input('Sua resposta: '))
    # sleep(0.9)

    # Condição da resposta do cliente
    if resp.lower() == 'sim':
        print('Bom, agora iremos coletar as informações referente ao senhor.')
        # sleep(0.9)
    else:
        print('Ah, tá certo então, tenha um bom dia!!!! Com carinho, Emprestimos M.A.')

    # Coletando os dados para empréstimo.
    valor_casa = float(input('Qual é o valor do imovél que você quer adiquirir?: '))
    salario_cliente = float(input('Qual é sua faixa salarial?: '))
    tempo_pagar = int(input('Em quantos anos você pretende pagar o empréstimo?: '))

    # definir anos em meses
    anos_to_meses = tempo_pagar * 12

    # Valores
    parcelas = valor_casa / anos_to_meses
    porcetagem_salario = salario_cliente * 0.3

    if parcelas <= porcetagem_salario:
        print(f'Você terá que pagar parcelas de R$: {round(parcelas)}, em {anos_to_meses} meses ou {tempo_pagar} anos')

    else:
        print('O valor das parcelas é acima do seu salário, logo, teremos que recusar sua solicitação')


def desafio_37():
    print(cores['amarelo'] + 'Olá, aqui convertemos os números inteiros para Binário, Octal e Hexadecimal' +
          cores['limpar'])
    sleep(0.3)

    base_conv = int(input('Digite o valor: '))
    print(cores['vermelho'] + 'Coletamos seu dados!' + cores['limpar'])
    sleep(0.3)
    print(cores['vermelho'] + 'Qual sistema de numeração deseja? (Binario, Octal ou Hexadecimal): '
                              '\n[ 1 ] BINARIO'
                              '\n[ 2 ] OCTAL'
                              '\n[ 3 ] HEXADECIMAL' + cores['limpar'])
    conversao = int(input('Sua resposta: '))

    if conversao == 1:
        valor = format(base_conv, "b")
        print(f'Seu valor em binario ficará: {valor}')
    elif conversao == 2:
        valor = format(base_conv, "o")
        print(f'Seu valor em octal ficará: {valor}')
    elif conversao == 3:
        valor = format(base_conv, "x")
        print(f'Seu valor em hexadecimal ficará: {valor}')
    else:
        print(cores['vermelho'] + 'Sinto muito, não temos esse sistema de numeração que deseja. :(' + cores['limpar'])


def desafio_38():
    print('Vamos comparar os números aqui nesse aplicativo')
    sleep(0.3)
    num_1 = int(input('Digite o primeiro número: '))
    sleep(0.3)
    num_2 = int(input('Digite o segundo número: '))
    sleep(0.3)

    if num_1 > num_2:
        print(f'O número {num_1} é maior do que o {num_2}')

    elif num_1 < num_2:
        print(f'O número {num_2} é maior do que o {num_1}')

    elif num_1 == num_2:
        print(f'Ambos números apresentam o mesmo valor! {num_1} = {num_2}')


def desafio_39():
    print(cores['amarelo'] + 'Bem vindo ao sistema de alistamento do exercito' + cores['limpar'])
    sleep(0.3)

    nome = str(input(cores['verde'] + 'Qual é seu nome?: ' + cores['limpar']))
    print(cores['amarelo'] + f'Hmmm, interessante Sr. {nome}, você poderia informar sua idade?' + cores['limpar'])
    sleep(0.3)

    idade = int(input(cores['amarelo'] + 'Sua idade?: ' + cores['limpar']))
    ano = 2022

    if idade < 17:
        alistar = 18 - idade
        ano_alistamento = ano + alistar
        print(cores['amarelo'] + f'Sinto muito, Sr. {nome}, mas sua idade está abaixo do permitido' +
              cores['limpar'])
        print(cores['amarelo'] + f'Apenas acima de 17 podem se alistar' + cores['limpar'])

        print(cores['amarelo'] + f'Você será convocado para se alistar em: {ano_alistamento}' + cores['limpar'])

    elif idade == 17:
        print(cores['amarelo'] + f'O alistamento para sua idade é facultativo, caso queira presseguir!!!' +
              cores['limpar'])
        resp = str(input(cores['verde'] + 'Deseja realizar o alistamento?: ' + cores['limpar']))

        if resp.lower() == 'sim':
            print(cores['amarelo'] + f'Pronto Sr. {nome}, vamos coletar seus dados. Seja bem vindo ao Exercito' +
                  cores['limpar'])
        else:
            print(f'Tá certo, Sr. {nome}, próximo ano o senhor pode voltar e realizar seu alistamento')

    elif 18 < idade < 24:
        print(cores['amarelo'] +
              f'O Alistamento é obrigátorio para você, vamos coletar os seus dados. Seja bem vindo ao Exercito'
              + cores['limpar'])

    elif 24 < idade:
        alistar = idade - 24
        ano_alistamento = ano - alistar
        ano_inicial_alistamento = ano_alistamento - 6

        print(cores['amarelo'] +
              f"Você já passou da idade de se alistar Sr. {nome},  seu alistamento foi do ano {ano_inicial_alistamento}"
              f", até o ano de {ano_alistamento}. O senhor terá que pagar uma multa!!" + cores['limpar'])


def desafio_40():
    print('Olá, aqui vamos verificar sua nota!')
    nome_aluno = str(input('Como se chama?: '))

    nota_1 = int(input(f'Olá {nome_aluno}, qual foi a sua primeira nota?: '))
    nota_2 = int(input('E sua segunda nota?: '))

    media_final = (nota_1 + nota_2) / 2

    if 7 <= media_final <= 10:
        print(cores['verde'] +
              f'Parabéns {nome_aluno}, você está APROVADO!!! Sua média ficou: {round(media_final)}' + cores['limpar'])

    elif 3 >= media_final < 7:
        print(cores['vermelho'] +
              f'Você vai ter que fazer a prova final, {nome_aluno}. Sua média ficou: {round(media_final)}' +
              cores['limpar'])

    elif media_final < 3:
        print(cores['vermelho'] +
              f'Você já está reprovado por apresentar uma média abaixo do limite 3. Sua média ficou: {media_final}' +
              cores['limpar'])

    elif media_final > 10:
        print(cores['vermelho'] +
              'Nosso sistema de nota avalia de 0 a 10, as notas que você colocou não condiz com nosso sistema!' +
              cores['limpar'])


def desafio_41():
    print('A confederação Nacional está precisando de atletas novos!!! Se você tem mais de 9 até 20 anos é sua hora!!!')

    nome = str(input('Olá, jovem, qual é seu nome?: '))
    ano_nascimento = int(input('Qual é o ano que você nasceu?: '))

    idade = 2022 - ano_nascimento

    if 9 <= idade < 14:
        print(f'Olá, {nome}, você tem {idade} anos, e se enquadra na categoria MIRIM. Bem vindo!!')

    elif 14 <= idade < 19:
        print(f'Olá, {nome}, você tem {idade} anos, e se enquadra na categoria INFANTIL. Bem vindo!!')

    elif idade == 19:
        print(f'Olá, {nome}, você tem {idade} anos, e se enquadra na categoria JUNIOR. Bem vindo!!')

    elif idade == 20:
        print(f'Olá, {nome}, você tem {idade} anos, e se enquadra na categoria SÊNIOR. Bem vindo!!')

    elif idade >= 21:
        print(f'Olá, {nome}, você tem {idade} anos, e se enquadra na categoria MASTER. Bem vindo!!')

    else:
        print(f'Sinto muito {nome}, mas você não se enquadra nas categorias.')


def desafio_42():
    print('Iremos agora analisar um triangulo.')

    var_a = float(input('Digite o primeiro valor: '))
    var_b = float(input('Digite o segundo valor: '))
    var_c = float(input('Digite o terceiro valor: '))

    if var_a + var_b > var_c and var_a + var_c > var_a and var_b + var_c > var_a:
        print('Os dados informados podem formar triangulo')
        if var_a == var_b > var_c or var_a == var_c > var_b or var_b == var_c > var_a:
            print('E o triangulo formado é um Triangulo isoceles')
        elif var_a == var_b == var_c:
            print('E o triangulo formado é um Triangulo equilatero')
        elif var_a != var_b != var_c:
            print('E o triangulo formado é um Triangulo escaleno')
    else:
        print('Infelizmente, com os dados informados não há presença de um triangulo')


def desafio_43():
    print('Olááá, agora vamos calcular seu IMC')

    nome = str(input('Qual é seu nome?: '))
    peso = int(input(f'Certo, {nome}, agora me diga qual é seu peso (Kg): '))
    altura = float(input('Agora, informe qual é sua altura: '))

    imc = peso / altura ** 2

    if imc < 18.5:
        print(f'Senhor {nome}, seu IMC ({round(imc, 2)}) indica MAGREZA!')

    elif 18.5 <= imc < 25:
        print(f'Senhor {nome}, seu IMC ({round(imc, 2)}) indica PESO IDEAL!')

    elif 25 <= imc < 30:
        print(f'Senhor {nome}, seu IMC ({round(imc, 2)}) indica SOBREPESO!')

    elif 30 <= imc < 40:
        print(f'Senhor {nome}, seu IMC ({round(imc, 2)}) indica OBESO!')

    elif imc >= 40:
        print(f'Senhor {nome}, seu IMC ({round(imc, 2)}) indica OBESIDADE MORBIDA!')

    else:
        print('Os valores informados não condiz com a tabela de IMC')

    print('O cálculo de IMC não leva em consideração a composição corporal. Por esse motivo, pessoas com muita'
          'massa muscular, como é o caso de alguns atletas, podem apresentar um IMC acima do normal.')


def desafio_44():
    print('Olá, bem vindo ao supermercado Luz!')

    produto = int(input('É esse produto que o senhor(a) deseja? Diga o preço dele: ').strip())
    selec_pag = str(
        input('O senhor deseja pagar A vista (Dinheiro/Cheque) ou Cartão (Parcelado ou a vista)?: ').strip())

    if selec_pag.lower() == 'a vista':
        perguntar = str(input('Dinheiro ou Cheque, Sr(a)?: ')).strip()

        if perguntar.lower() == 'dinheiro' or perguntar.lower() == 'cheque':
            print(f'Todo produto pago em dinheiro/cheque recebe 10% de desconto.'
                  f'O preço do produto com o desconto fica: R$: {round(produto - (produto * 0.1))}')

    elif selec_pag.lower() == 'cartão' or selec_pag.lower() == 'cartao':
        perguntar = str(input('Parcelado ou A vista?: '))

        if perguntar.lower() == 'a vista':
            print(f'Os produtos pago a vista no cartão recebem 5% de desconto!'
                  f'O preço do produto com o desconto fica: R$: {round(produto - (produto * 0.05))}')

        elif perguntar.lower() == 'parcelado':
            perguntar_1 = str(input('Dividimos em até 3x. O que deseja?: '))

            if perguntar_1.lower() == 'duas vezes' or perguntar_1 == '2x':
                print(f'Os produtos pago no cartão e parcelados ficam com preço normal. '
                      f'Seu produto custará: R${produto}')
            elif perguntar_1.lower() == 'três vezes' or \
                    perguntar_1.lower() == 'tres vezes' or perguntar_1.lower() == '3x':
                print(f'Os produtos parcelados em 3x recebem 20% de acréscimo. '
                      f'O preço do seu produto ficará: {round(produto + (produto * 0.2))}')


def desafio_45():
    print('Vamos brincar de Jokenpô?')

    lista = ['pedra', 'papel', 'tesoura']
    aleatorio_lista = random.choice(lista)

    jogador = str(input('Digite sua resposta: '))

    sleep(1)
    print('PEDRAAAA, PAPELLLLLL, TESOURAAAAAA!!')
    sleep(1)
    print(cores['vermelho'] + 'Analisando......' + cores['limpar'])
    sleep(1)
    print('Boa jogada, masssssssss')
    sleep(1)

    if aleatorio_lista.lower() == jogador.lower():
        print('Empatou o jogo!')

    elif aleatorio_lista.lower() == 'pedra' and jogador.lower() == 'tesoura':
        print(cores['vermelho'] + f'Ixiiiiiiii..... A maquina venceu.' + cores['limpar'])
        print('Maquina: HEHEHEHEH, perdeu otarioooo!!!')

    elif aleatorio_lista.lower() == 'tesoura' and jogador.lower() == 'pedra':
        print(cores['verde'] + 'Hahahahaha, você venceuuuu!!! Parabéns' + cores['limpar'])
        input('Deixe uma frase para a maquina: ')
        print('Maquina: sortudo, eu deixei vencer, desce o play ai dnv, corno.')

    elif aleatorio_lista.lower() == 'papel' and jogador.lower() == 'pedra':
        print(cores['vermelho'] + f'Ixiiiiiiii..... A maquina venceu.' + cores['limpar'])
        print('Maquina: HEHEHEHEH, perdeu otarioooo!!!')

    elif aleatorio_lista.lower() == 'pedra' and jogador.lower() == 'papel':
        print(cores['verde'] + 'Hahahahaha, você venceuuuu!!! Parabéns' + cores['limpar'])
        input('Deixe uma frase para a maquina: ')
        print('Maquina: sortudo, eu deixei vencer, desce o play ai dnv, corno.')

    elif aleatorio_lista.lower() == 'tesoura' and jogador.lower() == 'papel':
        print(cores['vermelho'] + f'Ixiiiiiiii..... A maquina venceu.' + cores['limpar'])
        print('Maquina: HEHEHEHEH, perdeu otarioooo!!!')

    elif aleatorio_lista.lower() == 'papel' and jogador.lower() == 'tesoura':
        print(cores['verde'] + 'Hahahahaha, você venceuuuu!!! Parabéns' + cores['limpar'])
        input('Deixe uma frase para a maquina: ')
        print('Maquina: sortudo, eu deixei vencer, desce o play ai dnv, corno.')

    else:
        print('Essa palavra não existe no jogo!')

    print('Obrigado humano :)')


def desafio_46():
    print('Contagem regressiva!!!!')


    for c in range(10, -1, -1):
        sleep(1)
        print(c)

    print('BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!')


def desafio_47():

    for c in range(1, 51):
        if c % 2 == 0:
            print(c)



def desafio_48():

    armazenador = 0

    for c in range(1, 501, 2):
        if c % 3 == 0:
            armazenador += c

    print(f'A soma é {armazenador}')


def desafio_49():
    numero_tabuada = int(input('Escolha qual numero da tabuada você quer: '))

    for tabuada in range(1, 11):
        print(f'Tabuada do {tabuada} x {numero_tabuada} = {numero_tabuada * tabuada}')


def desafio_50():
    num_pares = []
    for numero in range(1, 7):
        num = int(input('Digite um número: '))

        if num % 2 == 0:
            num_pares.append(num)

    print(sum(num_pares))

def desafio_50_1():
    armazenador = 0
    lista = []
    for numeros in range(1, 7):
        numeros += random.randint(1, 6)
        if numeros % 2 == 0:
            armazenador += numeros
        else:
            lista.append(numeros)


    print(f'A soma dos números pares foram: [{armazenador}]')
    print(f'Os números impares descartados foram: {lista}')


def desafio_51():
    print('Vamos fazer uma Progressão Aritmética')
    num = int(input('Digite o número inicial: '))
    razao = int(input('Digite a razão: '))
    num_total = num + 9 * razao

    for pa in range(num, num_total + 1, razao):
        print(pa, end='-> ')

    print('Acabou!')

def desafio_52():
    print(f'vamos verificar se o número é primo')
    num_dig = int(input('Digite o número: '))
    armazenador = 0

    for num in range(1, num_dig + 1):

        if num_dig % num == 0:
            armazenador += 1

    if armazenador == 2:
        print('É número primo!!!')
    else:
        print('Não é numero primo')

def desafio_53():

    frase_analisar = str(input('Digite a frase: ')).strip().lower()
    frase_junta = frase_analisar.replace(" ", "")
    frase_inverso = frase_junta[::-1]

    contador = 0

    for c in range(0, 1):

        if frase_junta == frase_inverso:
            contador += 1

    if contador >= 1:
        print('É um palindromo')
    else:
        print('Não é um palindromo')

def desafio_53_1():
    frase_analisar = str(input('Digite a frase: ')).strip().lower()
    frase_separar = frase_analisar.split()
    frase_junta = ''.join(frase_separar)

    inverso_frase = ''
    contador = 0

    for frase in range(len(frase_junta) - 1, -1, -1):
        inverso_frase += frase_junta[frase]

        if inverso_frase == frase_junta:
            contador += 1

    if contador >= 1:
        print('É um palindromo')
    else:
        print('Não é um palindromo')

def desafio_54():
    ano_atual = date.today().year
    contador = 0
    contador_1 = 0

    for c in range(1, 8):
        idade = int(input('Digite o seu ano de nascimento: '))

        if (ano_atual - idade) >= 21:
            contador += 1
        elif (ano_atual - idade) < 21:
            contador_1 += 1

    print(f'Apenas {contador} atigiram a maioridade, enquanto os outros {contador_1} não atingiram a maioridade')

def desafio_55():
    maiorpeso = 0
    menorpeso = 0

    for p in range(1, 6):
        pesos_pessoais = float(input('Digite o peso: '))
        if p == 1:
            maiorpeso = pesos_pessoais
            menorpeso = pesos_pessoais
        else:
            if pesos_pessoais > maiorpeso:
                maiorpeso = pesos_pessoais
            if pesos_pessoais < menorpeso:
                menorpeso = pesos_pessoais


    print(f'maior peso {maiorpeso}, menor peso {menorpeso}')

def desafio_55_1():
    lista_pesos = []

    for peso in range(1, 6):
        peso_pessoal = float(input(f'Digite o peso da {peso}° pessoa: '))
        lista_pesos.append(peso_pessoal)


    print(f'O maior peso foi: {max(lista_pesos)} Kg e o menor peso foi: {min(lista_pesos)} Kg')



def desafio_56():
    idade_total = []
    sex_fem = []

    homem_mais_velho = 0
    nome_homem_velho = ''
    lista_homens = []

    for group in range(1, 5):
        nome_pessoa = str(input(f'Nome da {group}° pessoa: '))
        idade_pessoa = int(input(f'Idade da {group}° pessoa: '))
        idade_total.append(idade_pessoa)
        sexo_pessoa = str(input(f'Sexo da {group}° pessoa [M/F]: ')).lower()


        if group == 1 and sexo_pessoa in 'Mm':
            homem_mais_velho = idade_pessoa
            nome_homem_velho = nome_pessoa
            lista_homens.append(nome_homem_velho)

        if sexo_pessoa in 'Mm' and idade_pessoa > homem_mais_velho:
            homem_mais_velho = idade_pessoa
            nome_homem_velho = nome_pessoa
            lista_homens.append(nome_homem_velho)

        if sexo_pessoa in 'Ff' and idade_pessoa < 20:
            sex_fem.append(sexo_pessoa)

    sumIdade = sum(idade_total) / len(idade_total)
    print(f'A média da idade do grupo é: {round(sumIdade)} anos')

    if len(lista_homens) >= 1:
        print(f'O homem mais velho tem {homem_mais_velho} anos, e o nome dele é: {nome_homem_velho} ')
    else:
        print('Não existe homens nesse grupo')


    if len(sex_fem) == 1:
        name = 'mulher'
        print(f'Existe {len(sex_fem)} {name} abaixo dos 20 anos.')
    elif len(sex_fem) >= 2:
        name = 'mulheres'
        print(f'Existe {len(sex_fem)} {name} abaixo dos 20 anos.')
    else:
        print('Não existe mulheres com idade abaixo de 20 anos nesse grupo')

desafio_56()