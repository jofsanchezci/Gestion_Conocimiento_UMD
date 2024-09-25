# Conjunto de reglas de diagnóstico
reglas = [
    {"condiciones": {"encendido": "no", "enchufado": "no"}, "resultado": "Enchufa el dispositivo."},
    {"condiciones": {"encendido": "no", "enchufado": "sí"}, "resultado": "Revisa el interruptor de encendido."},
    {"condiciones": {"encendido": "sí", "pantalla": "no"}, "resultado": "Revisa la conexión de la pantalla."},
    {"condiciones": {"encendido": "sí", "pantalla": "sí"}, "resultado": "El dispositivo parece estar funcionando correctamente."},
]

# Motor de inferencia
def diagnosticar_sistema(condiciones):
    for regla in reglas:
        if all(condiciones.get(k) == v for k, v in regla["condiciones"].items()):
            return regla["resultado"]
    return "No se encontró un diagnóstico para estas condiciones."

# Entrada del usuario
definir_condiciones = {
    "encendido": input("¿Está el dispositivo encendido? (sí/no): ").strip().lower(),
    "enchufado": input("¿Está el dispositivo enchufado? (sí/no): ").strip().lower(),
    "pantalla": input("¿Funciona la pantalla? (sí/no): ").strip().lower()
}

# Diagnóstico
diagnostico = diagnosticar_sistema(definir_condiciones)
print(f"Diagnóstico: {diagnostico}")
