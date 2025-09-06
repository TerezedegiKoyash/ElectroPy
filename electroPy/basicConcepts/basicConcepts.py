import math

# BASIC CONCEPTS OF ELECTRICITY

# 1.1 Static electricity 

neutral_charge = 0 
positive_charge = +1 
negative_charge = -1 

neutrons_charge = 0 # Neutrons have a neutral (0) electric charge
protonic_charge = +1 # Protons have a positive (+1) electric charge
electronic_charge = -1 # Electrons have a negative (-1) electric charge

electronic_charge == negative_charge # electrons_charge is the same as negative_charge
protonic_charge == positive_charge # protons_charge is the same as positive_charge
neutrons_charge == neutral_charge # neutrons_charge is the same as neutral_charge

atomic_charge = positive_charge + negative_charge + neutral_charge # an atom is neutral if it has equal numbers of protons and electrons
atomic_charge = electronic_charge + protonic_charge + neutrons_charge # an atom is neutral if it has equal numbers of protons and electrons

electrons_easily_removed = True
protons_hardly_removed = False
neutrons_hardly_removed = False # electrons can be dislodged from atoms much easier than protons or neutrons

proton_count_determines_element = True # the number of protons in an atom's nucleus determines its identity as a unique element

proton = 'proton'
neutron = 'neutron'
electron = 'electron'

protius = {
    proton: 1, 
    neutron: 0, 
    electron: 1
    } # Hydrogen-1, the most common isotope of hydrogen, has 1 proton, 0 neutrons, and 1 electron
protius_charge = protius[proton] + protius[electron] + protius[neutron] # the electric charge of protius is 0, because it has 1 proton (+1) and 1 electron (-1)

# 1.2 Conductors, insulators, and electron flow 

conductors = True # in conductive materials, the outer electrons in each atom can easily come or go, and are called free electrons

insulators = False # in insulators, the outer electrons are tightly bound to their atoms and cannot move freely

metals = True # metals are good conductors because their atoms have few outer electrons that are loosely bound

electric_current = True # dynamic electricity, or electric current, is the uniform motion of electrons through a conductor

static_electricity = False # static electricity is the accumulation of excess electric charge on an object

complete_circuit = True # a complete circuit is a closed loop that allows current to flow

# 1.3 Electric circuits

broken_circuit = False # a broken circuit is an open loop that prevents current from flowing

if complete_circuit:
    current_flows = True
    
elif not complete_circuit:
    current_flows = False
    
elif broken_circuit:
    current_flows = False

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

