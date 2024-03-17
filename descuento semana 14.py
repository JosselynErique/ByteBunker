def calcular_descuento(monto_total, porcentaje_descuento=35):

    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamada proporcionando solo el monto total de la compra
monto_compra_1 = 1500
descuento_1, monto_final_1 = calcular_descuento(monto_compra_1)
print("Descuento 1:", descuento_1)
print("Monto final a pagar después del descuento:", monto_final_1)

# Llamada proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_compra_2 = 3000
porcentaje_descuento_2 = 25
descuento_2, monto_final_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
print("Descuento 2:", descuento_2)
print("Monto final a pagar después del descuento:", monto_final_2)
