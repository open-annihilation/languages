# Bengali (bn) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the modern Bengali a player in Bangladesh or West Bengal
would expect in a strategy game (the Bengali interfaces of Windows and
Steam, and Bengali editions of real-time strategy games, are the model),
and keep that choice for the whole pack. Spelling is contemporary standard
Bengali (প্রমিত বাংলা), not সাধু ভাষা and not Roman Bengali.

The pack needs shaping. Bengali letters join, stack and reorder, which
side-by-side drawing cannot do. The letters come from the pack's own face,
Noto Sans Bengali Bold, cut to the Bengali block with its shaping tables
kept (`fonts/README.md`). The sans faces that travel with the game draw
Latin. Write real Bengali spelling, with hasanta (্) where a conjunct
belongs. Do not insert U+200C or U+200D unless a word would form the wrong
conjunct without one. End a sentence with the danda (।). U+0964 is the
danda Bengali uses, and the face draws it. Keep `.` in an abbreviation
(`রিভ.`, `উন্ন.`), a decimal, a version, a file name and `...`. Use `?`
and `!` as the English does. Do not use Bengali digits (০-৯). A number
stays in the ASCII digits the English wrote.

The language's own name, বাংলা, is not in the engine's faces. Settings ›
Language draws that name from those faces before the pack is installed, so
it can show as a box until the pack is on disk. The pack's face draws it
after that. Do not change the endonym to Latin.

Ukrainian is the structural template. Korean shows how a pack in another
script transliterates a nickname and translates a description. Neither is a
source of Bengali words: read the English, then write Bengali.

## 1. Voice and grammar

- The player is তুমি. Interface instructions use the second-person
  familiar imperative: `চাপো`, `বেছে নাও`, `খোলো`, `আবার চেষ্টা করো`,
  `নাম লেখো`. Never আপনি, never the formal imperative (`চাপুন`, `খুলুন`,
  `করুন`), never অনুগ্রহ করে as the way an instruction is given.
- Possessives are তোমার, তোমাকে, তোমায়. "Your folder" → `তোমার ফোল্ডার`.
  Leave the pronoun out when Bengali does not need it.
- Statements and hints: plain present or past, neutral. "Settings were not
  saved." → `সেটিংস সেভ হয়নি।` "The processor draws and scales the view."
  → `প্রসেসর দৃশ্য আঁকে এবং মাপ বদলায়।`
- Confirmation questions: the same familiar form, with `?`. "Replace the
  game files?" → `গেমের ফাইল বদলাবে?`
- Labels, buttons, menu items, setting names and headings: a noun phrase
  or a familiar imperative, no danda. Bengali has no capitals. Where
  the English is in capitals, the Bengali is the same short word, not a
  sentence. "Open folder" → `ফোল্ডার খোলো`, "Try again" → `আবার চেষ্টা`.
- Short status words: a noun of the action, or হয়নি / হয়েছে. "Installed"
  → `ইনস্টল হয়েছে`, "Downloading" → `নামছে…`, "Not found" → `মেলেনি`,
  "Failed" → `হয়নি`, "Waiting" → `অপেক্ষা…`, "Ready" → `তৈরি`, "Off" /
  "On" → `বন্ধ` / `চালু`.
- Mission briefings and in-fiction orders (HQ to the one Commander): the
  same familiar imperative, military and short. `ছায়াপথের ফটকের চারপাশে
  পাহারা বসাও।` `তোমার ইউনিট ফটকে নিয়ে যাও এবং সেটা ধরে রাখো।` The
  Commander is কমান্ডার. Own forces are `আমাদের বাহিনী`. No slang, and no
  exclamation the English does not have.
- Briefing stock lines: `MISSION` → `মিশন` (the code after it stays,
  `মিশন 1.0001ARME`), `Mission T01:` → `মিশন T01:`, `PRIORITY` →
  `অগ্রাধিকার`, `PRIORITY CRITICAL` → `অগ্রাধিকার সংকটপূর্ণ`, `INFO FEED`
  → `খবর`, `INTEL FEED` → `গোয়েন্দা খবর`, `INTELL-TAP:` → `আড়িপাতা:`,
  `END` → `শেষ`, `WARNING` → `সতর্কতা`, `Attention` / `Alert!` → `মনোযোগ`
  / `সতর্ক!`, `Suggestions:` → `পরামর্শ:`, `Battle Tactics:` → `যুদ্ধের
  কৌশল:`, `DO SO NOW.` → `এখনই করো।`, `Arm vermin` → `ARM-এর কীট`, `To
  complete this mission you must` → `এই মিশন শেষ করতে তোমাকে`.
- CORE's briefings are a machine talking: colder and more clipped than
  ARM's, still the familiar imperative.
- Unit speech and the message log: short, as on a radio.
- Key names stay as the keyboard prints them: Shift, Ctrl, Alt, Esc,
  Escape, Enter, Tab, Space, Backspace, Delete, Insert, Home, End, Page
  Up, Page Down, F1–F12, Win, Option. In a sentence, Space is `স্পেস`.
  Arrows are `উপরের তির`, `নিচের তির`, `বাঁ তির`, `ডান তির`. Numpad is
  `নামপ্যাড`. Mouse buttons: `বাঁ বোতাম`, `ডান বোতাম`, `মাঝের বোতাম`.
  Wheel: `চাকা উপরে`, `চাকা নিচে`.
- Acronyms kept in Latin: TCP, IP, CD, DirectPlay, GPU, CPU, HUD, fps, KB,
  MB, GB, ID, EMP, D-Gun. AI on a tiny button stays `AI`. In a sentence,
  AI is `AI`.
- Punctuation: no space before `: ? !` or `।`. Keep `…` or `...`, and `·`, `→`,
  `✓`, `✕`, `—`, exactly as the English uses them. Quotes are “ ”. Never
  write `;` (a table value ends at `;`): use a danda, a comma or a
  dash. Never write `//`. Never write a tab inside a value. A sentence
  ends with `।`. Keep `.` for an abbreviation, a decimal, a version, a
  file name and `...`.
- Hasanta belongs to the word (`ক্ষ`, `প্র`, `স্ট`). Do not break a
  conjunct with a space or a hyphen to make it narrower.

## 2. Placeholders and numbers (hard rules)

- Every placeholder stays exactly as written: `{name}`, `{size}`, `{count}`,
  `%s`, `%d`, `%i`, `%.1f`, `%%`, `%1$s` and the rest. Never translate,
  drop, add or respell one.
- printf conversions stay in the English order. They are filled in that
  order. Reword the sentence around them. `{name}` slots may move.
- Every number written in digits stays (`1/32`, `2x`, `3.1c`, `16x16`,
  `9 x 21`, `1997`). Decimal points stay as the English writes them.
  Never rewrite a digit as ০-৯.
- A string that is only digits, punctuation or a kept key name is copied
  unchanged (`2`, `3`, `,`, `+{n}`).
- Staged captions with `|` (`Easy|Medium|Hard`) keep the same number of
  stages, in the same order.
- Do not glue a Bengali ending onto a slot (`{name}কে` is allowed as a
  separate word after a space; `{name}র` is not). Prefer `এর {name}`,
  `{name}-এর` only when the hyphen is already how this pack writes a
  suffix, or restructure so the slot stands alone: `{name} সেভ হয়নি`.
- `{device}` is filled with this pack's word `ডিভাইস` or with a system
  name (`iPad`). `{cloud}` is filled with `ক্লাউড` or a system name
  (`iCloud`). Translate the entries `device` → `ডিভাইস` and `the cloud` →
  `ক্লাউড`, and write the sentences so either value fits.
- A count does not know its number. Use a wording that works for any
  count (`{count}টি ফাইল`).
- A tab or a line break never goes into a translation.
- Colour marks in a briefing (`&Y*`, `&R`, `*&`) stay exactly, and the
  count of `&` and of `*` in the file stays the same. A blank line stays
  blank. The line count stays the same. Line ends are LF.

## 3. Names kept as written

- **ARM** and **CORE**, always in Latin capitals, whatever the English
  case (Arm, Core, ARM, CORE). They take no Bengali spelling. A following
  word is Bengali: `ARM-এর ইউনিট`, `CORE-এর কমান্ডার`, `CORE অভিযান`.
- Open Annihilation, OA, Core Prime (the service and the planet), Total
  Annihilation, Total Annihilation: The Core Contingency, Total
  Annihilation: Battle Tactics, Cavedog Entertainment, GT Interactive,
  Steam, GOG, iCloud, Windows, macOS, Linux, DirectX, DirectPlay: as
  written.
- File names, folder names, extensions, URLs and version strings (`3.1c`,
  `oamod.yaml`, `totala1.hpi`, `.oalang`, `.oamut`, `.oabrain`, `.oakeys`):
  as written.
- **Kbot** (any capitalisation), **Moho**, **Gaat**, **D-Gun**, **EMP**,
  **FARK**, and model codes (`A.K.`, `L.L.T.`, `M-104`, `M-209`, `M-303`,
  `M-420`, `M-515`, `M-610`): Latin, as written.

## 4. Fiction: places and names

Invented proper names of places stay spelled as in the English. Ordinary
words are translated. Use each form once, including in mission titles and
briefings.

| English | Bengali |
|---|---|
| Galactic Gate / the Gate | ছায়াপথের ফটক / ফটক |
| Central Consciousness | কেন্দ্রীয় চেতনা |
| Larab Harbor | লারাব বন্দর |
| Bromid Maze | ব্রোমিডের গোলকধাঁধা |
| Brooban's Isle | ব্রুবানের দ্বীপ |
| Motien Ramp | মোটিয়েন ঢাল |
| Xantippe's Abyss | জ্যান্টিপির অতল |
| Vebreen Fleet | ভেব্রিন নৌবহর |
| the Arm/Core war | ARM আর CORE-এর যুদ্ধ |
| patterning | নকশা স্থানান্তর |
| Com Pattern | Com-এর নকশা |
| nanolathe, nanolathing | ন্যানোলেদ, ন্যানোলেদ করা |
| homeworld | মাতৃগ্রহ |
| Crustal 8 | ক্রাস্টাল 8 |
| the beacon (Alien Beacon) | বাতিঘর |
| the implosion device | অন্তর্মুখী বিস্ফোরণের যন্ত্র |
| the contingent Core Commander | দলের CORE কমান্ডার |
| Astrede Shoreline | অ্যাস্ট্রিড তট |
| Landown's Interface | ল্যান্ডাউনের ফাটল |
| Gauntlet | আগুনের পথ |

Empyrrean, Thalassean, Tergiverse IV, Barathrum, Rougpelt, Aqueous Minor,
Aegus, Dump, Hydross, Lusch, Temblor, Gelidus, Krogoth, Slolam Pilago and
Isle Parche stay spelled as in the English. Battle Tactics place names
(Hanan, Lipar, Meraldi and the rest) stay spelled as in the English. The
briefings use the missions table's spelling.

## 5. Game terms

| English | Bengali |
|---|---|
| Commander | কমান্ডার |
| unit | ইউনিট |
| building, structure | ভবন, কাঠামো |
| Building (construction under way, the sound page) | নির্মাণ |
| Building Sounds | নির্মাণের শব্দ |
| Kbot, KBot, kbot | Kbot |
| vehicle | যান |
| tank | ট্যাংক |
| aircraft / plane | বিমান |
| ship | জাহাজ |
| submarine, sub | ডুবোজাহাজ |
| hovercraft | হোভার |
| seaplane | জলবিমান |
| amphibious | উভচর |
| builder | নির্মাতা |
| factory, plant | কারখানা |
| lab (Kbot Lab) | ল্যাব |
| shipyard | জাহাজঘাট |
| metal | ধাতু |
| energy | শক্তি |
| resources | সম্পদ |
| storage | ভাণ্ডার |
| income / production | আয় / উৎপাদন |
| metal extractor | ধাতু খনন |
| metal maker | ধাতু কারক |
| Moho | Moho (খনন Moho, ধাতু কারক Moho) |
| solar collector | সৌর সংগ্রাহক |
| wind generator | বায়ু জেনারেটর |
| tidal generator | জোয়ার জেনারেটর |
| fusion reactor | ফিউশন চুল্লি |
| fusion power plant | ফিউশন বিদ্যুৎঘর |
| geothermal powerplant | ভূতাপ বিদ্যুৎঘর |
| radar | রাডার |
| sonar | সোনার |
| jammer | জ্যামার |
| line of sight, LOS | দৃষ্টিসীমা |
| cloak, cloaked | আড়াল, আড়ালে |
| stealth | গোপন |
| wreck, wreckage | ধ্বংসাবশেষ |
| feature | মানচিত্রের বস্তু |
| laser | লেজার |
| plasma | প্লাজমা |
| missile | মিসাইল |
| rocket | রকেট |
| artillery | কামান |
| flak | বিমানধ্বংসী |
| torpedo | টর্পেডো |
| depth charge | গভীর বোমা |
| mine | মাইন |
| nuke, nuclear missile | পারমাণবিক মিসাইল |
| anti-nuke, missile defense | মিসাইল প্রতিরক্ষা |
| EMP | EMP |
| D-Gun (Disintegrator Gun) | D-Gun |
| anti-air | বিমানধ্বংসী |
| ally, alliance | মিত্র, জোট |
| enemy | শত্রু |
| team | দল |
| kills / losses | ধ্বংস / ক্ষয় |
| veteran / veterancy | ভেটেরান / অভিজ্ঞতা |
| victory / defeat | জয় / হার |
| paused | বিরতি (battlefield title: বিরতি). STOP stays থাম. A download or a version that has paused is থেমে আছে; during a match or a game, থেমে থাকে. |
| Tech Level 1 / 2 | টেক স্তর 1 / টেক স্তর 2 |
| Adv., Advanced | উন্নত (উন্নত where the English shortens to Adv.) |
| build menu | বানানোর মেনু |
| control group | দল |
| selection, select | বাছাই, বাছো |
| waypoint | পথের বিন্দু |
| queue | সারি |
| self-destruct | আত্মধ্বংস |
| repair | মেরামত, সারাও |
| reclaim | উদ্ধার, উদ্ধার করো |
| patrol | টহল, টহল দাও |
| guard / defend | পাহারা, রক্ষা |
| capture | দখল, দখল করো |
| map | ম্যাপ |
| match, game (one played) | লড়াই |
| the game (the program) | গেম |
| fog of war | যুদ্ধের কুয়াশা |
| resurrect | ফিরিয়ে আনো |

### Orders (buttons and their states)

Captions on the order buttons are the short forms, not sentences. Bengali
conjuncts are wide, so these stay to one short word.

| English | Bengali |
|---|---|
| ATTACK | হামলা (in a sentence: আক্রমণ করো) |
| MOVE | চল |
| STOP | থাম |
| PATROL | টহল |
| DEFEND / GUARD | রক্ষা |
| RECLAIM | উদ্ধার |
| REPAIR | সারাও |
| CAPTURE | দখল |
| LOAD / UNLOAD | তোল / নামাও |
| ORDERS | আদেশ |
| BUILD | বানাও |
| BLAST / D-GUN | D-GUN |
| ASSIST | সাহায্য |
| QUEUE / ADD / FORCE / CLEAR / STORE (touch) | সারি / যোগ / জোর / মুছো / রাখো |
| arm (an order) / ARM ORDER | সশস্ত্র করো / সশস্ত্র |
| Patrolling / Guarding | টহল দিচ্ছে / পাহারা দিচ্ছে |

Staged captions keep every `|`. Copy these strings exactly:

- Fire orders (Hold Fire, Return Fire, Fire At Will, the button name): বন্ধ|ফিরতি|যেকোনো|আগুন
- Move orders (Hold Position, Maneuver, Roam, the button name): স্থির|চাল|ঘুর|চলা
- Power (Off, On, the button name): বন্ধ|চালু|বিদ্যুৎ
- Activate (Activate, Deactivate): সক্রিয়|নিষ্ক্রিয়
- Cloak (Visible, Cloaked, the button name): দেখা|আড়াল|আড়াল

The picture captions use these short forms. The battlefield titles are
`বিরতি`, `জয়!`, `হার`. Save and load dialog titles: `গেম সেভ`, `গেম খোলো`.

## 6. Menus and modes

| English | Bengali |
|---|---|
| Single Player | একক |
| Multiplayer | মাল্টিপ্লেয়ার |
| Campaign | অভিযান |
| Mission | মিশন |
| Briefing | ব্রিফিং |
| Skirmish | লড়াই |
| Battle Room | লড়াইয়ের ঘর |
| Lobby / Lounge | অপেক্ষাকক্ষ |
| host / join | হোস্ট / যোগ দাও |
| the Creator (3.1c's host) | হোস্ট |
| player | খেলোয়াড় |
| computer player | কম্পিউটার |
| AI | AI |
| watcher, spectator / watch | দর্শক / দেখো |
| replay | রিপ্লে |
| recorder, recording | রেকর্ডার, রেকর্ডিং |
| saved game / save / load | সেভ করা গেম / সেভ / খোলো |
| Options | অপশন |
| Settings | সেটিংস |
| Preferences | পছন্দ |
| Previous Menu / Back | আগের মেনু / ফেরত |
| Main menu / Game menu | মূল মেনু / গেম মেনু |
| Exit, Quit | বেরোও |
| Exit to the system | সিস্টেমে বেরোও |
| OK / Cancel / Done / Close / Apply | ঠিক / বাতিল / হয়ে গেছে / বন্ধ / প্রয়োগ |
| Retry, Try again | আবার চেষ্টা |
| Continue / Resume | চালিয়ে যাও |
| Restart | আবার শুরু |
| Restore Defaults | ডিফল্টে ফেরো |
| Easy / Medium / Hard | সহজ / মাঝারি / কঠিন |
| Help | সাহায্য |
| Chat | চ্যাট |
| Cheats | চিট |
| game speed | গেমের গতি |
| Sound / Music / Volume / Movies | শব্দ / সঙ্গীত / আওয়াজ / চলচ্চিত্র |
| Sound Volume / Music Volume | শব্দের ভলিউম / সঙ্গীতের ভলিউম |
| Credits | নির্মাতারা |
| Intro | ইন্ট্রো |
| Restrictions | বাধা |
| SINGLE / MULTI / INTRO / EXIT | একক / অনেকজন / ইন্ট্রো / বেরোও |
| On / Off (3.1c's sound toggles) | হ্যাঁ / না |
| Wind Speed / Gravity | বাতাস / মাধ্যাকর্ষণ |
| Narration / No Narration | বর্ণনা / বর্ণনা নেই |

Title-screen words that must fit a narrow button use the short forms
`একক` and `অনেকজন` (the word Multiplayer, where it has room, is
`মাল্টিপ্লেয়ার`). Apply is `প্রয়োগ`, also in `Applied in this order`. A
setting that takes effect later (applies at the next match, when the Library
closes) is `কার্যকর হয়`. Set, Place, Assign group and the bookmarks stay `বসাও`.

## 7. Open Annihilation's interface

| English | Bengali |
|---|---|
| Library | লাইব্রেরি |
| mod | মোড |
| mod profile | মোডের প্রোফাইল |
| hacks, standard hacks | হ্যাক, সাধারণ হ্যাক |
| map pack | ম্যাপ প্যাক |
| language pack | ভাষার প্যাক |
| package | প্যাকেজ |
| expansion | এক্সপানশন |
| base game | মূল গেম |
| registry | রেজিস্ট্রি |
| catalogue | তালিকা |
| download / install / update / remove / delete | নামাও / ইনস্টল / আপডেট / সরাও / মুছো |
| version / revision | ভার্সন / রিভিশন. The Library's short mark, where the English says `rev`, is `রিভ.` (`{version} · রিভ. {revision}`). Spelling রিভিশন there leaves no room for a mod's name. |
| roll back | ফিরিয়ে নাও |
| folder / file / archive | ফোল্ডার / ফাইল / আর্কাইভ |
| game files / game folder / game archives | গেমের ফাইল / গেমের ফোল্ডার / গেমের আর্কাইভ |
| device | ডিভাইস |
| free (space) | ফাঁকা (`{size} free` → `{size} ফাঁকা`) |
| screen / window / full screen | পর্দা / উইন্ডো / পুরো পর্দা |
| zoom, zoom in / out | জুম, বড় করো / ছোট করো |
| graphics | গ্রাফিক্স |
| hardware acceleration | হার্ডওয়্যার ত্বরণ |
| vertical sync | উল্লম্ব সিঙ্ক |
| anti-aliasing | অ্যান্টি-অ্যালায়াসিং |
| frame rate | ফ্রেম রেট |
| resolution | রেজোলিউশন |
| modern fonts | আধুনিক ফন্ট |
| font / text size | ফন্ট / লেখার মাপ |
| controller / trackpad / stick / gyro / D-pad | কন্ট্রোলার / ট্র্যাকপ্যাড / স্টিক / জাইরো / ডি-প্যাড |
| touch | স্পর্শ |
| haptics | হ্যাপটিক্স |
| pointer | পয়েন্টার |
| Developer Mode | ডেভেলপার মোড |
| Language / System default | ভাষা / সিস্টেমের নিজস্ব |
| snap (click snap) | স্ন্যাপ |
| shared game | শেয়ার করা গেম |
| HUD | HUD |
| Unicode | ইউনিকোড |
| install ID | ইনস্টল ID |
| demo | ডেমো |
| tag (a Library filter) | ট্যাগ |
| channel (updates) | চ্যানেল |

`Available to download` → `নামানোর জন্য`. `Play now` → `এখন খেলো`.
`Get mutators` → `মিউটেটর নাও`. `Open Annihilation Library` →
`OPEN ANNIHILATION লাইব্রেরি`.

## 8. Unit names

Generic names are translated with section 5's words. A proper nickname is
transliterated so a Bengali reader can say the English name back. Do not
translate a nickname's meaning (`Hammer` is `হ্যামার`, not `হাতুড়ি`.
`Peewee` is `পিউই`, not a word for "small"). Personal names, codes and
invented tokens in section 3 stay Latin: FARK, Fido, Jeffy, Jethro, Luger,
Marky, Merl, Morty, Nixer, Podger, Rocko, Samson, Krogoth, A.K., L.L.T.,
M-104, M-209, M-303, M-420, M-515, M-610. `Moho` and `Gaat` stay, and the
ordinary word beside them is translated (`Moho খনন`, `Gaat কামান`).

Use the name exactly, in `units.tdf` and anywhere a unit is named.
Descriptions are as short as the English.

Generic and descriptive names:

Adv. Aircraft Plant → উন্নত বিমান কারখানা · Aircraft Plant → বিমান
কারখানা · Adv. Construction Aircraft → উন্নত নির্মাণ বিমান · Construction
Aircraft → নির্মাণ বিমান · Adv. Construction Kbot → উন্নত নির্মাণ Kbot ·
Construction Kbot / Construction KBot → নির্মাণ Kbot · Advanced
Construction Sub → উন্নত নির্মাণ ডুবোজাহাজ · Adv. Construction Vehicle →
উন্নত নির্মাণ যান · Construction Vehicle → নির্মাণ যান · Construction Ship
→ নির্মাণ জাহাজ · Construction Seaplane → নির্মাণ জলবিমান · Construction
Hovercraft → নির্মাণ হোভার · Adv. Kbot Lab → উন্নত Kbot ল্যাব · Kbot Lab →
Kbot ল্যাব · Adv. Vehicle Plant → উন্নত যান কারখানা · Vehicle Plant → যান
কারখানা · Adv. Shipyard → উন্নত জাহাজঘাট · Shipyard → জাহাজঘাট · Advanced
Radar Tower → উন্নত রাডার টাওয়ার · Radar Tower → রাডার টাওয়ার · Advanced
Sonar Station → উন্নত সোনার স্টেশন · Sonar Station → সোনার স্টেশন ·
Advanced Torpedo Launcher → উন্নত টর্পেডো নিক্ষেপক · Torpedo Launcher →
টর্পেডো নিক্ষেপক · Air Repair Pad → বিমান মেরামত প্যাড · Hovercraft
Platform → হোভার প্ল্যাটফর্ম · Seaplane Platform → জলবিমান প্ল্যাটফর্ম ·
Krogoth Gantry → Krogoth গ্যান্ট্রি · Cloakable Fusion Reactor → আড়াল
ফিউশন চুল্লি · Fusion Reactor → ফিউশন চুল্লি · Fusion Power Plant →
ফিউশন বিদ্যুৎঘর · Geothermal Powerplant → ভূতাপ বিদ্যুৎঘর · Energy
Storage → শক্তির ভাণ্ডার · Metal Storage → ধাতুর ভাণ্ডার · Metal Extractor
→ ধাতু খনন · Metal Maker → ধাতু কারক · Moho Metal Maker → Moho ধাতু কারক ·
Moho Mine → Moho খনন · Floating Metal Maker → ভাসমান ধাতু কারক · Solar
Collector → সৌর সংগ্রাহক · Wind Generator → বায়ু জেনারেটর · Tidal
Generator → জোয়ার জেনারেটর · Underwater Energy Storage → পানির নিচের
শক্তির ভাণ্ডার · Underwater Fusion Plant → পানির নিচের ফিউশন বিদ্যুৎঘর ·
Underwater Metal Extractor → পানির নিচের ধাতু খনন · Underwater Metal
Storage → পানির নিচের ধাতুর ভাণ্ডার · Galactic Gate → ছায়াপথের ফটক ·
Dragon's Teeth → ড্রাগনের দাঁত · Floating Dragon's Teeth → ভাসমান ড্রাগনের
দাঁত · Fortification Wall → প্রাচীর · Alien Beacon → ভিনগ্রহের বাতিঘর ·
Implosion Device → অন্তর্মুখী বিস্ফোরণের যন্ত্র · Commander → কমান্ডার ·
Decoy Commander → নকল কমান্ডার · Light Laser Tower → হালকা লেজার টাওয়ার ·
Hydration Plant → পানির কারখানা · Fortitude Missile Defense → Fortitude
মিসাইল প্রতিরক্ষা · Resurrection Kbot → ফিরিয়ে আনা Kbot · Mobile
Artillery → চলন্ত কামান · Missile Frigate → মিসাইল ফ্রিগেট · Targeting
Facility → নিশানা কেন্দ্র · Area Mine → এলাকার মাইন · Focused Mine →
নিশানার মাইন · HE Area Mine → বিস্ফোরক মাইন · Precision Mine → নির্ভুল
মাইন · Nuclear Mine → পারমাণবিক মাইন · Defender - NS → ডিফেন্ডার - NS ·
Gaat Gun → Gaat কামান.

Nicknames, transliterated, not translated:

Albatross → অ্যালবাট্রস · Ambusher → অ্যামবুশার · Anaconda → অ্যানাকোন্ডা ·
Annihilator → অ্যানিহিলেটর · Archer → আর্চার · Atlas → অ্যাটলাস · Avenger
→ অ্যাভেঞ্জার · Bear → বিয়ার · Big Bertha → বিগ বার্থা · Brawler →
ব্রলার · Bulldog → বুলডগ · Buzzsaw → বাজস · Cobra → কোবরা · Colossus →
কলোসাস · Conqueror → কনকারার · Copperhead → কপারহেড · Crasher → ক্র্যাশার
· Crock → ক্রক · Crusader → ক্রুসেডার · Defender → ডিফেন্ডার · Deleter →
ডিলিটার · Diplomat → ডিপ্লোম্যাট · Dominator → ডমিনেটর · Doomsday Machine
→ ডুমসডে মেশিন · Eagle → ঈগল · Enforcer → এনফোর্সার · Envoy → এনভয় ·
Eraser → ইরেজার · Escort → এসকর্ট · Executioner → এক্সিকিউশনার · Fibber →
ফিবার · Fink → ফিঙ্ক · Flakker → ফ্ল্যাকার · Flash → ফ্ল্যাশ · Flea → ফ্লি
· Freaker → ফ্রিকার · Freedom Fighter → ফ্রিডম ফাইটার · Gimp → গিম্প ·
Goliath → গোলায়েথ · Guardian → গার্ডিয়ান · Hammer → হ্যামার · Hawk → হক
· Hedgehog → হেজহগ · Hive → হাইভ · Hulk → হাল্ক · Hunter → হান্টার ·
Hurricane → হারিকেন · Immolator → ইমোলেটর · Infiltrator → ইনফিলট্রেটর ·
Informer → ইনফর্মার · Instigator → ইনস্টিগেটর · Intimidator → ইন্টিমিডেটর
· Invader → ইনভেডার · Jammer → জ্যামার · Lancet → ল্যানসেট · Leveler →
লেভেলার · Leviathan → লেভিয়াথান · Lurker → লার্কার · Maverick → ম্যাভেরিক
· Millenium → মিলেনিয়াম · Neutron → নিউট্রন · Panther → প্যান্থার ·
Parasite → প্যারাসাইট · Peeper → পিপার · Peewee → পিউই · Pelican →
পেলিকান · Penetrator → পেনিট্রেটর · Phalanx → ফ্যালানক্স · Phantom →
ফ্যান্টম · Phoenix → ফিনিক্স · Piranha → পিরানহা · Protector → প্রোটেক্টর
· Pulverizer → পালভারাইজার · Punisher → পানিশার · Pyro → পাইরো · Raider →
রেইডার · Ranger → রেঞ্জার · Rapier → রেপিয়ার · Reaper → রিপার ·
Retaliator → রিটালিয়েটর · Roach → রোচ · Scarab → স্কারাব · Scorpion →
স্কর্পিয়ন · Scrubber → স্ক্রাবার · Sea Serpent → সি সার্পেন্ট · Seahawk →
সিহক · Searcher → সার্চার · Seer → সিয়ার · Sentinel → সেন্টিনেল · Shadow
→ শ্যাডো · Shark → শার্ক · Shooter → শুটার · Shredder → শ্রেডার · Silencer
→ সাইলেন্সার · Skeeter → স্কিটার · Skimmer → স্কিমার · Slasher → স্ল্যাশার
· Slinger → স্লিঙ্গার · Snake → স্নেক · Snapper → স্ন্যাপার · Spectre →
স্পেকটার · Spider → স্পাইডার · Spoiler → স্পয়লার · Stinger → স্টিঙ্গার ·
Stingray → স্টিংরে · Storm → স্টর্ম · Stumpy → স্টাম্পি · Stunner →
স্টানার · Sumo → সুমো · Swatter → সোয়াটার · The Can → দ্য ক্যান · Thud →
থাড · Thunder → থান্ডার · Thunderbolt → থান্ডারবোল্ট · Tiny → টাইনি ·
Titan → টাইটান · Toaster → টোস্টার · Tornado → টর্নেডো · Triton → ট্রাইটন
· Truck → ট্রাক · Turtle → টার্টল · Typhoon → টাইফুন · Valkyrie →
ভালকিরি · Vamp → ভ্যাম্প · Viper → ভাইপার · Voodoo → ভুডু · Voyeur →
ভয়েয়ার · Vulcan → ভালকান · Vulture → ভালচার · Warlord → ওয়ারলর্ড ·
Warrior → ওয়ারিয়র · Weasel → উইজেল · Wombat → ওমব্যাট · Zeus → জিউস ·
Zipper → জিপার.

`Ranger` is the missile ship, so `রেঞ্জার`, not the same word as
`Guardian` (`গার্ডিয়ান`). `Protector` is `প্রোটেক্টর`, not `ডিফেন্ডার`.

Description classes, used as the whole description:

Produces Aircraft → বিমান বানায় · Produces Kbots → Kbot বানায় ·
Produces Vehicles → যান বানায় · Produces Ships → জাহাজ বানায় · Produces
Energy → শক্তি বানায় · Produces Metal → ধাতু বানায় · Tech Level 1 → টেক
স্তর 1 · Tech Level 2 → টেক স্তর 2 · Extracts Metal → ধাতু তোলে · Converts
Energy into Metal → শক্তিকে ধাতু করে · Increases Energy Storage → শক্তির
ভাণ্ডার বাড়ায় · Increases Metal Storage → ধাতুর ভাণ্ডার বাড়ায় ·
Advanced Metal Extractor → উন্নত ধাতু খনন · Commander → কমান্ডার · Decoy
Commander → নকল কমান্ডার · Builds Hovercraft → হোভার বানায় · Builds
Seaplanes → জলবিমান বানায় · Builds Krogoth → Krogoth বানায় ·
Automatically repairs aircraft → নিজে বিমান সারায় · Creates Water → পানি
বানায় · Indigenous Lifeform → স্থানীয় জীব · Experimental Kbot →
পরীক্ষামূলক Kbot · SPY Kbot → গুপ্তচর Kbot · Infantry Kbot → পদাতিক Kbot ·
Medium Infantry Kbot → মাঝারি পদাতিক Kbot · Assault Kbot → আক্রমণ Kbot ·
Armored Assault Kbot → বর্ম আক্রমণ Kbot · Adv. Armored Assault Kbot →
উন্নত বর্ম আক্রমণ Kbot · Artillery Kbot → কামান Kbot · Fast Attack Kbot →
দ্রুত আক্রমণ Kbot · Fast Assist-Repair Kbot → দ্রুত সাহায্য Kbot · Fast
Light Scout Kbot → দ্রুত হালকা স্কাউট Kbot · Anti-Air Kbot → বিমানধ্বংসী
Kbot · Rocket Kbot → রকেট Kbot · Missile Kbot → মিসাইল Kbot · Heavy
Rocket Kbot → ভারী রকেট Kbot · Gun-slinging Kbot → বন্দুক Kbot · Mobile
Radar Kbot → চলন্ত রাডার Kbot · Mobile Mortar Kbot → চলন্ত মর্টার Kbot ·
Sniper Kbot → স্নাইপার Kbot · Resurrection Kbot → ফিরিয়ে আনা Kbot ·
Amphibious Kbot → উভচর Kbot · Scout → স্কাউট · Air Scout → আকাশ স্কাউট ·
Scout Ship → স্কাউট জাহাজ · Scout Hovercraft → স্কাউট হোভার · Fighter →
ফাইটার · Stealth Fighter → গোপন ফাইটার · Seaplane Fighter → জলবিমান
ফাইটার · Bomber → বোমারু · Strategic Bomber → কৌশলগত বোমারু · Torpedo
Bomber → টর্পেডো বোমারু · Gunship → গানশিপ · Air Transport → আকাশ পরিবহন ·
Radar Plane → রাডার বিমান · Airborne Sonar → আকাশ সোনার · Battleship →
যুদ্ধজাহাজ · Cruiser → ক্রুজার · Destroyer → ডেস্ট্রয়ার · Submarine →
ডুবোজাহাজ · Battle Sub → যুদ্ধ ডুবোজাহাজ · Submarine Killer → ডুবোজাহাজ
ঘাতক · Light Carrier → হালকা ক্যারিয়ার · Transport Ship → পরিবহন জাহাজ ·
Transport Hovercraft → পরিবহন হোভার · Ground Transport → স্থল পরিবহন ·
Missile Ship → মিসাইল জাহাজ · Anti-Air Ship → বিমানধ্বংসী জাহাজ · Anti-Air
Hovercraft → বিমানধ্বংসী হোভার · Anti-Air Flak Gun → বিমানধ্বংসী কামান ·
Hovertank → হোভার ট্যাংক · Amphibious Tank → উভচর ট্যাংক · Lightning Tank
→ বজ্র ট্যাংক · Assault Tank → আক্রমণ ট্যাংক · Fast Assault Tank → দ্রুত
আক্রমণ ট্যাংক · Medium Assault Tank → মাঝারি আক্রমণ ট্যাংক · Heavy Assault
Tank → ভারী আক্রমণ ট্যাংক · Very Heavy Assault Tank → অতি ভারী আক্রমণ
ট্যাংক · Riot Tank → দাঙ্গা ট্যাংক · Fast Attack Vehicle → দ্রুত আক্রমণ
যান · Spider Assault Vehicle → মাকড়সা আক্রমণ যান · Mine Layer Vehicle →
মাইন পাতার যান · Mobile Artillery → চলন্ত কামান · Mobile Flak Vehicle →
চলন্ত বিমানধ্বংসী যান · Mobile Missile Launcher → চলন্ত মিসাইল নিক্ষেপক ·
Mobile Missile Defense → চলন্ত মিসাইল প্রতিরক্ষা · Mobile Rocket Launcher
→ চলন্ত রকেট নিক্ষেপক · Mobile Energy Weapon → চলন্ত শক্তি অস্ত্র ·
Mobile Radar → চলন্ত রাডার · Mobile Radar Jammer → চলন্ত রাডার জ্যামার ·
Radar Jammer → রাডার জ্যামার · Radar Jammer Ship → রাডার জ্যামার জাহাজ ·
Sonar Jamming Sub → সোনার জ্যামার ডুবোজাহাজ · Hovercraft Rocket Launcher →
হোভার রকেট নিক্ষেপক · Missile Tower → মিসাইল টাওয়ার · Missile Tower -
Naval Series → মিসাইল টাওয়ার - নৌ সিরিজ · Missile Launcher → মিসাইল
নিক্ষেপক · Plasma Battery → প্লাজমা ব্যাটারি · Plasma Tower → প্লাজমা
টাওয়ার · Heavy Laser Tower → ভারী লেজার টাওয়ার · Light Laser Tower →
হালকা লেজার টাওয়ার · Floating Heavy Laser Tower → ভাসমান ভারী লেজার
টাওয়ার · Pop-up Heavy Cannon → ওঠা ভারী কামান · Pop-Up Heavy Laser → ওঠা
ভারী লেজার · Long Range Plasma Cannon → দূরপাল্লার প্লাজমা কামান · Rapid
Fire Plasma Cannon → দ্রুত প্লাজমা কামান · Energy Weapon / Energy weapon →
শক্তি অস্ত্র · EMP Missile Launcher → EMP মিসাইল নিক্ষেপক · Neutron
Missile Launcher → নিউট্রন মিসাইল নিক্ষেপক · Nuclear Missile Launcher →
পারমাণবিক মিসাইল নিক্ষেপক · Nuclear Mine → পারমাণবিক মাইন · Anti Missile
Defense System → মিসাইল প্রতিরক্ষা · Torpedo Launcher → টর্পেডো নিক্ষেপক
· Advanced Torpedo Launcher → উন্নত টর্পেডো নিক্ষেপক · Torpedo Seaplane →
টর্পেডো জলবিমান · Long Range Radar → দূরপাল্লার রাডার · Long Range Radar
Tower → দূরপাল্লার রাডার টাওয়ার · Extended Sonar → বর্ধিত সোনার · Locates
Water Units → পানির ইউনিট খুঁজে · Radar Tower → রাডার টাওয়ার · Sonar
Station → সোনার স্টেশন · Alien Beacon → ভিনগ্রহের বাতিঘর · Implosion
Device → অন্তর্মুখী বিস্ফোরণের যন্ত্র · Floating Dragon's Teeth → ভাসমান
ড্রাগনের দাঁত · Floating Metal Maker → ভাসমান ধাতু কারক · Perimeter
Defense → ঘের প্রতিরক্ষা · Metal Maker → ধাতু কারক · Space Teleporter →
মহাকাশ টেলিপোর্টার · Automatic Radar Targeting → স্বয়ংক্রিয় রাডার
নিশানা · Crawling Bomb → হামাগুড়ি বোমা · Low Damage, Med. Range Mine →
কম ক্ষতি, মাঝারি পাল্লা · Low Damage, Large Range Mine → কম ক্ষতি, বড়
পাল্লা · Med. Damage, Small Range Mine → মাঝারি ক্ষতি, ছোট পাল্লা · Med.
Damage, Med. Range Mine → মাঝারি ক্ষতি, মাঝারি পাল্লা · Med. Damage, Large
Range Mine → মাঝারি ক্ষতি, বড় পাল্লা · High Damage, Small Range Mine →
বেশি ক্ষতি, ছোট পাল্লা · High Damage, Med. Range Mine → বেশি ক্ষতি, মাঝারি
পাল্লা · High Damage, Large Range Mine → বেশি ক্ষতি, বড় পাল্লা.

## 9. Width

Bengali conjuncts are wider than a Latin letter. Captions on 3.1c's
fixed-size buttons stay to one short word, abbreviated with a full stop
when a button will not hold the word (`উন্নত` may become `উন্ন.`). The
attack button is `হামলা`. Prefer the shortest wording in this
file: `ফেরত` for "Previous Menu" when `আগের মেনু` will not fit, `একক`
for Single Player. Sentences in dialogs and hints may be as long as they
need to be. Unit descriptions stay about as short as the English.

## 10. Maps

In `translate.tdf`, a map description that starts with a size keeps the
English prefix exactly, spaces included (`18 x 18  `, and the odd
`11 x 10 map.  `). Translate only the words after that prefix. Translate
a descriptive map name. Leave an invented name spelled as in the English.
One leading `N: ` on a mission name stays exactly.

## 11. What this pack does not translate

Nothing in this glossary is left in English except the names section 3
and section 8 tell you to keep, key names, acronyms, and the product
names. ARM, CORE, Kbot, Moho, D-Gun, EMP and মোড are the pack's own
words, used as written here. সেভ, লোড as a verb of a saved game, and
গেম, are this pack's words (section 6), not English left behind.
