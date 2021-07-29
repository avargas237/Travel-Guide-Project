import requests
from geocoding import getGeocode
from config import CAM_KEY


headers = {
    "x-windy-key": CAM_KEY
}

def getWebcam(location):
    decoder = requests.get('https://api.windy.com/api/webcams/v2/list/nearby=' + str(location[0]) + ',' + str(location[1]) + ',2/?show=webcams:location,url', headers = headers).json()
    return decoder

def main():
    location = input('Enter a location: ')
    coordinates = getGeocode(location)
    print(getWebcam(coordinates))

if __name__ == "__main__":
    main()