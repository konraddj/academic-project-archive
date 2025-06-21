def Consumption():
  # Loop forever
  while True:
    try:
      
      fuel = int(input("Enter value of fuel: "))
      if fuel <= 0:
        raise Exception ("Values must be > 0")

      fuel_consumption = int(input("Enter value of fuel consumption: "))
      if fuel_consumption <= 0:
        raise Exception ("Values must be > 0")

    except:
      # Bad value,
      print("Error")

      continue

    else:
      print("Valid input")
      print ("Endurance is:", fuel/fuel_consumption)
      # Good value, exit the loop
      break
    
    finally:
      # Only runs after the except, continue
      print("Try again - enter an integer value only!")

Consumption()