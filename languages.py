english = {
    "temperature":"Temperature is out of range", 
    "soc" :"SOC is out of range", 
    "charge":"Charge is out of range"}

german = {
    "temperature" : "Die Temperatur liegt außerhalb des zulässigen Bereichs",
    "soc": "Der SOC liegt außerhalb des zulässigen Bereichs",
    "charge": "Die Ladung liegt außerhalb der Reichweite"
}

def get_message(language, parameter):
    return language[parameter]
