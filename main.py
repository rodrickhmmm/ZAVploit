# ZAVploit

from playwright.sync_api import sync_playwright
import time
import pyautogui
from screeninfo import get_monitors
import customtkinter
import threading
import os
from PIL import Image
import queue

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

for m in get_monitors():
    vyska = m.height
    sirka = m.width

jmeno = None
heslo = None
prohlizec = "firefox"
muzesSpustit = False
moznost = "Z*V theme"
browser = None
context = None
page = None
command_queue = queue.Queue()
kliknuto = 0

# Funkce ktera spusti prohlizec---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def spustitBrowser():
    global jmeno, heslo, muzesSpustit, prohlizec
    global browser, context, page

    if muzesSpustit == False:
        app.error.place(x=40, y=260)
        print("Nejprve zadej jméno a heslo!")
    else:
        with sync_playwright() as p:
            clear()
            print("ZAVploit browser spuštěn")
            print("Spouští se:", prohlizec)
            if prohlizec == "firefox":
                browser = p.firefox.launch(headless=False)
            else:
                browser = p.chromium.launch(headless=False)
            print("Program se spouští v rozlišení:", sirka, "x", vyska)
            context = browser.new_context(
                viewport={"width": sirka, "height": vyska}
            )
            page = context.new_page()
            print("Program otevírá ZAV stránku...")
            page.goto("https://student.zav.cz/#!/login")
            print("Zadává jméno...")
            time.sleep(.1)
            pyautogui.typewrite(jmeno, interval=0)
            pyautogui.press("tab")
            print("Zadává heslo...")
            pyautogui.typewrite(heslo, interval=0)
            pyautogui.press("enter")
            print("Přihlášen, teď dává exploit...")
            page.evaluate("document.documentElement.setAttribute('contenteditable', 'true');")
            print("Hotovo!")

            # Main loop to process commands from the queue
            while True:
                try:
                    cmd = command_queue.get(timeout=0.5)
                    if cmd == "activate_exploit":
                        page.evaluate("document.documentElement.setAttribute('contenteditable', 'true');")
                        print("Exploit je znovu aktivován")
                    elif cmd == "close_browser":
                        print("Zavírám browser...")
                        browser.close()
                        break
                except queue.Empty:
                    continue

            browser.close()
 
def run_browser_thread():
    threading.Thread(target=spustitBrowser, daemon=True).start()
    
def make_page_exploited():
    if page is not None:
        command_queue.put("activate_exploit")
    else:
        print("Prohlížeč není spuštěn nebo stránka není dostupná.")
        
def close_browser():
    if page is not None:
        command_queue.put("close_browser")
    else:
        print("Prohlížeč není spuštěn nebo stránka není dostupná.")
    
def eastereggvideo():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            viewport={"width": sirka, "height": vyska}
        )
        page = context.new_page()
        page.goto("https://packaged-media.redd.it/gq3bpywa60cb1/pb/m2-res_720p.mp4?m=DASHPlaylist.mpd&v=1&e=1750798800&s=0e156566946e5c307a649bcad3ead5d924003892")
        time.sleep(10000)
        browser.close()
def easteregg():
    global kliknuto
    kliknuto += 1
    print(kliknuto)
    if kliknuto == 20:
        threading.Thread(target=eastereggvideo, daemon=True).start()
        time.sleep(15)
        exit()
# Funkce ktera spusti prohlizec---------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Funkce na meneni themu---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def changethemezav():
    global moznost
    print("zavtheme")
    customtkinter.set_default_color_theme(r"themes\zav.json")
    moznost = "Z*V theme"
    app.recreate_content()  # přidejte tuto metodu do třídy App
    clear()

def changethemebreeze():
    global moznost
    print("breezetheme")
    customtkinter.set_default_color_theme(r"themes\breeze.json")
    moznost = "Breeze theme"
    app.recreate_content()  # přidejte tuto metodu do třídy App
    clear()

def changethememidnight():
    global moznost
    print("midnighttheme")
    customtkinter.set_default_color_theme(r"themes\midnight.json")
    moznost = "Midnight theme"
    app.recreate_content()  # přidejte tuto metodu do třídy App
    clear()
    
# Funkce na meneni themu---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Samotný GUI---------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global jmeno, heslo, prohlizec, check_firefox
        self.title("ZAVploit")
        self.geometry("800x400")
        self.resizable(width=False, height=False)
        self.iconbitmap('ikonky\icon.ico')
        customtkinter.set_default_color_theme("themes\zav.json")
        
        # --- NAČTENÍ IKON ---
        self.home_icon = customtkinter.CTkImage(
            light_image=Image.open("ikonky\home_icon.png"),
            dark_image=Image.open("ikonky\home_icon.png"),
            size=(40, 40)
        )
        self.settings_icon = customtkinter.CTkImage(
            light_image=Image.open("ikonky\settings_icon.png"),
            dark_image=Image.open("ikonky\settings_icon.png"),
            size=(40, 40)
        )
        self.logo_icon = customtkinter.CTkImage(
            light_image=Image.open("ikonky\logo.png"),
            dark_image=Image.open("ikonky\logo.png"),
            size=(120, 120)
        )

        # --- BUTTONY NA LEVÉ STRANĚ ---
        self.menu_frame = customtkinter.CTkFrame(self, width=150)
        self.menu_frame.pack(side="left", fill="y")
        
        self.icon_logo = customtkinter.CTkLabel(
            self.menu_frame,
            text="",
            image=self.logo_icon,
            fg_color="transparent",
            width=80,
            height=80)
        self.icon_logo.pack(pady=(0,20),padx=10)
        
        self.btn_hlavni = customtkinter.CTkButton(
            self.menu_frame,
            text="",  # bez textu, jen ikona
            image=self.home_icon,
            width=70,
            height=70,
            command=self.show_hlavni
        )
        self.btn_hlavni.pack(pady=(0,40), padx=10)

        self.btn_nastaveni = customtkinter.CTkButton(
            self.menu_frame,
            text="",  # bez textu, jen ikona
            image=self.settings_icon,
            width=70,
            height=70,
            command=self.show_nastaveni
        )
        self.btn_nastaveni.pack(pady=0, padx=10)

        # --- OBSAHOVÉ FRAMY ---
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.pack(side="left", fill="both", expand=True)

        self.hlavni_frame = customtkinter.CTkFrame(self.content_frame)
        self.nastaveni_frame = customtkinter.CTkFrame(self.content_frame)

        self.create_hlavni_content()
        self.create_nastaveni_content()

        self.show_hlavni()  # výchozí zobrazení

    def show_hlavni(self):
        self.nastaveni_frame.pack_forget()
        self.hlavni_frame.pack(fill="both", expand=True)

    def show_nastaveni(self):
        self.hlavni_frame.pack_forget()
        self.nastaveni_frame.pack(fill="both", expand=True)

    def create_hlavni_content(self):
        hlavni = self.hlavni_frame

        # --- LOGIN FRAME ---
        self.login_frame = customtkinter.CTkFrame(hlavni, width=350, height=280, corner_radius=20)
        self.login_frame.place(x=10, y=10)

        def clicked():
            global jmeno, heslo, muzesSpustit
            jmeno = jmenoentry.get()
            heslo = hesloentry.get()
            if jmeno != "":
                print("Jméno bylo uloženo!")
                muzesSpustit = True
            else:
                print("Není zadané jméno")
                muzesSpustit = False
            
            if heslo != "":
                print("Heslo bylo uloženo!")
                muzesSpustit = True
            else:
                print("Není zadané heslo")
                muzesSpustit = False
                
            if heslo and jmeno !="":
                self.error.place_forget()
            else:
                self.error.place(x=40,y=260)

        jmenoText = customtkinter.CTkLabel(self.login_frame,
                                           text="Jméno",
                                           font=("Sergoe UI", 30))
        jmenoText.place(x=20 , y=20)
        
        jmenoentry = customtkinter.CTkEntry(self.login_frame,
                                            placeholder_text="Zadej jméno",
                                            width=300,
                                            height=40,
                                            font=("Sergoe UI", 20)
        )
        jmenoentry.place(x=20, y=60)
        
        hesloText = customtkinter.CTkLabel(self.login_frame, text="Heslo", font=("Sergoe UI", 30))
        hesloText.place(x=20 , y=110)
        
        hesloentry = customtkinter.CTkEntry(self.login_frame,
                                            placeholder_text="Zadej heslo",
                                            width=300,
                                            height=40,
                                            font=("Sergoe UI", 20),
                                            show="*"
        )
        hesloentry.place(x=20, y=150)
        
        ulozitUdajeBTN = customtkinter.CTkButton(
            self.login_frame,
            text="Dočasně uložit",
            font=("", 40),
            corner_radius=50,
            width=300,
            text_color="white",
            command=clicked,
        )
        ulozitUdajeBTN.place(x=20,y=200)

        # --- BROWSER FRAME (pro checkboxy) ---
        self.browser_frame = customtkinter.CTkFrame(hlavni, width=270, height=190, corner_radius=20)
        self.browser_frame.place(x=370, y=10)

        label = customtkinter.CTkLabel(self.browser_frame,
                                       text=("Vyber prohlížeč:"),
                                       font=("Sergoe UI", 30),
                                       text_color="white")
        label.place(x=20, y=20)
        
        def checkbox_event2():
            global anoNe2
            anoNe2 = check_chrome.get()
            global prohlizec, check_firefox
            
            if anoNe2 == "on":
                prohlizec = "chrome"
                print(prohlizec, "zvolen")
                self.checkbox_firefox.toggle()
            elif anoNe2 == "off":
                prohlizec = "firefox"
                print(prohlizec, "zvolen")
                self.checkbox_chrome.deselect()
                self.checkbox_firefox.select()

        def checkbox_event():
            anoNe = check_firefox.get()
            global prohlizec, check_chrome, anoNe2
            
            if anoNe == "on":
                prohlizec = "firefox"
                print(prohlizec, "zvolen")
                self.checkbox_chrome.toggle()
            elif anoNe == "off":
                prohlizec = "chrome"
                print(prohlizec, "zvolen")
                self.checkbox_firefox.deselect()
                self.checkbox_chrome.select()

        check_firefox = customtkinter.StringVar(value="on")
        self.checkbox_firefox = customtkinter.CTkCheckBox(self.browser_frame,
                                                    text="Firefox",
                                                    font=("Sergoe UI", 30),
                                                    text_color="white",
                                                    variable=check_firefox,
                                                    onvalue="on",
                                                    offvalue="off",
                                                    command=checkbox_event)
        self.checkbox_firefox.place(x=20, y=62)
        
        check_chrome = customtkinter.StringVar(value="off")
        self.checkbox_chrome = customtkinter.CTkCheckBox(self.browser_frame,
                                                    text="Chrome",
                                                    font=("Sergoe UI", 30),
                                                    text_color="white",
                                                    variable=check_chrome,
                                                    onvalue="on",
                                                    offvalue="off",
                                                    command=checkbox_event2)
        self.checkbox_chrome.place(x=20, y=112)
        
        self.error = customtkinter.CTkLabel(hlavni, text="Nejprve zadej jméno a heslo!", text_color="red", font=("Courier New", 35, "bold"))
        
        self.button = customtkinter.CTkButton(
            hlavni,
            text="Spustit ZAVploit",
            font=("Sergoe UI", 50),
            corner_radius=20,
            height=70,
            text_color="white",
            command=run_browser_thread,
        )
        self.button.pack(side="bottom", fill="x", padx=20, pady=20)

    def create_nastaveni_content(self):
        global moznost
        
        nastaveni = self.nastaveni_frame
        nastaveni_label = customtkinter.CTkLabel(nastaveni, text="ZAVploit 1.0 Beta \n Rodirck/Rodra_ @2025", font=("Callibri", 10, "italic"), text_color="white")
        nastaveni_label.pack(side="right", padx=(0,10), pady=(370,0))
    
        
        vyberthemetext = customtkinter.CTkLabel(nastaveni, text="Vyber theme:", font=("Segoe UI", 30))
        vyberthemetext.place(x=30,y=20)
        def optionmenu_callback(choice):
            global moznost
            print("optionmenu dropdown clicked:", choice)
            
            if choice == "Z*V theme":
                changethemezav()
                
            elif choice == "Breeze theme":
                changethemebreeze()
                
            elif choice == "Midnight theme":
                changethememidnight()
            
                
        optionmenu_var = customtkinter.StringVar(value=moznost)
        self.optionmenu = customtkinter.CTkOptionMenu(nastaveni,values=["Z*V theme", "Breeze theme", "Midnight theme"],
                                                 command=optionmenu_callback,
                                                 variable=optionmenu_var,
                                                 font=("Segoe UI", 25),
                                                 width=200,
                                                 height=40)
        self.optionmenu.place(x=30,y=70)
        
        self.button = customtkinter.CTkButton(
            nastaveni,
            text="Zaktivuj znovu exploit",
            font=("Sergoe UI", 27),
            height=45,
            text_color="white",
            command=make_page_exploited,
        )
        self.button.place(x=340,y=70)
        
        self.button = customtkinter.CTkButton(
            nastaveni,
            text="Vypnout browser",
            font=("Sergoe UI", 27),
            height=45,
            text_color="white",
            command=close_browser,
        )
        self.button.place(x=340,y=130)

        self.button = customtkinter.CTkButton(
            nastaveni,
            text="Zahadny tlacitko",
            font=("Sergoe UI", 10),
            fg_color="transparent",
            text_color="grey15",
            width=100,
            command=easteregg,
        )
        self.button.place(x=0,y=370)
        
        
    def recreate_content(self):
        # Zničit staré framy včetně menu_frame
        self.menu_frame.destroy()
        self.content_frame.destroy()
        # Vytvořit znovu menu_frame a content_frame
        self.menu_frame = customtkinter.CTkFrame(self, width=150)
        self.menu_frame.pack(side="left", fill="y")

        self.icon_logo = customtkinter.CTkLabel(
            self.menu_frame,
            text="",
            image=self.logo_icon,
            fg_color="transparent",
            width=80,
            height=80)
        self.icon_logo.pack(pady=(0,20),padx=10)

        self.btn_hlavni = customtkinter.CTkButton(
            self.menu_frame,
            text="",
            image=self.home_icon,
            width=70,
            height=70,
            command=self.show_hlavni
        )
        self.btn_hlavni.pack(pady=(0,40), padx=10)

        self.btn_nastaveni = customtkinter.CTkButton(
            self.menu_frame,
            text="",
            image=self.settings_icon,
            width=70,
            height=70,
            command=self.show_nastaveni
        )
        self.btn_nastaveni.pack(pady=0, padx=10)

        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.pack(side="left", fill="both", expand=True)

        self.hlavni_frame = customtkinter.CTkFrame(self.content_frame)
        self.nastaveni_frame = customtkinter.CTkFrame(self.content_frame)
        self.create_hlavni_content()
        self.create_nastaveni_content()
        self.show_hlavni()
# Samotný GUI---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


print("==================")
print("")
print("ZAVploit konzole")
print("")
print("==================")

app = App()
app.mainloop()