import pandas as pd 
import json
import os
import csv
import logging
from datetime import datetime
import os
#from openpyxl import load_workbook


# ---------------------------
# Leer datos desde Excel determinado
# ---------------------------
def leer_datos_excel(ruta_excel):
    try:
        if not os.path.exists(ruta_excel):
            print(f"ERROR: No se encontró el archivo en la ruta: {ruta_excel}")
            return []

        df = pd.read_excel(ruta_excel)

        # Convertir a lista de diccionarios
        data = df.to_dict(orient="records")

        # Filtrar compras válidas (donde no haya None en producto, cliente, cantidad, precio)
        compras_validas = []
        for row in data:
            try:
                producto = row.get("producto")
                cliente = row.get("cliente")
                cantidad = int(row.get("cantidad", 0))
                precio_unitario = float(row.get("precio_unitario", 0))

                if producto and cliente and cantidad > 0 and precio_unitario > 0:
                    compras_validas.append({
                        "producto": producto,
                        "cliente": cliente,
                        "cantidad": cantidad,
                        "precio_unitario": precio_unitario
                    })
            except Exception:
                continue

        if not compras_validas:
            print("WARNING: No se encontraron compras válidas.")
        return compras_validas

    except Exception as e:
        print(f"ERROR al leer Excel: {e}")
        return []

# Estadística

def estadisticas(data):
    resumen = {
        "total_ingresos": 0,
        "top_producto_por_ingresos": None,
        "compras_por_cliente": {},
        "bono": False
    }

    ingresos_por_producto = {}

    for compra in data:
        producto = compra["producto"]
        cliente = compra["cliente"]
        cantidad = compra["cantidad"]
        precio = compra["precio_unitario"]

        ingreso = cantidad * precio
        resumen["total_ingresos"] += ingreso

        # Ingresos por producto
        if producto not in ingresos_por_producto:
            ingresos_por_producto[producto] = 0
            ingresos_por_producto[producto] += ingreso

        # Cantidad por cliente
        if cliente not in resumen["compras_por_cliente"]:
            resumen["compras_por_cliente"][cliente] = 0
            resumen["compras_por_cliente"][cliente] += cantidad

        # Producto top
        if ingresos_por_producto:
            resumen["top_producto_por_ingresos"] = max(
            ingresos_por_producto, key=ingresos_por_producto.get
        )

        # Bono
        if resumen["total_ingresos"] > 6_000_000:
            resumen["bono"] = True

    return resumen

# Generar reporte tipo JSON

def generar_reporte(resumen, ruta_salida):
    try:
        with open(ruta_salida, "w", encoding="utf-8") as f:
            json.dump(resumen, f, ensure_ascii=False, indent=4)

        print(f"Reporte generado en: {ruta_salida}")
        if resumen.get("bono"):
            print("Umbral superado, aplicar descuento corporativo 5% en próxima compra.")
    except Exception as e:
        print(f"ERROR al generar reporte: {e}")

# Punto de entrada

def run():
    ruta_excel = r"C:\Users\USUARIO CAB\Desktop\1er exámen\Punto 7\Informacion\Informacion.csv.xlsx"
    ruta_reporte = r"C:\Users\USUARIO CAB\Desktop\1er exámen\Punto 7\reporte.json"

    compras = leer_datos_excel(ruta_excel)
    if not compras:
        print("No se encontraron compras válidas.")
        return

    resumen = estadisticas(compras)
    generar_reporte(resumen, ruta_reporte)

    print("\n--- Resumen ---")
    print(f"Total ingresos: {resumen['total_ingresos']}")
    print(f"Top producto por ingresos: {resumen['top_producto_por_ingresos']}")
    print(f"Compras por cliente: {resumen['compras_por_cliente']}")
    print(f"Bono: {resumen['bono']}")














