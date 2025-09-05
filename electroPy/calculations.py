"""
Модуль для физических расчетов в электрических цепях
"""

from typing import Optional


def ohms_law(voltage: Optional[float] = None, 
             current: Optional[float] = None, 
             resistance: Optional[float] = None) -> float:
    """
    Закон Ома: U = I * R
    
    Args:
        voltage: Напряжение (В)
        current: Ток (А)
        resistance: Сопротивление (Ом)
    
    Returns:
        Недостающий параметр
    
    Raises:
        ValueError: Если предоставлено неправильное количество параметров
    """
    provided_params = sum(x is not None for x in [voltage, current, resistance])
    
    if provided_params != 2:
        raise ValueError("Необходимо предоставить ровно 2 параметра из 3")
    
    if voltage is None:
        return current * resistance
    elif current is None:
        return voltage / resistance
    elif resistance is None:
        return voltage / current


def power_calculation(voltage: Optional[float] = None,
                     current: Optional[float] = None,
                     resistance: Optional[float] = None,
                     power: Optional[float] = None) -> float:
    """
    Расчет мощности: P = U * I = I² * R = U² / R
    
    Args:
        voltage: Напряжение (В)
        current: Ток (А) 
        resistance: Сопротивление (Ом)
        power: Мощность (Вт)
    
    Returns:
        Недостающий параметр
    """
    provided_params = sum(x is not None for x in [voltage, current, resistance, power])
    
    if provided_params < 2:
        raise ValueError("Необходимо предоставить минимум 2 параметра")
    
    # Если мощность не дана, вычисляем её
    if power is None:
        if voltage is not None and current is not None:
            return voltage * current
        elif current is not None and resistance is not None:
            return current ** 2 * resistance
        elif voltage is not None and resistance is not None:
            return voltage ** 2 / resistance
        else:
            raise ValueError("Недостаточно данных для расчета мощности")
    
    # Если мощность дана, вычисляем недостающий параметр
    if voltage is None:
        if current is not None and resistance is not None:
            return current * resistance
        elif current is not None:
            return power / current
        elif resistance is not None:
            return (power * resistance) ** 0.5
    
    if current is None:
        if voltage is not None and resistance is not None:
            return voltage / resistance
        elif voltage is not None:
            return power / voltage
        elif resistance is not None:
            return (power / resistance) ** 0.5
    
    if resistance is None:
        if voltage is not None and current is not None:
            return voltage / current
        elif voltage is not None:
            return voltage ** 2 / power
        elif current is not None:
            return power / (current ** 2)
    
    raise ValueError("Невозможно вычислить недостающий параметр")


def parallel_resistance(*resistances: float) -> float:
    """
    Расчет общего сопротивления при параллельном соединении
    1/R_total = 1/R1 + 1/R2 + ... + 1/Rn
    """
    if not resistances:
        return 0.0
    
    reciprocal_sum = sum(1/r for r in resistances if r != 0)
    return 1/reciprocal_sum if reciprocal_sum != 0 else float('inf')


def series_resistance(*resistances: float) -> float:
    """
    Расчет общего сопротивления при последовательном соединении
    R_total = R1 + R2 + ... + Rn
    """
    return sum(resistances)


def voltage_divider(input_voltage: float, r1: float, r2: float) -> float:
    """
    Делитель напряжения
    U_out = U_in * R2 / (R1 + R2)
    """
    return input_voltage * r2 / (r1 + r2)
