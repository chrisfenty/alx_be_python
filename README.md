# alx_be_python# weather_advice.py
def get_clothing_advice(weather):
    weather = weather.lower()  # Normalize input to lowercase for easy comparison
    if weather == "cold":
        return "It's cold outside. Wear a heavy coat, scarf, and gloves."
    elif weather == "hot":
        return "It's hot outside. Wear light clothing like shorts and a t-shirt."
    elif weather == "rainy":
        return "It's rainy. Don't forget your umbrella and a waterproof jacket."
    elif weather == "snowy":
        return "It's snowy. Wear a warm coat, boots, and a hat."
    elif weather == "windy":
        return "It's windy. A windbreaker or jacket would be good."
    else:
        return "Hmm, I'm not sure about that weather. Dress comfortably and stay safe!"

def main():
    print("Welcome to the Weather Clothing Advisor!")
    user_weather = input("How is the weather today? (cold, hot, rainy, snowy, windy): ")
    advice = get_clothing_advice(user_weather)
    print(advice)

if __name__ == "__main__":
    main()
