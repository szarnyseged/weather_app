from PIL import ImageTk, Image


# images
# images must be globals, otherwise tkinter funcs cant show them properly

# list of all conditions and icons:
# https://openweathermap.org/weather-conditions
def load_images(window):
    """
    window = main tkinter window
    """
    global img_clear_sky
    global img_rain
    global img_few_clouds
    global img_scattered_clouds
    global img_broken_clouds
    global img_snow
    global img_thunderstorm
    global WEATHER_IMAGES

    global icon_clear_sky
    global icon_few_clouds
    global icon_scattered_clouds
    global icon_broken_clouds
    global icon_shower_rain
    global icon_rain
    global icon_thunderstorm
    global icon_snow
    global icon_mist
    global ICONS

    img_clear_sky = ImageTk.PhotoImage(Image.open("./img/images/clear_sky.jpg"))
    img_rain = ImageTk.PhotoImage(Image.open("./img/images/rain.jpg"))
    img_few_clouds = ImageTk.PhotoImage(Image.open("./img/images/few_clouds.jpg"))
    img_scattered_clouds = ImageTk.PhotoImage(Image.open("./img/images/scattered_clouds.jpg"))
    img_broken_clouds = ImageTk.PhotoImage(Image.open("./img/images/broken_clouds.jpg"))
    img_snow = ImageTk.PhotoImage(Image.open("./img/images/snow.jpg"))
    img_thunderstorm = ImageTk.PhotoImage(Image.open("./img/images/thunderstorm.jpg"))
    
    # "Clouds" handled by ID, not Main name
    WEATHER_IMAGES = {
        "Clear": img_clear_sky,
        "Rain": img_rain,
        "Drizzle": img_rain,
        "Snow": img_snow,
        "Thunderstorm": img_thunderstorm,
        "Mist": img_broken_clouds,
        "Smoke": img_broken_clouds,
        "Haze": img_broken_clouds,
        "Dust": img_broken_clouds,
        "Fog": img_broken_clouds,
        #"Sand": 
        #"Ash": 
        #"Squall": 
        #"Tornado": 
    }

    icon_clear_sky = ImageTk.PhotoImage(Image.open("./img/icons/01d@2x.png"))
    icon_few_clouds = ImageTk.PhotoImage(Image.open("./img/icons/02d@2x.png"))
    icon_scattered_clouds = ImageTk.PhotoImage(Image.open("./img/icons/03d@2x.png"))
    icon_broken_clouds = ImageTk.PhotoImage(Image.open("./img/icons/04d@2x.png"))
    icon_shower_rain = ImageTk.PhotoImage(Image.open("./img/icons/09d@2x.png"))
    icon_rain = ImageTk.PhotoImage(Image.open("./img/icons/10d@2x.png"))
    icon_thunderstorm = ImageTk.PhotoImage(Image.open("./img/icons/11d@2x.png"))
    icon_snow = ImageTk.PhotoImage(Image.open("./img/icons/13d@2x.png"))
    icon_mist = ImageTk.PhotoImage(Image.open("./img/icons/50d@2x.png"))

    # "Clouds" handled by ID, not Main name
    ICONS = {
        "Clear": icon_clear_sky,
        "Rain": icon_rain,
        "Drizzle": icon_rain,
        "Snow": icon_snow,
        "Thunderstorm": icon_thunderstorm,
        "Mist": icon_mist,
        "Smoke": icon_mist,
        "Haze": icon_mist,
        "Dust": icon_mist,
        "Fog": icon_mist,
        "Sand": icon_mist,
        "Ash": icon_mist,
        "Squall": icon_mist,
        "Tornado": icon_mist,
    }
    