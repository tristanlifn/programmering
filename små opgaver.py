import dearpygui.dearpygui as dpg
from random import randint
from time import sleep

def addition(sender, app_data):
    int1 = dpg.get_value(add1_id)
    int2 = dpg.get_value(add2_id)
    final = round(int1 + int2, 2)
    dpg.set_value("opg 1", final)

def division(sender, app_data):
    int1 = dpg.get_value(div1_id)
    int2 = dpg.get_value(div2_id)
    final = round(int1 / int2, 2)
    dpg.set_value("opg 2", final)

def euro(sender, app_data):
    int1 = dpg.get_value(dkk_id)
    final = round((int1 * 100) / 751, 2)
    dpg.set_value("opg 3", final)

def moms(sender, app_data):
    int1 = dpg.get_value(int_id)
    int2 = round(int1 * 0.25, 2)
    final = round(int1 * 1.25, 2)
    dpg.set_value("opg 4", f"{int1}+{int2}={final}")

def change(sender, app_data):
    beløb = round(dpg.get_value(beløb_id), 2)
    indbetalt = round(dpg.get_value(inbetales_id), 2)
    if beløb > indbetalt:
        dpg.set_value("opg 5", "Ikke nok pente til at betale")
    else:
        tilbage = indbetalt - beløb
        ti = tilbage // 10
        tilbage = tilbage % 10
        fem = tilbage // 5
        tilbage = tilbage % 5
        en = tilbage // 1
        tilbage = tilbage % 1
        halv = round(tilbage * 2) / 2
        dpg.set_value("opg 5", f"{ti} ti'er, {fem} fem'er\n{en} en'er, {halv} 50-ører")

def syg(sender, app_data):
    temp = dpg.get_value(temp_id)
    if temp <= 37:
        dpg.set_value("opg 6", "Du er rask")
    else:
        dpg.set_value("opg 6", "Du har feber. Gå hjem i seng")

def karakter(sender, app_data):
    prosent = dpg.get_value(prosent_id)
    if 92 <= prosent <= 100:
        dpg.set_value("opg 7", "du fik 12")
    elif 75 <= prosent <= 91:
        dpg.set_value("opg 7", "du fik 10")
    elif 67 <= prosent <= 74:
        dpg.set_value("opg 7", "du fik 7")
    elif 58 <= prosent <= 66:
        dpg.set_value("opg 7", "du fik 4")
    elif 50 <= prosent <= 57:
        dpg.set_value("opg 7", "du fik 02")
    elif 20 <= prosent <= 49:
        dpg.set_value("opg 7", "du fik 00")
    elif 0 <= prosent <= 19:
        dpg.set_value("opg 7", "du fik -3")
    else:
        dpg.set_value("opg 7", "Ugyldigt tal")

def prosess_temp(sender, app_data):
    for i in range(50):
        temp = dpg.get_value(prosess_temp_id)
        r1 = randint(-3, 3)
        dpg.set_value(prosess_temp_id, temp + r1)

        if temp < 90:
            dpg.set_value("opg 8", "Temperaturen er for lav")
        elif temp > 100:
            dpg.set_value("opg 8", "Temperaturen er for høj")
        else:
            dpg.set_value("opg 8", "Temperaturen er OK")
        sleep(1)

dpg.create_context()
dpg.create_viewport()

with dpg.window(label="Opg 1 Nr 1"):
    add1_id = dpg.add_input_int(width=100)
    add2_id = dpg.add_input_int(width=100)
    dpg.add_button(label="Beregn", width=100, callback=addition)
    dpg.add_text("Svar", tag="opg 1")

with dpg.window(label="Opg 1 Nr 2",pos=(115,0)):
    div1_id = dpg.add_input_int(width=100)
    div2_id = dpg.add_input_int(width=100)
    dpg.add_button(label="Beregn", width=100, callback=division)
    dpg.add_text("Svar", tag="opg 2")

with dpg.window(label="Opg 1 Nr 3",pos=(230,0)):
    dkk_id = dpg.add_input_float(label="DKK", width=100, format="%.2f")
    dpg.add_button(label="Beregn", width=100, callback=euro)
    dpg.add_text("Svar", tag="opg 3")

with dpg.window(label="Opg Nr 4",pos=(370,0)):
    int_id = dpg.add_input_float(label="DKK", width=100, format="%.2f")
    dpg.add_button(label="Beregn", width=100, callback=moms)
    dpg.add_text("Svar", tag="opg 4")

with dpg.window(label="Opg 1 Nr 5",pos=(0,150), height=133, width=180):
    beløb_id = dpg.add_input_float(label="beløb", width=100, format="%.2f")
    inbetales_id = dpg.add_input_float(label="inbetales", width=100, format="%.2f")
    dpg.add_button(label="Beregn", width=100, callback=change)
    dpg.add_text("Svar", tag="opg 5")

with dpg.window(label="Opg 2 Nr 1",pos=(180,150)):
    temp_id = dpg.add_input_float(label="Temperatur", width=100, format="%.2f")
    dpg.add_button(label="Beregn", width=100, callback=syg)
    dpg.add_text("Svar", tag="opg 6")

with dpg.window(label="Opg 2 Nr 2",pos=(370,150)):
    prosent_id = dpg.add_input_int(label="%", width=100, max_value=100)
    dpg.add_button(label="Beregn", width=100, callback=karakter)
    dpg.add_text("Svar", tag="opg 7")

with dpg.window(label="Opg 2 Nr 3",pos=(0,300), width=180):
    prosess_temp_id = dpg.add_input_int(label="°C", width=100, max_value=150, default_value=95)
    dpg.add_button(label="Start", width=100, callback=prosess_temp)
    dpg.add_text("Temperaturen er ok", tag="opg 8")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()