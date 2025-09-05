"""
Пример использования библиотеки ElectroPy
"""

import sys
import os

# Добавляем путь к модулю electroPy
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from electroPy import Circuit, Resistor, Capacitor, ohms_law, power_calculation, parallel_resistance


def main():
    print("=== ElectroPy Example ===\n")
    
    # Создаем цепь
    circuit = Circuit("Пример цепи")
    
    # Добавляем компоненты
    r1 = Resistor("R1", 100)  # 100 Ом
    r2 = Resistor("R2", 220)  # 220 Ом
    c1 = Capacitor("C1", 0.001)  # 1 мФ
    
    circuit.add_component(r1)
    circuit.add_component(r2)
    circuit.add_component(c1)
    
    print(circuit)
    print(f"\nОбщее сопротивление (последовательно): {circuit.get_total_resistance()} Ом\n")
    
    # Примеры расчетов
    print("=== Расчеты по закону Ома ===")
    
    # Известны напряжение и сопротивление, найти ток
    voltage = 12  # 12 В
    resistance = 100  # 100 Ом
    current = ohms_law(voltage=voltage, resistance=resistance)
    print(f"При U={voltage}В и R={resistance}Ом, ток I={current:.3f}А")
    
    # Расчет мощности
    power = power_calculation(voltage=voltage, current=current)
    print(f"Мощность P={power:.3f}Вт")
    
    print("\n=== Параллельное соединение резисторов ===")
    r_parallel = parallel_resistance(100, 220, 470)
    print(f"Параллельное соединение 100Ом, 220Ом, 470Ом = {r_parallel:.2f}Ом")
    

if __name__ == "__main__":
    main()
