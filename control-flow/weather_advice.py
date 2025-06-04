# weather_advice.py

# Ask the user about the current weather
user_weather = input("What is the weather like today? (sunny, rainy, cold, hot, snowy, windy): ").lower()

# Give clothing advice based on the weather
if weather == "sunny":
    print("Wear light clothes and sunglasses.")
elif weather == "rainy":
    print("Take an umbrella and wear a waterproof jacket.")
elif weather == "cold":
    print("Wear a jacket, scarf, and warm boots.")
elif weather == "hot":
    print("Wear breathable clothes and stay hydrated.")
elif weather == "snowy":
    print("Bundle up with a heavy coat, gloves, and boots.")
elif weather == "windy":
    print("Wear a windbreaker or something warm.")
else:
    print("Hmm, I don't recognize that weather. Dress appropriately!")

