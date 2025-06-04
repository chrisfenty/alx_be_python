# alx_be_python# weather_advice.py
import os
def check_file(path):
    if os.path.isfile(path) and os.path.getsize(path) > 0:
        print(f"✅ File '{path}' exists and is not empty.\n")
        return True
    else:
        print(f"❌ File '{path}' is missing or empty.")
        return False

def get_clothing_advice(weather):
    weather = weather.lower()
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
    # Optional: check if this script itself is valid
    if not check_file(__file__):
        return

    print("Welcome to the Weather Clothing Advisor!")
    user_weather = input("How is the weather today? (cold, hot, rainy, snowy, windy): ")
    advice = get_clothing_advice(user_weather)
    print(advice)

if __name__ == "__main__":
    main()
