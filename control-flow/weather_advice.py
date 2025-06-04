# weather_advice.py
weather = input("What is the weather like today? (cold, hot, rainy, snowy, windy): ").lower()
if weather == "cold":
    print("Wear a warm coat and a scarf.")
elif weather == "hot":
    print("Wear light clothes and drink plenty of water.")
elif weather == "rainy":
    print("Take an umbrella and wear waterproof shoes.")
elif weather == "snowy":
    print("Wear a thick coat, gloves, and boots.")
elif weather == "windy":
    print("Wear a windbreaker or jacket.")
else:
    print("I don't recognize that weather — dress comfortably!")
