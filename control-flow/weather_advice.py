weather = input("What is the weather like today? (sunny, rainy, cold): ").lower()
if weather == "sunny":
    print("Wear light clothes and sunglasses!")
elif weather == "rainy":
    print("Take an umbrella and wear waterproof shoes.")
elif weather == "cold":
    print("Wear a jacket or sweater.")
else:
    print("Sorry, I don't have advice for that kind of weather.")
