import random

class SistemaMonitoreo:
    def __init__(self):
        self.datos_registrados = []
    
    def leer_datos_sensor(self):
        """Simula la lectura de datos de un sensor.
        
        Returns:
            dict: Diccionario con temperatura en °C y humedad.
        """
        # En una implementación real, aquí se conectaría con el hardware del sensor
        return {
            'temperatura_c': round(random.uniform(-10, 40), 2),  # Valor simulado
            'humedad': round(random.uniform(0, 100), 2)         # Valor simulado
        }
    
    def convertir_a_fahrenheit(self, celsius):
        """Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius.
            
        Returns:
            float: Temperatura en grados Fahrenheit.
            
        Raises:
            ValueError: Si el valor de temperatura está por debajo del cero absoluto.
        """
        if celsius < -273.15:
            raise ValueError("La temperatura no puede estar por debajo del cero absoluto (-273.15°C)")
        return (celsius * 9/5) + 32
    
    def registrar_datos(self, dato):
        """Almacena los datos procesados en el sistema.
        
        Args:
            dato (dict): Diccionario con los datos a registrar.
            
        Raises:
            ValueError: Si los datos no tienen el formato esperado.
        """
        if not isinstance(dato, dict):
            raise ValueError("El dato debe ser un diccionario")
        
        required_keys = {'temperatura_c', 'humedad', 'temperatura_f'}
        if not required_keys.issubset(dato.keys()):
            raise ValueError(f"El dato debe contener las llaves: {required_keys}")
        
        self.datos_registrados.append(dato)
    
    def procesar_datos_sensor(self):
        """Flujo completo para leer, convertir y registrar datos."""
        try:
            # Leer datos del sensor
            datos = self.leer_datos_sensor()
            
            # Convertir temperatura
            temp_f = self.convertir_a_fahrenheit(datos['temperatura_c'])
            datos['temperatura_f'] = temp_f
            
            # Registrar datos
            self.registrar_datos(datos)
            
            return True
        except Exception as e:
            print(f"Error al procesar datos: {str(e)}")
            return False