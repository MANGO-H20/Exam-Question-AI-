const dailydata_stoke = `{
    "coord": { "lon": -2.8667, "lat": 53.25 },
    "weather": [
        {
            "id": 802,
            "main": "Clouds",
            "description": "scattered clouds",
            "icon": "03d"
        }
            // waffle waffle
    ],// waffle waffle
    "main": {
        "temp": 13.12,
        "feels_like": 12.5,
        "temp_min": 10.9,
        "temp_max": 14.58,
        "pressure": 1004,
        "humidity": 77
    },
    "name": "Stoke",
    "cod": 200
}`;

// Parse the JSON data
const daily = JSON.parse(dailydata_stoke);

// Populate HTML with parsed JSON data
document.getElementById('lon').innerHTML = daily.coord.lon;
document.getElementById('lat').innerHTML = daily.coord.lat;
document.getElementById('temp').innerHTML = daily.main.temp;
document.getElementById('feels-like').innerHTML = daily.main.feels_like;
document.getElementById('humidity').innerHTML = daily.main.humidity;
document.getElementById('weather-main').innerHTML = daily.weather[0].main;
document.getElementById('weather-description').innerHTML = daily.weather[0].description;
