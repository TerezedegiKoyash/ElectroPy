# OHM’s LAW

# 2.1 How voltage, current, and resistance relate

class OhmsLaw:
    def __init__(self):
        self.voltage = 'E'  # Voltage (E) in volts (V)
        self.current = 'I'  # Current (I) in amperes (A)
        self.resistance = 'R'  # Resistance (R) in ohms (Ω)
        self.coulomb = 'Q' # Coulomb (Q) in coulombs (C)
        self.coulomb_charge = 6.24e18  # number of electrons in one coulomb
        
    def getOhmsLawFormulas(self):
        """Return Ohm's Law formulas"""
        return {
            'voltage_formula': 'E = I * R',
            'current_formula': 'I = E / R',
            'resistance_formula': 'R = E / I'
        }
    
    def getVoltage(self, current, resistance):
        """Calculate voltage using Ohm's Law"""
        return current * resistance
    
    def getCurrent(self, voltage, resistance):
        """Calculate current using Ohm's Law"""
        return voltage / resistance

    def getResistance(self, voltage, current):
        """Calculate resistance using Ohm's Law"""
        return voltage / current

# 2.2 An analogy for Ohm’s Law

class OhmsLawAnalogy:
    def __init__(self):
        self.water_flow_analogy = True
        self.voltage_analogy = 'water pressure'
        self.current_analogy = 'water flow rate'
        self.resistance_analogy = 'pipe size/restrictions'
        
    def getAnalogyDescriptions(self):
        """Return descriptions of the water analogy for Ohm's Law"""
        return {
            'voltage_like_pressure': 'Voltage is like water pressure - it pushes current through circuit',
            'current_like_flow': 'Current is like water flow rate - amount flowing per second',
            'resistance_like_restrictions': 'Resistance is like pipe restrictions - limits flow',
            'relationship': 'Higher pressure = more flow, but restrictions limit the flow',
            'ohms_law_analogy': 'Flow Rate = Pressure / Restrictions'
        }
        
    def getVoltageCurrentRelationship(self):
        """Explain voltage-current relationship with steady resistance"""
        return {
            'steady_resistance': 'With resistance steady, current follows voltage',
            'voltage_increase': 'An increase in voltage means an increase in current',
            'voltage_decrease': 'A decrease in voltage means a decrease in current',
            'direct_relationship': 'Voltage and current have a direct proportional relationship'
        }

# 2.3 Power in electric circuits

class ElectricPower:
    def __init__(self):
        self.power = 'P'  # Power (P) in watts (W)
        self.voltage = 'E'  # Voltage (E) in volts (V)
        self.current = 'I'  # Current (I) in amperes (A)
        self.watt_per_horsepower = 746  # 1 horsepower = 746 watts
        
    def getPowerFormulas(self):
        """Return electric power formulas"""
        return {
            'basic_power': 'P = E * I',  # Power = Voltage × Current
        }
    
    def getPower(self, voltage, current):
        """Calculate power using voltage and current"""
        return voltage * current
    
    def getVoltage(self, power, current):
        """Calculate voltage using power and current"""
        return power / current

    def getCurrent(self, power, voltage):
        """Calculate current using power and voltage"""
        return power / voltage

    def convertHorsepowerToWatts(self, horsepower):
        """Convert horsepower to watts"""
        return horsepower * self.watt_per_horsepower
    
    def convertWattsToHorsepower(self, watts):
        """Convert watts to horsepower"""
        return watts / self.watt_per_horsepower
    

# 2.4 Calculating electric power

class CalculatingElectricPower:
    def __init__(self):
        self.electric_power = ElectricPower()
        
    def getPowerFormulas(self):
        """Get electric power formulas"""
        return {
            'power_from_current_and_voltage': self.electric_power.getPowerFormulas(),
            'power_from_resistance_and_current': 'P = I^2 * R',
            'power_from_voltage_and_resistance': 'P = E^2 / R'
        }

    def calculatePowerFromVoltageCurrent(self, voltage, current):
        """Calculate electric power"""
        return self.electric_power.getPower(voltage, current)
    
    def calculatePowerFromResistanceCurrent(self, resistance, current):
        """Calculate power from resistance and current"""
        return (current ** 2) * resistance
    
    def calculatePowerFromVoltageResistance(self, voltage, resistance):
        """Calculate power from voltage and resistance"""
        return (voltage ** 2) / resistance

    def calculateVoltage(self, power, current):
        """Calculate voltage"""
        return self.electric_power.getVoltage(power, current)

    def calculateCurrent(self, power, voltage):
        """Calculate current"""
        return self.electric_power.getCurrent(power, voltage)

# 2.5 Resistors



# 2.6 Nonlinear conduction

# 2.7 Circuit wiring

# 2.8 Polarity of voltage drops

# 2.9 Computer simulation of electric circuits