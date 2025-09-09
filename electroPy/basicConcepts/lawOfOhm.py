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



# 2.4 Calculating electric power

# 2.5 Resistors

# 2.6 Nonlinear conduction

# 2.7 Circuit wiring

# 2.8 Polarity of voltage drops

# 2.9 Computer simulation of electric circuits