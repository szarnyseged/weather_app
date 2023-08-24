from PIL import ImageTk, Image


# images
# images must be globals, otherwise tkinter funcs cant show them properly

# list of all conditions and icons:
# https://openweathermap.org/weather-conditions
def load_images(window):
    """
    window = main tkinter window
    """
    global img_background
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
    global ICONS_BY_ID

    img_background = ImageTk.PhotoImage(Image.open("./img/images/background.png"))
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

    icon_clear_sky = Image.open("./img/icons/01d@2x.png")
    # all icons share the same default size
    icons_original_dimension = (icon_clear_sky.width, icon_clear_sky.height)
    icons_new_dimension = int(icons_original_dimension[0]/2), int(icons_original_dimension[1]/2)
    icon_clear_sky = icon_clear_sky.resize(icons_new_dimension)
    icon_clear_sky = ImageTk.PhotoImage(icon_clear_sky)

    icon_few_clouds = Image.open("./img/icons/02d@2x.png").resize(icons_new_dimension)
    icon_few_clouds = ImageTk.PhotoImage(icon_few_clouds)
    icon_scattered_clouds = Image.open("./img/icons/03d@2x.png").resize(icons_new_dimension)
    icon_scattered_clouds = ImageTk.PhotoImage(icon_scattered_clouds)
    icon_broken_clouds = Image.open("./img/icons/04d@2x.png").resize(icons_new_dimension)
    icon_broken_clouds = ImageTk.PhotoImage(icon_broken_clouds)
    icon_shower_rain = Image.open("./img/icons/09d@2x.png").resize(icons_new_dimension)
    icon_shower_rain = ImageTk.PhotoImage(icon_shower_rain)
    icon_rain = Image.open("./img/icons/10d@2x.png").resize(icons_new_dimension)
    icon_rain = ImageTk.PhotoImage(icon_rain)
    icon_thunderstorm = Image.open("./img/icons/11d@2x.png").resize(icons_new_dimension)
    icon_thunderstorm = ImageTk.PhotoImage(icon_thunderstorm)
    icon_snow = Image.open("./img/icons/13d@2x.png").resize(icons_new_dimension)
    icon_snow = ImageTk.PhotoImage(icon_snow)
    icon_mist = Image.open("./img/icons/50d@2x.png").resize(icons_new_dimension)
    icon_mist = ImageTk.PhotoImage(icon_mist)


    #icon_clear_sky = ImageTk.PhotoImage(Image.open("./img/icons/01d@2x.png"))
    #icon_few_clouds = ImageTk.PhotoImage(Image.open("./img/icons/02d@2x.png"))
    #icon_scattered_clouds = ImageTk.PhotoImage(Image.open("./img/icons/03d@2x.png"))
    #icon_broken_clouds = ImageTk.PhotoImage(Image.open("./img/icons/04d@2x.png"))
    #icon_shower_rain = ImageTk.PhotoImage(Image.open("./img/icons/09d@2x.png"))
    #icon_rain = ImageTk.PhotoImage(Image.open("./img/icons/10d@2x.png"))
    #icon_thunderstorm = ImageTk.PhotoImage(Image.open("./img/icons/11d@2x.png"))
    #icon_snow = ImageTk.PhotoImage(Image.open("./img/icons/13d@2x.png"))
    #icon_mist = ImageTk.PhotoImage(Image.open("./img/icons/50d@2x.png"))


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

    ICONS_BY_ID = {
        200 : icon_thunderstorm,
        201 : icon_thunderstorm,
        202 : icon_thunderstorm,
        210 : icon_thunderstorm,
        211 : icon_thunderstorm,
        212 : icon_thunderstorm,
        221 : icon_thunderstorm,
        230 : icon_thunderstorm,
        231 : icon_thunderstorm,
        232 : icon_thunderstorm,
        300 : icon_rain,
        301 : icon_rain,
        302 : icon_rain,
        310 : icon_rain,
        311 : icon_rain, 
        312 : icon_rain, 
        313 : icon_rain, 
        314 : icon_rain, 
        321 : icon_rain, 
        500 : icon_rain,
        501 : icon_rain, 
        502 : icon_rain, 
        503 : icon_rain, 
        504 : icon_rain, 
        511 : icon_rain, 
        520 : icon_rain, 
        521 : icon_rain, 
        522 : icon_rain, 
        531 : icon_rain, 
        600 : icon_snow,
        601 : icon_snow, 
        602 : icon_snow, 
        611 : icon_snow, 
        612 : icon_snow, 
        613 : icon_snow, 
        615 : icon_snow, 
        616 : icon_snow, 
        620 : icon_snow, 
        621 : icon_snow, 
        622 : icon_snow, 
        701 : icon_mist,
        711 : icon_mist, 
        721 : icon_mist, 
        731 : icon_mist, 
        741 : icon_mist, 
        751 : icon_mist, 
        761 : icon_mist, 
        762 : icon_mist, 
        771 : icon_mist, 
        781 : icon_mist, 
        800 : icon_clear_sky,
        801 : icon_few_clouds,
        802 : icon_scattered_clouds,
        803 : icon_broken_clouds,
        804 : icon_broken_clouds
    }
    