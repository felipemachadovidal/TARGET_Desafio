import json

def calcular_faturamento(dados):
    faturamento = dados["faturamento_diario"]

    faturamento_filtrado = [dia for dia in faturamento if dia > 0]
    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

    dias_acima_da_media = sum(1 for dia in faturamento_filtrado if dia > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open('faturamento.json') as f:
    dados = json.load(f)

menor, maior, dias_acima_media = calcular_faturamento(dados)
print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
