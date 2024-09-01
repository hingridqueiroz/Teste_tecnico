faturamento = {
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "Outros" : 19849.53 
}

fat_total = sum(faturamento.values())
porcentagem = {}

for estado, valor in faturamento.items():
    porcentagem[estado] = (valor * 100) / fat_total
    print(f"{estado}: {porcentagem[estado]:.2f}%")