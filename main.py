# ZAVploit

from playwright.sync_api import sync_playwright
import time
import pyautogui
from screeninfo import get_monitors
import customtkinter
import threading
import os

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
    global jmeno, heslo, muzesSpustit, prohlizec, error
    if muzesSpustit == False:
        print("Nejprve zadej jméno a heslo!")
        error = customtkinter.CTkLabel(app, text="Nejprve zadej jméno a heslo!", text_color="red", font=("Courier New", 40)).place(x=70,y=250)
    else:
        error = customtkinter.CTkLabel(app, text="", text_color="red", font=("Courier New", 40)).place(x=70,y=250)
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
        customtkinter.set_appearance_mode("system")
        self.configure(fg_color="#252527")
        self.title("ZAVploit")
        self.geometry("800x400")
        self.resizable(width= False, height = False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.iconbitmap('icon.ico')
        
        self.button = customtkinter.CTkButton(
            self,
            text="Spustit ZAVploit",
            font=("Sergoe UI", 50),
            fg_color="#1CABB2",
            corner_radius=20,
            width=500,
            height=80,
            text_color="white",
            command=run_browser_thread,
            hover_color="#116970"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
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
        
        jmenoentry = customtkinter.CTkEntry(self,
                                            placeholder_text="Zadej jméno",
                                            width=300,
                                            height=40,
                                            font=("Sergoe UI", 20)
        )
        jmenoentry.place(x=20, y=10)
        
        
        hesloentry = customtkinter.CTkEntry(self,
                                            placeholder_text="Zadej heslo",
                                            width=300,
                                            height=40,
                                            font=("Sergoe UI", 20),
                                            show="*"
        )
        hesloentry.place(x=20, y=60)
        
        ulozitUdajeBTN = customtkinter.CTkButton(
            self,
            text="Uložit udaje",
            font=("Sergoe UI", 40),
            fg_color="#1CABB2",
            corner_radius=20,
            width=300,
            text_color="white",
            command=clicked,
            hover_color="#116970",
        ).place(x=20,y=110)
        
        label = customtkinter.CTkLabel(self, text=("Vyber prohlížeč:"), font=("Sergoe UI", 30),text_color="white", fg_color="transparent").place(x=400,y=10)
        
        
        def checkbox_event2():
            global anoNe2
            anoNe2 = check_chrome.get()
            global prohlizec, check_firefox
            
            if anoNe2 == "on":
                print("chrome zvolen")
                prohlizec = "chrome"
                self.checkbox_firefox.toggle()
            else:
                self.checkbox_chrome.deselect()
                self.checkbox_firefox.select()

                
        def checkbox_event():
            anoNe = check_firefox.get()
            global prohlizec, check_chrome, anoNe2
            
            if anoNe == "on":
                print("firefox zvolen")
                prohlizec = "firefox"
                self.checkbox_chrome.toggle()
            else:
                self.checkbox_firefox.deselect()
                self.checkbox_chrome.select()

                
        check_firefox = customtkinter.StringVar(value="on")
        self.checkbox_firefox = customtkinter.CTkCheckBox(self,
                                                    text="Firefox",
                                                    font=("Sergoe UI", 30),
                                                    text_color="white",
                                                    hover_color="green",
                                                    variable=check_firefox,
                                                    onvalue="on",
                                                    offvalue="off",
                                                    command=checkbox_event)
        self.checkbox_firefox.place(x=400,y=50)
        
                
        check_chrome = customtkinter.StringVar(value="off")
        self.checkbox_chrome = customtkinter.CTkCheckBox(self,
                                                    text="Chrome",
                                                    font=("Sergoe UI", 30),
                                                    text_color="white",
                                                    hover_color="green",
                                                    variable=check_chrome,
                                                    onvalue="on",
                                                    offvalue="off",
                                                    command=checkbox_event2)
        self.checkbox_chrome.place(x=400,y=90)
        
        
        

print("==================")
print("")
print("ZAVploit konzole")
print("")
print("==================")

app = App()
app.mainloop()
