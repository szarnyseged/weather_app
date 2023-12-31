import tkinter
from PIL import ImageTk, Image
import json
import resources
import datetime


#gui_funcs
def show_current_weather(window, *args):
    """
    window: main tkinter window
    args: optional windows or frames where widgets can be placed
    condition list: https://openweathermap.org/weather-conditions
    """

    #remove previous search
    for elem in args[0].grid_slaves():
        elem.grid_forget()

    with open("./data/last_data_converted.json", "r") as source_file:
        datas = json.load(source_file)
    description = datas["weather"][0]["description"]

    description_label = tkinter.Label(args[0], text=description)
    description_label.grid(column=0, row=1)
    weather_id = datas["weather"][0]["id"]
    main_weather = datas["weather"][0]["main"]


    if main_weather != "Clouds":
        show_image(window, resources.WEATHER_IMAGES[main_weather], args[0])

    if weather_id == 801:
        show_image(window, resources.img_few_clouds, args[0])
    elif weather_id == 802:
        show_image(window, resources.img_scattered_clouds, args[0])
    elif weather_id == 803 or weather_id == 804:
        show_image(window, resources.img_broken_clouds, args[0])


def show_five_day_forecast(window, bottom_frame):
    global img_label
    global description_label

    #remove previous search
    for elem in bottom_frame.grid_slaves():
        elem.grid_forget()
    
    #get selected data
    date_list, temp_list, weather_descr_list = select_json_info()

    #merge lists
    date_temp_descr_list = []
    for index in range(len(date_list)):
        date_temp_descr_list.append((date_list[index], temp_list[index], weather_descr_list[index]))

    #setup gui
    #0. column
    Label_row0_column0 = tkinter.Label(bottom_frame, text="").grid(row=0, column=0)
    Label_row1_column0 = tkinter.Label(bottom_frame, text="00:00:00").grid(row=1, column=0, rowspan=2)
    Label_row3_column0 = tkinter.Label(bottom_frame, text="06:00:00").grid(row=3, column=0, rowspan=2)
    Label_row5_column0 = tkinter.Label(bottom_frame, text="12:00:00").grid(row=5, column=0, rowspan=2)
    Label_row7_column0 = tkinter.Label(bottom_frame, text="18:00:00").grid(row=7, column=0, rowspan=2)

    #1. column
    #note: ".grid" line must be separated, because ".config"
    #create dictionaries of label objects with name:"Label_row{number}_column{number}"
    Label_row0_column1 = tkinter.Label(bottom_frame, text="Hétfő").grid(row=0, column=1)
    column1_dict = {}
    for index in range(1, 9):
        column1_dict["Label_row{}_column1".format(index)] = tkinter.Label(bottom_frame)
        column1_dict["Label_row{}_column1".format(index)].grid(row=index, column=1)


    #2. column
    Label_row0_column2 = tkinter.Label(bottom_frame, text="Kedd").grid(row=0, column=2)
    column2_dict = {}
    for index in range(1, 9):
        column2_dict["Label_row{}_column2".format(index)] = tkinter.Label(bottom_frame)
        column2_dict["Label_row{}_column2".format(index)].grid(row=index, column=2)

    #3. column
    Label_row0_column3 = tkinter.Label(bottom_frame, text="Szerda").grid(row=0, column=3)
    column3_dict = {}
    for index in range(1, 9):
        column3_dict["Label_row{}_column3".format(index)] = tkinter.Label(bottom_frame)
        column3_dict["Label_row{}_column3".format(index)].grid(row=index, column=3)


    #4. column
    Label_row0_column4 = tkinter.Label(bottom_frame, text="Csütörtök").grid(row=0, column=4)
    column4_dict = {}
    for index in range(1, 9):
        column4_dict["Label_row{}_column4".format(index)] = tkinter.Label(bottom_frame)
        column4_dict["Label_row{}_column4".format(index)].grid(row=index, column=4)


    #5. column
    Label_row0_column5 = tkinter.Label(bottom_frame, text="Péntek").grid(row=0, column=5)
    column5_dict = {}
    for index in range(1, 9):
        column5_dict["Label_row{}_column5".format(index)] = tkinter.Label(bottom_frame)
        column5_dict["Label_row{}_column5".format(index)].grid(row=index, column=5)

    #6. column
    Label_row0_column6 = tkinter.Label(bottom_frame, text="Szombat").grid(row=0, column=6)
    column6_dict = {}
    for index in range(1, 9):
        column6_dict["Label_row{}_column6".format(index)] = tkinter.Label(bottom_frame)
        column6_dict["Label_row{}_column6".format(index)].grid(row=index, column=6)

    #7. column
    Label_row0_column7 = tkinter.Label(bottom_frame, text="Vasárnap").grid(row=0, column=7)
    column7_dict = {}
    for index in range(1, 9):
        column7_dict["Label_row{}_column7".format(index)] = tkinter.Label(bottom_frame)
        column7_dict["Label_row{}_column7".format(index)].grid(row=index, column=7)


    #fill data
    for index in range(len(date_temp_descr_list)):
        day_time = datetime.datetime.strptime(date_temp_descr_list[index][0], "%Y-%m-%d %H:%M:%S")
        day = datetime.datetime.strftime(day_time, "%A")
        time = datetime.datetime.strftime(day_time, "%H:%M:%S")
        if day == "Monday":
            if time == "00:00:00":
                column1_dict["Label_row1_column1"].config(text=date_temp_descr_list[index][1])
                column1_dict["Label_row2_column1"].config(text=date_temp_descr_list[index][2])
            elif time == "06:00:00":
                column1_dict["Label_row3_column1"].config(text=date_temp_descr_list[index][1])
                column1_dict["Label_row4_column1"].config(text=date_temp_descr_list[index][2])
            elif time == "12:00:00":
                column1_dict["Label_row5_column1"].config(text=date_temp_descr_list[index][1])
                column1_dict["Label_row6_column1"].config(text=date_temp_descr_list[index][2])
            elif time == "18:00:00":
                column1_dict["Label_row7_column1"].config(text=date_temp_descr_list[index][1])
                column1_dict["Label_row8_column1"].config(text=date_temp_descr_list[index][2])
        elif day == "Tuesday":
            if time == "00:00:00":
                column2_dict["Label_row1_column2"].config(text=date_temp_descr_list[index][1])
                column2_dict["Label_row2_column2"].config(text=date_temp_descr_list[index][2])
            elif time == "06:00:00":
                column2_dict["Label_row3_column2"].config(text=date_temp_descr_list[index][1])
                column2_dict["Label_row4_column2"].config(text=date_temp_descr_list[index][2])
            elif time == "12:00:00":
                column2_dict["Label_row5_column2"].config(text=date_temp_descr_list[index][1])
                column2_dict["Label_row6_column2"].config(text=date_temp_descr_list[index][2])
            elif time == "18:00:00":
                column2_dict["Label_row7_column2"].config(text=date_temp_descr_list[index][1])
                column2_dict["Label_row8_column2"].config(text=date_temp_descr_list[index][2])
        elif day == "Wednesday":
            if time == "00:00:00":
                column3_dict["Label_row1_column3"].config(text=date_temp_descr_list[index][1])
                column3_dict["Label_row2_column3"].config(text=date_temp_descr_list[index][2])
            elif time == "06:00:00":
                column3_dict["Label_row3_column3"].config(text=date_temp_descr_list[index][1])
                column3_dict["Label_row4_column3"].config(text=date_temp_descr_list[index][2])
            elif time == "12:00:00":
                column3_dict["Label_row5_column3"].config(text=date_temp_descr_list[index][1])
                column3_dict["Label_row6_column3"].config(text=date_temp_descr_list[index][2])
            elif time == "18:00:00":
                column3_dict["Label_row7_column3"].config(text=date_temp_descr_list[index][1])
                column3_dict["Label_row8_column3"].config(text=date_temp_descr_list[index][2])
        elif day == "Thursday":
            if time == "00:00:00":
                column4_dict["Label_row1_column4"].config(text=date_temp_descr_list[index][1])
                column4_dict["Label_row2_column4"].config(text=date_temp_descr_list[index][2])
            elif time == "06:00:00":
                column4_dict["Label_row3_column4"].config(text=date_temp_descr_list[index][1])
                column4_dict["Label_row4_column4"].config(text=date_temp_descr_list[index][2])
            elif time == "12:00:00":
                column4_dict["Label_row5_column4"].config(text=date_temp_descr_list[index][1])
                column4_dict["Label_row6_column4"].config(text=date_temp_descr_list[index][2])
            elif time == "18:00:00":
                column4_dict["Label_row7_column4"].config(text=date_temp_descr_list[index][1])
                column4_dict["Label_row8_column4"].config(text=date_temp_descr_list[index][2])
        elif day == "Friday":
            if time == "00:00:00":
                column5_dict["Label_row1_column5"].config(text=date_temp_descr_list[index][1])
                column5_dict["Label_row2_column5"].config(text=date_temp_descr_list[index][2])
            if time == "06:00:00":
                column5_dict["Label_row3_column5"].config(text=date_temp_descr_list[index][1])
                column5_dict["Label_row4_column5"].config(text=date_temp_descr_list[index][2])
            if time == "12:00:00":
                column5_dict["Label_row5_column5"].config(text=date_temp_descr_list[index][1])
                column5_dict["Label_row6_column5"].config(text=date_temp_descr_list[index][2])
            if time == "18:00:00":
                column5_dict["Label_row7_column5"].config(text=date_temp_descr_list[index][1])
                column5_dict["Label_row8_column5"].config(text=date_temp_descr_list[index][2])
        elif day == "Saturday":
            if time == "00:00:00":
                column6_dict["Label_row1_column6"].config(text=date_temp_descr_list[index][1])
                column6_dict["Label_row2_column6"].config(text=date_temp_descr_list[index][2])
            elif time == "06:00:00":
                column6_dict["Label_row3_column6"].config(text=date_temp_descr_list[index][1])
                column6_dict["Label_row4_column6"].config(text=date_temp_descr_list[index][2])
            elif time == "12:00:00":
                column6_dict["Label_row5_column6"].config(text=date_temp_descr_list[index][1])
                column6_dict["Label_row6_column6"].config(text=date_temp_descr_list[index][2])
            elif time == "18:00:00":
                column6_dict["Label_row7_column6"].config(text=date_temp_descr_list[index][1])
                column6_dict["Label_row8_column6"].config(text=date_temp_descr_list[index][2])
        elif day == "Sunday":
            if time == "00:00:00":
                column7_dict["Label_row1_column7"].config(text=date_temp_descr_list[index][1])
                column7_dict["Label_row2_column7"].config(text=date_temp_descr_list[index][2])
            elif time == "06:00:00":
                column7_dict["Label_row3_column7"].config(text=date_temp_descr_list[index][1])
                column7_dict["Label_row4_column7"].config(text=date_temp_descr_list[index][2])
            elif time == "12:00:00":
                column7_dict["Label_row5_column7"].config(text=date_temp_descr_list[index][1])
                column7_dict["Label_row6_column7"].config(text=date_temp_descr_list[index][2])
            elif time == "18:00:00":
                column7_dict["Label_row7_column7"].config(text=date_temp_descr_list[index][1])
                column7_dict["Label_row8_column7"].config(text=date_temp_descr_list[index][2])


def show_image(window, image, bottom_frame, column=0, row=0):
    img_label = tkinter.Label(bottom_frame, image=image)
    img_label.grid(column=column, row=row)


def select_json_info():
    """
    select needed informations from last_data_converted.json
    returns (date_list, temp_list, weather_descr_list)
    """

    with open("./data/last_data_converted.json", "r") as source_file:
        datas = json.load(source_file)

    #select needed infos
    date_list = []
    temp_list = []
    weather_descr_list = []

    for index in range(len(datas["list"])):
        chosen_date = datas["list"][index]["dt_txt"]
        chosen_date = datetime.datetime.strptime(chosen_date, "%Y-%m-%d %H:%M:%S")
        chosen_date = str(chosen_date.time())
        #select 6:00, 12:00, 18:00, 00:00 time datas
        if chosen_date == "06:00:00" or chosen_date == "12:00:00" or chosen_date == "18:00:00" or chosen_date == "00:00:00":
            date_list.append(datas["list"][index]["dt_txt"])
            temp_list.append(datas["list"][index]["main"]["temp"])
            weather_descr_list.append(datas["list"][index]["weather"][0]["description"])
    return date_list, temp_list, weather_descr_list

