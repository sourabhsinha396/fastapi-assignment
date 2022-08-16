from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/{city}")
def read_root(city:str):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=47ed18d2447f09799cb91500493d0692")
        print(response.json())
        return response.json().get('weather')[0]["main"]
    except:
        return {"message":"Please enter valid city name"}

        
@app.get("/")
def read_index():
    return {"message":"append any city name to the url after / e.g. www.url.com/pune"}
