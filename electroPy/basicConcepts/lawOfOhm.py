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

class Resistors:
    
    def __init__(self):
        self.resistance_rating = True  # rated in ohms (Ω)
        self.power_rating = True       # rated in watts (W) - ability to dissipate heat
        self.tolerance = True          # precision of resistance value
        self.temperature_coefficient = True  # how resistance changes with temperature
        self.load_device = True        # resistors can represent loads in circuits
        
    def getResistorRatings(self):
        """Resistor ratings and specifications"""
        return {
            'resistance_rating': {
                'unit': 'ohms (Ω)',
                'description': 'Precise amount of resistance provided',
                'purpose': 'Controls current flow in circuits'
            },
            'power_rating': {
                'unit': 'watts (W)',
                'description': 'Ability to dissipate heat energy safely',
                'purpose': 'Prevents resistor overheating and damage'
            },
            'tolerance': {
                'unit': 'percentage (%)',
                'description': 'Precision of actual vs. rated resistance',
                'common_values': ['1%', '5%', '10%', '20%']
            }
        }
    
    def getResistorCharacteristics(self):
        """Physical and electrical characteristics of resistors"""
        return {
            'resistance_vs_size': {
                'rule': 'Resistance ratings cannot be determined from physical size',
                'reason': 'Resistance depends on material and construction, not size',
                'identification': 'Use color codes or printed values to determine resistance'
            },
            'power_vs_size': {
                'rule': 'Larger resistor = higher power rating (approximately)',
                'reason': 'Larger surface area dissipates heat more effectively',
                'safety': 'Prevents damage from overheating'
            },
            'load_representation': {
                'definition': 'Any device that performs useful task with electric power',
                'schematic_use': 'Resistor symbols often represent non-specific loads',
                'purpose': 'Simplified circuit analysis and design'
            }
        }
    
    def getResistorTypes(self):
        """Types of resistors"""
        return {
            'fixed_resistors': {
                'carbon_composition': 'Inexpensive, wide tolerance',
                'carbon_film': 'Better stability than composition',
                'metal_film': 'High precision, low noise',
                'wire_wound': 'High power handling capability'
            },
            'variable_resistors': {
                'potentiometer': 'Three terminals, voltage divider',
                'rheostat': 'Two terminals, current control',
                'trimmer': 'Small adjustment resistor'
            }
        }
    
    def calculatePowerDissipation(self, voltage=None, current=None, resistance=None):
        """Calculate power dissipated by resistor"""
        if voltage is not None and current is not None:
            return voltage * current
        elif current is not None and resistance is not None:
            return current**2 * resistance
        elif voltage is not None and resistance is not None:
            return voltage**2 / resistance
        else:
            raise ValueError("Need at least two parameters")
    
    def checkPowerRating(self, calculated_power, rated_power):
        """Check if resistor can handle the calculated power"""
        safety_factor = 0.8  # Use 80% of rated power for safety
        safe_power = rated_power * safety_factor
        
        return {
            'calculated_power': calculated_power,
            'rated_power': rated_power,
            'safe_operating_power': safe_power,
            'is_safe': calculated_power <= safe_power,
            'recommendation': 'Safe to use' if calculated_power <= safe_power else 'Use higher wattage resistor'
        }
        
    def explainLoadConcept(self):
        """Explain the concept of electrical loads"""
        return {
            'load_definition': 'Any device that performs some useful task with electric power',
            'examples': ['Light bulbs', 'Motors', 'Heaters', 'Electronic circuits'],
            'schematic_representation': 'Resistor symbols often represent non-specific loads in diagrams',
            'purpose': 'Simplifies circuit analysis by treating complex devices as resistive loads'
        }

# 2.6 Nonlinear conduction

# 2.7 Circuit wiring

# 2.8 Polarity of voltage drops

# 2.9 Computer simulation of electric circuits