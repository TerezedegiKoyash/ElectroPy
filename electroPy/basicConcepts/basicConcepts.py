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

# 1.5 Resistance

# 1.6 Voltage and current in a practical circuit 

# 1.7 Conventional versus electron flow 