"""
Базовые тесты для ElectroPy
"""

import unittest
import sys
import os

# Добавляем путь к модулю electroPy
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from electroPy.circuits import Resistor, Capacitor, Circuit
from electroPy.calculations import ohms_law, power_calculation, parallel_resistance, series_resistance


class TestCircuits(unittest.TestCase):
    
    def test_resistor_creation(self):
        """Тест создания резистора"""
        r = Resistor("R1", 100)
        self.assertEqual(r.name, "R1")
        self.assertEqual(r.resistance, 100)
    
    def test_circuit_total_resistance(self):
        """Тест расчета общего сопротивления цепи"""
        circuit = Circuit("Test")
        circuit.add_component(Resistor("R1", 100))
        circuit.add_component(Resistor("R2", 200))
        self.assertEqual(circuit.get_total_resistance(), 300)


class TestCalculations(unittest.TestCase):
    
    def test_ohms_law_voltage(self):
        """Тест закона Ома - расчет напряжения"""
        voltage = ohms_law(current=2, resistance=50)
        self.assertEqual(voltage, 100)
    
    def test_ohms_law_current(self):
        """Тест закона Ома - расчет тока"""
        current = ohms_law(voltage=12, resistance=4)
        self.assertEqual(current, 3)
    
    def test_ohms_law_resistance(self):
        """Тест закона Ома - расчет сопротивления"""
        resistance = ohms_law(voltage=24, current=2)
        self.assertEqual(resistance, 12)
    
    def test_power_calculation(self):
        """Тест расчета мощности"""
        power = power_calculation(voltage=12, current=2)
        self.assertEqual(power, 24)
    
    def test_parallel_resistance(self):
        """Тест расчета параллельного сопротивления"""
        # Два одинаковых резистора параллельно дают половину сопротивления
        result = parallel_resistance(100, 100)
        self.assertEqual(result, 50)
    
    def test_series_resistance(self):
        """Тест расчета последовательного сопротивления"""
        result = series_resistance(100, 200, 300)
        self.assertEqual(result, 600)


if __name__ == '__main__':
    unittest.main()
