#Main
def calcular_valor(duracao_minutos, preco_fixo_hora, preco_fixo_30min):
    
    #Verifica a duracao de até 30m
    if duracao_minutos <= 30:
        return preco_fixo_30min

    #Conversor de duracao
    horas = duracao_minutos // 60
    valor = preco_fixo_hora * horas

    #Desconto
    if horas > 5:
        desconto = 0.15
    elif horas > 3:
        desconto = 0.13
    elif horas > 2:
        desconto = 0.10
    elif horas > 1:
        desconto = 0.07  
    else:
        desconto = 0.0


    valor_com_desconto = valor * (1 - desconto)
    return valor_com_desconto

#Preço de cada serviço disponivel
def calcular_valor_lan_house(duracao_minutos):
    return calcular_valor(duracao_minutos, preco_fixo_hora=30, preco_fixo_30min=20)

def calcular_valor_lan_ps5(duracao_minutos):
    return calcular_valor(duracao_minutos, preco_fixo_hora=45, preco_fixo_30min=30)

def calcular_valor_lan_vr(duracao_minutos):
    return calcular_valor(duracao_minutos, preco_fixo_hora=100, preco_fixo_30min=50)

while True:
    print("-----Menu de Serviços-----")
    print("1. Lan House")
    print("2. PS5")
    print("3. VR")
    print("4. Sair")
    print("---------------------------")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '4':
        print("Saindo do programa...")
        break #Encerra o processo.

    if opcao in['1', '2', '3']:
        #Entrada de dados de tempo utilizado
        hora_entrada = list(map(int, input("Digite a hora e o minuto de entrada (HH MM): ").split()))
        hora_saida = list(map(int, input("Digite a hora e o minuto de saída (HH MM): ").split()))


    #Converte a entrada e a saída
    entrada_minutos = hora_entrada[0] * 60 + hora_entrada[1]
    saida_minutos = hora_saida[0] * 60 + hora_saida[1]

    #Transforma em minutos
    duracao_minutos = saida_minutos - entrada_minutos

    #Calculo de horas e minutos
    horas_totais = duracao_minutos // 60
    minutos_totais = duracao_minutos % 60


    #Faz o calculo do valor
    if opcao == '1':
        valor = calcular_valor_lan_house(duracao_minutos)
        servico = "Lan House"
    elif opcao == '2':
        valor = calcular_valor_lan_ps5(duracao_minutos)
        servico = "PS5"
    elif opcao == '3':
        valor = calcular_valor_lan_vr(duracao_minutos)
        servico = "VR"

    #Resultados
    print("---------------------------")
    print(f"Serviço: {servico}")
    print(f"Duração total: {horas_totais}h:{minutos_totais}m")
    print(f"Valor a pagar: R$ {valor:.2f}")
    print("---------------------------")

else:
    
    print("Opção invalida!")
