import tkinter
import api_request
import gui_funcs
import resources

#setup window
window = tkinter.Tk()
window.geometry("750x400+400+200")
window.title("new window")
resources.load_images(window)


#frames (panels)
top_frame=tkinter.LabelFrame(window, relief="flat")
top_frame.grid(column=0, row=0, pady=(10,0))
bottom_frame=tkinter.LabelFrame(window, relief="raised", borderwidth=4)
bottom_frame.grid(column=0, row=1, pady=(10,0))


#entrys
user_input_city_entry = tkinter.Entry(top_frame, width=25)
user_input_country_entry = tkinter.Entry(top_frame, width=6)


#labels
input_label_city= tkinter.Label(top_frame, text="város neve")
input_label_coutry =tkinter.Label(top_frame, text="(opcionális) országkódja")


#buttons
search_current_weather_button = tkinter.Button(top_frame, text="jelenlegi időjárás",
 command=lambda: [api_request.get_current_weather(user_input_city_entry.get(), user_input_country_entry.get()), gui_funcs.show_current_weather(window, bottom_frame)])
search_five_day_forecast_button = tkinter.Button(top_frame, text="5 napos előrejelzés",
 command=lambda: [api_request.get_five_day_forecast(user_input_city_entry.get(), user_input_country_entry.get()), gui_funcs.show_five_day_forecast(window, bottom_frame)])


#grid sys
user_input_city_entry.grid(column=0, row=0, pady=(5, 0), padx=(5, 0))
user_input_country_entry.grid(column=1, row=0)
input_label_city.grid(column=0, row=1, pady=(5, 0))
input_label_coutry.grid(column=1, row=1, pady=(5, 0), rowspan=4)

search_current_weather_button.grid(column=2, row=0, pady=(0, 10))
search_five_day_forecast_button.grid(column=2, row=1)

window.mainloop()