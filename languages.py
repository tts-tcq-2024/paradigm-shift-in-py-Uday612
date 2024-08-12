preferred_language = "english"
english = {
    "temperature":"Temperature is out of range", 
    "soc" :"SOC is out of range", 
    "charge":"Charge is out of range"}

german = {
    "temperature" : "Die Temperatur liegt außerhalb des zulässigen Bereichs",
    "soc": "Der SOC liegt außerhalb des zulässigen Bereichs",
    "charge": "Die Ladung liegt außerhalb der Reichweite"
}

def get_message(parameter):
    return preferred_language[parameter]

def set_preferred_language(language):
    global preferred_language
    preferred_language = language
