import tkinter
import json
import resources
import datetime


# openweather condition list: https://openweathermap.org/weather-conditions

class Forecast:
    # helper functions

    @classmethod
    def show_image(cls, window, image, row=0, column=0, bg=None):
        """
        window: tkinter window or frame where the image will be placed
        """
        img_label = tkinter.Label(window, image=image, background=bg)
        img_label.grid(column=column, row=row)

    @classmethod
    def remove_previous_search(cls, frame):
        """
        frame: window or frame to forget all grid
        """
        for elem in frame.grid_slaves():
            elem.grid_forget()


class CurrentWeather(Forecast):
    @classmethod
    def current_weather(cls, window, frame):
        """
        window: main tkinter window
        frame: window or frame where widgets will be placed
        """

        cls.remove_previous_search(frame)

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
            cls.show_image(frame, resources.WEATHER_IMAGES[weather_main], row=0, column=0)
        else:    
            # 801, 802, 803 -> clouds subtype
            if weather_id == 801:
                cls.show_image(frame, resources.img_few_clouds, row=0, column=0)
            elif weather_id == 802:
                cls.show_image(frame, resources.img_scattered_clouds, row=0, column=0)
            elif weather_id == 803 or weather_id == 804:
                cls.show_image(frame, resources.img_broken_clouds, row=0, column=0)


class FiveDayForecast(Forecast):
    background_color = "#6d9bc3"


    @classmethod
    def set_background_color(cls, *args):
        """
        args: tkinter window or frames
        """
        for elem in args:
            elem.config(background=cls.background_color)


    @classmethod
    def select_json_info(cls):
        """
        select needed informations from last_data_converted.json

        returns (date_list, temp_list, weather_descr_list, weather_id_list, weather_main_list)
        """

        with open("./data/last_data_converted.json", "r") as source_file:
            datas = json.load(source_file)

        # select needed infos
        date_list = []
        temp_list = []
        weather_descr_list = []
        weather_id_list = []
        weather_main_list = []

        for index in range(len(datas["list"])):
            chosen_date = datas["list"][index]["dt_txt"]
            chosen_date = datetime.datetime.strptime(chosen_date, "%Y-%m-%d %H:%M:%S")
            chosen_date = str(chosen_date.time())
            # select 6:00, 12:00, 18:00, 00:00 time datas
            if chosen_date == "06:00:00" or chosen_date == "12:00:00" or chosen_date == "18:00:00" or chosen_date == "00:00:00":
                date_list.append(datas["list"][index]["dt_txt"])
                temp_list.append(datas["list"][index]["main"]["temp"])
                weather_descr_list.append(datas["list"][index]["weather"][0]["description"])
                weather_id_list.append(datas["list"][index]["weather"][0]["id"])
                weather_main_list.append(datas["list"][index]["weather"][0]["main"])
        return date_list, temp_list, weather_descr_list, weather_id_list, weather_main_list


    @classmethod
    def merge_selected_datas(cls, json_datas):
        """
        merge the selected json datas
        returns: list of datas dict
        """
        date_list, temp_list, weather_descr_list, weather_id_list, weather_main_list = json_datas
        # merge lists
        merged_datas = []
        for index in range(len(date_list)):
            merged_datas.append({"date_list": date_list[index], 
                                "temp_list": temp_list[index], 
                                "weather_descr_list": weather_descr_list[index], 
                                "weather_id_list": weather_id_list[index], 
                                "weather_main_list": weather_main_list[index]})
        return merged_datas


    @classmethod
    def setup_table(cls, window, frame):
        """
        setup gui
        window: main tkinter window
        frame: window or frame where widgets will be placed
        """
        total_grid_row = 13
        total_grid_column = 8

        # 0. column
        Label_row0_column0 = tkinter.Label(frame, text="", background=cls.background_color).grid(row=0, column=0)
        Label_row1_column0 = tkinter.Label(frame, text="00:00:00", background=cls.background_color).grid(row=1, column=0, rowspan=3)
        Label_row3_column0 = tkinter.Label(frame, text="06:00:00", background=cls.background_color).grid(row=4, column=0, rowspan=3)
        Label_row5_column0 = tkinter.Label(frame, text="12:00:00", background=cls.background_color).grid(row=7, column=0, rowspan=3)
        Label_row7_column0 = tkinter.Label(frame, text="18:00:00", background=cls.background_color).grid(row=10, column=0, rowspan=3)


        # column headers
        Label_row0_column1 = tkinter.Label(frame, text="Hétfő", background=cls.background_color)
        Label_row0_column1.grid(row=0, column=1)
        Label_row0_column2 = tkinter.Label(frame, text="Kedd", background=cls.background_color)
        Label_row0_column2.grid(row=0, column=2)
        Label_row0_column3 = tkinter.Label(frame, text="Szerda", background=cls.background_color)
        Label_row0_column3.grid(row=0, column=3)
        Label_row0_column4 = tkinter.Label(frame, text="Csütörtök", background=cls.background_color)
        Label_row0_column4.grid(row=0, column=4)
        Label_row0_column5 = tkinter.Label(frame, text="Péntek", background=cls.background_color)
        Label_row0_column5.grid(row=0, column=5)
        Label_row0_column6 = tkinter.Label(frame, text="Szombat", background=cls.background_color)
        Label_row0_column6.grid(row=0, column=6)
        Label_row0_column7 = tkinter.Label(frame, text="Vasárnap", background=cls.background_color)
        Label_row0_column7.grid(row=0, column=7)


        # shorter
        # to fill the flexible data to the appropriate position, we must use separated widgets with names
        # create dictionaries of label objects with name:"Label_row{number}_column{number}"
        # note: ".grid" line must be separated, because ".config"
        all_columns = []
        for current_column in range(1, total_grid_column):
            one_column = {}
            for index in range(1, total_grid_row):
                one_column["Label_row{}_column{}".format(index, current_column)] \
                    = tkinter.Label(frame, background=cls.background_color)
                one_column["Label_row{}_column{}".format(index, current_column)].grid(row=index, column=current_column)
            all_columns.append(one_column)
        
        return all_columns

        """
        # longer
        # 1. column
        # to fill the flexible data to the appropriate position, we must use separated widgets with names
        # create dictionaries of label objects with name:"Label_row{number}_column{number}"
        # note: ".grid" line must be separated, because ".config"
        # hétfő
        column1_dict = {}
        for index in range(1, total_grid_row):
            column1_dict["Label_row{}_column1".format(index)] = tkinter.Label(frame, background=cls.background_color)
            column1_dict["Label_row{}_column1".format(index)].grid(row=index, column=1)

        # 2. column
        # kedd
        column2_dict = {}
        for index in range(1, total_grid_row):
            column2_dict["Label_row{}_column2".format(index)] = tkinter.Label(frame, background=cls.background_color)
            column2_dict["Label_row{}_column2".format(index)].grid(row=index, column=2)

        # 3. column
        # szerda
        column3_dict = {}
        for index in range(1, total_grid_row):
            column3_dict["Label_row{}_column3".format(index)] = tkinter.Label(frame, background=cls.background_color)
            column3_dict["Label_row{}_column3".format(index)].grid(row=index, column=3)

        # 4. column
        column4_dict = {}
        for index in range(1, total_grid_row):
            column4_dict["Label_row{}_column4".format(index)] = tkinter.Label(frame, background=cls.background_color)
            column4_dict["Label_row{}_column4".format(index)].grid(row=index, column=4)

        # 5. column
        column5_dict = {}
        for index in range(1, total_grid_row):
            column5_dict["Label_row{}_column5".format(index)] = tkinter.Label(frame, background=cls.background_color)
            column5_dict["Label_row{}_column5".format(index)].grid(row=index, column=5)

        # 6. column
        column6_dict = {}
        for index in range(1, total_grid_row):
            column6_dict["Label_row{}_column6".format(index)] = tkinter.Label(frame, background=cls.background_color)
            column6_dict["Label_row{}_column6".format(index)].grid(row=index, column=6)

        # 7. column
        column7_dict = {}
        for index in range(1, total_grid_row):
            column7_dict["Label_row{}_column7".format(index)] = tkinter.Label(frame, background=cls.background_color)
            column7_dict["Label_row{}_column7".format(index)].grid(row=index, column=7)

        column_dicts = [column1_dict, column2_dict, column3_dict, column4_dict, column5_dict,
                        column6_dict, column7_dict]
        return column_dicts
        """


    @classmethod
    def fill_data(cls, frame, datas, columns):
        """
        frame: window or frame where widgets will be placed
        datas: list of dicts with selected datas
        columns: list of dicts with label objects
        """
        for index in range(len(datas)):
            day_time = datetime.datetime.strptime(datas[index]["date_list"], "%Y-%m-%d %H:%M:%S")
            day = datetime.datetime.strftime(day_time, "%A")
            time = datetime.datetime.strftime(day_time, "%H:%M:%S")
            # use dict keys
            if day == "Monday":
                # columns[0] = monday
                if time == "00:00:00":
                    columns[0]["Label_row1_column1"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 1, 1, cls.background_color))
                    columns[0]["Label_row2_column1"].config(text=datas[index]["temp_list"])
                    columns[0]["Label_row3_column1"].config(text=datas[index]["weather_descr_list"])
                elif time == "06:00:00":
                    columns[0]["Label_row4_column1"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 4, 1, cls.background_color))
                    columns[0]["Label_row5_column1"].config(text=datas[index]["temp_list"])
                    columns[0]["Label_row6_column1"].config(text=datas[index]["weather_descr_list"])
                elif time == "12:00:00":
                    columns[0]["Label_row7_column1"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 7, 1, cls.background_color))
                    columns[0]["Label_row8_column1"].config(text=datas[index]["temp_list"])
                    columns[0]["Label_row9_column1"].config(text=datas[index]["weather_descr_list"])
                elif time == "18:00:00":
                    columns[0]["Label_row10_column1"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 10, 1, cls.background_color))
                    columns[0]["Label_row11_column1"].config(text=datas[index]["temp_list"])
                    columns[0]["Label_row12_column1"].config(text=datas[index]["weather_descr_list"])
            elif day == "Tuesday":
                # columns[1] = tuesday
                if time == "00:00:00":
                    columns[1]["Label_row1_column2"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 1, 2, cls.background_color))
                    columns[1]["Label_row2_column2"].config(text=datas[index]["temp_list"])
                    columns[1]["Label_row3_column2"].config(text=datas[index]["weather_descr_list"])
                elif time == "06:00:00":
                    columns[1]["Label_row4_column2"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 4, 2, cls.background_color))
                    columns[1]["Label_row5_column2"].config(text=datas[index]["temp_list"])
                    columns[1]["Label_row6_column2"].config(text=datas[index]["weather_descr_list"])
                elif time == "12:00:00":
                    columns[1]["Label_row7_column2"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 7, 2, cls.background_color))
                    columns[1]["Label_row8_column2"].config(text=datas[index]["temp_list"])
                    columns[1]["Label_row9_column2"].config(text=datas[index]["weather_descr_list"])
                elif time == "18:00:00":
                    columns[1]["Label_row10_column2"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 10, 2, cls.background_color))
                    columns[1]["Label_row11_column2"].config(text=datas[index]["temp_list"])
                    columns[1]["Label_row12_column2"].config(text=datas[index]["weather_descr_list"])
            elif day == "Wednesday":
                if time == "00:00:00":
                    columns[2]["Label_row1_column3"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 1, 3, cls.background_color))
                    columns[2]["Label_row2_column3"].config(text=datas[index]["temp_list"])
                    columns[2]["Label_row3_column3"].config(text=datas[index]["weather_descr_list"])
                elif time == "06:00:00":
                    columns[2]["Label_row4_column3"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 4, 3, cls.background_color))
                    columns[2]["Label_row5_column3"].config(text=datas[index]["temp_list"])
                    columns[2]["Label_row6_column3"].config(text=datas[index]["weather_descr_list"])
                elif time == "12:00:00":
                    columns[2]["Label_row7_column3"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 7, 3, cls.background_color))
                    columns[2]["Label_row8_column3"].config(text=datas[index]["temp_list"])
                    columns[2]["Label_row9_column3"].config(text=datas[index]["weather_descr_list"])
                elif time == "18:00:00":
                    columns[2]["Label_row10_column3"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 10, 3, cls.background_color))
                    columns[2]["Label_row11_column3"].config(text=datas[index]["temp_list"])
                    columns[2]["Label_row12_column3"].config(text=datas[index]["weather_descr_list"])
            elif day == "Thursday":
                if time == "00:00:00":
                    columns[3]["Label_row1_column4"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 1, 4, cls.background_color))
                    columns[3]["Label_row2_column4"].config(text=datas[index]["temp_list"])
                    columns[3]["Label_row3_column4"].config(text=datas[index]["weather_descr_list"])
                elif time == "06:00:00":
                    columns[3]["Label_row4_column4"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 4, 4, cls.background_color))
                    columns[3]["Label_row5_column4"].config(text=datas[index]["temp_list"])
                    columns[3]["Label_row6_column4"].config(text=datas[index]["weather_descr_list"])
                elif time == "12:00:00":
                    columns[3]["Label_row7_column4"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 7, 4, cls.background_color))
                    columns[3]["Label_row8_column4"].config(text=datas[index]["temp_list"])
                    columns[3]["Label_row9_column4"].config(text=datas[index]["weather_descr_list"])
                elif time == "18:00:00":
                    columns[3]["Label_row10_column4"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 10, 4, cls.background_color))
                    columns[3]["Label_row11_column4"].config(text=datas[index]["temp_list"])
                    columns[3]["Label_row12_column4"].config(text=datas[index]["weather_descr_list"])
            elif day == "Friday":
                if time == "00:00:00":
                    columns[4]["Label_row1_column5"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 1, 5, cls.background_color))
                    columns[4]["Label_row2_column5"].config(text=datas[index]["temp_list"])
                    columns[4]["Label_row3_column5"].config(text=datas[index]["weather_descr_list"])
                if time == "06:00:00":
                    columns[4]["Label_row4_column5"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 4, 5, cls.background_color))
                    columns[4]["Label_row5_column5"].config(text=datas[index]["temp_list"])
                    columns[4]["Label_row6_column5"].config(text=datas[index]["weather_descr_list"])
                if time == "12:00:00":
                    columns[4]["Label_row7_column5"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 7, 5, cls.background_color))
                    columns[4]["Label_row8_column5"].config(text=datas[index]["temp_list"])
                    columns[4]["Label_row9_column5"].config(text=datas[index]["weather_descr_list"])
                if time == "18:00:00":
                    columns[4]["Label_row10_column5"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 10, 5, cls.background_color))
                    columns[4]["Label_row11_column5"].config(text=datas[index]["temp_list"])
                    columns[4]["Label_row12_column5"].config(text=datas[index]["weather_descr_list"])
            elif day == "Saturday":
                if time == "00:00:00":
                    columns[5]["Label_row1_column6"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 1, 6, cls.background_color))
                    columns[5]["Label_row2_column6"].config(text=datas[index]["temp_list"])
                    columns[5]["Label_row3_column6"].config(text=datas[index]["weather_descr_list"])
                elif time == "06:00:00":
                    columns[5]["Label_row4_column6"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 4, 6, cls.background_color))
                    columns[5]["Label_row5_column6"].config(text=datas[index]["temp_list"])
                    columns[5]["Label_row6_column6"].config(text=datas[index]["weather_descr_list"])
                elif time == "12:00:00":
                    columns[5]["Label_row7_column6"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 7, 6, cls.background_color))
                    columns[5]["Label_row8_column6"].config(text=datas[index]["temp_list"])
                    columns[5]["Label_row9_column6"].config(text=datas[index]["weather_descr_list"])
                elif time == "18:00:00":
                    columns[5]["Label_row10_column6"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 10, 6, cls.background_color))
                    columns[5]["Label_row11_column6"].config(text=datas[index]["temp_list"])
                    columns[5]["Label_row12_column6"].config(text=datas[index]["weather_descr_list"])
            elif day == "Sunday":
                if time == "00:00:00":
                    columns[6]["Label_row1_column7"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 1, 7, cls.background_color))
                    columns[6]["Label_row2_column7"].config(text=datas[index]["temp_list"])
                    columns[6]["Label_row3_column7"].config(text=datas[index]["weather_descr_list"])
                elif time == "06:00:00":
                    columns[6]["Label_row4_column7"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 4, 7, cls.background_color))
                    columns[6]["Label_row5_column7"].config(text=datas[index]["temp_list"])
                    columns[6]["Label_row6_column7"].config(text=datas[index]["weather_descr_list"])
                elif time == "12:00:00":
                    columns[6]["Label_row7_column7"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 7, 7, cls.background_color))
                    columns[6]["Label_row8_column7"].config(text=datas[index]["temp_list"])
                    columns[6]["Label_row9_column7"].config(text=datas[index]["weather_descr_list"])
                elif time == "18:00:00":
                    columns[6]["Label_row10_column7"].config(image=cls.show_image \
                    (frame, resources.ICONS_BY_ID[datas[index]["weather_id_list"]], 10, 7, cls.background_color))
                    columns[6]["Label_row11_column7"].config(text=datas[index]["temp_list"])
                    columns[6]["Label_row12_column7"].config(text=datas[index]["weather_descr_list"])


    @classmethod
    def run(cls, window, frame):
        cls.remove_previous_search(frame)
        cls.set_background_color(frame)
        merged_datas = cls.merge_selected_datas(cls.select_json_info())
        column_dicts = cls.setup_table(window, frame)
        cls.fill_data(frame, merged_datas, column_dicts)


# gui callable
def show_five_day_forecast(window, frame):
    FiveDayForecast.run(window, frame)


# gui callable
def show_current_weather(window, frame):
    CurrentWeather.current_weather(window, frame)
