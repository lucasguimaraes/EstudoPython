precoCompra = float(input("Preço Comprado: "))
precoVenda = float(input("Preço Vendido: "))
precoVendaFinal = precoVenda - (precoVenda * 5/100)
lucro = precoVendaFinal - precoCompra
print("Lucro: ", lucro)

