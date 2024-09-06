def analisar_faturamento(faturamento):
    dias_com_faturamento = [valor for valor in faturamento if valor > 0]

    if not dias_com_faturamento:
        return None, None, 0 


    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = len([valor for valor in dias_com_faturamento if valor > media_faturamento])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Um exemplo de uso
faturamento = [
    0, 0, 0, 5000, 0, 3000, 0, 0, 0, 2000, 0, 10000, 0, 0, 0, 
    6000, 0, 0, 0, 1500, 0, 2000, 0, 0, 0, 0, 8000, 0, 0, 0,
    # ... adicionar os valores de faturamento para todos os dias do ano
]

menor_faturamento, maior_faturamento, dias_acima_da_media = analisar_faturamento(faturamento)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")