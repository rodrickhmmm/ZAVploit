# ZAVploit

> [!WARNING]
> Autor nenese žádnou zodpovědnost za jakékoliv použití tohoto programu. Používání této aplikace může být v rozporu s podmínkami služby [student.zav.cz](https://student.zav.cz/#!/login) nebo jinými právními předpisy. **Projekt je určen pouze pro vzdělávací účely. Používejte na vlastní nebezpečí! Silně nedoporučováno používat ve škole.**
> <br> Neboli - ***pokud vás někdo chytne, že tento program používáte, je to vaše chyba a ne autora tohoto programu.***

<img src="./ikonky/icon.png" width=auto height="300">

ZAVploit je desktopová aplikace napsaná v pythonu, která slouží jako exploit [ZAVu](https://student.zav.cz/#!/login). Hlavním cílem je zpřístupnění backspacu v jakémkoliv cvičení, bez mučení mozku, když uděláte chybu. 

## Funkce

- **Automatizované přihlášení** – Program podporuje uložení uživatelských údajů ze ZAVu. Pozor! Uživatelské údaje se ukládají do lokálního nešifrovaného souboru `nastaveni.json`!
- **Spuštění prohlížeče s exploitací** – Otevře vybraný prohlížeč (Firefox/Chromium), který hned zapne stránku ZAV, kde vás následně automaticky přihlásí a aplikuje exploit.
- **Notifikace** – Po úspěšném spuštění exploitu program informuje uživatele notifikací.
- **GUI v customtkinter** – Moderní rozhraní pro ovládání aplikace, nastavení témat a přihlášení.
- **Výběr motivů** – Na výběr je až z 10ti motivů
- **Možnost opakované aktivace exploitu** – V nastavení je možnost znovu aktivovat exploit

## Instalace

1. Stáhněte si zdrojový kód z [releases](https://github.com/rodrickhmmm/ZAVploit/releases/tag/v1.0) (`Source code (zip)`), následně tento zip soubor extrahujte a otevřete 

2. **Instalace závislostí**
   - na instalaci všech potřebných věcí spusťte **install.bat**. Tento soubor nainstaluje všechny potřebné knihony a samotný Python.

3. **Spuštění aplikace**
   - Windows: Spusťte soubor `ZAVploit.bat`
   - Nebo přímo pomocí příkazového řádku:
     ```bash
     python main.py
     ```

## Použití
  ![Preview](./readme/preview.png)

### ZAVploit se může spustit dvěma spouštěcími soubory: 
#### ZAVploit-Konzole.bat
  - `ZAVploit.bat` je spouštěcí soubor, který vám zobrazí desktopový program a ZAVploit "konzoli"
  - ZAVploit "konzole" si nemusíte všímat a můžete si ji skrýt (bacha, nezavírat - to zavře celý program!), funguje jako menší debuggovací okénko (nebo pokud se chcete cítit jako "hacker", tak si to můžete nechat otevřené)

#### ZAVploit.bat
  - `ZAVploit.bat` je spouštěcí soubor, který "konzoli" nezobrazuje, jen samotný desktopový program 

- V GUI lze přepínat mezi hlavní stránkou a nastavením.
- Na hlavní stránce najdete:
  - zadání uživatelských údajů
  - vybrání prohlížeče
  - spuštění samotného exploitu.

- V nastavení:
  - výběr motivů
  - zapnutí/vypnutí automatického přihlášení
  - nastavení exploitu:
    - zaktivovat znovu exploit
    - přihlásit znovu
    - vypnout prohlížeč.

## Cvičení, ve kterých exploit nefunguje
- Cvičení, kde po každé chybě tě to hodí na další řádek
- Padající písmenka
- Teď z hlavy jinak nevim dál, napište kdyžtak do issues nebo něco díky :D

> [!NOTE]
> Projekt je ve stádiu "Beta", může obsahovat chyby.

<br><br>
## QnA

"Nešel by udělat i program který by za tebe v ZAVu psal?" Bohužel ne. S kamarádem jsme tohle zkoušeli, já napsal program v Pythonu, on v C#. Oba programy ZAV detekoval a napsal varování.

"Proč by jsi vůbec takový program dělal?" Protože sám vím jaké mučení ten program je - jednu dobu jsem tam míval okolo 50 chyb kvůli mé nekorigované rychlosti. Proto když jsem přišel jak alespoň mazat text ve všech cvičeních, tak jsem chtěl udělat program, ktertý dokáže pochopit skoro každý jak nastavit a který pomůže také ostatním.

## Licence

Tento projekt je určen pouze pro vzdělávací účely. Používejte zodpovědně! 

---
> [!CAUTION]
> **Pokud narazíte na chybu nebo máte nápad na vylepšení, neváhejte otevřít [issues stránku](https://github.com/rodrickhmmm/ZAVploit/issues)!**
