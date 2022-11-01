
valor_inicial = 5988.21
taxa_mes = 15/12 * 14


vf_bruto = (valor_inicial/100 * (taxa_mes)) + valor_inicial
imposto_de_renda = ((vf_bruto - valor_inicial)/100) * 17.5
vf_liquido = vf_bruto - imposto_de_renda
rendimento = vf_liquido - valor_inicial

print(f'O valor investido foi de {valor_inicial}, o rendimento foi de {rendimento:.2f}, totalizando: {vf_liquido:.2f}')
