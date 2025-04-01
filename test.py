import pytest
from sistema import SistemaMonitoreo
from unittest.mock import patch

@pytest.fixture
def sistema():
    """Fixture que proporciona una instancia limpia del sistema para cada test."""
    return SistemaMonitoreo()

def test_convertir_a_fahrenheit(sistema):
    """Prueba la conversión correcta de Celsius a Fahrenheit."""
    assert sistema.convertir_a_fahrenheit(0) == 32
    assert sistema.convertir_a_fahrenheit(100) == 212
    assert sistema.convertir_a_fahrenheit(-40) == -40
    assert sistema.convertir_a_fahrenheit(37) == pytest.approx(98.6, rel=1e-2)

def test_convertir_temperatura_invalida(sistema):
    """Prueba que se lance error con temperatura por debajo del cero absoluto."""
    with pytest.raises(ValueError, match="La temperatura no puede estar por debajo del cero absoluto"):
        sistema.convertir_a_fahrenheit(-300)

def test_leer_datos_sensor(sistema):
    """Prueba que leer_datos_sensor devuelve un diccionario con las claves correctas."""
    datos = sistema.leer_datos_sensor()
    assert isinstance(datos, dict)
    assert 'temperatura_c' in datos
    assert 'humedad' in datos

def test_registrar_datos(sistema):
    """Prueba el registro correcto de datos."""
    dato_valido = {
        'temperatura_c': 25.0,
        'humedad': 45.0,
        'temperatura_f': 77.0
    }
    
    sistema.registrar_datos(dato_valido)
    assert len(sistema.datos_registrados) == 1
    assert sistema.datos_registrados[0] == dato_valido

@pytest.mark.parametrize("dato_invalido", [
    "no es un diccionario",
    {'temperatura_c': 25.0},  # Faltan campos
    None
])
def test_registrar_datos_invalidos(sistema, dato_invalido):
    """Prueba que se lance error con datos de formato incorrecto."""
    with pytest.raises(ValueError):
        sistema.registrar_datos(dato_invalido)

def test_procesar_datos_sensor(sistema, mocker):
    """Prueba el flujo completo de procesamiento de datos usando mocker de pytest."""
    # Configurar mock para leer_datos_sensor
    mocker.patch.object(
        sistema,
        'leer_datos_sensor',
        return_value={
            'temperatura_c': 20.0,
            'humedad': 60.0
        }
    )
    
    resultado = sistema.procesar_datos_sensor