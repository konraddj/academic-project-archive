Kelvin_temp_list=[278,280.1,280.7,282,285,287,291,294,297,300,308]
Conversion_to_Fahrenheit_first_element=1.8
Conversion_to_Fahrenheit_second_element=459.67

Fahrenheit_temp = [(round*Conversion_to_Fahrenheit_first_element-Conversion_to_Fahrenheit_second_element) for round in Kelvin_temp_list]

print(Fahrenheit_temp)