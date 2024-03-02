import openpyxl

valor_procurado = input('DADOS 2021\nDigite a TAG para consulta: ')

# Abrir planilha
readworkbook = openpyxl.load_workbook('dados.xlsx')
pagedados = readworkbook['Dados']

for linha in pagedados.iter_rows(min_row=5):
    tagaction = linha[0].value
    priceaction = linha[15].value

    if tagaction == valor_procurado:
        print(f"Tag: {tagaction}, Price: {priceaction:.2f}")
        break

else:
    print("Valor não encontrado na planilha.")