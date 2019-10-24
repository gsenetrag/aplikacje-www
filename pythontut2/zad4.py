def convertCelcius(temp_c, temperature_type):
        if temperature_type == "farenheit":
            temp_f = 9 * temp_c / 5 + 32
            return temp_f
        elif temperature_type == "rankine":
            temp_r = (temp_c + 273.15) * 9 / 5
            return temp_r
        elif temperature_type == "kelvin":
            temp_k = temp_c + 273.15
            return temp_k
        else:
            return "Invalid temperature type"
    

print(convertCelcius(25,"kelvin"))