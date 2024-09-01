def analisar_faturamento(dados):
    valores = [item['valor'] for item in dados if item['valor'] > 0]
    
    if not valores:
        return None, None, 0
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

dados = [
    {"dia": 1, "valor": 1500.00},
    {"dia": 2, "valor": 0.00},
    {"dia": 3, "valor": 1800.00},
    {"dia": 4, "valor": 2000.00},
    {"dia": 5, "valor": 1700.00},
    {"dia": 6, "valor": 0.00},
    {"dia": 7, "valor": 0.00},
    {"dia": 8, "valor": 1300.00},
    {"dia": 9, "valor": 0.00},
    {"dia": 10, "valor": 2200.00},
    {"dia": 11, "valor": 0.00},
    {"dia": 12, "valor": 1400.00},
    {"dia": 13, "valor": 1600.00},
    {"dia": 14, "valor": 0.00}
]

# Analisar faturamento
menor_valor, maior_valor, dias_acima_media = analisar_faturamento(dados)

# Imprimir resultados
print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
