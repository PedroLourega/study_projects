# Calcula os valores da Lan House
def calcular_valor_lan_hq(duracao_minutos):
    if duracao_minutos <= 30:
        return 20
    elif duracao_minutos <= 60:
        return 30
    elif duracao_minutos <= 120:
        return 50
    elif duracao_minutos <= 300:
        return 100 
    elif duracao_minutos <= 600:
        return 160 
    else:
        return "Duração excede o máximo permitido"

# Calcula os valores do PS5
def calcular_valor_ps5(duracao_minutos):
    if duracao_minutos <= 60:
        return 45
    elif duracao_minutos <= 120:
        return 75
    elif duracao_minutos <= 300:
        return 150
    else:
        return "Duração excede o máximo permitido"  

# Calcula os valores do VR
def calcular_valor_oculos(duracao_minutos):
    if duracao_minutos <= 30:
        return 50
    elif duracao_minutos <= 60:
        return 100
    else:
        return "Duração excede o máximo permitido" 

# Captura os horários de entrada e saída
hora_entrada = list(map(int, input("Digite a hora e o minuto de entrada (HH MM): ").split()))   
hora_saida = list(map(int, input("Digite a hora e o minuto de saída (HH MM): ").split()))  

# Converte horas e minutos para minutos
entrada_minutos = hora_entrada[0] * 60 + hora_entrada[1]
saida_minutos = hora_saida[0] * 60 + hora_saida[1]

# Duração em minutos
duracao_minutos = saida_minutos - entrada_minutos

# Tipo de Jogo
tipo_jogo = input("Digite o tipo de jogo (PC, PS5 ou VR): ").lower()  

# Aqui você deve usar minúsculas para a comparação
if tipo_jogo == 'pc':  
    valor = calcular_valor_lan_hq(duracao_minutos)
elif tipo_jogo == 'ps5':  
    valor = calcular_valor_ps5(duracao_minutos)   
elif tipo_jogo == 'vr':  
    valor = calcular_valor_oculos(duracao_minutos)    
else:
    valor = "Opção Inválida!"  

# Valores finais
print(f"Duração total: {duracao_minutos} minutos")
print(f"Valor a pagar: R$ {valor:.2f}" if isinstance(valor, (int, float)) else valor)
