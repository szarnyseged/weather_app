import tkinter
from PIL import ImageTk, Image
import json
import resources
import datetime


# openweather condition list: https://openweathermap.org/weather-conditions
# gui_funcs
def show_current_weather(window, frame):
    """
    window: main tkinter window
    frame: window or frame where widgets will be placed
    """

    remove_previous_search(frame)

    with open("./data/last_data_converted.json", "r") as source_file:
        datas = json.load(source_file)
    
    # labels
    description = datas["weather"][0]["description"]
    description_label = tkinter.Label(frame, text=description)
    temp = datas["main"]["temp"]
    temp_label = tkinter.Label(frame, text=temp)

    # grid positions
    description_label.grid(column=0, row=1)
    temp_label.grid(column=0, row=2)


    weather_id = datas["weather"][0]["id"]
    weather_main = datas["weather"][0]["main"]
    if weather_main != "Clouds":
        tkinter.Label(frame, image=resources.WEATHER_IMAGES[weather_main]).grid(row=0, column=0)
    else:    
        # 801, 802, 803 -> clouds subtype
        if weather_id == 801:
            tkinter.Label(frame, image=resources.img_few_clouds).grid(row=0, column=0)
        elif weather_id == 802:
            tkinter.Label(frame, image=resources.img_scattered_clouds).grid(row=0, column=0)
        elif weather_id == 803 or weather_id == 804:
            tkinter.Label(frame, image=resources.img_broken_clouds).grid(row=0, column=0)


class Five_day_forecast:

    def setup_table(self):
        # setup gui
        # 0. column
        Label_row0_column0 = tkinter.Label(bottom_frame, text="", background=background_color).grid(row=0, column=0)
        Label_row1_column0 = tkinter.Label(bottom_frame, text="00:00:00", background=background_color).grid(row=1, column=0, rowspan=3)
        Label_row3_column0 = tkinter.Label(bottom_frame, text="06:00:00", background=background_color).grid(row=4, column=0, rowspan=3)
        Label_row5_column0 = tkinter.Label(bottom_frame, text="12:00:00", background=background_color).grid(row=7, column=0, rowspan=3)
        Label_row7_column0 = tkinter.Label(bottom_frame, text="18:00:00", background=background_color).grid(row=10, column=0, rowspan=3)


        # 1. column
        # to fill the flexible data to the appropriate position, we must use separated widgets with names
        # create dictionaries of label objects with name:"Label_row{number}_column{number}"
        # note: ".grid" line must be separated, because ".config"
        Label_row0_column1 = tkinter.Label(bottom_frame, text="Hétfő", background=background_color)
        Label_row0_column1.grid(row=0, column=1)
        column1_dict = {}
        for index in range(1, total_grid_row):
            column1_dict["Label_row{}_column1".format(index)] = tkinter.Label(bottom_frame, background=background_color)
            column1_dict["Label_row{}_column1".format(index)].grid(row=index, column=1)


        # 2. column
        Label_row0_column2 = tkinter.Label(bottom_frame, text="Kedd", background=background_color)
        Label_row0_column2.grid(row=0, column=2)
        column2_dict = {}
        for index in range(1, total_grid_row):
            column2_dict["Label_row{}_column2".format(index)] = tkinter.Label(bottom_frame, background=background_color)
            column2_dict["Label_row{}_column2".format(index)].grid(row=index, column=2)

        # 3. column
        Label_row0_column3 = tkinter.Label(bottom_frame, text="Szerda", background=background_color)
        Label_row0_column3.grid(row=0, column=3)
        column3_dict = {}
        for index in range(1, total_grid_row):
            column3_dict["Label_row{}_column3".format(index)] = tkinter.Label(bottom_frame, background=background_color)
            column3_dict["Label_row{}_column3".format(index)].grid(row=index, column=3)


        # 4. column
        Label_row0_column4 = tkinter.Label(bottom_frame, text="Csütörtök", background=background_color)
        Label_row0_column4.grid(row=0, column=4)
        column4_dict = {}
        for index in range(1, total_grid_row):
            column4_dict["Label_row{}_column4".format(index)] = tkinter.Label(bottom_frame, background=background_color)
            column4_dict["Label_row{}_column4".format(index)].grid(row=index, column=4)


        # 5. column
        Label_row0_column5 = tkinter.Label(bottom_frame, text="Péntek", background=background_color)
        Label_row0_column5.grid(row=0, column=5)
        column5_dict = {}
        for index in range(1, total_grid_row):
            column5_dict["Label_row{}_column5".format(index)] = tkinter.Label(bottom_frame, background=background_color)
            column5_dict["Label_row{}_column5".format(index)].grid(row=index, column=5)

        # 6. column
        Label_row0_column6 = tkinter.Label(bottom_frame, text="Szombat", background=background_color)
        Label_row0_column6.grid(row=0, column=6)
        column6_dict = {}
        for index in range(1, total_grid_row):
            column6_dict["Label_row{}_column6".format(index)] = tkinter.Label(bottom_frame, background=background_color)
            column6_dict["Label_row{}_column6".format(index)].grid(row=index, column=6)

        # 7. column
        Label_row0_column7 = tkinter.Label(bottom_frame, text="Vasárnap", background=background_color)
        Label_row0_column7.grid(row=0, column=7)
        column7_dict = {}
        for index in range(1, total_grid_row):
            column7_dict["Label_row{}_column7".format(index)] = tkinter.Label(bottom_frame, background=background_color)
            column7_dict["Label_row{}_column7".format(index)].grid(row=index, column=7)



    def fill_data(self):
        # fill data
        for index in range(len(merged_datas)):
            day_time = datetime.datetime.strptime(merged_datas[index]["date_list"], "%Y-%m-%d %H:%M:%S")
            day = datetime.datetime.strftime(day_time, "%A")
            time = datetime.datetime.strftime(day_time, "%H:%M:%S")
        # use dict keys
        if day == "Monday":
            if time == "00:00:00":
                ###################### nincs "clouds" rendezve. id alapján kellett volna, ami így bajos. ->?egész ICONS-t id alapúra?. ->?átszervez ezt (kéne).
                column1_dict["Label_row1_column1"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 1, 1))
                column1_dict["Label_row2_column1"].config(text=merged_datas[index]["temp_list"])
                column1_dict["Label_row3_column1"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "06:00:00":
                column1_dict["Label_row4_column1"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 4, 1))
                column1_dict["Label_row5_column1"].config(text=merged_datas[index]["temp_list"])
                column1_dict["Label_row6_column1"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "12:00:00":
                column1_dict["Label_row7_column1"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 7, 1))
                column1_dict["Label_row8_column1"].config(text=merged_datas[index]["temp_list"])
                column1_dict["Label_row9_column1"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "18:00:00":
                column1_dict["Label_row10_column1"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 10, 1))
                column1_dict["Label_row11_column1"].config(text=merged_datas[index]["temp_list"])
                column1_dict["Label_row12_column1"].config(text=merged_datas[index]["weather_descr_list"])
        elif day == "Tuesday":
            if time == "00:00:00":
                column2_dict["Label_row1_column2"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 1, 2))
                column2_dict["Label_row2_column2"].config(text=merged_datas[index]["temp_list"])
                column2_dict["Label_row3_column2"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "06:00:00":
                column2_dict["Label_row4_column2"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 4, 2))
                column2_dict["Label_row5_column2"].config(text=merged_datas[index]["temp_list"])
                column2_dict["Label_row6_column2"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "12:00:00":
                column2_dict["Label_row7_column2"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 7, 2))
                column2_dict["Label_row8_column2"].config(text=merged_datas[index]["temp_list"])
                column2_dict["Label_row9_column2"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "18:00:00":
                column2_dict["Label_row10_column2"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 10, 2))
                column2_dict["Label_row11_column2"].config(text=merged_datas[index]["temp_list"])
                column2_dict["Label_row12_column2"].config(text=merged_datas[index]["weather_descr_list"])
        elif day == "Wednesday":
            if time == "00:00:00":
                column3_dict["Label_row1_column3"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 1, 3))
                column3_dict["Label_row2_column3"].config(text=merged_datas[index]["temp_list"])
                column3_dict["Label_row3_column3"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "06:00:00":
                column3_dict["Label_row4_column3"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 4, 3))
                column3_dict["Label_row5_column3"].config(text=merged_datas[index]["temp_list"])
                column3_dict["Label_row6_column3"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "12:00:00":
                column3_dict["Label_row7_column3"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 7, 3))
                column3_dict["Label_row8_column3"].config(text=merged_datas[index]["temp_list"])
                column3_dict["Label_row9_column3"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "18:00:00":
                column3_dict["Label_row10_column3"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 10, 3))
                column3_dict["Label_row11_column3"].config(text=merged_datas[index]["temp_list"])
                column3_dict["Label_row12_column3"].config(text=merged_datas[index]["weather_descr_list"])
        elif day == "Thursday":
            if time == "00:00:00":
                column4_dict["Label_row1_column4"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 1, 4))
                column4_dict["Label_row2_column4"].config(text=merged_datas[index]["temp_list"])
                column4_dict["Label_row3_column4"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "06:00:00":
                column4_dict["Label_row4_column4"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 4, 4))
                column4_dict["Label_row5_column4"].config(text=merged_datas[index]["temp_list"])
                column4_dict["Label_row6_column4"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "12:00:00":
                column4_dict["Label_row7_column4"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 7, 4))
                column4_dict["Label_row8_column4"].config(text=merged_datas[index]["temp_list"])
                column4_dict["Label_row9_column4"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "18:00:00":
                column4_dict["Label_row10_column4"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 10, 4))
                column4_dict["Label_row11_column4"].config(text=merged_datas[index]["temp_list"])
                column4_dict["Label_row12_column4"].config(text=merged_datas[index]["weather_descr_list"])
        elif day == "Friday":
            if time == "00:00:00":
                column5_dict["Label_row1_column5"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 1, 5))
                column5_dict["Label_row2_column5"].config(text=merged_datas[index]["temp_list"])
                column5_dict["Label_row3_column5"].config(text=merged_datas[index]["weather_descr_list"])
            if time == "06:00:00":
                column5_dict["Label_row4_column5"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 4, 5))
                column5_dict["Label_row5_column5"].config(text=merged_datas[index]["temp_list"])
                column5_dict["Label_row6_column5"].config(text=merged_datas[index]["weather_descr_list"])
            if time == "12:00:00":
                column5_dict["Label_row7_column5"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 7, 5))
                column5_dict["Label_row8_column5"].config(text=merged_datas[index]["temp_list"])
                column5_dict["Label_row9_column5"].config(text=merged_datas[index]["weather_descr_list"])
            if time == "18:00:00":
                column5_dict["Label_row10_column5"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 10, 5))
                column5_dict["Label_row11_column5"].config(text=merged_datas[index]["temp_list"])
                column5_dict["Label_row12_column5"].config(text=merged_datas[index]["weather_descr_list"])
        elif day == "Saturday":
            if time == "00:00:00":
                column6_dict["Label_row1_column6"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 1, 6))
                column6_dict["Label_row2_column6"].config(text=merged_datas[index]["temp_list"])
                column6_dict["Label_row3_column6"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "06:00:00":
                column6_dict["Label_row4_column6"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 4, 6))
                column6_dict["Label_row5_column6"].config(text=merged_datas[index]["temp_list"])
                column6_dict["Label_row6_column6"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "12:00:00":
                column6_dict["Label_row7_column6"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 7, 6))
                column6_dict["Label_row8_column6"].config(text=merged_datas[index]["temp_list"])
                column6_dict["Label_row9_column6"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "18:00:00":
                column6_dict["Label_row10_column6"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 10, 6))
                column6_dict["Label_row11_column6"].config(text=merged_datas[index]["temp_list"])
                column6_dict["Label_row12_column6"].config(text=merged_datas[index]["weather_descr_list"])
        elif day == "Sunday":
            if time == "00:00:00":
                column7_dict["Label_row1_column7"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 1, 7))
                column7_dict["Label_row2_column7"].config(text=merged_datas[index]["temp_list"])
                column7_dict["Label_row3_column7"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "06:00:00":
                column7_dict["Label_row4_column7"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 4, 7))
                column7_dict["Label_row5_column7"].config(text=merged_datas[index]["temp_list"])
                column7_dict["Label_row6_column7"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "12:00:00":
                column7_dict["Label_row7_column7"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 7, 7))
                column7_dict["Label_row8_column7"].config(text=merged_datas[index]["temp_list"])
                column7_dict["Label_row9_column7"].config(text=merged_datas[index]["weather_descr_list"])
            elif time == "18:00:00":
                column7_dict["Label_row10_column7"].config(image=show_image(bottom_frame, resources.ICONS_BY_ID[merged_datas[index]["weather_id_list"]], 10, 7))
                column7_dict["Label_row11_column7"].config(text=merged_datas[index]["temp_list"])
                column7_dict["Label_row12_column7"].config(text=merged_datas[index]["weather_descr_list"])


    def remove_previous_search(self, frame):
        """
        frame: window or frame to forget all grid
        """
        for elem in frame.grid_slaves():
            elem.grid_forget()


def show_five_day_forecast(window, bottom_frame):
    pass



def show_image(window, image, row=0, column=0):
    """
    window: tkinter window or frame where the image will be placed
    """
    img_label = tkinter.Label(window, image=image, background="#6d9bc3")
    img_label.grid(column=column, row=row)


def remove_previous_search(frame):
    """
    frame: window or frame to forget all grid
    """
    for elem in frame.grid_slaves():
        elem.grid_forget()
