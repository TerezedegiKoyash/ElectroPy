"""
ElectroPy - Библиотека для работы с электрическими цепями
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .circuits import Circuit, Resistor, Capacitor, Inductor
from .calculations import (
    ohms_law, 
    power_calculation, 
    parallel_resistance, 
    series_resistance,
    voltage_divider
)

__all__ = [
    "Circuit",
    "Resistor", 
    "Capacitor",
    "Inductor",
    "ohms_law",
    "power_calculation",
    "parallel_resistance",
    "series_resistance", 
    "voltage_divider"
]
