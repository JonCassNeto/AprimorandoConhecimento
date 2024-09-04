import json


with open('faturamento.json', 'r') as f:
    dados = json.load(f)


faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]


menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)


media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = len([faturamento for faturamento in faturamentos if faturamento > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")


# Resposta:

# Menor valor de faturamento: 373.78
# Maior valor de faturamento: 48924.24
# Número de dias com faturamento superior à média mensal: 10

