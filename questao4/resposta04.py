faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / total_mensal) * 100
    print(f"{estado}: {percentual:.2f}%")


# Resposta:

# SP: 37.53%
# RJ: 20.29%
# MG: 16.17%
# ES: 15.03%
# Outros: 10.98%