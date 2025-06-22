# ZAVploit

from playwright.sync_api import sync_playwright
import time
import pyautogui
from screeninfo import get_monitors
import customtkinter
import threading
import os
from PIL import Image

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

for m in get_monitors():
    vyska = m.height
    sirka = m.width

jmeno = None
heslo = None
prohlizec = "firefox"
muzesSpustit = False

def button_callback():
    print("button pressed")

    
def spustitBrowser():
    global jmeno, heslo, muzesSpustit, prohlizec
    if muzesSpustit == False:
        app.error.place(x=60,y=260)
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
            print("Program se spouští v rozlišení:", sirka,"x",vyska)
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
            input("Pro exitnutí s browseru zde odentruj: ")
            browser.close()
        
def run_browser_thread():
    threading.Thread(target=spustitBrowser, daemon=True).start()
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global jmeno, heslo, prohlizec, check_firefox
        self.title("ZAVploit")
        self.geometry("800x400")
        self.resizable(width=False, height=False)
        self.iconbitmap('icon.ico')
        customtkinter.set_default_color_theme("zav.json")
        #self.configure(bg="#242424")

        # --- NAČTENÍ IKON ---
        self.home_icon = customtkinter.CTkImage(
            light_image=Image.open("home_icon.png"),
            dark_image=Image.open("home_icon.png"),
            size=(40, 40)
        )
        self.settings_icon = customtkinter.CTkImage(
            light_image=Image.open("settings_icon.png"),
            dark_image=Image.open("settings_icon.png"),
            size=(40, 40)
        )
        self.logo_icon = customtkinter.CTkImage(
            light_image=Image.open("logo.png"),
            dark_image=Image.open("logo.png"),
            size=(120, 120)
        )

        # --- BUTTONY NA LEVÉ STRANĚ ---
        self.menu_frame = customtkinter.CTkFrame(self, width=150)
        self.menu_frame.pack(side="left", fill="y")
        
        self.icon_logo = customtkinter.CTkLabel(
            self.menu_frame,
            text="",
            image=self.logo_icon,
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

        self.btn_about = customtkinter.CTkButton(
            self.menu_frame,
            text="",  # bez textu, jen ikona
            image=self.settings_icon,
            width=70,
            height=70,
            command=self.show_about
        )
        self.btn_about.pack(pady=0, padx=10)

        # --- OBSAHOVÉ FRAMY ---
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.pack(side="left", fill="both", expand=True)

        self.hlavni_frame = customtkinter.CTkFrame(self.content_frame)
        self.about_frame = customtkinter.CTkFrame(self.content_frame)

        self.create_hlavni_content()
        self.create_about_content()

        self.show_hlavni()  # výchozí zobrazení

    def show_hlavni(self):
        self.about_frame.pack_forget()
        self.hlavni_frame.pack(fill="both", expand=True)

    def show_about(self):
        self.hlavni_frame.pack_forget()
        self.about_frame.pack(fill="both", expand=True)

    def create_hlavni_content(self):
        hlavni = self.hlavni_frame

        def clicked():
            global jmeno, heslo, muzesSpustit
            jmeno = jmenoentry.get()
            heslo = hesloentry.get()
            if jmeno != "":
                print("Jméno a heslo bylo uloženo!")
                muzesSpustit = True
            else:
                print("Není zadané jméno")
                muzesSpustit = False
            
            if heslo != "":
                print("Jméno a heslo bylo uloženo!")
                muzesSpustit = True
            else:
                print("Není zadané heslo")
                muzesSpustit = False
                
            if heslo and jmeno !="":
                self.error.place_forget()
            else:
                self.error.place(x=60,y=260)

        jmenoText = customtkinter.CTkLabel(hlavni,
                                           text="Jméno",
                                           font=("Sergoe UI", 30))
        jmenoText.place(x=20 , y=20)
        
        jmenoentry = customtkinter.CTkEntry(hlavni,
                                            placeholder_text="Zadej jméno",
                                            width=300,
                                            height=40,
                                            font=("Sergoe UI", 20)
        )
        jmenoentry.place(x=20, y=50)
        
        hesloText = customtkinter.CTkLabel(hlavni, text="Heslo", font=("Sergoe UI", 30))
        hesloText.place(x=20 , y=97)
        
        hesloentry = customtkinter.CTkEntry(hlavni,
                                            placeholder_text="Zadej heslo",
                                            width=300,
                                            height=40,
                                            font=("Sergoe UI", 20),
                                            show="*"
        )
        hesloentry.place(x=20, y=130)
        
        ulozitUdajeBTN = customtkinter.CTkButton(
            hlavni,
            text="Dočasně uložit",
            font=("", 40),
            corner_radius=50,
            width=300,
            text_color="white",
            command=clicked,
        )
        ulozitUdajeBTN.place(x=20,y=180)
        
        label = customtkinter.CTkLabel(hlavni,
                                       text=("Vyber prohlížeč:"),
                                       font=("Sergoe UI", 30),
                                       text_color="white")
        label.place(x=400,y=40)
        
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
        self.checkbox_firefox = customtkinter.CTkCheckBox(hlavni,
                                                    text="Firefox",
                                                    font=("Sergoe UI", 30),
                                                    text_color="white",
                                                    variable=check_firefox,
                                                    onvalue="on",
                                                    offvalue="off",
                                                    command=checkbox_event)
        self.checkbox_firefox.place(x=400,y=80)
        
        check_chrome = customtkinter.StringVar(value="off")
        self.checkbox_chrome = customtkinter.CTkCheckBox(hlavni,
                                                    text="Chrome",
                                                    font=("Sergoe UI", 30),
                                                    text_color="white",
                                                    variable=check_chrome,
                                                    onvalue="on",
                                                    offvalue="off",
                                                    command=checkbox_event2)
        self.checkbox_chrome.place(x=400,y=130)
        
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

    def create_about_content(self):
        about = self.about_frame
        about_label = customtkinter.CTkLabel(about, text="ZAVploit\nAutor: Rodrick\n2025", font=("Sergoe UI", 30), text_color="white")
        about_label.pack(pady=50)


print("==================")
print("")
print("ZAVploit konzole")
print("")
print("==================")

app = App()
app.mainloop()
