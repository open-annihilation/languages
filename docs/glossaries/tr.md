# Turkish (tr) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the modern Turkish a player in Turkey would expect (the
Turkish interfaces of Windows, Steam and the Turkish editions of StarCraft
II and Age of Empires II are the model), and keep that choice consistent.

The Ukrainian pack shows the tables' structure, the context of a line and
where a caption had to be shortened. It is never a source of words. The
European Portuguese pack is the nearest neighbour for length. Do not copy
either: read the English, then write the Turkish.

## 1. Voice and grammar

- The player is addressed as `sen`, and only when the sentence needs a
  subject. Most interface sentences need none.
- Instructions: the informal imperative. "Try again later." → `Sonra
  yeniden dene.`, "Choose the mod from the main menu." → `Modu ana menüden
  seç.`, "Press any key" → `Bir tuşa bas`. Never the formal `-in` / `-iniz`
  (`seçin`, `basın`, `deneyin`).
- Statements and hints: full sentences, neutral, present or past. "Settings
  were not saved." → `Ayarlar kaydedilmedi.` "The processor draws and scales
  the view." → `İşlemci görüntüyü çizer ve ölçekler.`
- Confirmation questions: the passive question, which does not need a
  pronoun. "Replace the game files?" → `Oyun dosyaları değiştirilsin mi?`,
  "Remove {name}?" → `{name} kaldırılsın mı?` A dialog title may be the
  same shape, shorter: `Oyundan çıkılsın mı?`
- Labels, buttons, menu items, setting names, headings: noun phrases or a
  short imperative, no full stop, sentence case (only the first word and
  names capitalised). "Open folder" → `Klasörü aç`, "Try again" → `Yeniden
  dene`, "Mouse wheel zoom" → `Fare tekerleğiyle yakınlaştırma`, "Restore
  defaults" → `Varsayılanlara dön`.
- Where the English is in capitals, the Turkish is in capitals too, with
  Turkish case: `i` becomes `İ`, `ı` becomes `I`, never the other way.
  `OPEN FOLDER` → `KLASÖRÜ AÇ`, `INFORMATION` → `BİLGİ`, `EXIT` → `ÇIKIŞ`
  (the word is çıkış: ı → I). `SETTINGS` → `AYARLAR`.
- Title Case English ("Load Game") becomes sentence case (`Oyunu yükle`).
- Short status words: the past or the `-iyor` form, no pronoun. "Installed"
  → `Kuruldu`, "Downloaded" → `İndirildi`, "Not found" → `Bulunamadı`,
  "Failed" → `Başarısız`, "Downloading…" → `İndiriliyor…`, "Waiting…" →
  `Bekleniyor…`, "Ready" → `Hazır`, "Off" / "On" → `Kapalı` / `Açık`.
- Mission briefings and HQ speaking to the Commander: a military register.
  Orders in the informal imperative (`Üssü yok et`, `Kapıyı koru`, `Yerini
  koru`). The Commander is `Komutan`. CORE's own lines are colder and stay
  as mechanical as the English (`HEMEN YERİNE GETİR.`). No slang, and no
  exclamation the English does not have.
- Units' spoken lines and the message log: short, as a soldier on the
  radio.
- Key names stay Latin as the keyboard prints them: Shift, Ctrl, Alt, Esc,
  Escape, Enter, Tab, F1–F12, Space (`boşluk` only inside a sentence).
  Acronyms kept in Latin: TCP, IP, CD, DirectPlay, DLL, URL, GPU, CPU, HUD,
  fps, ID, OK. `YZ` for AI in a sentence, `EMP` for EMP.
- Units of measure: `KB`, `MB`, `GB`, `ms`, `sn`, `dk`, as the English
  writes the unit. A space only where the English has one.
- Punctuation: no space before `: ? !`. Straight quotes `"` and `'`, as the
  English writes them. Keep `…`, `·`, `→`, `›`, `✓`, `✕`, `—` only where
  the English has them. Never write `;` (a table value ends at `;`): use a
  full stop, a comma or a dash. Never write `//`. Never write a tab or a
  line break inside a value.
- The letters this language uses are `ç ğ ı i ö ş ü` and `Ç Ğ I İ Ö Ş Ü`.
  Write `ı` and `i` by the word, not by eye: `kayıt`, `çıkış`, `ısı`,
  `yapı`, `saldırı` take dotless `ı`. `bilgi`, `giriş`, `için`, `bir`,
  `indir`, `işlem` take dotted `i`. A capital at the start of `indir` is
  `İndir`, never `Indir`. The capitals of `çıkış` are `ÇIKIŞ`: both I
  letters are dotless (the word is çık-ış). Never write a dotted `İ` in
  `çıkış`, and never drop the cedilla or the ş (`CIKIS`). Do not use
  `â î û`: write `rüzgar`, `hala`, `katil`.

## 2. Placeholders and numbers (hard rules)

- Every placeholder of the English stays, exactly as written: `{name}`,
  `{size}`, `%s`, `%d`, `%i`, `%.1f`, `%%`, `%1$s` and so on. Never
  translate, drop, add or respell one.
- printf conversions (`%s`, `%d`, …) stay in the same ORDER as in the
  English, because they are filled in that order. `{name}` slots may move.
- Every number written in digits stays (`1/32`, `2x`, `3.1c`, `16x16`,
  `9 x 21`).
- Staged captions written with `|` (`Easy|Medium|Hard`) keep exactly the
  same number of stages, each translated, in order.
- A slot's value has no vowel harmony and no case. Never attach a suffix
  to a slot (`{name}'ı`, `{name}'e`, `{name}'den`). Put the slot where the
  bare form is right: after a colon (`Kurulum: {name}`), after a noun that
  governs it (`{name} modu`, `{name} haritası`), or as the subject
  (`{name} kuruldu`).
- A count's noun stays singular after a digit, which is already correct
  Turkish: `{count} harita`, `{n} dosya`, `{n} dk`.
- `{device}` is filled with this pack's `cihaz` or with the system's own
  name (`iPad`). `{cloud}` is filled with `bulut` or a service name
  (`iCloud`). Write every sentence so either fits, with no suffix on the
  slot: `bu {device} üzerinde`, `{cloud} içinde`, `{cloud} üzerinden`.
- A tab or a line break never goes into a translation.

## 3. Names kept as written

- **ARM** and **CORE**, the two sides: always Latin capitals, whatever the
  English case (Arm, Core, ARM, CORE). They take Turkish suffixes on an
  apostrophe, by their last vowel. ARM (a, back unrounded): `ARM'ın`,
  `ARM'a`, `ARM'ı`, `ARM'da`, `ARM'dan`. CORE (o, back rounded): `CORE'un`,
  `CORE'a`, `CORE'u`, `CORE'da`, `CORE'dan`. As a label with no suffix:
  `ARM Komutanı`, `CORE seferi`, `CORE birlikleri`.
- Open Annihilation, OA, Core Prime (the service and the registry), Total
  Annihilation, Total Annihilation: The Core Contingency, Battle Tactics,
  Core Contingency, Cavedog Entertainment, GT Interactive, Steam, Steam
  Deck, Steam Input, GOG, Windows, macOS, Linux, DirectX, DirectPlay: as
  written. No suffix on them when a recast is easy. Where a suffix is
  unavoidable, apostrophe and harmony on the last vowel (`Steam'e`,
  `Windows'ta`).
- File names, folder names, extensions, keys, URLs, version strings
  (`3.1c`, `oamod.yaml`, `totala1.hpi`, `.oalang`, `Mods`): as written.

## 4. Fiction: places and names

Invented names that are ordinary English words are translated. Coined
names stay as written (they are already Latin). `CORE Prime` keeps CORE
in Latin because it is the side.

| English | Turkish |
|---|---|
| Core Prime (the CORE home planet) | CORE Prime |
| Empyrrean | Empyrrean |
| Galactic Gate / the Gate | Galaktik Kapı / Kapı |
| Thalassean | Thalassean |
| Tergiverse IV | Tergiverse IV |
| Barathrum | Barathrum |
| Rougpelt | Rougpelt |
| Aqueous Minor | Aqueous Minor |
| Aqueous Body 397 | Su kütlesi 397 |
| Aegus | Aegus |
| Dump (moon of Core Prime) | Çöplük |
| Hydross | Hydross |
| Lusch | Lusch |
| Temblor | Temblor |
| Gelidus | Gelidus |
| Krogoth | Krogoth |
| Central Consciousness | Merkezi Bilinç |
| the alien beacon | uzaylı feneri |
| the contingent Core Commander | yedek CORE Komutanı |
| the Serpents of Hydross (Sea Serpent) | deniz yılanları |
| the Scorpions of Lusch | akrepler |
| the Cloud Fortress | Bulut Kalesi |
| the Gauntlet (a passage) | Koridor |
| vermin (CORE's word for ARM) | haşere |
| the Arm/Core war | ARM ve CORE savaşı |
| patterning (CORE's transfer of minds into machines) | bilinç aktarımı |
| nanolathe, nanolathing | nanotornavida, nanotorna |

Briefing headings:

| English | Turkish |
|---|---|
| MISSION 1.0001ARME | MİSYON 1.0001ARME |
| Mission T01: | Misyon T01: |
| INFO FEED, INTEL FEED | BİLGİ AKIŞI, İSTİHBARAT |
| INTELL-TAP | İSTİHBARAT HATTI |
| END / DO SO NOW. | SON / HEMEN YERİNE GETİR. |
| PRIORITY / SPECIAL PRIORITY / PRIORITY CRITICAL / Top Priority | ÖNCELİK / ÖZEL ÖNCELİK / KRİTİK ÖNCELİK / En yüksek öncelik |
| WARNING / Attention / Emergency! / Alert! | UYARI / Dikkat / Acil durum! / Alarm! |
| Suggestions: / Battle Tactics: / Note: | Öneriler: / Savaş taktikleri: / Not: |
| To complete this mission you must … | Bu görevi bitirmek için … (imperative) |

Campaign place names that are coined (Hanan, Lipar, Brooban, Xantippe and
the rest) stay as written, the same spelling in `missions.tdf` and in the
briefings. Ordinary words in a mission title are translated (`the beacon`
→ `fener`, `the swamp` → `bataklık`). A leading `N: ` on a mission name
stays exactly, digits and colon included.

## 5. Game terms

| English | Turkish |
|---|---|
| Commander | Komutan |
| unit | birim |
| building, structure | bina, yapı |
| Kbot, KBot | Kbot |
| vehicle | araç |
| tank | tank |
| aircraft, plane | uçak |
| ship | gemi |
| submarine, sub | denizaltı |
| hovercraft | hoverkraft |
| hovertank | hovertank |
| seaplane | deniz uçağı |
| amphibious | amfibi |
| builder (a unit that builds) | inşaat birimi |
| factory, plant | fabrika |
| lab (Kbot Lab) | laboratuvar |
| shipyard | tersane |
| metal | metal |
| energy | enerji |
| resources | kaynaklar |
| storage | depo |
| metal extractor | metal çıkarıcı |
| metal maker | metal üretici |
| solar collector | güneş toplayıcı |
| wind generator | rüzgar üreteci |
| tidal generator | gelgit üreteci |
| fusion reactor / fusion power plant | füzyon reaktörü / füzyon santrali |
| geothermal | jeotermal |
| radar | radar |
| sonar | sonar |
| jammer | karıştırıcı |
| line of sight, LOS | görüş hattı |
| cloak, cloaked | gizlenme, gizli |
| stealth | gizlilik |
| wreck, wreckage | enkaz |
| feature (rocks, trees, wrecks) | yer öğesi |
| laser | lazer |
| plasma | plazma |
| missile / rocket | füze / roket |
| artillery | topçu |
| flak | uçaksavar |
| torpedo | torpido |
| depth charge | derinlik bombası |
| mine (weapon) | mayın |
| nuke, nuclear missile | nükleer füze |
| anti-nuke, missile defense | füze savunması |
| EMP | EMP |
| D-Gun (Disintegrator Gun) | D-Gun |
| anti-air | uçaksavar |
| ally, alliance | müttefik, ittifak |
| enemy | düşman |
| team | takım |
| kills / losses | imha / kayıp |
| veteran | gazi |
| victory / defeat | zafer / yenilgi |
| paused | durdu (the title: DURDU) |
| Tech Level 1 / 2 | Teknoloji 1 / Teknoloji 2 |
| Adv., Advanced | Glş. |
| build menu | inşa menüsü |
| control group | grup |
| selection, select | seçim, seç |
| waypoint | ara nokta |
| queue | sıra |
| self-destruct | kendini yok et |
| repair | onar |
| reclaim | geri al |
| patrol | devriye |
| guard | koru |
| map | harita |
| match, game (one played) | maç, oyun |
| the game (the program) | oyun |

### Orders (buttons and their states)

Captions drawn on the order buttons are one short word, in capitals, so
the picture can draw them large. Abbreviate with a full stop only when
the table below already does.

| English | Turkish |
|---|---|
| ATTACK | SALDIR |
| MOVE | GİT |
| STOP | DUR |
| PATROL | DEVRİYE |
| DEFEND / GUARD | SAVUN / KORU |
| RECLAIM | GERİ AL |
| REPAIR | ONAR |
| CAPTURE | ELE GEÇ |
| LOAD / UNLOAD | YÜKLE / BOŞALT |
| ORDERS | EMİR |
| BUILD | İNŞA |
| BLAST / D-GUN | D-GUN |
| ASSIST | YARDIM |
| Fire orders: Hold Fire / Return Fire / Fire At Will | Ateş kes / Karşılık ver / Serbest ateş |
| Move orders: Hold Position / Maneuver / Roam | Yerinde kal / Manevra / Dolan |
| On / Off (a unit) | Açık / Kapalı |
| Activate / Deactivate | Etkinleştir / Durdur |
| Cloaked / Visible | Gizli / Görünür |
| Resurrect | Dirilt |
| arm (an order) / ARM ORDER | hazırla / HAZIRLA |
| QUEUE / ADD / FORCE / CLEAR / STORE (touch) | SIRA / EKLE / ZORLA / TEMİZLE / SAKLA |

The order-button picture uses these capitals, with `|` between states:
`ATEŞ KES|KARŞILIK|SERBEST|ATEŞ EMRİ`,
`YERİNDE KAL|MANEVRA|DOLAN|HAREKET EMRİ`,
`KAPALI|AÇIK|AÇ/KAPA`, `GÖRÜNÜR|GİZLİ|GİZLENME`,
`ETKİNLEŞTİR|DURDUR`. The top bar is `METAL|ENERJİ`. The battlefield
titles are `DURDU`, `ZAFER!`, `YENİLGİ`. The load and save titles are
`YÜKLE`, `OYUNU KAYDET`, `OYUNU YÜKLE`.

## 6. Menus and modes

| English | Turkish |
|---|---|
| Single Player | Tek oyuncu |
| Multiplayer | Çok oyunculu |
| Campaign | Sefer |
| Mission | Görev |
| Briefing | Bilgilendirme |
| Skirmish | Çatışma |
| Battle Room | Savaş odası |
| Lobby / Lounge | Lobi |
| host / join | kur (a game) / katıl; the host: kurucu |
| player | oyuncu |
| computer player, AI | Bilgisayar (3.1c's "Computer"), YZ ("AI") |
| watcher, spectator / watch | izleyici / izle |
| replay | tekrar |
| recorder, recording | kaydedici, kayıt |
| saved game / save / load | kayıtlı oyun / kaydet / yükle |
| Options | Seçenekler |
| Settings | Ayarlar |
| Preferences | Tercihler |
| Previous Menu / Back | Önceki menü / Geri |
| Main menu / Game menu | Ana menü / Oyun menüsü |
| Exit, Quit | Çık |
| Exit to the system | Sistemden çık |
| OK / Cancel / Done / Close / Apply | OK / İptal / Bitti / Kapat / Uygula |
| Retry, Try again | Yeniden dene |
| Continue / Resume | Devam et / Sürdür |
| Easy / Medium / Hard | Kolay / Orta / Zor |
| Help | Yardım |
| Chat | Sohbet |
| Cheats | Hileler |
| game speed | oyun hızı |
| Sound / Music / Volume / Movies | Ses / Müzik / Ses düzeyi / Filmler |
| Credits | Jenerik |
| Intro | Giriş |
| Restrictions | Kısıtlamalar |
| SINGLE / MULTI / INTRO / EXIT (title screen) | TEK OYUNCU / ÇOK OYUNCULU / GİRİŞ / ÇIKIŞ |
| On / Off (3.1c's sound toggles) | Açık / Kapalı |
| the game menu's Settings | Ayarlar, or Ayar where it does not fit |
| Wind Speed / Gravity (briefing) | Rüzgar / Yerçekimi |

## 7. Open Annihilation's interface

| English | Turkish |
|---|---|
| Library | Kitaplık |
| mod | mod |
| mod profile | mod profili |
| hacks, standard hacks | ince ayar, hazır ince ayarlar |
| mutator | mutatör |
| brain (a computer player's mind) | beyin |
| map / map pack | harita / harita paketi |
| language pack | dil paketi |
| package | paket |
| expansion | genişleme |
| base game | temel oyun |
| registry (a server listing packages) | kayıt yeri |
| catalogue | katalog |
| download (verb / noun) | indir / indirme |
| install / update / remove / delete | kur / güncelle, güncelleme / kaldır / sil |
| version / revision | sürüm / düzeltme |
| roll back | geri al (an update) |
| folder / file | klasör / dosya |
| archive (an .hpi, .ufo, .ccx or .gp3 file) | arşiv |
| game files / game folder / game archives | oyun dosyaları / oyun klasörü / oyun arşivleri |
| device | cihaz |
| the cloud | bulut |
| free (space) | boş (`{size} free` → `{size} boş`) |
| screen / window / full screen | ekran / pencere / tam ekran |
| zoom, zoom in / out | yakınlaştırma, yakınlaştır / uzaklaştır |
| graphics | grafikler |
| graphics card | ekran kartı |
| hardware acceleration | donanım hızlandırma |
| vertical sync | dikey eşitleme |
| anti-aliasing | kenar yumuşatma |
| frame rate / frame | kare hızı / kare |
| pixel | piksel |
| resolution | çözünürlük |
| modern fonts | modern yazı tipleri |
| font / text size | yazı tipi / yazı boyutu |
| controller / trackpad / stick / gyro / D-pad | kumanda / izleme dörtgeni / çubuk / jiroskop / yön tuşu |
| control (a thing on screen) | denetim |
| touch | dokunma |
| haptics | titreşim |
| pointer | işaretçi |
| mouse / mouse wheel | fare / fare tekerleği |
| keyboard | klavye |
| press (a key) | bas (`Enter'a bas`) |
| type (text) | yaz (`Bir ad yaz`) |
| scroll | kaydır |
| show / hide | göster / gizle |
| enable / disable | aç / kapat |
| user | kullanıcı |
| password | parola |
| share | paylaş |
| manage | yönet |
| access (verb) | eriş |
| default | varsayılan |
| preview | önizleme |
| log (a file of messages) | günlük |
| Developer Mode | Geliştirici kipi |
| Language / System default | Dil / Sistem varsayılanı |
| snap (click snap) | yapışma |
| the host (of a shared game) | kurucu |
| shared game / network play | ortak oyun / ağ oyunu |
| install ID | kurulum kimliği |
| demo | demo |
| content | içerik |
| key (keyboard) / key binding | tuş / tuş ataması |
| key layout | tuş düzeni |
| key editor | tuş düzenleyici |
| action (a binding) | eylem |
| latch / latched | kilitle / kilitli |
| hold to confirm | onaylamak için basılı tut |
| unbound | atanmamış |
| app | uygulama |
| phone / tablet | telefon / tablet |
| the old copy / the new copy | eski kopya / yeni kopya |
| revision {revision} | düzeltme {revision} |

`device` and `the cloud` are the bare nouns `cihaz` and `bulut`, with no
article and no suffix, because other sentences drop them into a slot.

Named keys that are words, in a label: arrows `Yukarı ok`, `Aşağı ok`,
`Sol ok`, `Sağ ok`. Numpad is `Sayısal tuş takımı`. Mouse buttons: `Sol
tuş`, `Sağ tuş`, `Orta tuş`. Wheel: `Tekerlek yukarı`, `Tekerlek aşağı`.

## 8. Unit names

Proper names stay in English, as written: they are the units' code names
(`Peewee`, `Flash`, `Zeus`, `Fido`, `Pelican`, `Big Bertha`, `Freedom
Fighter`, `Sea Serpent`, `The Can`). Generic names, which say what a unit
or building is, are translated, and kept short enough for the bottom bar.
Use these exactly, in `units.tdf` and wherever a unit is named.

| English | Turkish |
|---|---|
| Adv. Aircraft Plant | Glş. uçak fabrikası |
| Adv. Construction Aircraft | Glş. inşaat uçağı |
| Adv. Construction Kbot | Glş. inşaat Kbotu |
| Advanced Construction Sub | Glş. inşaat denizaltısı |
| Adv. Construction Vehicle | Glş. inşaat aracı |
| Adv. Kbot Lab | Glş. Kbot laboratuvarı |
| Aircraft Plant | Uçak fabrikası |
| Advanced Radar Tower | Glş. radar kulesi |
| Advanced Sonar Station | Glş. sonar istasyonu |
| Air Repair Pad | Uçak onarım pisti |
| Adv. Shipyard | Glş. tersane |
| Advanced Torpedo Launcher | Glş. torpido fırlatıcı |
| Adv. Vehicle Plant | Glş. araç fabrikası |
| Alien Beacon | Uzaylı feneri |
| Construction Aircraft | İnşaat uçağı |
| Construction Hovercraft | İnşaat hoverkraftı |
| Construction Kbot / KBot | İnşaat Kbotu |
| Cloakable Fusion Reactor | Gizli füzyon reaktörü |
| Commander | Komutan |
| Construction Ship | İnşaat gemisi |
| Construction Seaplane | İnşaat deniz uçağı |
| Construction Vehicle | İnşaat aracı |
| Decoy Commander | Yem Komutan |
| Implosion Device | Çökertme aygıtı |
| Dragon's Teeth | Ejderha dişleri |
| Floating Dragon's Teeth | Yüzer ejderha dişleri |
| Energy Storage | Enerji deposu |
| Floating Metal Maker | Yüzer metal üretici |
| Fortification Wall | Tahkimat duvarı |
| Fusion Reactor | Füzyon reaktörü |
| Fusion Power Plant | Füzyon santrali |
| Galactic Gate | Galaktik Kapı |
| Geothermal Powerplant | Jeotermal santral |
| Hovercraft Platform | Hoverkraft platformu |
| Kbot Lab | Kbot laboratuvarı |
| L.L.T. | L.L.T. |
| Light Laser Tower | Hafif lazer kulesi |
| Heavy Laser Tower | Ağır lazer kulesi |
| Metal Maker | Metal üretici |
| Metal Extractor | Metal çıkarıcı |
| Area Mine | Alan mayını |
| Focused Mine | Odaklı mayın |
| HE Area Mine | YH alan mayını |
| Precision Mine | Hassas mayın |
| Nuclear Mine | Nükleer mayın |
| Moho Metal Maker | Moho metal üretici |
| Moho Mine | Moho madeni |
| Metal Storage | Metal deposu |
| Seaplane Platform | Deniz uçağı platformu |
| Radar Tower | Radar kulesi |
| Solar Collector | Güneş toplayıcı |
| Sonar Station | Sonar istasyonu |
| Shipyard | Tersane |
| Targeting Facility | Hedefleme tesisi |
| Tidal Generator | Gelgit üreteci |
| Torpedo Launcher | Torpido fırlatıcı |
| Underwater Energy Storage | Sualtı enerji deposu |
| Underwater Fusion Plant | Sualtı füzyon santrali |
| Underwater Metal Extractor | Sualtı metal çıkarıcı |
| Underwater Metal Storage | Sualtı metal deposu |
| Vehicle Plant | Araç fabrikası |
| Wind Generator | Rüzgar üreteci |
| Hydration Plant | Hidrasyon santrali |
| Fortitude Missile Defense | Fortitude füze savunması |
| Krogoth Gantry | Krogoth iskelesi |
| Mobile Artillery | Gezici topçu |
| Missile Frigate | Füze fırkateyni |
| Resurrection Kbot | Diriltme Kbotu |

Descriptions stay as short as the English. Recurring ones:

| English | Turkish |
|---|---|
| Produces Energy | Enerji üretir |
| Produces Aircraft | Uçak üretir |
| Produces Kbots | Kbot üretir |
| Produces Ships | Gemi üretir |
| Produces Vehicles | Araç üretir |
| Tech Level 1 | Teknoloji 1 |
| Tech Level 2 | Teknoloji 2 |
| Perimeter Defense | Çevre savunması |
| Increases Energy Storage | Enerji deposunu artırır |
| Increases Metal Storage | Metal deposunu artırır |
| Extracts Metal | Metal çıkarır |
| Indigenous Lifeform | Yerel yaşam |
| Assault Kbot | Taarruz Kbotu |
| Bomber | Bombardıman |
| Anti-Air Ship | Uçaksavar gemisi |
| Anti-Air Hovercraft | Uçaksavar hoverkraft |
| Pop-up Heavy Cannon | Çıkan ağır top |
| Anti Missile Defense System | Füze savunması |
| Amphibious Kbot | Amfibi Kbot |
| Radar Jammer | Radar karıştırıcı |
| Automatically repairs aircraft | Uçakları kendi onarır |
| Air Transport | Hava nakliyesi |
| Radar Plane | Radar uçağı |

## 9. Width

A caption on one of 3.1c's fixed-size buttons has to stay about as long
as the English, or shorter. Turkish adds suffixes, so pick the short word
from this glossary (`Çık` not `Çıkış yap`, `Kur` not `Yükle ve kur`, `Ayar`
when `Ayarlar` will not fit). The order buttons in section 5 are already
the short forms. A map description starts with the English's own size
prefix, copied exactly, including its spaces (`5 x 8  `, `11 x 10 map.  `).
Translate a descriptive map name. Leave a coined map name as written.

## 10. What stays in English, and why

ARM, CORE, D-Gun, OK, mod, demo, HUD, EMP, Moho, Kbot, hovertank, and
every proper unit name. Open Annihilation, Core Prime, Total Annihilation
and the expansions, Cavedog, and every file name, key name and version.
Coined place names. These are the words a player already meets in the
game's own data and in mods, and translating them would hide the unit.
