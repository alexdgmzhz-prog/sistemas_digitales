lluvia = True
sombrilla = True
bajo_techo = True

print("=== SISTEMA DE PROTECCIÓN CONTRA LLUVIA ===")
print(f"☔ ¿Está lloviendo? {lluvia}")
print(f"🌂 ¿Tienes sombrilla? {sombrilla}")
print(f"🏠 ¿Estás bajo techo? {bajo_techo}")
print()

if lluvia:
    print("🌧️  ESTÁ LLOVIENDO - Evaluar protección...")
    
    tiene_proteccion_correcta = (sombrilla or bajo_techo) and not (sombrilla and bajo_techo)
    
    if tiene_proteccion_correcta:
        print("✅ Estás haciendo lo correcto")
        
        if sombrilla and not bajo_techo:
            print("   → Estás afuera con sombrilla")
        elif bajo_techo and not sombrilla:
            print("   → Estás resguardado bajo techo")
    else:
        print("⚠️  ¿Dónde te equivocaste?")
        
        if sombrilla and bajo_techo:
            print("   → No necesitas sombrilla si estás bajo techo")
            print("   → Guarda la sombrilla")
        elif not sombrilla and not bajo_techo:
            print("   → ¡Te estás mojando!")
            print("   → Busca sombrilla o refugio")
else:
    print("☀️  NO ESTÁ LLOVIENDO")
    print("ℹ️  No necesitas sombrilla ni preocuparte por refugio")

print("\n--- DIAGNÓSTICO FINAL ---")
if lluvia and (sombrilla or bajo_techo) and not (sombrilla and bajo_techo):
    print("Estado: PROTEGIDO ADECUADAMENTE ✅")
elif lluvia:
    print("Estado: PROTECCIÓN INCORRECTA ⚠️")
else:
    print("Estado: SIN LLUVIA - SIN PROBLEMAS ☀️")
