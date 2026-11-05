# Polish (pl) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the modern Polish a player in Poland would expect (the
Polish interfaces of Windows, macOS and Steam, and the Polish editions of
StarCraft II, Warcraft III and Command & Conquer are the model), and keep
that choice for the whole pack. Spelling is contemporary standard Polish.

The pack is drawn in the modern fonts. 3.1c's menu fonts have no glyph for
ą, ć, ę, ł, ń, ó, ś, ź, ż or the capitals Ą, Ć, Ę, Ł, Ń, Ó, Ś, Ź, Ż. The
sans faces that travel with the game (`fonts/engine-faces.json`, DejaVu
Sans in both weights) hold every one of those letters, and also „ ” — … →
✓ ✕. The pack brings no font of its own. Write real Polish spelling. Do
not strip accents to stay inside an old code page.

Ukrainian is the structural template (captions already shortened). Russian
is the nearest Slavic wording. European Portuguese shows how a Latin pack
of this length reads. None of them is a source of Polish words: read the
English, then write Polish.

## 1. Voice and grammar

- The player is `ty`. Interface instructions use the second-person
  singular imperative: `Naciśnij`, `Wybierz`, `Spróbuj ponownie później.`,
  `Wpisz nazwę`. Never `pan` / `pani`, never the formal plural (`wybierzcie`,
  `państwa`), never `proszę` as the way an instruction is given.
- Possessives are `twój`, `twoja`, `twoje`, `twoim`, `ci`, `cię`, `tobie`.
  "Your folder" → `twój folder`. Leave the pronoun out when Polish does
  not need it.
- Statements and hints: plain present or past, neutral. "Settings were not
  saved." → `Nie zapisano ustawień.` "The processor draws and scales the
  view." → `Procesor rysuje i skaluje widok.`
- Confirmation questions: the infinitive. "Replace the game files?" →
  `Zastąpić pliki gry?` A dialog title may be the same infinitive.
- Labels, buttons, menu items, setting names and headings: a noun phrase
  or an infinitive, no full stop, sentence case (only the first word and
  proper names capitalized). "Open folder" → `Otwórz folder`, "Try again"
  → `Spróbuj ponownie`, "Mouse wheel zoom" → `Zoom kółkiem myszy`. Where
  the English is in capitals, so is the Polish (`OTWÓRZ FOLDER`, `ATAK`).
- Short status words: an impersonal `-no` / `-to` form, or a noun of the
  action. "Installed" → `Zainstalowano`, "Downloading" → `Pobieranie…`,
  "Not found" → `Nie znaleziono`, "Failed" → `Nie udało się`, "Waiting" →
  `Oczekiwanie…`, "Ready" → `Gotowe`, "Off" / "On" → `Wył.` / `Wł.` on a
  small control, `Wyłączone` / `Włączone` where there is room.
- Mission briefings and in-fiction orders (HQ to the one Commander): the
  same informal imperative, military and short. `Wystaw ochronę wokół
  Bramy Galaktycznej.` `Poprowadź swoje jednostki do Bramy i zabezpiecz
  ją.` The Commander is `Dowódca` (vocative `Dowódco` only when someone
  addresses him by the title). Own forces are `nasze siły`. No slang, and
  no exclamation the English does not have.
- Briefing stock lines: `MISSION` → `MISJA` (the code after it stays,
  `MISJA 1.0001ARME`), `Mission T01:` → `Misja T01:`, `PRIORITY` →
  `PRIORYTET`, `PRIORITY CRITICAL` → `PRIORYTET KRYTYCZNY`, `INFO FEED` →
  `MELDUNEK`, `INTEL FEED` → `MELDUNEK WYWIADU`, `INTELL-TAP:` →
  `PODSŁUCH:`, `END` → `KONIEC`, `WARNING` → `OSTRZEŻENIE`, `Attention` /
  `Alert!` → `Uwaga` / `Alarm!`, `Suggestions:` → `Sugestie:`, `Battle
  Tactics:` → `Taktyka bitwy:`, `DO SO NOW.` → `ZRÓB TO TERAZ.`, `Arm
  vermin` → `robactwo ARM`, `To complete this mission you must` → `Aby
  ukończyć tę misję, musisz`.
- CORE's briefings are a machine talking: colder and more clipped than
  ARM's, still the informal imperative.
- Unit speech and the message log: short, as on a radio.
- Key names stay as the keyboard prints them: Shift, Ctrl, Alt, Esc,
  Escape, Enter, Tab, Space, Backspace, Delete, Insert, Home, End, Page
  Up, Page Down, F1–F12, Win, Option. In a sentence, Space is `spacja`.
  Arrows are `Strzałka w górę`, `Strzałka w dół`, `Strzałka w lewo`,
  `Strzałka w prawo`. Numpad is `Blok numeryczny`. Mouse buttons: `Lewy
  przycisk`, `Prawy przycisk`, `Środkowy przycisk`. Wheel: `Kółko w górę`,
  `Kółko w dół`.
- Acronyms kept in Latin: TCP, IP, CD, DirectPlay, GPU, CPU, HUD, fps, KB,
  MB, GB, ID, EMP, D-Gun. AI in prose is `SI` (the seat's label `AI` on a
  tiny button may stay `SI`).
- Punctuation: no space before `: ? !`. Quotes are Polish „…”, inner
  quotes «…». Keep `…` or `...`, and `·`, `→`, `✓`, `✕`, `—`, exactly as
  the English uses them. Never write `;` (a table value ends at `;`): use
  a full stop, a comma or a dash. Never write `//`. Never write a tab
  inside a value.
- Orthography: standard Polish. `nie` separately from a verb (`nie udało
  się`), together with an adjective it negates as one word
  (`niezapisany`). `w` / `z` take the form `we` / `ze` before a hard
  cluster (`we Wrocławiu`, `ze stoczni`).

## 2. Placeholders and numbers (hard rules)

- Every placeholder stays exactly as written: `{name}`, `{size}`, `{count}`,
  `%s`, `%d`, `%i`, `%.1f`, `%%`, `%1$s` and the rest. Never translate,
  drop, add or respell one.
- printf conversions stay in the English order. They are filled in that
  order. Reword the sentence around them. `{name}` slots may move.
- Every number written in digits stays (`1/32`, `2x`, `3.1c`, `16x16`,
  `9 x 21`, `1997`). Decimal points stay as the English writes them.
- A string that is only digits, punctuation or a kept key name is copied
  unchanged (`2`, `3`, `,`, `+{n}`).
- Staged captions with `|` (`Easy|Medium|Hard`) keep the same number of
  stages, in the same order.
- A slot has no case and no gender. Put it where the nominative is right:
  `mod {name}`, `mapa {map}`, `{name} jest zainstalowany`. Never glue an
  ending onto a slot (`{name}a`, `w {name}ie`).
- `{device}` is filled with this pack's word `urządzenie` or with a
  system name (`iPad`). `{cloud}` is filled with `chmura` or a system name
  (`iCloud`). Translate the entries `device` → `urządzenie` and `the
  cloud` → `chmura`, with no article, and write the sentences so either
  value fits: `na {device}`, `w {cloud}`, `przez {cloud}`. Do not put
  `tym` / `tej` immediately before the slot.
- A count's noun would change with the number (`1 plik`, `2 pliki`,
  `5 plików`), and a slot does not know the number. Use a form that works
  for any count, usually the genitive plural after the number when the
  English uses a plural (`{count} plików`), or name the thing before the
  number (`pliki: {count}`).
- A tab or a line break never goes into a translation.

## 3. Names kept as written

- **ARM** and **CORE**, always in Latin capitals, whatever the English
  case (Arm, Core, ARM, CORE). Both are masculine, like `obóz`: `ARM`,
  `CORE`, `jednostki CORE`, `siły ARM`, `Dowódca ARM`, `kampania CORE`,
  `przeciwko ARM`. They do not take a Polish ending.
- Open Annihilation, OA, Core Prime (the service and the planet), Total
  Annihilation, Total Annihilation: The Core Contingency, Total
  Annihilation: Battle Tactics, Cavedog Entertainment, GT Interactive,
  Steam, GOG, iCloud, Windows, macOS, Linux, DirectX, DirectPlay: as
  written.
- File names, folder names, extensions, URLs and version strings (`3.1c`,
  `oamod.yaml`, `totala1.hpi`, `.oalang`, `.oamut`, `.oabrain`, `.oakeys`):
  as written.

## 4. Fiction: places and names

Invented names stay spelled as in the English. Ordinary words are
translated. Use each form once, including in mission titles and briefings.

| English | Polish |
|---|---|
| Galactic Gate / the Gate | Brama Galaktyczna / Brama |
| Empyrrean | Empyrrean |
| Thalassean | Thalassean |
| Tergiverse IV | Tergiverse IV |
| Barathrum | Barathrum |
| Rougpelt | Rougpelt |
| Aqueous Minor | Aqueous Minor |
| Aegus | Aegus |
| Dump (the moon) | Dump |
| Hydross | Hydross |
| Lusch | Lusch |
| Temblor | Temblor |
| Gelidus | Gelidus |
| Krogoth | Krogoth |
| Central Consciousness | Centralna Świadomość |
| Larab Harbor | Port Larab |
| Bromid Maze | Labirynt Bromid |
| Brooban's Isle | Wyspa Broobana |
| Motien Ramp | Rampa Motien |
| Xantippe's Abyss | Otchłań Ksantypy |
| Slolam Pilago | Slolam Pilago |
| Isle Parche | Wyspa Parche |
| Vebreen Fleet | Flota Vebreen |
| the Arm/Core war | wojna ARM z CORE |
| patterning | przeniesienie wzorca |
| Com Pattern | Wzorzec Com |
| nanolathe, nanolathing | nanotokarka, nanotokowanie |
| homeworld | planeta macierzysta |
| Crustal 8 | Skorupa 8 |
| the beacon (Alien Beacon) | latarnia |
| the implosion device | urządzenie implozyjne |
| the contingent Core Commander | Dowódca CORE kontyngentu |
| Astrede Shoreline | Wybrzeże Astrede |

Battle Tactics place names (Hanan, Lipar, Meraldi, Wayneston, Vetes,
Ansapp, Novespin IV, Ravenstein, Yrdac, Prasad, Destral II, Kerrap, Arnen,
Zedtopt, Guditha, Grantham, Krocark, Terseknos, Labrodorite, Kral, Caranat,
Retorb, Chimo, Rotrey, Yollets and the rest) stay spelled as in the
English. The briefings use the missions table's spelling.

## 5. Game terms

| English | Polish |
|---|---|
| Commander | Dowódca |
| unit | jednostka |
| building, structure | budynek, struktura |
| Kbot, KBot, kbot | Kbot (m., liczba mnoga Kboty, dopełniacz Kbotów) |
| vehicle | pojazd |
| tank | czołg |
| aircraft / plane | samolot (zbiorowo: lotnictwo) |
| ship | okręt |
| submarine, sub | okręt podwodny |
| hovercraft | poduszkowiec |
| seaplane | wodnosamolot |
| amphibious | amfibijny |
| builder | budowniczy |
| factory, plant | fabryka |
| lab (Kbot Lab) | laboratorium |
| shipyard | stocznia |
| metal | metal |
| energy | energia |
| resources | zasoby |
| storage | magazyn |
| income / production | przychód / produkcja |
| metal extractor | ekstraktor metalu |
| metal maker | przetwornik metalu |
| Moho | Moho (w nazwach: kopalnia Moho, przetwornik Moho) |
| solar collector | kolektor słoneczny |
| wind generator | generator wiatrowy |
| tidal generator | generator pływowy |
| fusion reactor | reaktor fuzyjny |
| fusion power plant | elektrownia fuzyjna |
| geothermal powerplant | elektrownia geotermalna |
| radar | radar |
| sonar | sonar |
| jammer | zagłuszacz |
| line of sight, LOS | pole widzenia |
| cloak, cloaked | maskowanie, zamaskowany |
| stealth | skryty (myśliwiec skryty) |
| wreck, wreckage | wrak, szczątki |
| feature | obiekt mapy |
| laser | laser |
| plasma | plazma |
| missile | pocisk |
| rocket | rakieta |
| artillery | artyleria |
| flak | plot. (przeciwlotniczy) |
| torpedo | torpeda |
| depth charge | bomba głębinowa |
| mine | mina |
| nuke, nuclear missile | pocisk jądrowy |
| anti-nuke, missile defense | obrona przeciwrakietowa |
| EMP | EMP |
| D-Gun (Disintegrator Gun) | D-Gun (działo dezintegrujące) |
| anti-air | przeciwlotniczy |
| ally, alliance | sojusznik, sojusz |
| enemy | wróg |
| team | drużyna |
| kills / losses | zniszczone / straty |
| veteran / veterancy | weteran / doświadczenie |
| victory / defeat | zwycięstwo / porażka |
| paused | pauza (tytuł na polu bitwy: PAUZA) |
| Tech Level 1 / 2 | poziom tech. 1 / poziom tech. 2 |
| Adv., Advanced | zaawansowany (Zaaw. tam, gdzie angielski skraca do Adv.) |
| build menu | menu budowy |
| control group | grupa |
| selection, select | zaznaczenie, zaznacz |
| waypoint | punkt trasy |
| queue | kolejka |
| self-destruct | samozniszczenie |
| repair | naprawa, naprawiać |
| reclaim | odzysk, odzyskiwać |
| patrol | patrol, patrolować |
| guard / defend | ochrona, chronić |
| capture | przejęcie, przejmować |
| map | mapa |
| match, game (one played) | partia, bitwa |
| the game (the program) | gra |
| fog of war | mgła wojny |
| resurrect | wskrzesić |

### Orders (buttons and their states; also touch and controller)

| English | Polish |
|---|---|
| ATTACK | ATAK |
| MOVE | RUCH |
| STOP | STOP |
| PATROL | PATROL |
| DEFEND / GUARD | OBRONA / ochrona (w zdaniu: chroń) |
| RECLAIM | ODZYSK |
| REPAIR | NAPRAWA |
| CAPTURE | PRZEJ. (w zdaniu: przejmij, przejęcie) |
| LOAD / UNLOAD | ZAŁAD. / WYŁAD. (w zdaniu: załaduj / wyładuj) |
| ORDERS | ROZKAZY |
| BUILD | BUDUJ |
| BLAST / D-GUN | D-GUN |
| ASSIST | WSPARCIE (w zdaniu: wspieraj) |
| Fire orders: Hold Fire / Return Fire / Fire At Will | Rozkazy ognia: Bez ognia / Ogień zwrotny / Ogień dowolny |
| Move orders: Hold Position / Maneuver / Roam | Rozkazy ruchu: Na pozycji / Manewr / Luźny ruch |
| On / Off | Wł. / Wył. |
| Activate / Deactivate | Aktywuj / Dezaktywuj |
| Cloaked / Visible | Zamaskowany / Widoczny |
| QUEUE / ADD / FORCE / CLEAR / STORE (touch) | KOLEJKA / DODAJ / WYMUŚ / WYCZYŚĆ / ODŁÓŻ |
| arm (an order) / ARM ORDER | uzbrój (rozkaz) / UZBRÓJ |
| Patrolling / Guarding | Patroluje / Chroni |

The picture captions drawn on the order buttons use the short forms above,
in capitals, abbreviated with a full stop where the column shows one.

## 6. Menus and modes

| English | Polish |
|---|---|
| Single Player | Jeden gracz |
| Multiplayer | Wieloosobowa |
| Campaign | Kampania |
| Mission | Misja |
| Briefing | Odprawa |
| Skirmish | Potyczka |
| Battle Room | Pokój bitwy |
| Lobby / Lounge | Poczekalnia |
| host / join | gospodarz / dołącz |
| the Creator (3.1c's host) | gospodarz |
| player | gracz |
| computer player | komputer |
| AI | SI |
| watcher, spectator / watch | obserwator / obserwuj |
| replay | powtórka |
| recorder, recording | rejestrator, nagranie |
| saved game / save / load | zapis gry / zapisz / wczytaj |
| Options | Opcje |
| Settings | Ustawienia |
| Preferences | Preferencje |
| Previous Menu / Back | Poprzednie menu / Wstecz |
| Main menu / Game menu | Menu główne / Menu gry |
| Exit, Quit | Wyjdź |
| Exit to the system | Wyjście do systemu |
| OK / Cancel / Done / Close / Apply | OK / Anuluj / Gotowe / Zamknij / Zastosuj |
| Retry, Try again | Spróbuj ponownie |
| Continue / Resume | Kontynuuj / Wznów |
| Easy / Medium / Hard | Łatwy / Średni / Trudny |
| Help | Pomoc |
| Chat | Czat |
| Cheats | Kody |
| game speed | prędkość gry |
| Sound / Music / Volume / Movies | Dźwięk / Muzyka / Głośność / Filmy |
| Credits | Autorzy |
| Intro | Intro |
| Restrictions | Ograniczenia |
| SINGLE / MULTI / INTRO / EXIT | JEDEN GRACZ / WIELOOSOBOWA / INTRO / WYJDŹ |
| On / Off (3.1c's sound toggles) | Tak / Nie |
| Wind Speed / Gravity | Wiatr / Grawitacja |
| Narration / No Narration | Narracja / Bez narracji |

Title-screen words that must fit a narrow button may drop to `1 GRACZ` and
`WIELOOS.`. The in-game pause title is `PAUZA`, the victory title on the
field is `WYGRANA!`, the defeat title is `PORAŻKA`. Save and load dialog
titles: `ZAPISZ GRĘ`, `WCZYTAJ GRĘ`.

## 7. Open Annihilation's interface

| English | Polish |
|---|---|
| Library | Biblioteka |
| mod | mod (m., liczba mnoga mody) |
| mod profile | profil modu |
| hacks, standard hacks | poprawki, poprawki standardowe |
| map pack | paczka map |
| language pack | paczka językowa |
| package | paczka |
| expansion | dodatek |
| base game | gra podstawowa |
| registry | rejestr |
| catalogue | katalog |
| download | pobierz / pobieranie |
| install / update / remove / delete | zainstaluj / aktualizuj, aktualizacja / usuń / usuń |
| version / revision | wersja / rewizja |
| roll back | cofnij |
| folder / file | folder / plik |
| archive | archiwum |
| game files / game folder | pliki gry / folder gry |
| device | urządzenie |
| the cloud | chmura |
| free (space) | wolne (`{size} wolne`) |
| screen / window / full screen | ekran / okno / pełny ekran |
| zoom, zoom in / out | zoom, przybliż / oddal |
| graphics | grafika |
| graphics card | karta graficzna |
| hardware acceleration | akceleracja sprzętowa |
| vertical sync | synchronizacja pionowa |
| anti-aliasing | wygładzanie |
| frame rate / frame | liczba klatek / klatka |
| pixel | piksel |
| resolution | rozdzielczość |
| modern fonts | nowoczesne czcionki |
| font / text size | czcionka / rozmiar tekstu |
| controller / trackpad / stick / gyro / D-pad | kontroler / gładzik / drążek / żyroskop / krzyżak |
| control (an on-screen control) | element sterowania |
| touch | dotyk |
| haptics | wibracje |
| pointer | wskaźnik |
| mouse / mouse wheel | mysz / kółko myszy |
| keyboard | klawiatura |
| press | naciśnij |
| type (text) | wpisz |
| scroll | przewiń |
| show / hide | pokaż / ukryj |
| enable / disable | włącz / wyłącz |
| user | użytkownik |
| password | hasło |
| share | udostępnij |
| manage | zarządzaj |
| default | domyślne (`Domyślne systemu`) |
| preview | podgląd |
| log (messages) | dziennik |
| Developer Mode | tryb dewelopera |
| Language / System default | Język / Jak w systemie |
| snap (click snap) | przyciąganie |
| shared game / network play | gra wspólna / gra sieciowa |
| install ID | identyfikator instalacji |
| demo | demo |
| content | zawartość |
| key binding | skrót |
| app | aplikacja |
| phone / tablet | telefon / tablet |
| mutator | mutator (m., mutatory) |
| brain (a computer player's) | mózg (m., mózgi) |
| overlay | nakładka |
| key layout | układ klawiszy |
| key editor | edytor klawiszy |
| action (a binding) | akcja |
| changes of your own | własne zmiany |
| clash | konflikt |
| latch / latched | zatrzask / zatrzaśnięte |
| latchable | Do zatrzaśnięcia |
| unbound | Puste |
| letter (of a key) | litera |
| place (of a key) | pozycja |
| hold to confirm | Przytrzymaj, by potwierdzić |
| accessibility | dostępność |
| smooth motion | płynny ruch |
| full 3D | pełne 3D |
| fog of war (the setting) | mgła wojny |
| tag (a Library filter) | znacznik |
| channel (updates) | kanał |

`Available to download` → `DO POBRANIA`. `Play now` → `GRAJ TERAZ`.
`Get mutators` → `POBIERZ MUTATORY`. `Open Annihilation Library` →
`BIBLIOTEKA OPEN ANNIHILATION`.

## 8. Unit names

Generic names are translated. A proper name that is an ordinary English
word is translated. A personal name, a code or an invented token stays
spelled as in the English (Polish already uses Latin letters, so there is
nothing to respell): FARK, Fido, Jeffy, Jethro, Luger, Marky, Merl, Morty,
Nixer, Podger, Rocko, Samson, Krogoth, A.K., L.L.T., M-104, M-209, M-303,
M-420, M-515, M-610. `Moho` and `Gaat` stay, and the ordinary word beside
them is translated (`Kopalnia Moho`, `Działo Gaat`).

Use the name exactly, in `units.tdf` and anywhere a unit is named. Names
are sentence case. Descriptions are sentence case and as short as the
English. `Adv.` and a spelled-out `Advanced` at the start of a unit name
are both `Zaaw.`

Generic and descriptive names:

Adv. Aircraft Plant → Zaaw. fabryka samolotów · Aircraft Plant → Fabryka
samolotów · Adv. Construction Aircraft → Zaaw. samolot budowlany ·
Construction Aircraft → Samolot budowlany · Adv. Construction Kbot → Zaaw.
Kbot budowlany · Construction Kbot / Construction KBot → Kbot budowlany ·
Advanced Construction Sub → Zaaw. okręt podwodny budowlany · Adv.
Construction Vehicle → Zaaw. pojazd budowlany · Construction Vehicle →
Pojazd budowlany · Construction Ship → Okręt budowlany · Construction
Seaplane → Wodnosamolot budowlany · Construction Hovercraft → Poduszkowiec
budowlany · Adv. Kbot Lab → Zaaw. laboratorium Kbotów · Kbot Lab →
Laboratorium Kbotów · Adv. Vehicle Plant → Zaaw. fabryka pojazdów ·
Vehicle Plant → Fabryka pojazdów · Adv. Shipyard → Zaaw. stocznia ·
Shipyard → Stocznia · Advanced Radar Tower → Zaaw. wieża radaru · Radar
Tower → Wieża radaru · Advanced Sonar Station → Zaaw. stacja sonaru ·
Sonar Station → Stacja sonaru · Advanced Torpedo Launcher → Zaaw. wyrzutnia
torped · Torpedo Launcher → Wyrzutnia torped · Air Repair Pad → Lądowisko
naprawcze · Hovercraft Platform → Platforma poduszkowców · Seaplane
Platform → Platforma wodnosamolotów · Krogoth Gantry → Suwnica Krogotha ·
Cloakable Fusion Reactor → Reaktor fuzyjny z maskowaniem · Fusion Reactor
→ Reaktor fuzyjny · Fusion Power Plant → Elektrownia fuzyjna · Geothermal
Powerplant → Elektrownia geotermalna · Energy Storage → Magazyn energii ·
Metal Storage → Magazyn metalu · Metal Extractor → Ekstraktor metalu ·
Metal Maker → Przetwornik metalu · Moho Metal Maker → Przetwornik Moho ·
Moho Mine → Kopalnia Moho · Floating Metal Maker → Pływający przetwornik
metalu · Solar Collector → Kolektor słoneczny · Wind Generator → Generator
wiatrowy · Tidal Generator → Generator pływowy · Underwater Energy Storage
→ Podwodny magazyn energii · Underwater Fusion Plant → Podwodna elektrownia
fuzyjna · Underwater Metal Extractor → Podwodny ekstraktor metalu ·
Underwater Metal Storage → Podwodny magazyn metalu · Galactic Gate → Brama
Galaktyczna · Dragon's Teeth → Smocze zęby · Floating Dragon's Teeth →
Pływające smocze zęby · Fortification Wall → Mur obronny · Alien Beacon →
Obca latarnia · Implosion Device → Urządzenie implozyjne · Commander →
Dowódca · Decoy Commander → Dowódca-przynęta · Light Laser Tower → Lekka
wieża laserowa · Hydration Plant → Zakład nawadniania · Fortitude Missile
Defense → Obrona Fortitude · Resurrection Kbot → Kbot wskrzeszenia · Mobile
Artillery → Artyleria mobilna · Missile Frigate → Fregata rakietowa ·
Targeting Facility → Ośrodek namierzania · Area Mine → Mina obszarowa ·
Focused Mine → Mina skupiona · HE Area Mine → Mina burząca · Precision
Mine → Mina precyzyjna · Nuclear Mine → Mina jądrowa · Defender - NS →
Obrońca - NS · Gaat Gun → Działo Gaat.

Ordinary-word proper names:

Albatross → Albatros · Ambusher → Zasadnik · Anaconda → Anakonda ·
Annihilator → Anihilator · Archer → Łucznik · Atlas → Atlas · Avenger →
Mściciel · Bear → Niedźwiedź · Big Bertha → Gruba Berta · Brawler →
Zabijaka · Bulldog → Buldog · Buzzsaw → Piła · Cobra → Kobra · Colossus →
Kolos · Conqueror → Zdobywca · Copperhead → Miedziogłów · Crasher → Łomot ·
Crock → Krokodyl · Crusader → Krzyżowiec · Defender → Obrońca · Deleter →
Wymazywacz · Diplomat → Dyplomata · Dominator → Dominator · Doomsday
Machine → Maszyna zagłady · Eagle → Orzeł · Enforcer → Egzekutor · Envoy →
Poseł · Eraser → Gumka · Escort → Eskorta · Executioner → Kat · Fibber →
Łgarz · Fink → Kapuś · Flakker → Flakowiec · Flash → Błysk · Flea → Pchła ·
Freaker → Świr · Freedom Fighter → Bojownik · Gimp → Kuternoga · Goliath →
Goliat · Guardian → Strażnik · Hammer → Młot · Hawk → Jastrząb · Hedgehog
→ Jeż · Hive → Ul · Hulk → Olbrzym · Hunter → Łowca · Hurricane → Huragan ·
Immolator → Spopielacz · Infiltrator → Infiltrator · Informer → Informator
· Instigator → Podżegacz · Intimidator → Zastraszacz · Invader → Najeźdźca
· Jammer → Zagłuszacz · Lancet → Lancet · Leveler → Walec · Leviathan →
Lewiatan · Lurker → Czyhacz · Maverick → Odmieniec · Millenium → Milenium ·
Neutron → Neutron · Panther → Pantera · Parasite → Pasożyt · Peeper →
Oczko · Peewee → Mikrus · Pelican → Pelikan · Penetrator → Przebijacz ·
Phalanx → Falanga · Phantom → Fantom · Phoenix → Feniks · Piranha →
Pirania · Protector → Protektor · Pulverizer → Miażdżyciel · Punisher →
Karzący · Pyro → Piro · Raider → Rajdowiec · Ranger → Strażnik wybrzeża ·
Rapier → Rapier · Reaper → Żniwiarz · Retaliator → Odwetowiec · Roach →
Karaluch · Scarab → Skarabeusz · Scorpion → Skorpion · Scrubber →
Czyściciel · Sea Serpent → Wąż morski · Seahawk → Rybołów · Searcher →
Szperacz · Seer → Wieszcz · Sentinel → Wartownik · Shadow → Cień · Shark →
Rekin · Shooter → Strzelec · Shredder → Rozdrabniacz · Silencer → Tłumik ·
Skeeter → Komar · Skimmer → Ślizgacz · Slasher → Rębacz · Slinger → Procarz
· Snake → Wąż · Snapper → Kąsacz · Spectre → Widmo · Spider → Pająk ·
Spoiler → Psuj · Stinger → Żądło · Stingray → Płaszczka · Storm → Sztorm ·
Stumpy → Krępy · Stunner → Ogłuszacz · Sumo → Sumo · Swatter → Packa ·
The Can → Puszka · Thud → Huk · Thunder → Grom · Thunderbolt → Piorun ·
Tiny → Drobiazg · Titan → Tytan · Toaster → Toster · Tornado → Tornado ·
Triton → Tryton · Truck → Ciężarówka · Turtle → Żółw · Typhoon → Tajfun ·
Valkyrie → Walkiria · Vamp → Wampir · Viper → Żmija · Voodoo → Wudu ·
Voyeur → Podglądacz · Vulcan → Wulkan · Vulture → Sęp · Warlord → Wódz ·
Warrior → Wojownik · Weasel → Łasica · Wombat → Wombat · Zeus → Zeus ·
Zipper → Suwak.

`Ranger` is the missile ship, so `Strażnik wybrzeża`, not the same word as
`Guardian` (`Strażnik`). `Protector` (the anti-missile building) is
`Protektor`, not `Obrońca` (`Defender`).

Description classes, used as the whole description:

Produces Aircraft → Produkuje samoloty · Produces Kbots → Produkuje Kboty ·
Produces Vehicles → Produkuje pojazdy · Produces Ships → Produkuje okręty ·
Produces Energy → Produkuje energię · Produces Metal → Produkuje metal ·
Tech Level 1 → Poziom tech. 1 · Tech Level 2 → Poziom tech. 2 · Extracts
Metal → Wydobywa metal · Converts Energy into Metal → Zamienia energię w
metal · Increases Energy Storage → Zwiększa magazyn energii · Increases
Metal Storage → Zwiększa magazyn metalu · Advanced Metal Extractor →
Zaawansowany ekstraktor metalu · Commander → Dowódca · Decoy Commander →
Dowódca-przynęta · Builds Hovercraft → Buduje poduszkowce · Builds
Seaplanes → Buduje wodnosamoloty · Builds Krogoth → Buduje Krogotha ·
Automatically repairs aircraft → Sam naprawia samoloty · Creates Water →
Tworzy wodę · Indigenous Lifeform → Tubylcza forma życia · Experimental
Kbot → Eksperymentalny Kbot · SPY Kbot → Kbot szpiegowski · Infantry Kbot →
Kbot piechoty · Medium Infantry Kbot → Średni Kbot piechoty · Assault Kbot
→ Kbot szturmowy · Armored Assault Kbot → Opancerzony Kbot szturmowy ·
Adv. Armored Assault Kbot → Zaaw. opancerzony Kbot szturmowy · Artillery
Kbot → Kbot artylerii · Fast Attack Kbot → Szybki Kbot szturmowy · Fast
Assist-Repair Kbot → Szybki Kbot wsparcia · Fast Light Scout Kbot → Szybki
lekki zwiadowca · Anti-Air Kbot → Kbot plot. · Rocket Kbot → Kbot rakietowy
· Missile Kbot → Kbot pocisków · Heavy Rocket Kbot → Ciężki Kbot rakietowy
· Gun-slinging Kbot → Kbot rewolwerowiec · Mobile Radar Kbot → Mobilny Kbot
radaru · Mobile Mortar Kbot → Mobilny Kbot moździerzy · Sniper Kbot → Kbot
snajper · Resurrection Kbot → Kbot wskrzeszenia · Amphibious Kbot → Kbot
amfibijny · Scout → Zwiadowca · Air Scout → Zwiad powietrzny · Scout Ship →
Okręt zwiadowczy · Scout Hovercraft → Poduszkowiec zwiadowczy · Fighter →
Myśliwiec · Stealth Fighter → Myśliwiec skryty · Seaplane Fighter →
Wodnosamolot myśliwski · Bomber → Bombowiec · Strategic Bomber → Bombowiec
strategiczny · Torpedo Bomber → Bombowiec torpedowy · Gunship → Szturmowiec
· Air Transport → Transport powietrzny · Radar Plane → Samolot radaru ·
Airborne Sonar → Sonar latający · Battleship → Pancernik · Cruiser →
Krążownik · Destroyer → Niszczyciel · Submarine → Okręt podwodny · Battle
Sub → Bojowy okręt podwodny · Submarine Killer → Zabójca okrętów podwodnych
· Light Carrier → Lekki lotniskowiec · Transport Ship → Okręt transportowy
· Transport Hovercraft → Poduszkowiec transportowy · Ground Transport →
Transport lądowy · Missile Ship → Okręt pocisków · Anti-Air Ship → Okręt
plot. · Anti-Air Hovercraft → Poduszkowiec plot. · Anti-Air Flak Gun →
Działo plot. · Hovertank → Czołg na poduszce · Amphibious Tank → Czołg
amfibijny · Lightning Tank → Czołg błyskawic · Assault Tank → Czołg
szturmowy · Fast Assault Tank → Szybki czołg szturmowy · Medium Assault
Tank → Średni czołg szturmowy · Heavy Assault Tank → Ciężki czołg szturmowy
· Very Heavy Assault Tank → Bardzo ciężki czołg szturmowy · Riot Tank →
Czołg tłumiący · Fast Attack Vehicle → Szybki pojazd szturmowy · Spider
Assault Vehicle → Pajęczy pojazd szturmowy · Mine Layer Vehicle → Stawiacz
min · Mobile Artillery → Artyleria mobilna · Mobile Flak Vehicle → Mobilne
działo plot. · Mobile Missile Launcher → Mobilna wyrzutnia pocisków ·
Mobile Missile Defense → Mobilna obrona przeciwrakietowa · Mobile Rocket
Launcher → Mobilna wyrzutnia rakiet · Mobile Energy Weapon → Mobilna broń
energetyczna · Mobile Radar → Mobilny radar · Mobile Radar Jammer →
Mobilny zagłuszacz radaru · Radar Jammer → Zagłuszacz radaru · Radar
Jammer Ship → Okręt zagłuszający radar · Sonar Jamming Sub → Zagłuszacz
sonaru · Hovercraft Rocket Launcher → Poduszkowiec z rakietami · Missile
Tower → Wieża pocisków · Missile Tower - Naval Series → Wieża pocisków -
seria morska · Missile Launcher → Wyrzutnia pocisków · Plasma Battery →
Bateria plazmowa · Plasma Tower → Wieża plazmowa · Heavy Laser Tower →
Ciężka wieża laserowa · Light Laser Tower → Lekka wieża laserowa ·
Floating Heavy Laser Tower → Pływająca ciężka wieża laserowa · Pop-up
Heavy Cannon → Wysuwane ciężkie działo · Pop-Up Heavy Laser → Wysuwany
ciężki laser · Long Range Plasma Cannon → Dalekonośne działo plazmowe ·
Rapid Fire Plasma Cannon → Szybkostrzelne działo plazmowe · Energy Weapon
/ Energy weapon → Broń energetyczna · EMP Missile Launcher → Wyrzutnia
pocisków EMP · Neutron Missile Launcher → Wyrzutnia pocisków neutronowych
· Nuclear Missile Launcher → Wyrzutnia pocisków jądrowych · Nuclear Mine →
Mina jądrowa · Anti Missile Defense System → Obrona przeciwrakietowa ·
Torpedo Launcher → Wyrzutnia torped · Advanced Torpedo Launcher →
Zaawansowana wyrzutnia torped · Torpedo Seaplane → Wodnosamolot torpedowy ·
Long Range Radar → Radar dalekiego zasięgu · Long Range Radar Tower → Wieża
radaru dalekiego zasięgu · Extended Sonar → Sonar rozszerzony · Locates
Water Units → Wykrywa jednostki na wodzie · Radar Tower → Wieża radaru ·
Sonar Station → Stacja sonaru · Alien Beacon → Obca latarnia · Implosion
Device → Urządzenie implozyjne · Floating Dragon's Teeth → Pływające
smocze zęby · Floating Metal Maker → Pływający przetwornik metalu ·
Perimeter Defense → Obrona obwodu · Metal Maker → Przetwornik metalu ·
Space Teleporter → Teleport kosmiczny · Automatic Radar Targeting →
Automatyczne namierzanie radaru · Crawling Bomb → Pełzająca bomba · Low
Damage, Med. Range Mine → Małe obrażenia, średni zasięg · Low Damage,
Large Range Mine → Małe obrażenia, duży zasięg · Med. Damage, Small Range
Mine → Średnie obrażenia, mały zasięg · Med. Damage, Med. Range Mine →
Średnie obrażenia, średni zasięg · Med. Damage, Large Range Mine → Średnie
obrażenia, duży zasięg · High Damage, Small Range Mine → Duże obrażenia,
mały zasięg · High Damage, Med. Range Mine → Duże obrażenia, średni zasięg
· High Damage, Large Range Mine → Duże obrażenia, duży zasięg.

## 9. Width

Polish runs longer than English, about as long as the Portuguese. Captions
on 3.1c's fixed-size buttons (menu buttons, tabs, the order buttons, short
labels) stay at or under the Portuguese caption's length. Where the
Ukrainian or the Portuguese abbreviated, abbreviate, with a full stop:
`Zaaw.`, `Maks.`, `Tech.`, `Poz.`, `Wył.`, `Wł.`, `PRZEJ.`, `ZAŁAD.`,
`WYŁAD.`. Prefer the shortest natural wording: `Wstecz` for "Previous
Menu", `Graj` when the screen already says what is played. Sentences in
dialogs and hints may be as long as they need to be. Unit descriptions
stay about as short as the English, because they share the bottom bar.

## 10. Maps

In `translate.tdf`, a map description that starts with a size keeps the
English prefix exactly, spaces included (`18 x 18  `, and the odd
`11 x 10 map.  `). Translate only the words after that prefix. Translate a
descriptive map name (`painted desert` → `Malowana pustynia`). Leave an
invented name spelled as in the English. One leading `N: ` on a mission
name stays exactly.

## 11. What this pack does not translate

Nothing in this glossary is left in English except the names section 3 and
section 8 tell you to keep, key names, acronyms, and the product names.
ARM, CORE, Kbot, Moho, D-Gun, EMP and mod are the pack's own words, used
as written here.
