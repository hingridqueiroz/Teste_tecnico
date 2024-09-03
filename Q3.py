import json

# Carregar dados do arquivo JSON
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

def analisar_faturamento(dados):
    valores = [item['valor'] for item in dados if item['valor'] > 0]
    
    if not valores:
        return None, None, 0
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

# Analisar faturamento
menor_valor, maior_valor, dias_acima_media = analisar_faturamento(dados)

# Imprimir resultados
print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
