#Função principal
def  calcular_valor(duracao_minutos, preco_fixo_hora, preco_fixo_30min):

    if duracao_minutos <= 30:
        return preco_fixo_30min

    horas = duracao_minutos // 60

    valor = preco_fixo_hora * horas

    
    if horas > 5:
        desconto = 0.15
    elif horas > 3:
        desconto = 0.13
    elif horas > 2:
        desconto = 0.10
    elif horas > 1:
        desconto = 0.7
    else:
        desconto = 0.0

    valor_com_desconto = valor * (1 - desconto)
    return valor_com_desconto

#Funções para cada serviço
def calcular_valor_lan_house(duracao_minutos):
    return calcular_valor(duracao_minutos, preco_fixo_hora=30, preco_fixo_30min=20)

def calcular_valor_lan_ps5(duracao_minutos):
    return calcular_valor(duracao_minutos, preco_fixo_hora=45, preco_fixo_30min=30)

def calcular_valor_lan_vr(duracao_minutos):
    return calcular_valor(duracao_minutos, preco_fixo_hora=100, preco_fixo_30min=50)

#Coletor de entrada e saída da lan
hora_entrada = list(map(int, input("Digite a hora e o minuto de entrada (HH MM):").split()))
hora_saida = list(map(int, input("Digite a hora e o minuto de entrada (HH MM):").split()))

#Converte as horas de entrada e saída
entrada_minutos = hora_entrada[0] * 60 + hora_entrada[1]
saida_minutos = hora_saida[0] * 60 + hora_saida[1]

#Calcula a duração em minutos
duracao_minutos = saida_minutos - entrada_minutos

#Pergunta para o usuário
tipo_servico = input("Digite o tipo de serviço (LanHouse, PS5, VR): ").lower()


if tipo_servico == 'lanhouse':
    valor = calcular_valor_lan_house(duracao_minutos)
elif tipo_servico == 'ps5':
    valor = calcular_valor_lan_ps5(duracao_minutos)
elif tipo_servico == 'vr':
    valor = calcular_valor_lan_vr(duracao_minutos)
else:
    valor = "Serviço inválido!" #Error!


#Interface de resultado
print(f"Duração total: {duracao_minutos} minutos")
print(f"Valor a pagar: R$ {valor:2.f}" if isinstance(valor,(int, float))else valor)
