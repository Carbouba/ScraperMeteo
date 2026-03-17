import customtkinter as ctk
from PIL import Image
import sys
import os

# D'abord tous les chemins
sys.path.append("..")
sys.path.append("../data")

# Ensuite tous les imports externes
from style import DARK_COLOR, LIGHT_COLOR, FONTS, DIMENSIONS



base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, "..", "images")

def entry(parent, placeholder, width, heigh):
    return ctk.CTkEntry(parent,
                placeholder_text=placeholder,
                placeholder_text_color=DARK_COLOR["text_dim"],
                text_color=DARK_COLOR["text"],
                fg_color=DARK_COLOR["surface2"],
                border_width=1,
                border_color=DARK_COLOR["border"],
                width=width, height=heigh,
                corner_radius=DIMENSIONS["border_radius"],
                font=FONTS["placeholder"],
                )

def label(parent, text, font_key="label", color_key="text_muted"):
    return ctk.CTkLabel(parent, text=text,
                    text_color=DARK_COLOR["bg"],
                    font=FONTS[font_key])

def btn_primary(parent, text, command, width, height, img):
    return ctk.CTkButton(parent, text=text,
                     font=FONTS["button"],
                     text_color=DARK_COLOR["white"],
                     fg_color=DARK_COLOR["primary"],
                     hover_color=DARK_COLOR["primary_hover"],
                     corner_radius=DIMENSIONS["border_radius"],
                     cursor="hand2",
                     command=command,
                     width=width, height=height,
                     image=img, compound="left")

def action_btn(parent, text, command, width, height, btn_color, img):
    return ctk.CTkButton(parent, text=text,
                     font=FONTS["button"],
                     text_color=DARK_COLOR["white"],
                     image=ctk.CTkImage(Image.open(os.path.join(img_dir, img)), size=(20, 20)),
                     compound="left",
                     fg_color=DARK_COLOR["action_btn"][btn_color],
                     corner_radius=DIMENSIONS["border_radius"],
                     cursor="hand2",
                     command=command,
                     width=width, height=height,
                     )

# Bouton thème
def on_toggle(parent, img, text):
    if text == "Dark":
        return ctk.CTkButton(parent, image=img,
                                text="Light", font=FONTS["button"],
                                fg_color=DARK_COLOR["surface2"],
                                compound="left",
                                width=115, height=40,
                                corner_radius=DIMENSIONS["border_radius"])
                                
    else:
        return ctk.CTkButton(parent, image=img,
                                text="Dark", font=FONTS["button"],
                                fg_color=LIGHT_COLOR["surface"],
                                width=115, height=40)

# ── Vue principale ────────────────────────────────────────────
def main_view():
    app = ctk.CTk()
    app.title("ScraperMeteo")
    app.geometry("1100x800")
    app.resizable(0,0)
    app.configure(fg_color=DARK_COLOR["bg"])

    # Header frame
    header_frame = ctk.CTkFrame(app, fg_color=DARK_COLOR["bg"],width=1050, height=60)
    header_frame.pack_propagate(False)
    header_frame.pack(pady=(15, 5))
    
    ctk.CTkLabel(header_frame, text="ScraperMeteo", font=FONTS["title"],
                 text_color=DARK_COLOR["text"]).place(x=0, y=15)
    
    switch_theme_btn_img = ctk.CTkImage(Image.open(os.path.join(img_dir, "sun.png")), size=(20, 20))
    switch_theme_btn = on_toggle(header_frame, switch_theme_btn_img, "Dark")
    switch_theme_btn.place(relx=1.0, x=-0, y=10, anchor="ne")
    
    # Search frame
    search_frame = ctk.CTkFrame(app, fg_color=DARK_COLOR["bg"], width=1050, height=65)
    search_frame.pack_propagate(False)
    search_frame.pack(pady=5)

    search_entry = entry(search_frame, "Entrer le nom d'une ville...", 650, 45)
    search_entry.place(x=0, y=10)

    search_img = ctk.CTkImage(Image.open(os.path.join(img_dir, "search.png")))    
    search_btn = btn_primary(search_frame, "Rechercher", "", 145, 45, search_img)
    search_btn.place(x=665, y=10)
    
    filter_btn = ctk.CTkOptionMenu(search_frame, values=["Filtrer", "Date"],
                                   fg_color=DARK_COLOR["primary"],
                                   text_color=DARK_COLOR["white"],
                                   font=FONTS["button"], cursor="hand2",
                                   corner_radius=DIMENSIONS["border_radius"],
                                   width=145, height=45,)
    filter_btn.place(x=820, y=10)
    
    center_frame = ctk.CTkFrame(app, fg_color=DARK_COLOR["bg"], width=1050, height=330)
    center_frame.pack(pady=(10, 5))

    locat_ind_img = ctk.CTkImage(Image.open(os.path.join(img_dir, "locate.png")), size=(12, 15))
    locat_ind = ctk.CTkButton(center_frame, 
                            text="Niamey, NE", font=FONTS["subtitle"], 
                            text_color=DARK_COLOR["white"],
                            image=locat_ind_img,
                            fg_color="#134e4a",
                            corner_radius=500,
                            compound="left",
                            width=120, height=30,
                            hover=False
                            )
    locat_ind.place(x=5, y=0)

    # Chart frame
    chart_frame = ctk.CTkFrame(center_frame, fg_color=DARK_COLOR["surface2"],
                            border_width=1,
                            border_color=DARK_COLOR["border"],
                            corner_radius=DIMENSIONS["border_radius"],
                            width=1050, height=280)
    chart_frame.pack_propagate(False)
    chart_frame.place(x=0, y=40)
   

    # Cards frame
    cards_frame = ctk.CTkFrame(app, fg_color=DARK_COLOR["bg"], width=1050, height=330)
    cards_frame.pack_propagate(False)
    cards_frame.pack(pady=(5, 0))

    # Température
    temp_frame = ctk.CTkFrame(cards_frame, fg_color=DARK_COLOR["cards"]["temp"],
                            width=335, height=120, corner_radius=DIMENSIONS["border_radius"])
    temp_frame.pack_propagate(False)
    temp_frame.grid(row=0, column=0, padx=10, pady=10)
    temp_img = ctk.CTkImage(Image.open(os.path.join(img_dir, "temp.png")), size=(14, 20))
    ctk.CTkLabel(temp_frame, text="  Température", font=FONTS["subtitle"],
                 image=temp_img, compound="left", text_color=DARK_COLOR["white"]).place(x=15, y=15)
    ctk.CTkLabel(temp_frame, text="25 C°", font=FONTS["h1"],
                 text_color=DARK_COLOR["white"]).place(x=15, y=48)

    # Humidité
    humidity_frame = ctk.CTkFrame(cards_frame, fg_color=DARK_COLOR["cards"]["humidity"],
                            width=335, height=120, corner_radius=DIMENSIONS["border_radius"])
    humidity_frame.pack_propagate(False)
    humidity_frame.grid(row=0, column=1, padx=10, pady=10)
    humidity_img = ctk.CTkImage(Image.open(os.path.join(img_dir, "humidity.png")), size=(20, 20))
    ctk.CTkLabel(humidity_frame, text="  Humidité", font=FONTS["subtitle"],
                 image=humidity_img, compound="left", text_color=DARK_COLOR["white"]).place(x=15, y=15)
    ctk.CTkLabel(humidity_frame, text="25%", font=FONTS["h1"],
                 text_color=DARK_COLOR["white"]).place(x=15, y=48)

    # Vent
    wind_frame = ctk.CTkFrame(cards_frame, fg_color=DARK_COLOR["cards"]["wind"],
                            width=335, height=120, corner_radius=DIMENSIONS["border_radius"])
    wind_frame.pack_propagate(False)
    wind_frame.grid(row=0, column=2, padx=10, pady=10)
    wind_img = ctk.CTkImage(Image.open(os.path.join(img_dir, "wind.png")), size=(20, 20))
    ctk.CTkLabel(wind_frame, text="  Vent", font=FONTS["subtitle"],
                 image=wind_img, compound="left", text_color=DARK_COLOR["white"]).place(x=15, y=15)
    ctk.CTkLabel(wind_frame, text="25 km/h", font=FONTS["h1"],
                 text_color=DARK_COLOR["white"]).place(x=15, y=48)

    # Action frame
    Action_frame = ctk.CTkFrame(app, fg_color=DARK_COLOR["bg"],
                  width=1050, height=60)
    Action_frame.pack_propagate(False)
    Action_frame.pack(pady=10)

    # History button
    history_btn = action_btn(Action_frame, "Historique", "", 145, 45, "history", "history.png")
    history_btn.pack(anchor="w", padx=(0,10), side="left")

    # Forecast button
    forecast_btn = action_btn(Action_frame, "Prévisions", "", 145, 45, "forecast", "forecast.png")
    forecast_btn.pack(anchor="w", padx=10, side="left")

    # Export button
    export_btn = action_btn(Action_frame, "Exporter", "", 145, 45, "export", "export.png")
    export_btn.pack(anchor="w", padx=10, side="left")

    # Footer frame
    footer_frame = ctk.CTkFrame(app, fg_color=DARK_COLOR["surface2"],
                                width=1050, height=50,
                                border_width=1,
                                border_color=DARK_COLOR["border"],
                                corner_radius=DIMENSIONS["border_radius"])
    footer_frame.pack_propagate(False)
    footer_frame.pack(pady=10)

    updt_label = ctk.CTkLabel(footer_frame, text="Dernière synchronisation depuis : 2026-03-16 ",
                            font=FONTS["placeholder"],
                            fg_color=DARK_COLOR["surface2"],
                            text_color=DARK_COLOR["white"])
    updt_label.place(x=10, y=10)

    sync_btn = action_btn(footer_frame, "Sync", "", 50, 20, "export", "sync.png")
    sync_btn.place(x=950, y=10)

    app.mainloop()

main_view()