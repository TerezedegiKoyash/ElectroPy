import math

# BASIC CONCEPTS OF ELECTRICITY

# 1.1 Static electricity 
class StaticElectricity:
    
    def __init__(self):
        self.charges = self.getCharges()
        self.electron_mobility = self.electronMobility()
        self.atomic_identity = self.atomicIdentity()
        self.isotope_example = self.isotopeExample()
        
    def getCharges(self):
        """Define basic charge values for particles"""
        neutral_charge = 0
        positive_charge = +1
        negative_charge = -1
        neutrons_charge = neutral_charge
        protonic_charge = positive_charge
        electronic_charge = negative_charge

        return {
            'neutral_charge': neutral_charge,
            'positive_charge': positive_charge,
            'negative_charge': negative_charge,
            'neutrons_charge': neutrons_charge,
            'protonic_charge': protonic_charge,
            'electronic_charge': electronic_charge
        }
    
    def getAtomicCharge(self, protons, neutrons, electrons):
        """Calculate total charge of an atom"""
        proton_charge = protons * self.charges['protonic_charge']
        neutron_charge = neutrons * self.charges['neutrons_charge']
        electron_charge = electrons * self.charges['electronic_charge']

        return proton_charge + neutron_charge + electron_charge

    def electronMobility(self):
        """Properties of particle removal from atoms"""
        return {
            'electrons_easily_removed': True,
            'protons_hardly_removed': False,
            'neutrons_hardly_removed': False
        }

    def atomicIdentity(self):
        """Define particle types and element identity rule"""
        
        return {
            'proton_count_determines_element': True,
            'proton': 'proton',
            'neutron': 'neutron',
            'electron': 'electron'
        }
        
    def isotopeExample(self):
        """Create hydrogen-1 (protium) example"""
        proton_count = 1
        neutron_count = 0
        electron_count = 1

        protium = {
            'proton': proton_count,
            'neutron': neutron_count,
            'electron': electron_count
        }
        protium_charge = self.getAtomicCharge(proton_count, neutron_count, electron_count)
        # Hydrogen-1, the most common isotope of hydrogen, has 1 proton, 0 neutrons, and 1 electron
        # the electric charge of protium is 0, because it has 1 proton (+1) and 1 electron (-1)

        return {
            'atom': protium,
            'charge': protium_charge,
            'is_neutral': protium_charge == 0,
            'element': 'Hydrogen-1 (Protium)'
        }

# 1.2 Conductors, insulators, and electron flow 
class ElectricalSubstances: 
    
    def __init__(self):
        self.conductors = self.getConductors()
        self.insulators = self.getInsulators()
        self.metals = self.getMetals()
        self.current_types = self.getCurrentTypes()

    def getConductors(self):
        """Properties of conductive substances"""
        return {
            'free_electrons': True,
            'description': 'In conductive materials, the outer electrons in each atom can easily come or go, and are called free electrons.'
        }
        
    def getInsulators(self):
        """Properties of insulative substances"""
        return {
            'free_electrons': False,
            'description': 'In insulators, the outer electrons are tightly bound to their atoms and cannot move freely.'
        }
        
    def getMetals(self):
        """Properties of metals as conductors"""
        return {
            'good_conductors': True,
            'description': 'Metals are good conductors because their atoms have few outer electrons that are loosely bound.'
        }
    
    def getCurrentTypes(self):
        """Types of electrical phenomena"""
        return {
            'electric_current': True,
            'static_electricity': False,
            'electric_current_description': 'Dynamic electricity, or electric current, is the uniform motion of electrons through a conductor.',
            'static_electricity_description': 'Static electricity is the accumulation of excess electric charge on an object.'
        }
        
    def getCircuitTypes(self):
        """Types of electric circuits"""
        return {
            'complete_circuit': {
                'status': True,
                'current_flows': True,
                'description': 'A complete circuit is a closed loop that allows current to flow.'
            },
            'broken_circuit': {
                'status': True,
                'current_flows': False,
                'description': 'A broken circuit is an open loop that prevents current from flowing.'
            }
        }

# 1.3 Electric circuits
class ElectricCircuits:

    def __init__(self):
        self.electrical_substances = ElectricalSubstances()
        circuit_types = self.electrical_substances.getCircuitTypes()
        self.complete_circuit = circuit_types['complete_circuit']
        self.broken_circuit = circuit_types['broken_circuit']
        self.is_complete = True # circuit starts as complete
        self.current_flows = self.checkCurrentFlow()
        self.circuit_description = self.getCircuitDescription()

    def checkCurrentFlow(self):
        """Determine if current flows based on circuit status"""
        if self.is_complete == self.complete_circuit['current_flows']:
            return { 'complete_circuit': self.complete_circuit }
        elif self.is_complete == self.broken_circuit['current_flows']:
            return { 'broken_circuit': self.broken_circuit }

    def breakCircuit(self):
        """Simulate breaking the circuit"""
        self.is_complete = False
        self.current_flows = self.checkCurrentFlow()
        return self.current_flows

    def completeCircuit(self):
        """Simulate completing the circuit"""
        self.is_complete = True
        self.current_flows = self.checkCurrentFlow()
        return self.current_flows

    def getCircuitDescription(self):
        """Get descriptions of circuit types"""
        circuit_description = self.electrical_substances.getCircuitTypes()
        return {
            'complete_circuit_description': circuit_description['complete_circuit']['description'],
            'broken_circuit_description': circuit_description['broken_circuit']['description']
        }


# 1.4 Voltage and current 
class VoltageAndCurrent:
    
    def __init__(self):
        self.electrostatic_force = True
        self.voltage = True
        self.voltage_drop = True
        self.current = True
        self.current_constant_in_single_loop = True
        self.polarity = self.getPolarity()
        self.circuit_broken = ElectricalSubstances().getCircuitTypes()['broken_circuit']

    def getPolarity(self):
        """Define polarity of voltage drop"""
        positive_terminal = '+'
        negative_terminal = '-'
        return {
            'positive_terminal': positive_terminal,
            'negative_terminal': negative_terminal,
            'polarity': positive_terminal + negative_terminal,
            'description': 'The +/- orientation of a voltage drop is called the polarity. It is also relative between two points.'
        }
        
    def getVoltageAcrossBreak(self, source_voltage):
        """Determine voltage across a break in the circuit"""
        if not self.circuit_broken['current_flows']:
            return source_voltage
        else:
            return 0


# 1.5 Resistance
class Resistance: 

    def __init__(self):
        self.resistance = True
        self.short_circuit = True
        self.short_circuit_dangerous = True
        self.open_circuit = False
        self.closed_circuit = True
        self.switch = True
    
    def getCircuitResistance(self, circuit_type):
        """Determine resistance based on circuit type"""
        if circuit_type == 'open':
            return math.inf
        elif circuit_type == 'closed':
            return 0
        elif circuit_type == 'short':
            return 0.001
        
    def getCurrentFlow(self, circuit_type):
        """Determine if current flows based on circuit type"""
        if circuit_type == 'open':
            return False
        elif circuit_type in ['closed', 'short']:
            return True
        else:
            return False
    
    def getSwitchState(self, switch_position):
        """Get switch resistance and current flow"""
        flow = ElectricCircuits()
        break_flow = flow.breakCircuit()
        complete_flow = flow.completeCircuit()
        if switch_position == 'open':
            return {
                'resistance': math.inf,
                'current_flows': break_flow,
                'description': 'Open switch creates an open circuit with infinite resistance.'
            }
        elif switch_position == 'closed':
            return {
                'resistance': 0,
                'current_flows': complete_flow,
                'description': 'Closed switch creates a closed circuit with very low resistance.'
            }

# 1.6 Voltage and current in a practical circuit 
class PracticalCircuit:
    
    def __init__(self):
        self.voltage_dropped_across_resistance = True
        self.current_uniform_voltage_varies = True
        
    def explainVoltageCurrent(self):
        """Explain voltage and current behavior in a practical circuit"""
        return {
            'voltage_behavior': 'In a practical circuit, voltage is dropped across the resistance.',
            'current_behavior': 'Current remains uniform throughout the circuit, while voltage varies depending on resistance.'
        }

# 1.7 Conventional versus electron flow 
class CurrentFlow:
    
    def __init__(self):
        self.conventional_flow = True
        self.electron_flow = False
        self.conventional_direction = '+ -> -'
        self.electron_direction = '- -> +'
        self.flow_directions_opposite = True
        
    def getCompareFlows(self):
        """Compare conventional and electron flow directions"""
        return {
            'conventional_flow_direction': self.conventional_direction,
            'electron_flow_direction': self.electron_direction,
            'are_opposite': self.flow_directions_opposite,
            'description': 'Conventional current flow is from positive to negative, while electron flow is from negative to positive.'
        }