from functions import *

accepted_commands = ["START", "QUIT", "RESTART"]
current_stage = ""
operation_values = {}


# stage_functions = {
#     "calculate_damaged_zone": calculate_damaged_zone
# }


def check_command_validity(command: str) -> bool:
    return accepted_commands.__contains__(command.upper())


def start_program():
    global current_stage, operation_values
    operation_values = {}
    try:
        print("Provide all permeability, if none provide 0")
        kc_crushed_zone_permeability = receive_number_input("crushed zone permeability => Kc")
        k_permeability = receive_number_input("permeability => K")
        kd_damaged_zone_permeability = receive_number_input("damaged zone permeability => Kd")

        # current_stage = "calculate_damaged_zone"
        rd_damaged_zone_radius = receive_number_input("damaged zone radius")
        rw_wellbore_radius = receive_number_input("wellbore radius")
        ld_damaged_zone = calculate_damaged_zone(rd_damaged_zone_radius, rw_wellbore_radius)
        # current_stage = "check_perforation_beyond_damaged_zone"
        lp_perforation_length = receive_number_input("Perforation length")
        if lp_perforation_length > ld_damaged_zone:
            print("Perforation is beyond damage zone...")

            print("Calculating dimensionless perforation parameters beyond the damage zone...")

        else:
            print("Perforation not beyond damage zone")
    except ValueError:
        print("Invalid input try again")
        start_program()
