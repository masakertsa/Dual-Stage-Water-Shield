"""
Dual-Stage Water Shield - Calculation Framework
This script provides the foundational mathematical scaffolding for simulating thermal energy conversion,
radiation attenuation, self-healing chemical kinetics, and AI bioreactor bypass states.
"""

import math

def calculate_radiation_attenuation(water_layer_thickness=1.2, cosmic_ray_flux=1.0):
    """
    Calculates the cosmic radiation reduction through the 1.2-meter water envelope.
    Models the scintillation effect converting ionizing radiation to visible light wavelengths.
    Uses the exponential decay law (Beer-Lambert equivalent) for radiation attenuation.
    
    Parameters:
    - water_layer_thickness (float): Thickness of the shield in meters (default 1.2).
    - cosmic_ray_flux (float): Input radiation levels in Sieverts/hour.
    
    Returns:
    - tuple: (Remaining radiation reaching crew in Sv/h, Light energy flux generated for Perovskite cells in W/m^2)
    """
    if water_layer_thickness <= 0 or cosmic_ray_flux <= 0:
        return (0.0, 0.0)
        
    # Attenuation coefficient for water against high-energy cosmic rays (in m^-1)
    # Water is hydrogen-rich, making it highly effective at absorbing and scattering cosmic protons.
    attenuation_coefficient = 3.5  
    
    # Calculate remaining radiation using exponential decay: I = I0 * e^(-mu * x)
    remaining_radiation = cosmic_ray_flux * math.exp(-attenuation_coefficient * water_layer_thickness)
    
    # Scintillation efficiency: amount of ionizing energy converted down to visible light wavelengths
    scintillation_efficiency = 0.12  # 12% conversion rate into the optical spectrum
    
    # Convert absorbed radiation flux into equivalent optical light energy flux
    absorbed_radiation = cosmic_ray_flux - remaining_radiation
    # Conversion factor from Sievert flux density equivalents to optical energy density (W/m^2)
    energy_conversion_factor = 250.0  
    
    light_energy_flux = absorbed_radiation * energy_conversion_factor * scintillation_efficiency
    
    return (round(remaining_radiation, 6), round(light_energy_flux, 2))


def estimate_seebeck_power_output(sun_side_temp, shadow_side_temp, flow_rate):
    """
    Estimates the kilowatt (kW) energy harvested by the thermoelectric generators (TEGs)
    based on the deep space temperature delta and active water circulation.
    
    Parameters:
    - sun_side_temp (float): Sun-facing hull temperature in Kelvin.
    - shadow_side_temp (float): Shadow-sector hull temperature in Kelvin.
    - flow_rate (float): Active circulation loop flow rate in liters/second.
    
    Returns:
    - float: Total generated power in kilowatts (kW).
    """
    if sun_side_temp <= shadow_side_temp or flow_rate <= 0:
        return 0.0
        
    temp_delta = sun_side_temp - shadow_side_temp
    
    # Seebeck coefficient for advanced bismuth telluride modules (V/K)
    seebeck_coefficient = 0.00022  
    
    # Number of thermocouple junctions integrated into the circulation loops
    number_of_junctions = 15000  
    
    # Internal electrical resistance of the system (Ohms)
    internal_resistance = 1.8  
    
    # Calculate open-circuit voltage: V = N * alpha * dT
    open_circuit_voltage = number_of_junctions * seebeck_coefficient * temp_delta
    
    # Maximum power transfer theorem: P = V^2 / (4 * R)
    max_electrical_power_watts = (open_circuit_voltage ** 2) / (4 * internal_resistance)
    
    # Scale power based on the fluid dynamic heat supply capacity (flow rate limits efficiency)
    fluid_efficiency_factor = min(1.0, flow_rate / 5.0)
    final_power_kw = (max_electrical_power_watts * fluid_efficiency_factor) / 1000.0
    
    return round(final_power_kw, 2)


def simulate_self_healing_kinetics(puncture_diameter, internal_pressure):
    """
    Models the pressure-driven cross-linking polymerization and flash-freezing 
    of the STF/polymer matrix when exposed to the vacuum of space.
    
    Parameters:
    - puncture_diameter (float): Size of the micrometeoroid breach in millimeters.
    - internal_pressure (float): Atmospheric internal vessel pressure in kiloPascals (kPa).
    
    Returns:
    - bool: True if the autogenous freeze-plug seal seals successfully, False if decompression occurs.
    """
    if puncture_diameter <= 0 or internal_pressure <= 0:
        return False
        
    # Critical breach size boundary in mm (large debris cannot be healed by fluid dynamics alone)
    critical_breach_threshold = 45.0  
    
    if puncture_diameter > critical_breach_threshold:
        return False  # Structural failure requires mechanical patching
        
    # Curing and freeze-plug rate factor dictated by outer space thermal drop and pressure drop
    cross_linking_rate_constant = 0.85  
    
    # Time required for the gel polymer matrix to seal the boundary completely (seconds)
    time_to_seal = (puncture_diameter * internal_pressure) / (100.0 * cross_linking_rate_constant)
    
    # The vessel must seal within a 4-second structural window to prevent catastrophic mass depletion
    if time_to_seal <= 4.0:
        return True
    else:
        return False


def monitor_bioreactor_gas_exchange(cell_id, chlorophyll_density):
    """
    Simulates the AI spectroscopic scanning loop tracking CO2 to O2 conversion.
    Triggers isolation sequence if density drops below critical mutation thresholds.
    
    Parameters:
    - cell_id (int): Unique identifier for the parallelized quartz tube unit.
    - chlorophyll_density (float): Current scanned density profile (normalized 0.0 to 1.0).
    
    Returns:
    - str: "OPERATIONAL", "BYPASS_ISOLATED", or "CRITICAL_SYSTEM_ALERT"
    """
    # Critical threshold: mutation or toxic infection drops chlorophyll density below 0.35
    critical_mutation_threshold = 0.35
    
    if chlorophyll_density < 0.0 or chlorophyll_density > 1.0:
        return "CRITICAL_SYSTEM_ALERT"
        
    if chlorophyll_density < critical_mutation_threshold:
        # 0-latency AI network activates magnetic valves to redirect the local atmospheric lines
        return "BYPASS_ISOLATED"
        
    return "OPERATIONAL"


if __name__ == "__main__":
    print("--- Dual-Stage Water Shield: Calculation Framework ---")
    
    # 1. Test Radiation Attenuation through the 1.2-meter envelope (Input: 1.5 Sv/h solar flare environment)
    remaining_rad, light_flux = calculate_radiation_attenuation(1.2, 1.5)
    print(f"1. Remaining Radiation: {remaining_rad} Sv/h | Generated Scintillation Light: {light_flux} W/m^2")
    
    # 2. Test Thermoelectric Seebeck Harvesting (Sun-side = 390K, Shadow-side = 120K, Flow = 3.5 L/s)
    harvested_power = estimate_seebeck_power_output(390, 120, 3.5)
    print(f"2. Harvested Thermoelectric Power: {harvested_power} kW")
    
    # 3. Test Self-Healing Kinetics against a 8mm micrometeoroid breach at 101.3 kPa internal pressure
    sealed_successfully = simulate_self_healing_kinetics(8.0, 101.3)
    print(f"3. Autogenous Puncture Seal Status: {'SUCCESSFUL (Plug Cured)' if sealed_successfully else 'FAILED (Decompression)'}")
    
    # 4. Test AI Spectroscopic Monitoring loop on a healthy quartz bioreactor cell
    reactor_status = monitor_bioreactor_gas_exchange(101, 0.78)
    print(f"4. Quartz Bioreactor Cell #101 Status: {reactor_status}")
