# ==========================================
# 1. IMPORTS (Dependencies)
# ==========================================
# This is where we tell Python we need the built-in "requests" tool 
# so we can talk to the internet.
# ==========================================
# 2. CONFIGURATION (Constants)
# ==========================================
# This is where we store things that don't change, like the 
# base website URL for the Open-Meteo weather service.
# ==========================================
# 3. CORE LOGIC (Functions)
# ==========================================
# We will write a tool here (e.g., `def fetch_weather():`) that 
# grabs the raw data from the internet and finds the exact 
# temperature and wind speed we care about.
# ==========================================
# 4. USER INTERFACE
# ==========================================
# We will write a tool here (e.g., `def main():`) that prompts the 
# user to type a city name, passes that city to our Logic tool, 
# and then prints the beautiful final result on the screen.
# ==========================================
# 5. EXECUTION POINT (The "On Switch")
# ==========================================
# This is a special, standard Python trick at the very bottom of the file.
# It tells Python: "When someone types 'python weather.py' in the terminal, 
# start by running the User Interface tool!"
if __name__ == "__main__":
    # Start the app here!
