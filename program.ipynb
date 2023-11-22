from command_utils import (
    NumberType,
    calculate_horizontal_skin,
    calculate_crushed_zone_skin,
    calculate_total_skin_factor,
    calculate_critical_flow_rate,
    calculate_wellbore_skin,
)
from math import sqrt, exp, log10, log as ln

"""
THE FOLLOWING QUANTITIES ARE IN FT
"""
rw_wellbore_radius = 0.25
re_drainage_radius = 660
rd_damaged_zone_radius = 0.96
rc_crushed_zone_radius = 0.042
h_oil_column_thickness = 50
# hp_perforated_interval = (15, 20, 25, 30, 35)
hp_perforated_interval = 15
Db = 35

"""
THE FOLLOWING QUANTITIES ARE IN (in)
"""
#
# lp_perforation_length = (6, 18, 30, 42, 48) # in
# lp_perforation_length = (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4.0)  # ft
lp_perforation_length = (0.5, 1.5, 2.5, 3.5, 4.0)  # ft
# (0.36, 0.336, 0.312, 0.288, 0.264, .... , 0.12)
# rp_perforation_radius = (0.36, 0.12)
# rp_perforation_radius = (0.03, 0.01) # in
rp_perforation_radius = (0.0096, 0.0146, 0.0196, 0.0246, 0.0296)  # ft
# hs_spacing_between_perforation = (1, 3) #in
hs_spacing_between_perforation = (
    0.25,
    0.2,
    0.167,
    0.142,
    0.125,
    0.111,
    0.1,
    0.091,
    0.083,
)  # ft

"""
THE FOLLOWING QUANTITIES ARE IN MD (MILLI DARCY)
"""
K_permeability = 110
kc_crushed_zone_permeability = 20
kd_damaged_zone_permeability = 50
kv_vertical_permeability = 110
kh_horizontal_permeability = 110
ko_effective_oil_permeability = 95
# ko_effective_oil_permeability = (93.5, 95)

"""
THE FOLLOWING QUANTITIES ARE IN ACRE
"""
A_area = 31.41  # acre

"""
THE FOLLOWING QUANTITIES ARE IN PERCENTAGE
"""
# phi_porosity = 20
# φ_porosity = 20
φ_porosity = 0.2

"""
THE FOLLOWING QUANTITY(S) ARE  IN 1/psi
"""
Ct_total_compressibility = 0.000015

"""
THE FOLLOWING QUANTITY(S) ARE  IN CENTI-POISE (cp)
"""
μw_water_viscosity = 0.5
# (0.73, 0.757, 0.784, 0.811, 0.838, 0.865, 0.892, 0.919, 0.946, 0.973, 1)
# (0.73, 0.76, 0.79, 0.82, 0.85, 0.88, 0.91, 0.94, 0.97, 1)
# μo_oil_viscosity = (0.73, 1)
μo_oil_viscosity = 0.73

"""
THE FOLLOWING QUANTITY(S) ARE DIMENSIONLESS
"""
Krw_Sor_Water_rel_permeability_at_residual_oil_sat = 0.45
Kro_Swc_Oil_rel_permeability_at_conn_water_sat = 0.8

"""
THE FOLLOWING QUANTITY(S) ARE IN POUND PER CUBIC-FEET (lb/ft^3)
"""
# ρo_oil_density = (47, 39)
ρo_oil_density = 47
# ρw_water_density = (62.4, 63.76)
ρw_water_density = 62.4
ρw_water_density_two = 63.76

"""
THE FOLLOWING QUANTITY(S) ARE IN (bbl/STB)
"""
# Bo_formation_volume_factor = (1, 1.1)

# Bo_formation_volume_factor = (1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7)
Bo_formation_volume_factor = 1

"""
THE FOLLOWING QUANTITY(S) ARE IN degree
"""
phasing = (0, 180, 120, 90, 60, 45)

"""
THE FOLLOWING DICT MAPS EACH MAPS EACH PHASING ANGLE TO ITS GUN-PHASING PARAMETER
"""
GUN_PHASING_PARA = {
    0: {
        "α": "N/A",
        "C1": 0.000016e-5,
        "C2": 2_675e-3,
        "a1": -2_091e-3,
        "a2": 453e-4,
        "b1": 51_313e-4,
        "b2": 18_672e-4,
    },
    180: {
        "α": 50,
        "C1": 0.0026e-5,
        "C2": 4_532e-3,
        "a1": -2_025e-3,
        "a2": 943e-4,
        "b1": 30_373e-4,
        "b2": 18_115e-4,
    },
    120: {
        "α": 64.8,
        "C1": 0.066e-5,
        "C2": 5_320e-3,
        "a1": -2_018e-3,
        "a2": 634e-4,
        "b1": 16_136e-4,
        "b2": 17_770e-4,
    },
    90: {
        "α": 72.6,
        "C1": 0.019e-5,
        "C2": 6_155e-3,
        "a1": -1_905e-3,
        "a2": 1_038e-4,
        "b1": 15_674e-4,
        "b2": 16_935e-4,
    },
    60: {
        "α": 81.3,
        "C1": 0.3e-5,
        "C2": 7_509e-3,
        "a1": -1_898e-3,
        "a2": 1_023e-4,
        "b1": 13_654e-4,
        "b2": 16_490e-4,
    },
    45: {
        "α": 86,
        "C1": 4.6e-5,
        "C2": 8_791e-3,
        "a1": -1_788e-3,
        "a2": 2_398e-4,
        "b1": 11_915e-4,
        "b2": 16_392e-4,
    },
}


def start_program(lp: NumberType, hs: NumberType) -> None:
    global rw_wellbore_radius, rd_damaged_zone_radius, kd_damaged_zone_permeability, K_permeability, phasing
    ld_damaged_zone_length = rd_damaged_zone_radius - rw_wellbore_radius
    print(f"Damaged zone length is: >> {ld_damaged_zone_length}")

    if lp > ld_damaged_zone_length:
        permeability_ratio = kd_damaged_zone_permeability / K_permeability
        one_minus_permeability_ratio = 1 - permeability_ratio
        l_prime_p_modified_perforation_length = lp - (
            one_minus_permeability_ratio * ld_damaged_zone_length
        )
        print(
            f"Modified perforation length is: >> {l_prime_p_modified_perforation_length}"
        )
        r_prime_w_modified_wellbore_radius = rw_wellbore_radius + (
            one_minus_permeability_ratio * ld_damaged_zone_length
        )
        print(f"Modified wellbore radius is: >> {r_prime_w_modified_wellbore_radius}")
        r_prime_wD_dimensionless_wellbore_radius = (
            r_prime_w_modified_wellbore_radius
            / (
                l_prime_p_modified_perforation_length
                + l_prime_p_modified_perforation_length
            )
        )
        print(
            f"Dimensionless wellbore radius is: >> {r_prime_wD_dimensionless_wellbore_radius}\n\n"
        )
        h_prime_D_dimensionless_spacing_between_perforation = (
            hs
            / l_prime_p_modified_perforation_length
            * sqrt(kh_horizontal_permeability / kv_vertical_permeability)
        )
        print(
            f"Dimensionless spacing between perforation is: >> {h_prime_D_dimensionless_spacing_between_perforation}"
        )
        for rp in rp_perforation_radius:
            print(f"Perforation radius is: >> {rp}")
            rpD_dimensionless_perforation_radius = (rp / 2 * hs) * (
                1 + sqrt(kh_horizontal_permeability / kv_vertical_permeability)
            )
            print(
                f"Dimensionless perforation radius is: >> {rpD_dimensionless_perforation_radius}"
            )
            for phasing_angle in phasing:
                print(f"Phasing angle is: >> {phasing_angle}")
                # Horizontal skin calculation
                S_prime_h_horizontal_skin = calculate_horizontal_skin(
                    phasing_angle,
                    GUN_PHASING_PARA[phasing_angle]["α"],
                    rw_wellbore_radius,
                    r_prime_w_modified_wellbore_radius,
                    l_prime_p_modified_perforation_length,
                )
                print(f"Horizontal skin is: >> {S_prime_h_horizontal_skin}")
                C1 = GUN_PHASING_PARA[phasing_angle]["C1"]
                C2 = GUN_PHASING_PARA[phasing_angle]["C2"]
                print(f"C1 used in calculation is: >> {C1}")
                print(f"C2 used in calculation is: >> {C2}")
                S_prime_wb_modified_wellbore_skin = C1 * exp(
                    C2 * r_prime_wD_dimensionless_wellbore_radius
                )
                print(f"Wellbore skin is: >> {S_prime_wb_modified_wellbore_skin}")
                a1 = GUN_PHASING_PARA[phasing_angle]["a1"]
                a2 = GUN_PHASING_PARA[phasing_angle]["a2"]
                b1 = GUN_PHASING_PARA[phasing_angle]["b1"]
                b2 = GUN_PHASING_PARA[phasing_angle]["b2"]
                a = (a1 * log10(rpD_dimensionless_perforation_radius)) + a2
                b = (b1 * rpD_dimensionless_perforation_radius) + b2

                # Vertical skin calculation
                S_prime_v_vertical_skin = (
                    pow(10, a)
                    * pow(h_prime_D_dimensionless_spacing_between_perforation, (b - 1))
                    * pow(rpD_dimensionless_perforation_radius, b)
                )
                print(f"Vertical skin is: >> {S_prime_v_vertical_skin}")

                # Crushed zone skin
                S_prime_c_crushed_zone_skin = calculate_crushed_zone_skin(
                    hs,
                    l_prime_p_modified_perforation_length,
                    K_permeability,
                    kc_crushed_zone_permeability,
                    rc_crushed_zone_radius,
                    rp,
                )
                print(f"Crushed zone skin is: >> {S_prime_c_crushed_zone_skin}")

                # Calculate total skin factor
                Sdp_total_skin_factor = calculate_total_skin_factor(
                    S_prime_h_horizontal_skin,
                    S_prime_wb_modified_wellbore_skin,
                    S_prime_v_vertical_skin,
                    S_prime_c_crushed_zone_skin,
                )
                print(f"Total skin factor is: >> {Sdp_total_skin_factor}")

                # Critical flow rate
                Qoc_critical_flow_rate = calculate_critical_flow_rate(
                    ρw_water_density,
                    ρo_oil_density,
                    re_drainage_radius,
                    rw_wellbore_radius,
                    Sdp_total_skin_factor,
                    ko_effective_oil_permeability,
                    μo_oil_viscosity,
                    Bo_formation_volume_factor,
                    h_oil_column_thickness,
                    hp_perforated_interval,
                )
                print(f"Critical flow rate is: >> {Qoc_critical_flow_rate}\n")
    else:
        rwD_dimensionless_wellbore_radius = rw_wellbore_radius / (
            lp + rw_wellbore_radius
        )
        print(f"Dimension wellbore radius: >> {rwD_dimensionless_wellbore_radius}")
        for rp in rp_perforation_radius:
            print(f"Perforation radius is: >> {rp}")
            rpD_dimensionless_perforation_radius = (rp / 2 * hs) * (
                1 + sqrt(kh_horizontal_permeability / kv_vertical_permeability)
            )
            print(
                f"Dimensionless perforation radius is: >> {rpD_dimensionless_perforation_radius}"
            )

            hD_dimensionless_spacing_between_perforation = (hs / lp) * sqrt(
                kh_horizontal_permeability / kv_vertical_permeability
            )
            print(
                f"Dimensionless spacing between perforation is: >> {hD_dimensionless_spacing_between_perforation}"
            )

            for phasing_angle in phasing:
                print(f"Phasing angle is: >> {phasing_angle}")
                C1 = GUN_PHASING_PARA[phasing_angle]["C1"]
                C2 = GUN_PHASING_PARA[phasing_angle]["C2"]
                print(f"C1 used in calculation is: >> {C1}")
                print(f"C2 used in calculation is: >> {C2}")
                Swb_wellbore_skin = calculate_wellbore_skin(
                    C1, C2, rwD_dimensionless_wellbore_radius
                )
                print(f"Wellbore skin is: >> {Swb_wellbore_skin}")

                a1 = GUN_PHASING_PARA[phasing_angle]["a1"]
                a2 = GUN_PHASING_PARA[phasing_angle]["a2"]
                b1 = GUN_PHASING_PARA[phasing_angle]["b1"]
                b2 = GUN_PHASING_PARA[phasing_angle]["b2"]
                a = (a1 * log10(rpD_dimensionless_perforation_radius)) + a2
                b = (b1 * rpD_dimensionless_perforation_radius) + b2
                Sv_vertical_skin = (
                    pow(10, a)
                    * pow(hD_dimensionless_spacing_between_perforation, b - 1)
                    * pow(rpD_dimensionless_perforation_radius, b)
                )
                print(f"Vertical skin is: >> {Sv_vertical_skin}")

                Sc_crushed_zone_skin = calculate_crushed_zone_skin(
                    hs,
                    lp,
                    K_permeability,
                    kc_crushed_zone_permeability,
                    rc_crushed_zone_radius,
                    rp,
                )
                print(f"Crushed zone skin is: >> {Sc_crushed_zone_skin}")

                Sh_horizontal_skin = calculate_horizontal_skin(
                    phasing_angle,
                    GUN_PHASING_PARA[phasing_angle]["α"],
                    rw_wellbore_radius,
                    r_prime_w_modified_wellbore_radius=rw_wellbore_radius,
                    l_prime_p_modified_perforation_length=lp,
                )
                print(f"Horizontal skin is: >> {Sh_horizontal_skin}")

                Sp_perforation_skin = (
                    Sh_horizontal_skin
                    + Swb_wellbore_skin
                    + Sv_vertical_skin
                    + Sc_crushed_zone_skin
                )
                print(f"Perforation skin is: >> {Sp_perforation_skin}")

                Sdp_total_skin_factor = (
                    ((K_permeability / kd_damaged_zone_permeability) - 1)
                    * ln(rd_damaged_zone_radius / rw_wellbore_radius)
                ) + (
                    (K_permeability / kd_damaged_zone_permeability)
                    * (Sp_perforation_skin + 0)
                )
                print(f"Total skin factor is: >> {Sdp_total_skin_factor}")

                # Critical flow rate
                Qoc_critical_flow_rate = calculate_critical_flow_rate(
                    ρw_water_density,
                    ρo_oil_density,
                    re_drainage_radius,
                    rw_wellbore_radius,
                    Sdp_total_skin_factor,
                    ko_effective_oil_permeability,
                    μo_oil_viscosity,
                    Bo_formation_volume_factor,
                    h_oil_column_thickness,
                    hp_perforated_interval,
                )
                print(f"Critical flow rate is: >> {Qoc_critical_flow_rate}\n")


# print(exp(ln(1.4)))
# print(log10(100))
# print(sqrt(4))
start_program(0.5, 0.083333)
# start_program(6, 1)
# start_program(0.2, 1)
# start_program(6, 1.2)
# start_program(6, 1.7)
# start_program(6, 2.4)
# start_program(6, 3)
