from typing import Union
from math import log as ln, exp

NumberType = Union[float, int]
NumberLiteralType = Union[NumberType, str]
QOC_CONVERSION_FACTOR = 0.246e-4


def calculate_damaged_zone(rd: NumberType, rw: NumberType) -> NumberType:
    # This function calculates the damaged zone by subtracting the
    # wellbore radius from the damaged zone radius
    try:
        return rd - rw
    except ValueError:
        print("Invalid input")
        return calculate_damaged_zone()


def receive_number_input(text) -> NumberType:
    try:
        return float(input(f"Enter {text} >> ").strip())
    except ValueError:
        print("Invalid input")
        return receive_number_input()


# def calculate_modified_perforation_length():
#     print("Calculate Modified Perforation length")


def calculate_horizontal_skin(
    phasing_angle: NumberType,
    alpha: NumberLiteralType,
    rw_wellbore_radius: NumberType,
    r_prime_w_modified_wellbore_radius: NumberType,
    l_prime_p_modified_perforation_length: NumberType,
):
    if phasing_angle != 0:
        S_prime_h_horizontal_skin = ln(
            rw_wellbore_radius
            / (
                alpha
                * (
                    r_prime_w_modified_wellbore_radius
                    + l_prime_p_modified_perforation_length
                )
            )
        )
        # print(f"Horizontal skin is: >>  {S_prime_h_horizontal_skin}")
    else:
        S_prime_h_horizontal_skin = ln(
            (4 * rw_wellbore_radius) / l_prime_p_modified_perforation_length
        )
        # print(f"Horizontal skin is: >>  {S_prime_h_horizontal_skin}")
    return S_prime_h_horizontal_skin


def calculate_crushed_zone_skin(
    hs: NumberType,
    l_prime_p_modified_perforation_length: NumberType,
    K_permeability: NumberType,
    kc_crushed_zone_permeability: NumberType,
    rc_crushed_zone_radius: NumberType,
    rp: NumberType,
):
    S_prime_c_crushed_zone_skin = (
        (hs / l_prime_p_modified_perforation_length)
        * ((K_permeability / kc_crushed_zone_permeability) - 1)
        * ln(rc_crushed_zone_radius / rp)
    )
    return S_prime_c_crushed_zone_skin


def calculate_total_skin_factor(
    S_prime_h_horizontal_skin: NumberType,
    S_prime_wb_modified_wellbore_skin: NumberType,
    S_prime_v_vertical_skin: NumberType,
    S_prime_c_crushed_zone_skin: NumberType,
):
    return (
        S_prime_h_horizontal_skin
        + S_prime_wb_modified_wellbore_skin
        + S_prime_v_vertical_skin
        + S_prime_c_crushed_zone_skin
    )


def calculate_critical_flow_rate(
    ρw_water_density: NumberType,
    ρo_oil_density: NumberType,
    re_drainage_radius: NumberType,
    rw_wellbore_radius: NumberType,
    Sdp_total_skin_factor: NumberType,
    ko_effective_oil_permeability: NumberType,
    μo_oil_viscosity: NumberType,
    Bo_formation_volume_factor: NumberType,
    h_oil_column_thickness: NumberType,
    hp_perforated_interval: NumberType,
):
    Qoc_critical_flow_rate = (
        QOC_CONVERSION_FACTOR
        * (
            ρw_water_density
            - ρo_oil_density
            / (ln(re_drainage_radius / rw_wellbore_radius) + Sdp_total_skin_factor)
        )
        * (
            ko_effective_oil_permeability
            / (μo_oil_viscosity * Bo_formation_volume_factor)
        )
    ) * (h_oil_column_thickness**2 - hp_perforated_interval**2)
    return Qoc_critical_flow_rate


def calculate_wellbore_skin(
    C1: NumberType, C2: NumberType, rwD_dimensionless_wellbore_radius: NumberType
):
    return C1 * exp(C2 * rwD_dimensionless_wellbore_radius)
