def check_in_range(value, lowerBound, upperBound):
    return (value > lowerBound and value < upperBound);
    
def battery_is_ok(temperature, soc, charge_rate):
    parameter_status = [check_in_range(temperature, 0, 45), 
    check_in_range(soc, 20, 80), 
    (charge_rate <= 0.8)]
    
    for status in parameter_status:
        if not status:
            return False
    return True
