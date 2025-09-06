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
            'complete_circuit': True,
            'broken_circuit': False,
            'complete_circuit_description': 'A complete circuit is a closed loop that allows current to flow.',
            'broken_circuit_description': 'A broken circuit is an open loop that prevents current from flowing.'
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
        if self.is_complete == True:
            return { 'complete_circuit': self.complete_circuit }
        elif self.is_complete == False:
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
            'complete_circuit_description': circuit_description['complete_circuit_description'],
            'broken_circuit_description': circuit_description['broken_circuit_description']
        }


# 1.4 Voltage and current 

electrostatic_force = True # electrons can be motivated to flow through a conductor by the same force manifested in static electricity

voltage = True # voltage is the measure of specific potential energy (potential energy per unit charge) between two locations, the measure of "push" available to motivate electrons

voltage_drop = True # voltage, as an expression of potential energy, is always relative between two locations, or points. Sometimes it is called a voltage "drop."

current = True # when a voltage source is connected to a circuit, the voltage will cause a uniform flow of electrons through that circuit called a current

current_constant_in_single_loop = True # in a single (one loop) circuit, the amount of current at any point is the same as the amount of current at any other point

if broken_circuit:
    voltage_across_break = voltage # if a circuit containing a voltage source is broken, the full voltage of that source will appear across the points of the break

positive_terminal = '+'
negative_terminal = '-'
polarity = positive_terminal + negative_terminal # the +/- orientation of a voltage drop is called the polarity. It is also relative between two points

# 1.5 Resistance

resistance = True # resistance is the measure of opposition to electric current

short_circuit = True # a short circuit is an electric circuit offering little or no resistance to the flow of electrons
short_circuit_dangerous = True # short circuits are dangerous with high voltage power sources because the high currents encountered can cause large amounts of heat energy to be released

open_circuit = False # an open circuit has infinite resistance, because no current can flow
close_circuit = True # a closed circuit has very low resistance, because current can flow easily

if complete_circuit == open_circuit:
    resistance = math.inf # infinite resistance in an open circuit
    current_flows = False
    
elif complete_circuit == close_circuit:
    resistance = 0 # zero resistance in a closed circuit
    current_flows = True
    
elif broken_circuit == close_circuit or complete_circuit == open_circuit:
    resistance = math.inf
    current_flows = False
    
switch = True # a switch is a device that can open or close a circuit
    
switch_open = False # an open switch creates an open circuit with infinite resistance
switch_closed = True # a closed switch creates a closed circuit with very low resistance

if switch == switch_open:
    resistance = math.inf
    current_flows = False
    
elif switch == switch_closed:
    resistance = 0
    current_flows = True

# 1.6 Voltage and current in a practical circuit 

voltage_dropped_across_resistance = True # because it takes energy to force electrons to flow against the opposition of a resistance, there will be voltage manifested (or "dropped") between any points in a circuit with resistance between them

current_uniform_voltage_varies = True # although the amount of current is uniform in a simple circuit, the amount of voltage between different sets of points in a single circuit may vary considerably

# 1.7 Conventional versus electron flow 

conventional_flow = True # conventional flow assumes current flows from positive to negative terminal
electron_flow = False # electron flow is the actual physical movement of electrons from negative to positive terminal

conventional_current_direction = '+' + ' -> ' + '-' # conventional current flows from positive to negative
electron_flow_direction = '-' + ' -> ' + '+' # electrons actually flow from negative to positive

flow_directions_opposite = True # conventional flow and electron flow are opposite in direction but mathematically equivalent

