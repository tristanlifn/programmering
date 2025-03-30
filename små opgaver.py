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
        add = temp + r1
        dpg.set_value(prosess_temp_id, add)

        if temp < 90:
            dpg.set_value("opg 8", "Temperaturen er for lav")
        elif temp > 100:
            dpg.set_value("opg 8", "Temperaturen er for høj")
        else:
            dpg.set_value("opg 8", "Temperaturen er OK")
        sleep(1)

def løn(sender, app_data):
    time = dpg.get_value(løn_id)
    wage = 170.93
    if time <= 37:
        dpg.set_value("opg 9", time * wage)
    elif 37 < time:
        overtime = time - 37
        dpg.set_value("opg 9", overtime * (1.3 * wage) + 6324.41 )
    else:
        dpg.set_value("opg 9", time * (wage * 1.3) + 1235.5)

def kaffe(sender, app_data):
    størelse = dpg.get_value(kaffe_størelse_id)
    if størelse == 1:
        dpg.set_value("opg 10", "15")
    elif størelse == 2:
        dpg.set_value("opg 10", "27")
    elif størelse == 3:
        dpg.set_value("opg 10", "40")

def syv_tabellen(sender, app_data):
    a = []
    for i in range(10):
        a.append(7 * (i + 1))

    dpg.set_value("opg 11", a)

def største_tal(sender, app_data):
    tal_1 = dpg.get_value(tal1_id)
    tal_2 = dpg.get_value(tal2_id)
    a = max(tal_1, tal_2)
    dpg.set_value("opg 12", a)

def gæt_tallet(sender, app_data):
    tal = dpg.get_value("tal")
    forsøg = dpg.get_value("forsøg")
    gættet = dpg.get_value(gættet_tal_id)
    
    if forsøg > 0:
        if gættet == tal:
            dpg.set_value("opg 13", "Tillykke! Du gættede rigtigt!")
            dpg.set_value("forsøg", 0)
        else:
            forsøg -= 1
            dpg.set_value("forsøg", forsøg)
            
            if forsøg == 0:
                dpg.set_value("opg 13", f"Du tabte. Tallet var {tal}")
            elif gættet < tal:
                dpg.set_value("opg 13", f"For lavt, {forsøg} forsøg tilbage")
            elif gættet > tal:
                dpg.set_value("opg 13", f"For højt, {forsøg} forsøg tilbage")

def slå_tærninger(sender, app_data):
    slag = randint(1, 6)
    print(slag)

    if slag == 6:
        dpg.set_value("opg 14", "Du slog en 6'er")
    else:
        dpg.set_value("opg 14", f"Du slog en {slag}'er")

dpg.create_context()

with dpg.window(label="Python små opgaver", width=600, height=600):
    with dpg.tab_bar(label="Opgaver"):
        with dpg.tab(label="Variabler og aritmatik"):
            
            with dpg.tree_node(label="Addition"):
                    add1_id = dpg.add_input_int(width=100)
                    add2_id = dpg.add_input_int(width=100)
                    dpg.add_button(label="Beregn", width=100, callback=addition)
                    dpg.add_text("Svar", tag="opg 1")

            with dpg.tree_node(label="Division"):
                div1_id = dpg.add_input_int(width=100)
                div2_id = dpg.add_input_int(width=100)
                dpg.add_button(label="Beregn", width=100, callback=division)
                dpg.add_text("Svar", tag="opg 2")

            with dpg.tree_node(label="DKK til EURO"):
                dkk_id = dpg.add_input_float(label="DKK", width=100, format="%.2f")
                dpg.add_button(label="Beregn", width=100, callback=euro)
                dpg.add_text("Svar", tag="opg 3")

            with dpg.tree_node(label="Moms regner"):
                int_id = dpg.add_input_float(label="DKK", width=100, format="%.2f")
                dpg.add_button(label="Beregn", width=100, callback=moms)
                dpg.add_text("Svar", tag="opg 4")

            with dpg.tree_node(label="Byttepenge"):
                beløb_id = dpg.add_input_float(label="beløb", width=100, format="%.2f")
                inbetales_id = dpg.add_input_float(label="inbetales", width=100, format="%.2f")
                dpg.add_button(label="Beregn", width=100, callback=change)
                dpg.add_text("Svar", tag="opg 5")


        with dpg.tab(label="If them else"):
            with dpg.tree_node(label="Har du feber?"):
                temp_id = dpg.add_input_float(label="Temperatur", width=100, format="%.2f")
                dpg.add_button(label="Beregn", width=100, callback=syg)
                dpg.add_text("Svar", tag="opg 6")

            with dpg.tree_node(label="Hvilken karakter"):
                prosent_id = dpg.add_input_int(label="%", width=100, min_value=0, max_value=100, min_clamped=True, max_clamped=True)
                dpg.add_button(label="Beregn", width=100, callback=karakter)
                dpg.add_text("Svar", tag="opg 7")

            with dpg.tree_node(label="Hold temperaturen mellem 90-100"):
                prosess_temp_id = dpg.add_input_int(label="°C", width=100, max_value=150, max_clamped=True, default_value=95)
                dpg.add_button(label="Start", width=100, callback=prosess_temp)
                dpg.add_text("Temperaturen er ok", tag="opg 8")
            
            with dpg.tree_node(label="IT arbejder løn"):
                løn_id = dpg.add_input_int(label="Timer", width=100, default_value=95)
                dpg.add_button(label="Start", width=100, callback=løn)
                dpg.add_text("Svar", tag="opg 9")

            with dpg.tree_node(label="Kaffe automat"):
                kaffe_størelse_id = dpg.add_input_int(width=100, min_value=1, max_value=3, min_clamped=True, max_clamped=True, default_value=1)
                dpg.add_button(label="Beregn", width=100, callback=kaffe)
                dpg.add_text("Svar", tag="opg 10")


        with dpg.tab(label="Itteration - løkker"):
            with dpg.tree_node(label="7 tabellen"):
                dpg.add_button(label="Udskriv", callback=syv_tabellen)
                dpg.add_text("Svar", tag="opg 11")

            with dpg.tree_node(label="Find det største tal"):
                tal1_id = dpg.add_input_int(width=100)
                tal2_id = dpg.add_input_int(width=100)
                dpg.add_button(label="Beregn", callback=største_tal)
                dpg.add_text("Svar", tag="opg 12")

            with dpg.tree_node(label="Gæt tallet"):
                gættet_tal_id = dpg.add_input_int(default_value=1, min_value=1, max_value=100, min_clamped=True, max_clamped=True)
                dpg.add_input_int(default_value=5, tag="forsøg", show=False)  # Corrected to add_input_int
                dpg.add_input_int(default_value=randint(1, 100), tag="tal", show=False)  # Corrected to add_input_int
                dpg.add_button(label="Gæt", callback=gæt_tallet)
                dpg.add_text("Tryk på start", tag="opg 13")

            with dpg.tree_node(label="Slå indtil det er en 6'er"):
                dpg.add_button(label="Kast", callback=slå_tærninger)  
                dpg.add_text("Slå tærningen", tag="opg 14")

dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()