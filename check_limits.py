
def battery_is_ok(temperature, soc, charge_rate):
    battery_ok = 0
    temp_ok = (temperature < 0 or temperature > 45)
    soc_ok = (soc < 20 or soc > 80)
    charge_ok = (charge_rate > 0.8)
    battery_ok = temp_ok + soc_ok + charge_ok
    if battery_ok >= 1:
        print('Battery is Not okay!')
        return False
    else:
        print("Battery is okay!")
        return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
