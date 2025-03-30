import dearpygui.dearpygui as dpg

def set_temp(sender, app_data):
    slider_value = dpg.get_value(slider)
    if slider_value <= 15:
        dpg.set_value(1, f"Temperaturen er {slider_value}°C.\nVarmen er sat på høj styrke!")
    elif slider_value <= 20:
        dpg.set_value(1, f"Temperaturen er {slider_value}°C.\nVarmen er sat på lav styrke!")
    elif slider_value > 20:
        dpg.set_value(1, f"Temperaturen er {slider_value}°C.\nVarmen er slukket.")

dpg.create_context()

with dpg.window(label="Styr varmen", width=250, height=200):
    with dpg.group(horizontal=True):
        slider = dpg.add_slider_int(default_value=16, max_value=30, clamped=True, vertical=True, callback=set_temp, tag="slider")

    dpg.add_text("Temperaturen er 16°C.\nVarmen er sat på lav styrke!", tag=1, pos=(36, 23))

dpg.create_viewport(title="Styr varmen", width=250, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()