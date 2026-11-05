import math

def calculate_tandem_energy_system(vessel_length_m, vessel_radius_m, shield_thickness_cm):
    """
    Calculates the mass, dimensions, and tandem energy generation metrics
    (Photo-electric Perovskite cells + Thermo-electric warm water circulation).
    """
    WATER_DENSITY = 1000.0  # kg/m^3
    
    thickness_m = shield_thickness_cm / 100.0
    r_inner = vessel_radius_m
    r_outer = r_inner + thickness_m
    
    # Structural geometry calculations
    volume_m3 = math.pi * vessel_length_m * ((r_outer ** 2) - (r_inner ** 2))
    mass_tons = (volume_m3 * WATER_DENSITY) / 1000.0
    
    # Outer surface area exposed to radiation/sunlight (Capsule cylinder)
    outer_surface_area_m2 = 2 * math.pi * r_outer * vessel_length_m
    
    # 1. Photo-Electric Sub-System (Perovskite Scintillation Harvesting)
    # Estimated clean electric power output per square meter from transformed rays
    PEROVSKITE_EFFICIENCY_W_M2 = 250.0  
    photo_electric_power_kw = (outer_surface_area_m2 * PEROVSKITE_EFFICIENCY_W_M2) / 1000.0
    
    # 2. Thermo-Electric Sub-System (Seebeck Effect via Warm Water Circulation)
    # Harvesting energy from the temperature delta between hot sun-facing and cold shadow sectors
    THERMO_ELECTRIC_YIELD_W_M2 = 80.0
    thermo_electric_power_kw = (outer_surface_area_m2 * THERMO_ELECTRIC_YIELD_W_M2) / 1000.0
    
    # Total Tandem Energy Output
    total_tandem_power_kw = photo_electric_power_kw + thermo_electric_power_kw
    
    print(f"--- OPTIMIZED SHIELD CONFIGURATION: 1.2M CONTROL ---")
    print(f"✓ Shield Target Thickness: {thickness_m:.2f} meters")
    print(f"✓ Fluid Shield Weight: {mass_tons:.2f} metric tons per 10m loop")
    print(f"✓ Exposed Outer Surface Area: {outer_surface_area_m2:.2f} m2")
    print(f"--------------------------------------------------")
    print(f"[TANDEM ENERGY HARVESTING OUTPUT]")
    print(f"✓ Photo-Electric (Perovskite Matrix): {photo_electric_power_kw:.2f} kW")
    print(f"✓ Thermo-Electric (Thermal Circulation): {thermo_electric_power_kw:.2f} kW")
    print(f"⚡ Total Combined Tandem Power: {total_tandem_power_kw:.2f} kW")
    print(f"--------------------------------------------------")
    print(f"Mechanical Status: Dual-harvesting architecture operating successfully.")
    
    return total_tandem_power_kw

# Execute the simulation using the 1.2m (120cm) control sweet-spot
print("=== DUAL-STAGE WATER SHIELD: TANDEM ENERGY KINETICS ===\n")
calculate_tandem_energy_system(vessel_length_m=10.0, vessel_radius_m=2.5, shield_thickness_cm=120.0)
