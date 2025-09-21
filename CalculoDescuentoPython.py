CalculoDescuentoPython.py
# CalculoDescuentoPython.py
# Programa para calcular descuentos en compras usando funciones en Python

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.
    
    Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).
    
    Retorna:
        float: Valor del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada: usando solo el monto (descuento por defecto 10%)
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print("Compra 1:")
    print(f"  Monto total: ${monto1:.2f}")
    print(f"  Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"  Monto final a pagar: ${total1:.2f}\n")

    # Segunda llamada: especificando monto y porcentaje de descuento
    monto2 = 250.0
    porcentaje = 20
    descuento2 = calcular_descuento(monto2, porcentaje)
    total2 = monto2 - descuento2
    print("Compra 2:")
    print(f"  Monto total: ${monto2:.2f}")
    print(f"  Descuento aplicado ({porcentaje}%): ${descuento2:.2f}")
    print(f"  Monto final a pagar: ${total2:.2f}")
