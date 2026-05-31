# tests/test_dummy.py
from dummy import saludar

def test_saludar():
    assert saludar() == "Hola, pipeline funcionando"