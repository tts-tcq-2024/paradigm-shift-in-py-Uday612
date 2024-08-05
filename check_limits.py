def check_in_range(value, lower_bound, upper_bound):
    return (value > lower_bound and value < upper_bound);

def temperature_in_range(temperature):
    return check_in_range(temperature, 0, 45)

def soc_in_range(soc):
    return check_in_range(soc, 20, 80)

def charge_in_range(charge_rate):
    return (charge_rate <= 0.8)

def battery_is_ok(temperature, soc, charge_rate):
    parameter_status = [temperature_in_range(temperature), soc_in_range(soc), charge_in_range(charge_rate)]
    for status in parameter_status:
        if not status:
            return False
    return True
