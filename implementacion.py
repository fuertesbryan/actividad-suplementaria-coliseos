from clase_coliseo import ColiseoDeportivo

def crear_coliseo_manual():
    """
    Función para crear un coliseo ingresando datos manualmente
    """
    print("\n--- CREAR NUEVO COLISEO ---")
    nombre = input("Nombre del coliseo: ")
    capacidad = int(input("Capacidad (personas): "))
    ciudad = input("Ciudad: ")
    año = int(input("Año de construcción: "))
    
    coliseo = ColiseoDeportivo(nombre, capacidad, ciudad, año)
    print(f"\n✓ Coliseo '{nombre}' creado exitosamente!")
    return coliseo

def menu_principal():
    """
    Menú principal de la aplicación
    """
    print("    SISTEMA DE GESTIÓN DE COLISEOS DEPORTIVOS")
    print("1. Ver todos los coliseos")
    print("2. Crear nuevo coliseo")
    print("3. Ver estadísticas")
    print("4. Salir")

# Lista para almacenar los coliseos
coliseos = []

# Crear objetos de ejemplo - Coliseo 1
print("\nCreando coliseos de ejemplo...")
coliseo1 = ColiseoDeportivo("Estadio Atahualpa", 35000, "Quito", 1948)
coliseo1.cambiar_cesped("Sintético")
coliseos.append(coliseo1)

# Crear objetos de ejemplo - Coliseo 2
coliseo2 = ColiseoDeportivo("Estadio Monumental", 57000, "Guayaquil", 1987)
coliseo2.cambiar_estado("En mantenimiento")
coliseos.append(coliseo2)

# Crear objetos de ejemplo - Coliseo 3
coliseo3 = ColiseoDeportivo("Estadio Gonzalo Pozo Ripalda", 16500, "Riobamba", 1992)
coliseos.append(coliseo3)

# Crear objetos de ejemplo - Coliseo 4
coliseo4 = ColiseoDeportivo("Estadio Bellavista", 18000, "Ambato", 1945)
coliseo4.cambiar_cesped("Híbrido")
coliseos.append(coliseo4)

# Mostrar todos los coliseos creados
print("\n" + "="*60)
print("         LISTADO DE COLISEOS DEPORTIVOS DEL ECUADOR")
print("="*60)

for i, coliseo in enumerate(coliseos, 1):
    print(f"\n--- COLISEO #{i} ---")
    coliseo.mostrar_info()
    print(f"Antigüedad: {coliseo.calcular_antiguedad()} años")
    print(f"¿Es moderno?: {'Sí' if coliseo.es_moderno() else 'No'}")

# Mostrar estadísticas generales
print("\n" + "="*60)
print("              ESTADÍSTICAS GENERALES")
print("="*60)
print(f"Total de coliseos registrados: {ColiseoDeportivo.obtener_total()}")
print(f"Capacidad total: {sum(c.capacidad for c in coliseos):,} personas")
print(f"Coliseos modernos: {sum(1 for c in coliseos if c.es_moderno())}")
print("="*60)