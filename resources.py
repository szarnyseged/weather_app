from PIL import ImageTk, Image


#images
#images must be globals outside, otherwise tkinter funcs cant show them properly
img_clear_sky = None
img_rain = None
img_few_clouds = None
img_scattered_clouds = None
img_broken_clouds = None
img_snow = None
img_thunderstorm = None


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

    img_clear_sky = ImageTk.PhotoImage(Image.open("./img/clear_sky.jpg"))
    img_rain = ImageTk.PhotoImage(Image.open("./img/rain.jpg"))
    img_few_clouds = ImageTk.PhotoImage(Image.open("./img/few_clouds.jpg"))
    img_scattered_clouds = ImageTk.PhotoImage(Image.open("./img/scattered_clouds.jpg"))
    img_broken_clouds = ImageTk.PhotoImage(Image.open("./img/broken_clouds.jpg"))
    img_snow = ImageTk.PhotoImage(Image.open("./img/snow.jpg"))
    img_thunderstorm = ImageTk.PhotoImage(Image.open("./img/thunderstorm.jpg"))
    
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
        "Fog": img_broken_clouds
    }
    