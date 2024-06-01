# file: microservice.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/lut-buffet-menu-today')
def lut_buffet_menu_today():
    menu = {
        "vegetarian_soup": "Indian bean and vegetable soup",
        "vegetarian_lunch": "NO Chicken tikka masala, Whole grain rice"
    }
    return JSONResponse(content=menu)

@app.get('/lut-gym-occupancy-now')
def lut_gym_occupancy_now():
    occupancy = {
        "total": 19,
        "muscle_training": 11,
        "others": 8
    }
    return JSONResponse(content=occupancy)

@app.get('/next-incoming-bus')
def next_incoming_bus():
    buses = [
        {"bus": 5, "time": "11:45"},
        {"bus": 1, "time": "12:00"}
    ]
    return JSONResponse(content=buses)

@app.get('/next-prayer-time')
def next_prayer_time():
    prayer_time = {
        "Dhur": "13:20"
    }
    return JSONResponse(content=prayer_time)

@app.get('/vierula-sauna-schedule')
def vierula_sauna_schedule():
    sauna_schedule = {
        "sauna_today": "18:00"
    }
    return JSONResponse(content=sauna_schedule)

@app.get('/library-room-occupancy')
def library_room_occupancy():
    occupancy = {
        "Einstein": "free",
        "Faraday": "free",
        "Doppler": "occupied",
        "Galilei": "occupied"
    }
    return JSONResponse(content=occupancy)

@app.get('/tek-event')
def tek_event():
    event = {
        "event_today": "none"
    }
    return JSONResponse(content=event)

@app.get('/sports-hall-status')
def sports_hall_status():
    status = {
        "status": "occupied"
    }
    return JSONResponse(content=status)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level='debug')
