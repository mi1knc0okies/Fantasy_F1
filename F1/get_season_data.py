import requests

headers = {
    'x-rapidapi-key': "f6e273c277msh0f74e17c5a67fc8p12f7a6jsneea422ea1463",
    'x-rapidapi-host': "api-formula-1.p.rapidapi.com"
    }

querystring = {"season":"2020"}

def get_Drivers():
    try:
        drivers = requests.get('http://ergast.com/api/f1/2008/driverStandings',)
        drivers.raise_for_status()
    except Exception as E:
        print(E)

    return drivers.json()

print(get_Drivers())
