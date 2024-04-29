def main():
  AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
  while True:
      print("********************************")
      print("AutoCountry Vehicle Finder v0.3")
      print("********************************")
      print("Please Enter the following number below from the following menu:")
      print("1. PRINT all Authorized Vehicles")
      print("2. SEARCH for Authorized Vehicle")
      print("3. ADD Authorized Vehicle")
      print("4. DELETE Authorized Vehicle")
      print("5. Exit")
      print("********************************")
      choice = input("Enter Choice (1-5): ")
      if choice == "1":
          print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
          for vehicle in AllowedVehiclesList:
              print(vehicle)
      elif choice == "2":
          search_query = input("Please Enter the full Vehicle name: ")
          if search_query in AllowedVehiclesList:
              print(f"{search_query} is an authorized vehicle")
          else:
              print(f"{search_query} is not an authorized vehicle, if you received this in error please check the spelling and try again")
      elif choice == "3":
          new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
          AllowedVehiclesList.append(new_vehicle)
          print(f"You have added \"{new_vehicle}\" as an authorized vehicle")
      elif choice == "4":
          remove_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
          if remove_vehicle in AllowedVehiclesList:
              confirmation = input(f"Are you sure you want to remove \"{remove_vehicle}\" from the Authorized Vehicles List? ")
              if confirmation.lower() == "yes":
                  AllowedVehiclesList.remove(remove_vehicle)
                  print(f"You have REMOVED \"{remove_vehicle}\" as an authorized vehicle")
              elif confirmation.lower() == "no":
               pass
                
          else:
              print(f"{remove_vehicle} is not in the authorized vehicles list")
      elif choice == "5":
          print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
          break
     

if __name__ == "__main__":
  main()
