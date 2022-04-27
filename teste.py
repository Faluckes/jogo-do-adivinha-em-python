from random import randint


print("===================================================")
print("Jogo do Adivinha. Acerte e ganhe tiro no pé")
print("===================================================")
print("TOTALMENTE RANDOMIZADO!!")
print("===================================================")

numero_aleatorio = randint(1, 20)
tentativas = 10
rodada = 1
print("Você tem {} tentativas para acertar o número de 1 a 20".format(tentativas))
while(rodada <= tentativas):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite o número: ")
    chute = int(chute_str)
    print("Você colocou o número: ", chute_str)
    if(numero_aleatorio == chute):    
        print("\n===================================================")
        print("Você acertou o número, parabéns!")
        print("=================================================== \n")

        rodada = tentativas
    else:
        if(chute > numero_aleatorio):
            print("\n===================================================")
            print("Você errou! O chute foi maior que o Numero randomizado")
            print("=================================================== \n")

        elif(chute < numero_aleatorio):
            print("\n===================================================")
            print("Você errou! O chute foi menor que o Numero randomizado")
            print("=================================================== \n")

    rodada = rodada + 1
print("O numero randomizado era: ", numero_aleatorio)
print("Acabou \n \n")
print("Aperte ENTER para finalizar a tarefa")
input()



