"""
Модуль для работы с электрическими цепями и компонентами
"""

import numpy as np
from typing import List, Dict, Optional


class Component:
    """Базовый класс для электрических компонентов"""
    
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"{self.name}: {self.value}"


class Resistor(Component):
    """Резистор"""
    
    def __init__(self, name: str, resistance: float):
        super().__init__(name, resistance)
        self.resistance = resistance
    
    def __str__(self):
        return f"Резистор {self.name}: {self.resistance} Ом"


class Capacitor(Component):
    """Конденсатор"""
    
    def __init__(self, name: str, capacitance: float):
        super().__init__(name, capacitance)
        self.capacitance = capacitance
    
    def __str__(self):
        return f"Конденсатор {self.name}: {self.capacitance} Ф"


class Inductor(Component):
    """Катушка индуктивности"""
    
    def __init__(self, name: str, inductance: float):
        super().__init__(name, inductance)
        self.inductance = inductance
    
    def __str__(self):
        return f"Катушка {self.name}: {self.inductance} Гн"


class Circuit:
    """Электрическая цепь"""
    
    def __init__(self, name: str = "Circuit"):
        self.name = name
        self.components: List[Component] = []
        self.connections: Dict = {}
    
    def add_component(self, component: Component):
        """Добавить компонент в цепь"""
        self.components.append(component)
    
    def remove_component(self, component_name: str):
        """Удалить компонент из цепи"""
        self.components = [c for c in self.components if c.name != component_name]
    
    def get_total_resistance(self) -> float:
        """Получить общее сопротивление цепи (для последовательного соединения)"""
        total = 0.0
        for component in self.components:
            if isinstance(component, Resistor):
                total += component.resistance
        return total
    
    def __str__(self):
        components_str = "\n".join([str(c) for c in self.components])
        return f"Цепь {self.name}:\n{components_str}"
