# Russian (ru) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the natural modern Russian a Russian RTS player would expect
(the Russian editions of StarCraft II, Warcraft III and Command & Conquer 3
/ Red Alert 3 are the model), and keep your own choice consistent within
your chunk.

Russian is its own language. The Ukrainian pack shows the tables' structure,
the context of a line and where a caption had to be shortened; it is never a
source of words. The letters і, ї, є and ґ never appear in Russian text, and
neither do Ukrainian words that happen to use shared letters (`мапа`, `обрати`,
`наразі`, `типові`, `підрозділ` and the like).

## 1. Voice and grammar

- The player is addressed as `вы`, lower case, and only when the sentence
  needs a subject at all. Most interface sentences need none.
- Instructions to the player: the formal imperative. "Try again later." →
  `Попробуйте ещё раз позже.`, "Choose the mod from the main menu." →
  `Выберите мод в главном меню.`, "Press any key" → `Нажмите любую клавишу`.
- Statements and hints: full sentences in the present or past, neutral
  register. "Settings were not saved." → `Настройки не сохранены.`,
  "The processor draws and scales the view." → `Процессор рисует и
  масштабирует изображение.`
- Confirmation questions: the infinitive. "Replace the game files?" →
  `Заменить файлы игры?`, "Remove {name}?" → `Удалить {name}?`
- Labels, buttons, menu items, settings names, headings: noun phrases or
  infinitives, as Russian interfaces write them. "Open folder" → `Открыть
  папку`, "Try again" → `Повторить`, "Mouse wheel zoom" → `Масштаб
  колесом мыши`, "Restore defaults" → `Сбросить`.
- Short status words: the short participle, neuter when there is no noun
  (`Установлено`, `Скачано`, `Не найдено`), a noun of action with an
  ellipsis for a process (`Загрузка…`, `Скачивание…`, `Ожидание…`),
  `Ошибка` for "Failed".
- Mission briefings and in-fiction messages (HQ talking to the Commander):
  a military register. Orders in the formal imperative (`Уничтожьте`,
  `Захватите`, `Удерживайте позицию`), reports in short declarative
  sentences. CORE's voice is colder and more mechanical than ARM's
  (`ВЫПОЛНЯЙТЕ НЕМЕДЛЕННО.`), as the English is.
- English capitals (OPEN FOLDER, SETTINGS) stay capitals in Russian:
  `ОТКРЫТЬ ПАПКУ`, `НАСТРОЙКИ`. Title Case English ("Load Game") becomes
  sentence case in Russian (`Загрузить игру`).
- Key names stay in Latin as the keyboard prints them: Shift, Ctrl, Alt,
  Esc, Escape, Enter, Tab, F1–F12, Space (`пробел` only in a sentence).
  Acronyms kept in Latin: TCP, IP, CD, DirectPlay, DLL, URL, GPU, CPU, HUD,
  fps, ID, AI only inside a file or key name. Otherwise `ИИ` for AI, `ЭМИ`
  for EMP, `ПРО` for anti-missile defence.
- Units of measure: `КБ`, `МБ`, `ГБ`, `мс`, `с`, `мин`; a space between the
  number and the unit (`2 ГБ`, `60 fps`). Sizes the engine fills in
  (`{size}`) are written by the engine as they are.
- Punctuation: Russian quotes `«…»`, inner quotes `„…“`. The dash in a
  sentence is `—` with spaces. Keep `…` or `...` as the English writes it.
  Never write `;` anywhere (a table value ends at `;`); use a full stop, a
  comma or a dash instead. A colon after a label stays a colon.
- `ё` is always written where it belongs, as the Russian editions of
  Blizzard's games write it: `ещё`, `всё`, `её`, `самолёт`, `манёвр`,
  `объём`, `включён`, `сохранён`, `отключён`, `приём`, `вертолёт`, `зелёный`,
  `чёрный`, `Орёл`, `Ёж`. Never an `е` where `ё` belongs.

## 2. Placeholders and numbers (hard rules)

- Every placeholder of the English stays, exactly as written: `{name}`,
  `{size}`, `%s`, `%d`, `%i`, `%.1f`, `%%`, `%1$s` and so on. Never
  translate, drop, add or respell one.
- printf conversions (`%s`, `%d`, …) stay in the same ORDER as in the
  English, because they are filled in that order. Reword the sentence around
  them. `{name}` slots may move freely.
- Every number written in digits in the English stays (`1/32`, `2x`,
  `3.1c`, `16x16`, `9 x 21`).
- Staged captions written with `|` (`Easy|Medium|Hard`): exactly the same
  number of stages, each translated in order.
- A slot's value has no case: the engine fills in a name in the nominative.
  Put the slot where the nominative is right: after a colon (`Установка:
  {name}`), after a noun that governs it (`мод {name}`, `карта {name}`,
  `версия {to}`), or as the subject (`{name} установлен`). Never decline
  around a slot (`{name}а`, `в {name}е`).
- A count's noun takes a form that depends on the number (1 карта, 2 карты,
  5 карт), which a slot does not know. Put the noun before the number with a
  colon (`Карт: {count}`, `Файлов: {n}`), or use an abbreviation that does
  not change (`{n} шт.`, `{n} мин`, `{n} с`), or a word that does not agree
  (`{count} из {total}`).
- Past tense after a slot has a gender the slot does not know. Prefer a
  passive with a neuter subject, a noun or a present tense: "{name} left the
  game" → `{name} покидает игру` or `{name}: выход из игры`, not `{name}
  покинул игру`.
- Two slots are filled with a word this pack translates in a case, not the
  nominative, so their sentences keep one shape: `{device}` is `устройстве`
  (or the platform's own name), always written `на этом {device}`, and
  `{cloud}` is `облаке` (or the service's name), always `в {cloud}`. A
  sentence that needs another case is rebuilt around them.
- A tab or a line break never goes into a translation.

## 3. Names kept as written

- **ARM** and **CORE**, the two sides: always Latin capitals, whatever the
  English case (Arm, Core, ARM, CORE). `войска CORE`, `Командир ARM`,
  `Кампания ARM`. They do not decline. As a bare subject they take a
  singular verb in the present or future (`CORE ждёт в засаде`, `ARM
  прибывает на Гидросс`). A past tense would need a gender they do not
  have: write `силы CORE построили`, `противник проник`, or a present
  tense instead.
- Open Annihilation, OA, Core Prime (the service and registry), Total
  Annihilation, Total Annihilation: The Core Contingency, Battle Tactics, Core
  Contingency, Cavedog Entertainment, GT Interactive, Steam, Steam Deck,
  Steam Input, GOG, Windows, macOS, Linux, DirectX, DirectPlay: as written,
  undeclined.
- File names, folder names, extensions, keys, URLs, version strings (`3.1c`,
  `oamod.yaml`, `totala1.hpi`, `.oalang`, `Mods`): as written.

## 4. Fiction: places and names

Invented names are transliterated into Cyrillic, by their English sound;
ordinary words are translated. Places do not take the ARM/CORE Latin rule:
`CORE Прайм` keeps CORE in Latin because it is the side's name.

| English | Russian |
|---|---|
| Core Prime (the CORE home planet, in the fiction) | CORE Прайм |
| Empyrrean | Эмпирриан |
| Galactic Gate / the Gate | Галактические врата / Врата |
| Thalassean | Таласиан |
| Tergiverse IV | Тергиверс IV |
| Barathrum | Баратрум |
| Rougpelt | Ругпелт |
| Aqueous Minor | Аквеус Минор |
| Aqueous Body 397 | водоём 397 |
| Aegus | Эгус |
| Dump (moon of Core Prime) | Свалка |
| Hydross | Гидросс |
| Lusch | Луш |
| Temblor | Темблор |
| Gelidus | Гелидус |
| Krogoth | Крогот |
| Central Consciousness | Центральное Сознание |
| Larab Harbor | гавань Лараб |
| Bromid Maze | Лабиринт Бромид |
| Brooban's Isle | остров Брубана |
| Motien Ramp | Насыпь Мотиен |
| Landown's Interface | Разлом Лэндауна |
| the Abutment | Контрфорс |
| Xantippe's Abyss | Бездна Ксантиппы |
| Slolam Pilago | Слолам Пилаго |
| Isle Parche | остров Парче |
| the Lost Isle | Затерянный остров |
| Vebreen Fleet / Vebreen Atoll | Вебринский флот / атолл Вебрин |
| Nigh Pilago | Най Пилаго |
| Cloud Isle | Облачный остров |
| Crustal 2, Crustal 12 (a world's crustal plates) | плита 2, плита 12 |
| Novespin IV / Novaspin IV (the English has both) | Новеспин IV / Новаспин IV |
| the alien beacon | инопланетный маяк |
| the contingent Core Commander | резервный Командир CORE |
| the Serpents of Hydross (Sea Serpent) | морские змеи |
| the Scorpions of Lusch | Скорпионы |
| the Cloud Fortress | Облачная крепость |
| the Gauntlet (a passage) | Огненный коридор |
| vermin (CORE's word for ARM) | нечисть |
| the Arm/Core war | война ARM и CORE |
| patterning (CORE's transfer of minds into machines) | перенос сознания |
| nanolathe, nanolathing | наносборщик, наносборка |

Briefing headings and set phrases:

| English | Russian |
|---|---|
| MISSION 1.0001ARME / Mission T01: | МИССИЯ 1.0001ARME / Миссия T01: |
| INFO FEED, INTEL FEED | СВОДКА |
| INTELL-TAP | РАЗВЕДДАННЫЕ |
| END / DO SO NOW. | КОНЕЦ / ВЫПОЛНЯЙТЕ НЕМЕДЛЕННО. |
| PRIORITY / SPECIAL PRIORITY / PRIORITY CRITICAL / Top Priority | ПРИОРИТЕТ / ОСОБЫЙ ПРИОРИТЕТ / ВЫСШИЙ ПРИОРИТЕТ / Высший приоритет |
| WARNING / Attention / Emergency! / Alert! | ВНИМАНИЕ / Внимание / Тревога! / Тревога! |
| Suggestions: / Battle Tactics: / Note: | Советы: / Боевая тактика: / Примечание: |
| To complete this mission you must … | Для выполнения миссии … (imperative) |

The Battle Tactics missions' places (Hanan, Lipar, Meraldi, Wayneston,
Vetes, Ansapp, Novespin IV, Ravenstein, Yrdac, Prasad, Destral II, Kerrap,
Arnen, Zedtopt, Guditha, Grantham, Krocark, Terseknos, Labrodorite, Kral,
Caranat, Retorb, Chimo, Rotrey, Yollets and the rest) are transliterated once
in `missions.tdf`; the briefings use the same spelling.

## 5. Game terms

| English | Russian |
|---|---|
| Commander | Командир (capitalised, as the English does) |
| unit | юнит (interface, help); подразделение, войска, силы (briefings) |
| building, structure | здание, сооружение |
| Kbot, KBot | К-бот (К-боты, К-ботов) |
| vehicle | машина; vehicles collectively: техника |
| tank | танк |
| aircraft, plane | самолёт; aircraft collectively: авиация |
| ship | корабль |
| submarine, sub | подлодка (подводная лодка in a sentence) |
| hovercraft | ховеркрафт |
| hovertank | ховертанк |
| seaplane | гидросамолёт |
| amphibious | амфибия (`К-бот-амфибия`, `танк-амфибия`) |
| builder (a unit that builds) | строитель |
| factory, plant | завод |
| lab (Kbot Lab) | лаборатория |
| shipyard | верфь |
| metal | металл |
| energy | энергия |
| resources | ресурсы |
| storage | запас (amount), хранилище (building) |
| income / production | доход / производство |
| metal extractor (mex) | экстрактор металла |
| metal maker | синтезатор металла |
| solar collector | солнечный коллектор |
| wind generator | ветрогенератор |
| tidal generator | приливный генератор |
| fusion reactor / fusion power plant | термоядерный реактор / термоядерная электростанция |
| geothermal | геотермальный |
| radar / sonar | радар / сонар |
| jammer (radar/sonar) | глушитель (глушитель радаров, глушитель сонаров) |
| line of sight, LOS | обзор |
| cloak, cloaked | маскировка, замаскирован |
| stealth | стелс |
| wreck, wreckage, corpse | обломки |
| feature (rocks, trees, wrecks on a map) | объект |
| laser / plasma | лазер / плазма (лазерный, плазменный) |
| missile / rocket | ракета / реактивный снаряд (rocket launcher: реактивная установка) |
| artillery | артиллерия |
| flak | зенитный огонь (flak gun: зенитная пушка) |
| torpedo / depth charge | торпеда / глубинная бомба |
| mine | мина |
| nuke, nuclear missile | ядерная ракета |
| anti-nuke, missile defense | ПРО, противоракетная оборона |
| EMP | ЭМИ |
| D-Gun (Disintegrator Gun) | D-пушка (дезинтегратор) |
| anti-air | ПВО, зенитный |
| ally, alliance | союзник, союз |
| enemy | противник (враг in speech and briefings) |
| team | команда |
| kills / losses | уничтожено / потери |
| veteran / veterancy | ветеран / опыт |
| victory / defeat | победа / поражение |
| paused | пауза |
| Tech Level 1 / 2 | Тех. уровень 1 / Тех. уровень 2 |
| Adv., Advanced (unit names) | Улучш. (written out, `Улучшенный`, where the English writes Advanced and the line has room) |
| build menu | меню строительства |
| control group | группа |
| selection, select | выделение, выделить |
| waypoint | путевая точка |
| queue | очередь |
| self-destruct | самоуничтожение |
| wall (Fortification Wall, DT) | стена; Dragon's Teeth: надолбы |

### Orders (buttons and their states; also used in touch controls)

| English | Russian |
|---|---|
| ATTACK | АТАКА |
| MOVE | ДВИЖЕНИЕ |
| STOP | СТОП |
| PATROL | ПАТРУЛЬ |
| DEFEND / GUARD | ОХРАНА |
| RECLAIM | УТИЛИЗ. (утилизация, утилизировать in text) |
| REPAIR | РЕМОНТ |
| CAPTURE | ЗАХВАТ |
| LOAD / UNLOAD (transports) | ПОГРУЗ. / ВЫГРУЗ. (погрузка / выгрузка in text) |
| ORDERS | ПРИКАЗЫ |
| BUILD | СТРОЙКА (строительство in text) |
| BLAST / D-GUN | D-ПУШКА |
| ASSIST | помощь, помогать |
| Fire orders: Hold Fire / Return Fire / Fire At Will | Режим огня: Не стрелять / Ответный огонь / Свободный огонь |
| Move orders: Hold Position / Maneuver / Roam | Режим движения: На месте / Манёвр / Свободно |
| On / Off (a unit) | Включено / Выключено (ВКЛ. / ВЫКЛ. on a small button) |
| Activate / Deactivate | Активировать / Деактивировать |
| Resurrect | Воскресить |
| Patrolling / Guarding (builders) | В патруле / На охране |

## 6. Menus and modes

| English | Russian |
|---|---|
| Single Player | Одиночная игра |
| Multiplayer | Сетевая игра |
| Campaign | Кампания |
| Mission | Миссия |
| Briefing | Брифинг |
| Skirmish | Схватка |
| Battle Room, Lounge (3.1c's game setup room) | Лобби |
| host / join | хост, создать игру / присоединиться |
| the Creator (3.1c's word for the host) | хост |
| player | игрок |
| computer player, AI | компьютер (3.1c's "Computer"), ИИ ("AI") |
| watcher, spectator / watch | зритель / наблюдать |
| replay | повтор |
| recorder, recording | запись |
| saved game / save / load | сохранённая игра / сохранить / загрузить |
| Options | Параметры |
| Settings | Настройки |
| Preferences | Настройки (3.1c's own menu) |
| Previous Menu / Back | Назад |
| Main menu / Game menu | Главное меню / Меню игры |
| Exit, Quit | Выйти, Выход |
| Exit to the system | Выход в систему |
| OK / Cancel / Done / Close / Apply | OK / Отмена / Готово / Закрыть / Применить |
| Retry, Try again | Повторить |
| Continue | Продолжить |
| Easy / Medium / Hard | Лёгкий / Средний / Сложный (agreeing with the noun) |
| Help | Справка |
| Narration / No Narration | Озвучка / Без голоса (the briefing's button is narrow) |
| Chat | Чат |
| Cheats | Читы, чит-коды |
| game speed | скорость игры |
| Sound / Music / Volume / Movies | Звук / Музыка / Громкость / Видеоролики |
| Credits | Авторы |
| Intro | Заставка |

## 7. Open Annihilation's interface

| English | Russian |
|---|---|
| Library | Библиотека |
| mod | мод |
| mod profile | профиль мода |
| hacks, standard hacks (engine behaviour a mod switches on) | доработки, стандартные доработки |
| map / map pack | карта / набор карт |
| language pack | языковой пакет |
| expansion | дополнение |
| base game | основная игра |
| registry (a server listing packages) | реестр |
| catalogue | каталог |
| download (verb / noun) | скачать / скачивание; Settings › Downloads: Загрузки |
| install / update / remove / delete | установить / обновить / удалить / удалить |
| version / revision | версия / ревизия |
| roll back | откатить |
| folder / file / archive | папка / файл / архив |
| game files / game folder / game archives | файлы игры / папка игры / архивы игры |
| device | устройство |
| free (space) | свободно (`{size} free` → `Свободно: {size}`) |
| screen / window / full screen | экран / окно / полноэкранный режим |
| zoom, zoom in / out | масштаб, приблизить / отдалить |
| graphics | графика |
| hardware acceleration | аппаратное ускорение |
| vertical sync | вертикальная синхронизация |
| anti-aliasing | сглаживание |
| frame rate | частота кадров |
| resolution | разрешение |
| modern fonts | современные шрифты |
| font / text size | шрифт / размер текста |
| controller / trackpad / stick / gyro / D-pad | контроллер / трекпад / стик / гироскоп / крестовина |
| touch | сенсорное управление |
| haptics | вибрация |
| pointer | указатель |
| Developer Mode | режим разработчика |
| Language / System default | Язык / Как в системе |
| snap (click snap) | привязка |
| the host (of a shared game) | хост |
| shared game / network play | сетевая игра |
| HUD | HUD |
| Unicode | Юникод |
| install ID | ID установки |
| demo | демоверсия |
| the engine | движок |
| film (a recorded game) | запись |
| screenshot | снимок экрана |

## 8. Unit names

Generic names are translated. Proper names that are ordinary English words
are translated as Russian names (Archer → Лучник, Zipper → Молния); personal
names and invented words are transliterated (Jeffy → Джеффи, Podger →
Поджер). Use these exactly, in units.tdf and wherever a unit is named
(briefings, help, messages). A name declines in a sentence as an ordinary
Russian noun (`уничтожьте Молота`), except in a list or after a colon. A
name standing alone is written bare and declines, animate like a soldier
(`захватите Зевса`, `не потеряйте Доминаторов`); a name after its class
noun is quoted and does not decline (`эсминцы «Крестоносец»`, `пушку
«Берта»`, `транспорт «Атлас»`).

Generic: Adv. Aircraft Plant Улучш. авиазавод · Adv. Construction Aircraft
Улучш. строительный самолёт · Adv. Construction Kbot Улучш. строительный
К-бот · Advanced Construction Sub Улучш. строительная подлодка · Adv.
Construction Vehicle Улучш. строительная машина · Adv. Kbot Lab Улучш.
лаборатория К-ботов · Adv. Shipyard Улучш. верфь · Adv. Vehicle Plant Улучш.
завод техники · Advanced Radar Tower Улучшенная радарная вышка · Advanced
Sonar Station Улучшенная сонарная станция · Advanced Torpedo Launcher
Улучшенный торпедный аппарат · Air Repair Pad Ремонтная площадка · Aircraft
Plant Авиазавод · Alien Beacon Инопланетный маяк · Area Mine Площадная мина ·
Cloakable Fusion Reactor Маскируемый термоядерный реактор · Commander
Командир · Construction Aircraft Строительный самолёт · Construction
Hovercraft Строительный ховеркрафт · Construction Kbot / KBot Строительный
К-бот · Construction Seaplane Строительный гидросамолёт · Construction Ship
Строительный корабль · Construction Vehicle Строительная машина · Decoy
Commander Командир-приманка · Dragon's Teeth Надолбы · Energy Storage
Хранилище энергии · Floating Dragon's Teeth Плавучие надолбы · Floating Metal
Maker Плавучий синтезатор металла · Focused Mine Фокусированная мина ·
Fortification Wall Оборонительная стена · Fortitude Missile Defense ПРО
«Стойкость» · Fusion Power Plant Термоядерная электростанция · Fusion Reactor
Термоядерный реактор · Gaat Gun Гаат-пушка · Galactic Gate Галактические
врата · Geothermal Powerplant Геотермальная станция · HE Area Mine Фугасная
площадная мина · Hovercraft Platform Платформа ховеркрафтов · Hydration Plant
Станция гидратации · Implosion Device Имплозивное устройство · Kbot Lab
Лаборатория К-ботов · Krogoth Gantry Ангар Крогота · Light Laser Tower Лёгкая
лазерная башня · L.L.T. Л.Л.Б. · Metal Extractor Экстрактор металла · Metal
Maker Синтезатор металла · Metal Storage Хранилище металла · Missile Frigate
Ракетный фрегат · Mobile Artillery Мобильная артиллерия · Moho Metal Maker
Мохо-синтезатор металла · Moho Mine Мохо-шахта · Nuclear Mine Ядерная мина ·
Precision Mine Высокоточная мина · Radar Tower Радарная вышка · Resurrection
Kbot К-бот воскрешения · Seaplane Platform Платформа гидросамолётов ·
Shipyard Верфь · Solar Collector Солнечный коллектор · Sonar Station Сонарная
станция · Targeting Facility Центр наведения · Tidal Generator Приливный
генератор · Torpedo Launcher Торпедный аппарат · Underwater Energy Storage
Подводное хранилище энергии · Underwater Fusion Plant Подводная термоядерная
станция · Underwater Metal Extractor Подводный экстрактор металла ·
Underwater Metal Storage Подводное хранилище металла · Vehicle Plant Завод
техники · Wind Generator Ветрогенератор · Defender - NS Защитник - МС ·
M-104, M-209, M-303, M-420, M-515, M-610 as written · FARK FARK · A.K. А.К.

Proper, translated (ordinary words): Albatross Альбатрос · Ambusher Засада ·
Anaconda Анаконда · Annihilator Аннигилятор · Archer Лучник · Atlas Атлас ·
Avenger Мститель · Bear Медведь · Big Bertha Большая Берта · Brawler Задира ·
Bulldog Бульдог · Buzzsaw Циркулярка · Cobra Кобра · Colossus Колосс ·
Conqueror Завоеватель · Copperhead Медянка · Crasher Крушитель · Crock
Крокодил · Crusader Крестоносец · Defender Защитник · Deleter Ликвидатор ·
Diplomat Дипломат · Dominator Доминатор · Doomsday Machine Машина Судного дня
· Eagle Орёл · Enforcer Силовик · Envoy Посланник · Eraser Ластик · Escort
Эскорт · Executioner Палач · Fibber Враль · Fink Стукач · Flakker Зенитчик ·
Flash Вспышка · Flea Блоха · Freaker Псих · Freedom Fighter Борец за свободу
· Gimp Хромой · Goliath Голиаф · Guardian Страж · Hammer Молот · Hawk Ястреб
· Hedgehog Ёж · Hive Улей · Hulk Махина · Hunter Охотник · Hurricane Ураган ·
Immolator Испепелитель · Infiltrator Лазутчик · Informer Информатор ·
Instigator Подстрекатель · Intimidator Устрашитель · Invader Захватчик ·
Jammer Глушилка · Lancet Ланцет · Leveler Каток · Leviathan Левиафан · Lurker
Скрытень · Maverick Сорвиголова · Millenium Тысячелетие · Neutron Нейтрон ·
Panther Пантера · Parasite Паразит · Peeper Глазок · Peewee Малыш · Pelican
Пеликан · Penetrator Пробойник · Phalanx Фаланга · Phantom Фантом · Phoenix
Феникс · Piranha Пиранья · Protector Хранитель · Pulverizer Дробилка ·
Punisher Каратель · Pyro Поджигатель · Raider Рейдер · Ranger Рейнджер ·
Rapier Рапира · Reaper Жнец · Retaliator Возмездие · Roach Таракан · Samson
Самсон · Scarab Скарабей · Scorpion Скорпион · Scrubber Чистильщик · Sea
Serpent Морской змей · Seahawk Морской ястреб · Searcher Искатель · Seer
Провидец · Sentinel Часовой · Shadow Тень · Shark Акула · Shooter Стрелок ·
Shredder Шредер · Silencer Усмиритель · Skeeter Комар · Skimmer Глиссер ·
Slasher Рубака · Slinger Пращник · Snake Змея · Snapper Кусака · Spectre
Призрак · Spider Паук · Spoiler Вредитель · Stinger Жало · Stingray Скат ·
Storm Шторм · Stumpy Коротышка · Stunner Шокер · Sumo Сумо · Swatter
Мухобойка · The Can Жестянка · Thud Бух · Thunder Гром · Thunderbolt
Громовержец · Tiny Кроха · Titan Титан · Toaster Тостер · Tornado Торнадо ·
Triton Тритон · Truck Грузовик · Turtle Черепаха · Typhoon Тайфун · Valkyrie
Валькирия · Vamp Вампир · Viper Гадюка · Voodoo Вуду · Voyeur Соглядатай ·
Vulcan Вулкан · Vulture Стервятник · Warlord Полководец · Warrior Воин ·
Weasel Ласка · Wombat Вомбат · Zeus Зевс · Zipper Молния · Krogoth Крогот.

Proper, transliterated (personal names and invented words): Fido Фидо ·
Jeffy Джеффи · Jethro Джетро · Luger Люгер · Marky Марки · Merl Мерл · Morty
Морти · Nixer Никсер · Podger Поджер · Rocko Роко.

Unit classes in descriptions: Bomber Бомбардировщик · Fighter Истребитель ·
Stealth Fighter Истребитель-невидимка · Strategic Bomber Стратегический
бомбардировщик · Gunship Штурмовик · Scout / Air Scout Разведчик /
Воздушный разведчик · Radar Plane Самолёт-радар · Transport / Air Transport
Транспорт / Воздушный транспорт · Battleship Линкор · Cruiser Крейсер ·
Destroyer Эсминец · Submarine Подлодка · Battle Sub Боевая подлодка ·
Submarine Killer Охотник за подлодками · (Light) Carrier (Лёгкий) авианосец ·
Light / Medium / Heavy Tank Лёгкий / Средний / Тяжёлый танк · Assault Tank
Штурмовой танк · Amphibious Tank Танк-амфибия · Infantry Kbot Пехотный К-бот
· Assault Kbot Штурмовой К-бот · Artillery Kbot Артиллерийский К-бот ·
Missile Tower Ракетная башня · Plasma Battery Плазменная батарея · Plasma
Cannon Плазменная пушка · Energy Weapon Энергетическое оружие · Mine Layer
Vehicle Минный заградитель · Radar Jammer Глушитель радаров · Mobile Radar
Мобильный радар · Produces Aircraft / Kbots / Vehicles / Ships Производит
самолёты / К-ботов / технику / корабли · Produces Energy Производит энергию ·
Produces Metal Производит металл · Increases Energy Storage Увеличивает запас
энергии · Increases Metal Storage Увеличивает запас металла · Indigenous
Lifeform Местная форма жизни · Crawling Bomb Ползучая бомба.

## 9. Width

Russian runs longer than English, about as long as the Ukrainian. The
engine's text-fit check at 640x480 is the hard gate for Open Annihilation's
own screens. Captions on 3.1c's fixed-size buttons (its menus' buttons,
tabs, short labels) must be no longer than the Ukrainian pack's caption of
the same button; where the Ukrainian shortened or abbreviated, shorten the
Russian the same way, abbreviating with a full stop (`Улучш.`, `Макс.`,
`Тех.`, `Стр.`). Prefer the shortest natural wording for a button: `Начать`
over `Начать игру` when the screen already says "game", `Назад` for
"Previous Menu". Sentences in dialogs and hints may be as long as they need
to be.

## 10. Keys

One word for each idea, in the key editor, the overlay, Settings › Controls,
Settings › Accessibility, Library › Keys and the install question. Sentence
case in a label (`Раскладка клавиш`), as the rest of this file.

| English | Russian |
|---|---|
| key layout | раскладка клавиш |
| key editor | редактор клавиш |
| action (a binding; also where English still says "command" for one) | действие |
| changes of your own | свои изменения |
| clash | конфликт |
| latch / latched | закрепить / закреплено |
| latchable (the filter) | Закрепить |
| unbound (the filter) | Пусто |
| letter (of a key) | буква |
| place (of a key) | позиция |
| hold to confirm | Держать, подтверждая |

Named keys stay Latin where the keyboard prints them: Shift, Ctrl, Alt, Esc,
Escape, Enter, Tab, Space, Backspace, Delete, Insert, Home, End, Page Up,
Page Down, F1–F12, Win. In a sentence, Space is `пробел`. Arrows are
`Стрелка вверх`, `Стрелка вниз`, `Стрелка влево`, `Стрелка вправо`. Numpad
is `Цифровой блок` (`Numpad add` → `Цифровой блок +`). Mouse buttons:
`Левая кнопка`, `Правая кнопка`, `Средняя кнопка`. Wheel: `Колесо вверх`,
`Колесо вниз`. The order-wheel chips abbreviate the held button, `Сред.`
and `Прав.`. Settings › Accessibility is `Доступность` (heading
`ДОСТУПНОСТЬ`).
