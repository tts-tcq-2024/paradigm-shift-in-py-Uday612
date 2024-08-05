def check_in_range(value, lowerBound, upperBound):
    return (value > lowerBound and value < upperBound);
    
def battery_is_ok(temperature, soc, charge_rate):
    battery_status = [check_in_range(temperature, 0, 45), 
    check_in_range(soc, 20, 80), 
    (charge_rate <= 0.8)]
    
    for value in battery_status:
        if not value:
            return False
    return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
