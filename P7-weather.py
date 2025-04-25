class Weather:
    def __init__(self, *params):
        self.parameters = list(params)

    def __contains__(self, item):
        return item in self.parameters

    def __str__(self):
        return ', '.join(str(param) for param in self.parameters)

# Example usage:
weather = Weather('Temperature: 30°C', 'Humidity: 75%', 'Wind Speed: 10 km/h', 'Pressure: 1013 hPa')

# Check if certain weather parameters are in the list
print("Is 'Temperature: 30°C' in weather parameters?", 'Temperature: 30°C' in weather)
print("Is 'Rainfall: 20mm' in weather parameters?", 'Rainfall: 20mm' in weather)

# Print the weather parameters
print("Weather Parameters:",weather)
