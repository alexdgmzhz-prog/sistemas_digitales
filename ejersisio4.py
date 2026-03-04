helado = True
dulce = False

def dar_recompensa(tiene_helado, tiene_dulce):
    if tiene_helado and not tiene_dulce:
        print("🍦 Recompensa: HELADO")
    elif tiene_dulce and not tiene_helado:
        print("🍬 Recompensa: DULCE")
    elif tiene_helado and tiene_dulce:
        print("❌ ERROR: No puedes tener ambos")
    else:
        print("😢 Sin recompensa")

print("=== SISTEMA DE RECOMPENSAS ===")
print(f"Helado solicitado: {helado}")
print(f"Dulce solicitado: {dulce}")
print()

es_xor = (helado or dulce) and not (helado and dulce)

if es_xor:
    print("✅ Recompensa válida (solo una opción elegida)")
    dar_recompensa(helado, dulce)
else:
    print("⚠️  Configuración inválida")
    dar_recompensa(False, False)