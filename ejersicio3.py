gasolina = 10
temperatura = 10

min_gasolina = 5
max_temperatura = 45

print("=== SISTEMA DE DIAGNÓSTICO DEL VEHÍCULO ===")
print(f"🔋 Gasolina actual: {gasolina} litros")
print(f"🌡️  Temperatura motor: {temperatura}°C")
print(f"\n--- Límites de seguridad ---")
print(f"⛽ Mínimo de gasolina: {min_gasolina} litros")
print(f"🔥 Temperatura máxima: {max_temperatura}°C")

if gasolina > min_gasolina and temperatura < max_temperatura:
    movimiento = True
    print("\n✅ VEHÍCULO LISTO PARA MOVERSE")
    print("🚗 Todas las condiciones de seguridad cumplidas")
else:
    movimiento = False
    print("\n⛔ VEHÍCULO NO PUEDE MOVERSE")
    
    if gasolina <= min_gasolina:
        print("⚠️  Nivel de gasolina insuficiente")
    if temperatura >= max_temperatura:
        print("⚠️  Temperatura del motor muy alta")

print(f"\n🔧 Estado de movimiento: {movimiento}")