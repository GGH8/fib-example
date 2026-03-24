# ==========================================
# 1. IMPORTS
# ==========================================
import requests

# ==========================================
# 2. CONFIGURATION (Constants)
# ==========================================
DEFAULT_CITY = "Targu Mures"
GEO_URL      = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL  = "https://api.open-meteo.com/v1/forecast"


# ==========================================
# 3. CORE LOGIC (Functions)
# ==========================================

def get_coordinates(city_name):
    """Translates a human city name into exact GPS coordinates."""
    try:
        full_url = f"{GEO_URL}?name={city_name}"
        response = requests.get(full_url)
        response.raise_for_status() 
        
        data = response.json()
        
        if "results" not in data:
            print(f"Error: The city '{city_name}' could not be found!")
            return None, None
            
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
        
        return lat, lon
        
    except Exception:
        print("Error connecting to the internet!")
        return None, None


def get_weather(lat, lon):
    """Uses exact GPS coordinates to look up the temperature."""
    try:
        full_url = f"{WEATHER_URL}?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(full_url)
        response.raise_for_status() 
        
        data = response.json()
        temperature = data["current_weather"]["temperature"]
        #WINDSPEED
        windspeed = data["current_weather"]["windspeed"]
        return temperature, windspeed

    except Exception:
        print("Error securely fetching the temperature data!")
        return None


# ==========================================
# 4. USER INTERFACE
# ==========================================

def main():
    # 1. Provide immediate value by showing the default city's weather!
    print("\n🌤️  Welcome to the Python Weather App! 🌤️")
    print("------------------------------------------")
    print(f"Loading local weather for {DEFAULT_CITY}...")
    
    default_lat, default_lon = get_coordinates(DEFAULT_CITY)
    
    if default_lat is not None:
        default_temp, default_wind = get_weather(default_lat, default_lon)
        print(f"📍 {DEFAULT_CITY}: {default_temp}°C with a {default_wind}km/h wind right now!")
        
    print("==========================================\n")
    
    # 2. Start the infinite hamster wheel!
    while True:
        human_input = input("Want to check another city? (Type a city or press Enter to quit): ")
        
        # If they just hit Enter, we cleanly exit the wheel
        if human_input == "":
            print("\n👋 Goodbye, and thank you for using our Weather App!\n")
            break 
            
        print(f"\nChecking the weather models for {human_input}...")
        
        # 3. Pass the human's word to the Workers!
        lat, lon = get_coordinates(human_input)
        
        # Skip this spin of the wheel if the city wasn't found
        if lat is None:
            continue

        # Catch both the temp AND the wind speed
        temperature, windspeed = get_weather(lat, lon)
        
        if temperature is not None:
            # 4. Presentation
            print("=========================================")
            print(f"📍 Location: {human_input}")
            print(f"🌡️  Current Temperature: {temperature}°C")
            
            # ADD THIS LINE: Print the wind speed!
            print(f"💨  Wind Speed: {windspeed} km/h")
            print("=========================================\n")



# ==========================================
# 5. EXECUTION POINT
# ==========================================

# When the user runs 'python weather.py', power on the UI!
if __name__ == "__main__":
    main()
