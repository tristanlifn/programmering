import dearpygui.dearpygui as dpg

def set_temp(sender, app_data):
    # Get the value of the slider by using the slider's unique ID
    slider_value = dpg.get_value(slider)
    if slider_value <= 15:
        dpg.set_value(1, f"Temperaturen er {slider_value}°C.\nVarmen er sat på høj styrke!")
    elif slider_value <= 20:
        dpg.set_value(1, f"Temperaturen er {slider_value}°C.\nVarmen er sat på lav styrke!")
    elif slider_value > 20:
        dpg.set_value(1, f"Temperaturen er {slider_value}°C.\nVarmen er slukket.")

dpg.create_context()
dpg.create_viewport(title="Styr varmen", width=200, height=200)

with dpg.window(label="Styr varmen"):
    slider = dpg.add_slider_int(label="", default_value=16, max_value=30, width=106)
    dpg.add_button(label="Set temepratur", callback=set_temp)
    dpg.add_text("Temperaturen er 16°C.\nVarmen er sat på lav styrke!", tag=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()