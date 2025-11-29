class ColiseoDeportivo:
    """
    Clase que representa un Coliseo Deportivo
    con sus características principales
    """
    
    # Variable de clase para contar coliseos
    total_coliseos = 0
    
    def __init__(self, nombre, capacidad, ciudad, año_construccion):
        """
        Constructor de la clase ColiseoDeportivo
        """
        self.nombre = nombre
        self.capacidad = capacidad
        self.ciudad = ciudad
        self.año_construccion = año_construccion
        self.estado = "Disponible"
        self.tipo_cesped = "Natural"
        self.iluminacion = True
        ColiseoDeportivo.total_coliseos += 1
    
    def mostrar_info(self):
        """
        Muestra la información completa del coliseo
        """
        print(f"INFORMACIÓN DEL COLISEO")
        print(f"Nombre: {self.nombre}")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"Ciudad: {self.ciudad}")
        print(f"Año de construcción: {self.año_construccion}")
        print(f"Estado: {self.estado}")
        print(f"Tipo de césped: {self.tipo_cesped}")
        print(f"Iluminación: {'Sí' if self.iluminacion else 'No'}")
    
    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado del coliseo
        """
        self.estado = nuevo_estado
        print(f"Estado actualizado a: {self.estado}")
    
    def cambiar_cesped(self, tipo):
        """
        Cambia el tipo de césped del coliseo
        """
        self.tipo_cesped = tipo
        print(f"Césped actualizado a: {self.tipo_cesped}")
    
    def calcular_antiguedad(self, año_actual=2024):
        """
        Calcula los años de antigüedad del coliseo
        """
        antiguedad = año_actual - self.año_construccion
        return antiguedad
    
    def es_moderno(self):
        """
        Determina si el coliseo es moderno (menos de 30 años)
        """
        return self.calcular_antiguedad() < 30
    
    @classmethod
    def obtener_total(cls):
        """
        Retorna el total de coliseos creados
        """
        return cls.total_coliseos