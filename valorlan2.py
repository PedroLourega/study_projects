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


#Pergunta o serviço
tipo_servico = input("Digite o tipo de serviço (lanhouse, ps5, vr): ").lower()

#Faz o calculo do valor
if tipo_servico == 'lanhouse':
    valor = calcular_valor_lan_house(duracao_minutos)
elif tipo_servico == 'ps5':
    valor = calcular_valor_lan_ps5(duracao_minutos)
elif tipo_servico == 'vr':
    valor = calcular_valor_lan_vr(duracao_minutos)
else:
    valor = "Serviço inválido!"  #Erro!

#Duração
print(f"Duraçãoem minutos: {duracao_minutos} ")
print(f"Duração total: {horas_totais}h:{minutos_totais}m ")
print(f"Valor a pagar: R$ {valor:.2f}" if isinstance(valor, (int, float)) else valor)
