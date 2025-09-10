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

class NonlinearConduction:
    
    def __init__(self):
        self.linear_function = True    # plotted as straight line on graph
        self.nonlinear_function = True # not a straight line
        self.stable_resistance = True  # most conductive materials
        self.variable_resistance = True # some materials change resistance
        
    def getConductionTypes(self):
        """Types of electrical conduction"""
        return {
            'linear_conduction': {
                'definition': 'Any function that can be plotted on a graph as a straight line',
                'characteristic': 'Stable resistance over wide range of conditions',
                'formula': 'I = E/R (straight line plot of current over voltage)',
                'materials': 'Most conductive materials (metals, carbon)'
            },
            'nonlinear_conduction': {
                'definition': 'Resistance varies with changes in voltage or current',
                'characteristic': 'Plot of current over voltage is not a straight line',
                'cause': 'Resistance changes with operating conditions',
                'examples': 'Semiconductor devices, gas discharge tubes'
            }
        }
    
    def getVaristorProperties(self):
        """Properties of varistor components"""
        return {
            'varistor_definition': 'Component that changes resistance with voltage across it',
            'normal_operation': {
                'low_voltage': 'High resistance with little voltage across it',
                'protection_mode': 'Resistance decreases dramatically at breakdown voltage'
            },
            'breakdown_voltage': {
                'also_called': 'Firing voltage',
                'behavior': 'Resistance drops suddenly when voltage reaches this level',
                'application': 'Surge protection in electrical circuits'
            }
        }
    
    def getNegativeResistance(self):
        """Explain negative resistance phenomenon"""
        return {
            'negative_resistance_definition': 'Current decreases as applied voltage increases',
            'unusual_behavior': 'Opposite of normal resistive behavior',
            'examples': {
                'electron_tubes': 'Tetrode tube exhibits negative resistance',
                'semiconductor_diodes': 'Esaki (tunnel) diode shows negative resistance'
            },
            'voltage_range': 'Occurs over certain range of voltages only',
            'applications': 'Used in oscillators and amplifiers'
        }
    
    def explainResistanceStability(self):
        """Explain why some materials have stable vs variable resistance"""
        return {
            'stable_materials': {
                'characteristic': 'Resistance stable over wide range of conditions',
                'examples': 'Most metals, carbon resistors',
                'graph_behavior': 'Linear I-V relationship (straight line)'
            },
            'variable_materials': {
                'characteristic': 'Resistance changes with voltage, current, or temperature',
                'factors': ['Temperature', 'Electric field strength', 'Current density'],
                'graph_behavior': 'Nonlinear I-V relationship (curved line)'
            },
            'practical_implications': {
                'circuit_design': 'Must account for resistance variations',
                'component_selection': 'Choose appropriate device for application'
            }
        }
    
    def getIVCharacteristics(self):
        """Current-Voltage characteristics of different devices"""
        return {
            'linear_devices': {
                'resistor': 'Straight line through origin (I = V/R)',
                'slope': 'Slope = 1/R (conductance)'
            },
            'nonlinear_devices': {
                'diode': 'Exponential curve, conducts mainly one direction',
                'varistor': 'Low current until breakdown, then sharp increase',
                'tunnel_diode': 'Shows negative resistance region',
                'incandescent_bulb': 'Resistance increases with temperature/current'
            }
        }

# 2.7 Circuit wiring

class CircuitWiring:
    
    def __init__(self):
        self.ideal_wire_resistance = 0  # Assumed zero resistance
        self.real_wire_resistance = True  # Has some resistance in reality
        self.electrically_common_points = True
        self.wire_length_irrelevant = True
        
    def getWiringAssumptions(self):
        """Basic assumptions about circuit wiring"""
        return {
            'zero_resistance_assumption': {
                'ideal_condition': 'Connecting wires assumed to have zero resistance',
                'unless_stated': 'Exception when wire resistance is specifically mentioned',
                'purpose': 'Simplifies circuit analysis'
            },
            'wire_length_flexibility': {
                'rule': 'Wires can be shortened or lengthened without impacting circuit function',
                'what_matters': 'Components must be attached in same sequence',
                'implication': 'Physical wire length irrelevant to electrical function'
            }
        }
    
    def getElectricalCommonPoints(self):
        """Explain electrically common points in circuits"""
        return {
            'definition': 'Points directly connected by zero resistance wire',
            'characteristics': {
                'zero_voltage_drop': 'Zero voltage dropped between common points',
                'regardless_of_current': 'True regardless of current magnitude (ideally)',
                'same_potential': 'All common points at same electrical potential'
            },
            'measurement_implications': {
                'voltage_readings': 'Same voltage readings between sets of common points',
                'resistance_readings': 'Same resistance readings between common points',
                'practical_use': 'Simplifies circuit analysis and troubleshooting'
            }
        }
    
    def getIdealVsRealConditions(self):
        """Compare ideal and real-world wiring conditions"""
        return {
            'ideal_conditions': {
                'wire_resistance': 'Absolutely zero resistance',
                'voltage_drop': 'No voltage drop across wires',
                'current_capacity': 'Unlimited current capacity',
                'use_case': 'Theoretical circuit analysis'
            },
            'real_world_conditions': {
                'wire_resistance': 'Small but non-zero resistance',
                'voltage_drop': 'Slight voltage drop under high current',
                'current_capacity': 'Limited by wire gauge and heat dissipation',
                'design_consideration': 'Wire resistance should be low enough for general principles to hold'
            },
            'practical_application': {
                'circuit_design': 'Choose appropriate wire gauge for current levels',
                'analysis_validity': 'Ideal assumptions valid when wire resistance << circuit resistance'
            }
        }
    
    def explainWireResistanceEffects(self):
        """Explain when wire resistance becomes significant"""
        return {
            'negligible_conditions': {
                'low_current_circuits': 'Wire resistance effect minimal',
                'short_wire_runs': 'Resistance proportional to length',
                'thick_wires': 'Lower resistance with larger cross-sectional area'
            },
            'significant_conditions': {
                'high_current_circuits': 'Wire voltage drop becomes noticeable',
                'long_wire_runs': 'Resistance adds up over distance',
                'thin_wires': 'Higher resistance limits current capacity'
            },
            'practical_examples': {
                'household_wiring': 'Heavy appliances need thick wires',
                'automotive': 'Starter circuits use very thick cables',
                'electronics': 'PCB traces designed for minimal resistance'
            }
        }
    
    def calculateWireResistance(self, resistivity, length, cross_sectional_area):
        """Calculate wire resistance using material properties"""
        return {
            'formula': 'R = ρ × L / A',
            'calculated_resistance': (resistivity * length) / cross_sectional_area,
            'units': 'ohms (Ω)',
            'parameters': {
                'resistivity': f'{resistivity} Ω·m (material property)',
                'length': f'{length} m',
                'area': f'{cross_sectional_area} m²'
            }
        }

# 2.8 Polarity of voltage drops

class VoltageDropPolarity:
    
    def __init__(self):
        self.electron_flow_direction = True
        self.conventional_current_direction = True
        self.voltage_drop_polarity = True
        self.resistive_component_polarity = True
        
    def getPolarityRules(self):
        """Rules for determining voltage drop polarity"""
        return {
            'electron_flow_rule': {
                'description': 'Polarity determined by direction of electron flow through resistive component',
                'negative_terminal': 'Where electrons enter the component',
                'positive_terminal': 'Where electrons exit the component',
                'principle': 'Electrons flow from negative to positive through the component'
            },
            'conventional_current_rule': {
                'description': 'Conventional current flows opposite to electron flow',
                'positive_terminal': 'Where conventional current enters the component',
                'negative_terminal': 'Where conventional current exits the component',
                'relationship': 'Opposite polarity compared to electron flow direction'
            }
        }
    
    def explainPolarityDetermination(self):
        """Explain how to determine voltage drop polarity"""
        return {
            'step_1': 'Identify direction of current flow through component',
            'step_2_electron_flow': {
                'method': 'Using electron flow convention',
                'negative_end': 'Mark negative (-) where electrons enter',
                'positive_end': 'Mark positive (+) where electrons exit'
            },
            'step_2_conventional': {
                'method': 'Using conventional current convention',
                'positive_end': 'Mark positive (+) where conventional current enters',
                'negative_end': 'Mark negative (-) where conventional current exits'
            },
            'result': 'Voltage drop polarity established across resistive component'
        }
    
    def getVoltageDropExamples(self):
        """Examples of voltage drop polarity in circuits"""
        return {
            'simple_resistor_circuit': {
                'description': 'Single resistor with battery',
                'electron_flow': 'From battery negative terminal through resistor to positive terminal',
                'resistor_polarity': 'Negative where electrons enter, positive where electrons exit',
                'voltage_measurement': 'Positive voltage drop measured from negative to positive end'
            },
            'multiple_resistors': {
                'description': 'Series circuit with multiple resistors',
                'current_direction': 'Same current flows through all resistors',
                'individual_polarities': 'Each resistor has voltage drop with same polarity pattern',
                'sum_verification': 'Sum of voltage drops equals source voltage'
            }
        }
    
    def explainPolarityImportance(self):
        """Explain why voltage drop polarity matters"""
        return {
            'circuit_analysis': {
                'kirchhoffs_voltage_law': 'Correct polarity needed for KVL calculations',
                'voltage_summation': 'Signs matter when adding voltage drops',
                'troubleshooting': 'Polarity helps identify circuit problems'
            },
            'measurement_techniques': {
                'multimeter_connections': 'Red probe to positive, black to negative',
                'expected_readings': 'Positive reading confirms correct polarity',
                'reverse_connection': 'Negative reading indicates reversed polarity'
            },
            'practical_applications': {
                'component_orientation': 'Some components are polarity sensitive',
                'circuit_design': 'Proper polarity ensures correct operation',
                'safety_considerations': 'Wrong polarity can damage sensitive components'
            }
        }
    
    def compareFlowConventions(self):
        """Compare electron flow vs conventional current for polarity"""
        return {
            'electron_flow_convention': {
                'flow_direction': 'Negative to positive terminal (actual electron movement)',
                'voltage_drop_polarity': 'Negative where electrons enter, positive where they exit',
                'used_by': 'Some textbooks and electron theory explanations'
            },
            'conventional_current_convention': {
                'flow_direction': 'Positive to negative terminal (historical convention)',
                'voltage_drop_polarity': 'Positive where current enters, negative where it exits',
                'used_by': 'Most engineering practices and circuit analysis'
            },
            'consistency_requirement': {
                'important_note': 'Use same convention throughout entire analysis',
                'result': 'Both methods give same final answers when used consistently',
                'recommendation': 'Choose one convention and stick with it'
            }
        }
        
# 2.9 Computer simulation of electric circuits

class CircuitSimulation:
    
    def __init__(self):
        self.simulation_software = True
        self.spice_simulators = True
        self.educational_simulators = True
        
    def getSimulationTools(self):
        """Circuit simulation tools and software"""
        return {
            'professional_tools': {
                'SPICE': 'Industry standard circuit simulator',
                'LTSpice': 'Free version from Linear Technology', 
                'PSpice': 'Commercial SPICE version',
                'Multisim': 'Educational circuit simulation'
            },
            'educational_tools': {
                'CircuitJS': 'Web-based circuit simulator',
                'Tinkercad': 'Online electronics simulator',
                'PhET': 'Interactive physics simulations',
                'EveryCircuit': 'Visual circuit simulator'
            },
            'advantages': {
                'cost_effective': 'Test circuits without physical components',
                'safety': 'No risk of damage or injury',
                'analysis': 'Detailed measurements and waveform viewing',
                'iteration': 'Quick design modifications and testing',
                'learning': 'Visual feedback helps understand concepts'
            }
        }
    
    def simulateOhmsLawCircuit(self, voltage, resistance):
        """Simulate basic Ohm's Law circuit"""
        current = voltage / resistance
        power = voltage * current
        
        return {
            'input_parameters': {
                'source_voltage': f"{voltage} V",
                'resistance': f"{resistance} Ω"
            },
            'calculated_results': {
                'current': f"{current:.3f} A",
                'power': f"{power:.3f} W"
            },
            'verification': {
                'ohms_law': f"V = I × R: {voltage} = {current:.3f} × {resistance}",
                'power_law': f"P = V × I: {power:.3f} = {voltage} × {current:.3f}"
            }
        }
    
    def getSimulationBenefits(self):
        """Benefits of using circuit simulation"""
        return {
            'educational_benefits': {
                'visualization': 'See current flow and voltage drops',
                'experimentation': 'Try different component values safely',
                'understanding': 'Immediate feedback helps learning'
            },
            'practical_benefits': {
                'prototyping': 'Test designs before building',
                'troubleshooting': 'Identify problems early',
                'optimization': 'Fine-tune component values'
            },
            'limitations': {
                'ideal_components': 'May not account for real-world imperfections',
                'temperature_effects': 'Limited modeling of thermal effects',
                'parasitic_elements': 'May ignore stray capacitance/inductance'
            }
        }
