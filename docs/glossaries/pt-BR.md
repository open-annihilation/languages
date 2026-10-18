# Brazilian Portuguese (pt-BR) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the modern Brazilian Portuguese a Brazilian RTS player would
expect (the Brazilian editions of StarCraft, Age of Empires and Command &
Conquer, and the Brazilian interfaces of today's games and operating
systems are the model), and keep your own choice consistent within your
chunk. The spelling is the 2009 orthographic agreement's, as Brazil writes
it (`ação`, `ideia`, `autodestruição`, `antiaéreo`, `contra-ataque`).

## 1. Voice and grammar

- Statements and hints (a full sentence): the present indicative, neutral
  and plain. "Settings were not saved." → `As configurações não foram
  salvas.` "The processor draws and scales the view." → `O processador
  desenha e dimensiona a imagem.`
- Instructions to the player: the impersonal imperative of Brazilian
  interfaces, the third person singular (`Clique`, `Selecione`, `Escolha`,
  `Tente novamente mais tarde.`). Never `tu` and its forms (`clica`,
  `seleciona`, `teu`). Leave the subject out; write `você` only when a
  sentence cannot do without it. `seu`, `sua` are the player's.
- Confirmation questions: `Deseja` and an infinitive. "Replace the game
  files?" → `Deseja substituir os arquivos do jogo?` A short question that
  is a dialog's title may be a bare infinitive: `Sair do jogo?`
- Labels, buttons, menu items, setting names and headings: noun phrases
  or infinitives, no full stop, in sentence case (only the first word and
  names capitalized). "Open folder" → `Abrir pasta`, "Try again" →
  `Tentar novamente`, "Mouse wheel zoom" → `Zoom com a roda do mouse`.
  Where the English is in capitals, so is the Portuguese (`OPÇÕES`,
  `SAIR`).
- Short status words: the participle or the gerund, agreeing with what it
  describes, masculine singular when nothing says otherwise. "Installed"
  → `Instalado`, "Downloading" → `Baixando`, "Not found" → `Não
  encontrado`, "Failed" → `Falhou`, "Waiting" → `Aguardando`, "Ready" →
  `Pronto`, "Off" / "On" → `Desligado` / `Ligado`.
- Mission briefings and in-fiction messages (HQ talking to the Commander):
  a crisp military register. Orders in the imperative (`Leve suas unidades
  até o Portal e proteja-o.`), statements in the indicative, the
  Commander addressed as `Comandante`, the side's own forces as `nossas
  forças`. No slang, no exclamations the English does not have.
- The briefings' fixed words: `MISSION` → `MISSÃO`, `PRIORITY` →
  `PRIORIDADE`, `PRIORITY CRITICAL` → `PRIORIDADE CRÍTICA`, `INFO FEED` →
  `INFORMAÇÕES`, `INTEL FEED` → `INFORMAÇÕES DA INTELIGÊNCIA`, `END` →
  `FIM`, `WARNING` → `ATENÇÃO`, `Suggestions:` → `Sugestões:`, `Battle
  Tactics:` → `Táticas de batalha:`, `Mission T01: …` → `Missão T01: …`
  with the missions table's name. CORE's own briefings speak as a machine:
  `INTELL-TAP:` → `GRAMPO-INTEL:`, `DO SO NOW.` → `EXECUTE AGORA.`, and
  `Arm vermin` → `a praga ARM`.
- Units' spoken lines and the message log: short and clipped, as a
  soldier speaks on the radio.
- Keep Latin acronyms and key names as written: SHIFT, CTRL, ALT, ESC,
  Esc, TCP, IP, CD, DirectPlay, GPU, fps, KB, MB, GB, F1-F12.
- Punctuation: Portuguese spacing (no space before `: ? !`). Quotes are
  straight `"` and `'`, never “ ” or « », which the game's fonts lack.
  Keep `…`, `·`, `→`, `›`, `✓`, `✕`, `—` only where the English has them.
  Never write `;` (the table format ends a value at `;`): use a comma, a
  full stop or a dash. Never write `//`.
- Characters: the pack is drawn in the modern fonts (3.1c's menu fonts lack
  `ã`, `õ` and the capitals `Ã Õ Ç Â Ê Ô À`), but its own words keep to
  Windows-1252 all the same; only the signs the English itself uses (`✓`,
  `✕`, `→`) go beyond it. The letters the language needs are `á à â ã é ê
  í ó ô õ ú ü ç` and their capitals. Do not use `ª` or `º` (ordinals):
  write the number as a word or recast.

## 2. Placeholders and numbers (hard rules)

- Every placeholder of the English stays, exactly as written: `{name}`,
  `{size}`, `%s`, `%d`, `%i`, `%.1f`, `%%`, `%1$s` and so on. Never
  translate, drop, add or respell one.
- printf conversions (`%s`, `%d`, …) stay in the ORDER of the English,
  since they are filled in that order. Reword the sentence if needed.
  `{name}` slots may move.
- Every number written in digits stays (`1/32`, `2x`, `3.1c`, `16x16`,
  `9 x 21`). Decimal points stay as the English writes them: the engine
  fills its own values in that form.
- Staged captions written with `|` (`Easy|Medium|Hard`) keep exactly the
  same number of stages, each translated in order.
- Gender and number after a slot are unknown. Do not put an article or a
  contracted preposition (`do`, `da`, `no`, `na`, `ao`) straight before a
  slot whose gender is not known: name the thing first (`o mapa {map}`,
  `o pacote {pack}`, `de {name}`), or recast. After a count, write the
  plural (`{count} arquivos`), as the English does.
- A tab or line break never goes into a translation.

## 3. Names kept as written

- **ARM** and **CORE**, the two sides: always Latin capitals, whatever the
  English case (Arm, Core, ARM, CORE). Both are masculine, as `o
  exército`: `o ARM`, `o CORE`, `do CORE`, `contra o ARM`. Used as an
  adjective they take no article and do not agree: `unidades CORE`,
  `forças ARM`, `Comandante ARM`, `Campanha CORE`.
- Open Annihilation, OA, Core Prime (the service and registry), Total
  Annihilation, Total Annihilation: The Core Contingency, Total
  Annihilation: Battle Tactics, Cavedog Entertainment, GT Interactive,
  Steam, GOG, Windows, macOS, Linux, DirectX, DirectPlay: as written.
- File names, folder names, extensions, keys, URLs and version strings
  (`3.1c`, `oamod.yaml`, `totala1.hpi`, `.oalang`): as written.

## 4. Fiction: places and names

Invented names stay as written; ordinary words are translated.

| English | Portuguese |
|---|---|
| Core Prime (the CORE home planet, in the fiction) | Core Prime |
| Empyrrean | Empyrrean |
| Galactic Gate / the Gate | Portal Galáctico / o Portal |
| Thalassean | Thalassean |
| Tergiverse IV | Tergiverse IV |
| Barathrum | Barathrum |
| Rougpelt | Rougpelt |
| Aqueous Minor | Aqueous Minor |
| Aegus | Aegus |
| Dump (moon of Core Prime) | Dump |
| Hydross | Hydross |
| Lusch | Lusch |
| Temblor | Temblor |
| Gelidus | Gelidus |
| Krogoth | Krogoth |
| Central Consciousness | Consciência Central |
| Larab Harbor | Porto de Larab |
| Bromid Maze | Labirinto de Bromid |
| Brooban's Isle | Ilha de Brooban |
| Motien Ramp | Rampa de Motien |
| Xantippe's Abyss | Abismo de Xantippe |
| Slolam Pilago | Slolam Pilago |
| Isle Parche | Ilha Parche |
| Vebreen Fleet | Frota Vebreen |
| the Arm/Core war | a guerra entre ARM e CORE |
| patterning (CORE's transfer of minds into machines) | transferência de padrão |
| Com Pattern (a mission's name) | Padrão Com |
| nanolathe, nanolathing | nanotorno, nanotorneamento |
| homeworld | planeta natal |
| Crustal 8 (Barathrum's plates) | Crosta 8 |
| the Serpent, the Scorpion (indigenous life-forms, units Sea Serpent and Scorpion) | o Serpent, o Scorpion (plural Serpents, Scorpions), kept as unit names |
| the beacon (Alien Beacon) / the implosion device | o sinalizador / o dispositivo de implosão |
| the contingent Core Commander | o Comandante CORE da contingência |

## 5. Game terms

| English | Portuguese |
|---|---|
| Commander | Comandante |
| unit | unidade |
| building, structure | construção, estrutura |
| Kbot, KBot, kbot | Kbot (masc., plural Kbots) |
| vehicle | veículo |
| tank | tanque |
| aircraft / plane | aeronave / avião |
| ship | navio |
| submarine, sub | submarino |
| hovercraft | hovercraft (masc., plural hovercrafts) |
| seaplane | hidroavião |
| amphibious | anfíbio |
| builder (a unit that builds) | construtor, unidade de construção |
| factory, plant | fábrica |
| lab (Kbot Lab) | laboratório |
| shipyard | estaleiro |
| metal | metal |
| energy | energia |
| resources | recursos |
| storage | armazenamento (amount), depósito (building) |
| income / production | renda / produção |
| metal extractor (mex) | extrator de metal |
| metal maker | conversor de metal |
| solar collector | coletor solar |
| wind generator | gerador eólico |
| tidal generator | gerador maremotriz |
| fusion reactor / fusion power plant | reator de fusão / usina de fusão |
| geothermal | geotérmico |
| radar | radar |
| sonar | sonar |
| jammer (radar/sonar) | bloqueador (bloqueador de radar, de sonar) |
| line of sight, LOS | linha de visão |
| cloak, cloaked | camuflagem, camuflado |
| stealth | furtivo |
| wreck, wreckage, corpse | destroços |
| feature (rocks, trees, wrecks on a map) | elemento, elementos do mapa |
| laser | laser |
| plasma | plasma |
| missile / rocket | míssil / foguete |
| artillery | artilharia |
| flak | antiaéreo, flak |
| torpedo | torpedo |
| depth charge | carga de profundidade |
| mine (land / sea) | mina / mina naval |
| nuke, nuclear missile | míssil nuclear |
| anti-nuke, missile defense | defesa antimísseis |
| EMP | EMP |
| D-Gun (Disintegrator Gun) | D-Gun (Canhão Desintegrador) |
| anti-air | antiaéreo |
| ally, alliance | aliado, aliança |
| enemy | inimigo |
| team | equipe |
| kills / losses | abates / perdas |
| veteran / veterancy | veterano / experiência |
| victory / defeat | vitória / derrota |
| paused | pausado (the title: PAUSA) |
| Tech Level 1 / 2 | Nível tecnológico 1 / 2 |
| Adv., Advanced (unit names) | Avançado, Avançada (after the noun) |
| build menu | menu de construção |
| control group (select groups) | grupo |
| selection, select | seleção, selecionar |
| waypoint | ponto de passagem |
| queue | fila |
| self-destruct | autodestruição |
| map | mapa |
| match, game (one played) | partida |
| the game (the program) | o jogo |

### Orders (buttons and their states; also used in touch controls)

| English | Portuguese |
|---|---|
| ATTACK | ATACAR |
| MOVE | MOVER |
| STOP | PARAR |
| PATROL | PATRULHAR |
| DEFEND / GUARD | DEFENDER / proteger (in sentences) |
| RECLAIM | RECICLAR |
| REPAIR | REPARAR |
| CAPTURE | CAPTURAR |
| LOAD / UNLOAD (transports) | CARREGAR / DESCARREGAR |
| ORDERS | ORDENS |
| BUILD | CONSTRUIR |
| BLAST / D-GUN | D-GUN |
| ASSIST | AJUDAR |
| Fire orders: Hold Fire / Return Fire / Fire At Will | Ordens de fogo: Cessar fogo / Revidar / Fogo à vontade |
| Move orders: Hold Position / Maneuver / Roam | Ordens de movimento: Manter posição / Manobrar / Vagar |
| On / Off (a unit) | Ligado / Desligado |
| Activate / Deactivate | Ativar / Desativar |
| Cloaked / Visible | Camuflado / Visível |
| Resurrect | Ressuscitar |
| arm (an order, on touch and controller rings) / ARM ORDER | preparar (a ordem) / PREPARAR |
| QUEUE / ADD / FORCE / CLEAR / STORE (touch) | FILA / ADICIONAR / FORÇAR / LIMPAR / GUARDAR |
| Patrolling / Guarding (builders) | Patrulhando / Protegendo |

## 6. Menus and modes

| English | Portuguese |
|---|---|
| Single Player | Um jogador |
| Multiplayer | Multijogador |
| Campaign | Campanha |
| Mission | Missão |
| Briefing | Briefing |
| Skirmish | Escaramuça |
| Battle Room | Sala de batalha |
| Lobby / Lounge | Lobby |
| host / join | criar (a game) / entrar; the host: o anfitrião |
| player | jogador |
| computer player, AI | Computador (3.1c's "Computer"), IA ("AI") |
| watcher, spectator / watch | espectador / assistir |
| replay | replay |
| recorder, recording | gravador, gravação |
| saved game / save / load | jogo salvo / salvar / carregar |
| Options | Opções |
| Settings | Configurações |
| Preferences | Preferências |
| Previous Menu / Back | Menu anterior / Voltar |
| Main menu / Game menu | Menu principal / Menu do jogo |
| Exit, Quit | Sair |
| Exit to the system | Sair para o sistema |
| OK / Cancel / Done / Close / Apply | OK / Cancelar / Concluído / Fechar / Aplicar |
| Retry, Try again | Tentar novamente |
| Continue / Resume | Continuar / Continuar (the game menu's button is too narrow for Voltar ao jogo) |
| Easy / Medium / Hard | Fácil / Médio / Difícil |
| Help | Ajuda |
| Chat | Chat |
| Cheats | Trapaças |
| game speed | velocidade do jogo |
| Sound / Music / Volume / Movies | Som / Música / Volume / Vídeos |
| Credits | Créditos |
| Intro | Introdução |
| Restrictions | Restrições |
| SINGLE / MULTI / INTRO / EXIT (title screen) | UM JOGADOR / MULTIJOGADOR / ABERTURA / SAIR |
| On / Off (3.1c's sound toggles) | Sim / Não, as 3.1c's French and Italian say Oui and Sì |
| the game menu's Settings (OA settings) | Config. |
| Wind Speed / Gravity (briefing) | Vento / Gravidade |

## 7. Open Annihilation's interface

| English | Portuguese |
|---|---|
| Library | Biblioteca |
| mod | mod (masc., plural mods) |
| mod profile | perfil do mod |
| hacks, standard hacks (engine behaviour a mod switches on) | ajustes, ajustes padrão |
| map / map pack | mapa / pacote de mapas |
| language pack | pacote de idioma |
| package | pacote |
| expansion | expansão |
| base game | jogo base |
| registry (a server listing packages) | repositório |
| catalogue | catálogo |
| download (verb / noun) / install / update / remove / delete | baixar / download / instalar / atualizar, atualização / remover / excluir |
| version / revision | versão / revisão |
| roll back | reverter |
| folder / file | pasta / arquivo |
| archive (an .hpi, .ufo, .ccx or .gp3 file; a zip) | arquivo compactado |
| game files / game folder / game archives | arquivos do jogo / pasta do jogo / arquivos compactados do jogo |
| device | dispositivo |
| free (space) | livre (`{size} free` → `{size} livres`) |
| screen / window / full screen | tela / janela / tela cheia |
| zoom, zoom in / out | zoom, aproximar / afastar |
| graphics | gráficos |
| hardware acceleration | aceleração por hardware |
| vertical sync | sincronização vertical |
| anti-aliasing | antisserrilhamento |
| frame rate | taxa de quadros |
| resolution | resolução |
| modern fonts | fontes modernas |
| font / text size | fonte / tamanho do texto |
| controller / trackpad / stick / gyro / D-pad | controle / trackpad / analógico / giroscópio / direcional |
| touch | toque |
| haptics | vibração |
| pointer | ponteiro |
| Developer Mode | Modo desenvolvedor |
| Language / System default | Idioma / Padrão do sistema |
| snap (click snap) | encaixe, encaixar (the click is drawn to the nearest target) |
| the host (of a shared game) | anfitrião |
| shared game / network play | partida em rede / jogo em rede |
| HUD | HUD |
| Unicode | Unicode |
| install ID | ID de instalação |
| demo | demo |
| content | conteúdo |
| key (keyboard) / key binding | tecla / atalho |

## 8. Unit names

Proper names stay in English, as written, as Brazilian editions of RTS
games keep them: they are the units' code names, and a player recognizes
them across languages and mods. Generic names, which say what a unit or
building is, are translated. Use these exactly, in units.tdf and wherever
a unit is named (briefings, help, messages). Names are written with their
main words capitalized; descriptions in sentence case.

Generic: Adv. Aircraft Plant Fábrica de Aeronaves Avançada · Adv.
Construction Aircraft Aeronave de Construção Avançada · Adv. Construction
Kbot Kbot de Construção Avançado · Advanced Construction Sub Submarino de
Construção Avançado · Adv. Construction Vehicle Veículo de Construção
Avançado · Adv. Kbot Lab Laboratório de Kbots Avançado · Aircraft Plant
Fábrica de Aeronaves · Advanced Radar Tower Torre de Radar Avançada ·
Advanced Sonar Station Estação de Sonar Avançada · Air Repair Pad
Plataforma de Reparo Aéreo · Adv. Shipyard Estaleiro Avançado · Advanced
Torpedo Launcher Lançador de Torpedos Avançado · Adv. Vehicle Plant Fábrica
de Veículos Avançada · Alien Beacon Sinalizador Alienígena · Construction
Aircraft Aeronave de Construção · Construction Hovercraft Hovercraft de
Construção · Construction Kbot / KBot Kbot de Construção · Cloakable Fusion
Reactor Reator de Fusão Camuflável · Commander Comandante · Construction
Ship Navio de Construção · Construction Seaplane Hidroavião de Construção ·
Construction Vehicle Veículo de Construção · Decoy Commander Comandante
Isca · Implosion Device Dispositivo de Implosão · Dragon's Teeth Dentes de
Dragão · Floating Dragon's Teeth Dentes de Dragão Flutuantes · Energy
Storage Depósito de Energia · Floating Metal Maker Conversor de Metal
Flutuante · Fortification Wall Muralha de Fortificação · Fusion Reactor
Reator de Fusão · Fusion Power Plant Usina de Fusão · Galactic Gate Portal
Galáctico · Geothermal Powerplant Usina Geotérmica · Hovercraft Platform
Plataforma de Hovercrafts · Kbot Lab Laboratório de Kbots · L.L.T. L.L.T. ·
Light Laser Tower Torre de Laser Leve · Heavy Laser Tower Torre de Laser
Pesado · Metal Maker Conversor de Metal · Metal Extractor Extrator de Metal
· Area Mine Mina de Área · Focused Mine Mina Focada · HE Area Mine Mina de
Área AE · Precision Mine Mina de Precisão · Nuclear Mine Mina Nuclear · Moho
Metal Maker Conversor de Metal Moho · Moho Mine Mina Moho · Metal Storage
Depósito de Metal · Seaplane Platform Plataforma de Hidroaviões · Radar
Tower Torre de Radar · Solar Collector Coletor Solar · Sonar Station
Estação de Sonar · Shipyard Estaleiro · Targeting Facility Central de Mira ·
Tidal Generator Gerador Maremotriz · Torpedo Launcher Lançador de Torpedos
· Underwater Energy Storage Depósito de Energia Submarino · Underwater
Fusion Plant Usina de Fusão Submarina · Underwater Metal Extractor Extrator
de Metal Submarino · Underwater Metal Storage Depósito de Metal Submarino ·
Vehicle Plant Fábrica de Veículos · Wind Generator Gerador Eólico ·
Hydration Plant Usina de Hidratação · Fortitude Missile Defense Defesa
Antimísseis Fortitude · Krogoth Gantry Pórtico Krogoth · Mobile Artillery
Artilharia Móvel · Missile Frigate Fragata de Mísseis · Resurrection Kbot
Kbot de Ressurreição.

Kept as written (proper names, codes and the like): FARK · A.K. · Gaat Gun
· Defender - NS · M-104, M-209, M-303, M-420, M-515, M-610 · Archer ·
Swatter · Ambusher · Protector · Pelican · Anaconda · Annihilator · Eraser
· Atlas · Eagle · Millenium · Brawler · Big Bertha · Bulldog · Colossus ·
Triton · Conqueror · Stunner · Zipper · Jeffy · Stingray · Fido · Freedom
Fighter · Flakker · Flash · Flea · Guardian · Hammer · Hawk · Sentinel ·
Jammer · Jethro · Lancet · Panther · Penetrator · Marky · Luger · Maverick
· Merl · Wombat · Tiny · Podger · Ranger · Peeper · Phoenix · Skeeter ·
Peewee · Defender · Rocko · Crusader · Samson · Scarab · Scorpion · Fibber
· Albatross · Seer · Seahawk · Tornado · Skimmer · Retaliator · Escort ·
Shooter · Spider · Infiltrator · Sea Serpent · Stumpy · Lurker · Piranha ·
Bear · Thunder · Hulk · Invader · Vulcan · Warrior · Phalanx · Zeus ·
Slinger · Gimp · Rapier · Shredder · Vulture · Warlord · Buzzsaw · The Can
· Hive · Crasher · Executioner · Doomsday Machine · Deleter · Freaker ·
Weasel · Thunderbolt · Fink · Cobra · Stinger · Instigator · Goliath ·
Dominator · Hunter · Hurricane · Intimidator · Krogoth · Leveler ·
Hedgehog · Nixer · Slasher · Spoiler · Morty · Immolator · Searcher ·
Punisher · Pyro · Raider · Reaper · Pulverizer · Roach · Enforcer · Crock
· Typhoon · Copperhead · Voodoo · Scrubber · Shadow · Shark · Silencer ·
Phantom · Snapper · Spectre · Parasite · Leviathan · Storm · Snake · Sumo
· Turtle · Thud · Titan · Toaster · Neutron · Truck · Envoy · Valkyrie ·
Vamp · Avenger · Viper · Voyeur · Informer · Diplomat. A kept name takes
the article of what it is: `o Flash` (a tank), `a Big Bertha` (a cannon),
`o Krogoth`.

Unit classes in descriptions: Bomber bombardeiro · Fighter caça · Stealth
Fighter caça furtivo · Strategic Bomber bombardeiro estratégico · Gunship
aeronave de ataque · Scout / Air Scout batedor / batedor aéreo · Radar
Plane avião-radar · Transport transporte (Air Transport transporte aéreo,
Transport Ship navio de transporte) · Battleship encouraçado · Cruiser
cruzador · Destroyer destróier · Frigate fragata · Submarine submarino ·
Submarine Killer caça-submarinos · (Light) Carrier porta-aviões (leve) ·
Light / Medium / Heavy Tank tanque leve / médio / pesado · Assault Tank
tanque de assalto · Amphibious Tank tanque anfíbio · Hovertank tanque
hovercraft · Infantry Kbot Kbot de infantaria · Assault Kbot Kbot de
assalto · Artillery Kbot Kbot de artilharia · Missile Tower torre de
mísseis · Plasma Battery bateria de plasma · Plasma Cannon canhão de plasma
· Energy Weapon arma de energia · Mine Layer lança-minas · Mobile Radar
radar móvel · Radar Jammer bloqueador de radar · Perimeter Defense defesa
de perímetro · Produces Aircraft / Kbots / Vehicles / Ships produz
aeronaves / Kbots / veículos / navios · Produces Energy produz energia ·
Produces Metal produz metal · Extracts Metal extrai metal · Converts Energy
into Metal converte energia em metal · Increases Energy Storage aumenta o
armazenamento de energia · Increases Metal Storage aumenta o armazenamento
de metal · Indigenous Lifeform forma de vida nativa · Naval Series série
naval.

## 9. Width

Portuguese runs about a quarter longer than English, close to the
Ukrainian. Captions on 3.1c's fixed-size buttons (its menus' buttons, tabs,
short labels) must stay short: no more than the English's letters and
about a third, and no longer than the Ukrainian's. Prefer the shortest
natural wording for a button: `Iniciar` over `Iniciar campanha` when the
screen already says it, `Carregar` over `Carregar jogo`. Abbreviate with a
full stop only when nothing shorter is natural (`Avanç.`, `Descarr.`), and
never in a sentence. Sentences in dialogs and hints may be as long as they
need to be; the text-fit check measures Open Annihilation's own screens.
The pictures' captions (pictures.tdf) are one word each.
