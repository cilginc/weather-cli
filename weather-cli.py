import requests

def inputwhere():
    return input("Search for a place? (x for exit): ")

def getweather():
    getinput = inputwhere()
    if getinput == "x":
        return "Exited"
    else:
        url = f"https://wttr.in/{getinput}?format=j1"
        response = requests.get(url)
        if response.status_code == 200:
           data = response.json()
           current_condition = data.get('current_condition', [])[0]
           nearest_area = data.get('nearest_area', [])[0]
           print("------------------------------")
           print("Current Weather:")
           print(f"Temp: {current_condition.get('temp_C')}°C")
           print(f"Feels Like Temp: {current_condition.get('FeelsLikeC')}°C")
           print(f"Humidity: {current_condition.get('humidity')}%")
           print(f"Wind Speed: {current_condition.get('windspeedKmph')} km/s")
           print(f"Weather Description: {current_condition.get('weatherDesc')[0].get('value')}")
           print("Location:")
           print(f"Area: {nearest_area.get('areaName')[0].get('value')}")
           print(f"Region: {nearest_area.get('region')[0].get('value')}")
           print(f"Country: {nearest_area.get('country')[0].get('value')}")
           print("-----------------------------")
        elif response.status_code == 404:
            print(f"There is nowhere named {getinput} ")
        else:
            print("Something went wrong")1

if __name__ == "__main__":
    while True:
        weather = getweather()
        if weather == "Exited":
            break

