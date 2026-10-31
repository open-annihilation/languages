# European Portuguese (pt-PT) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the modern European Portuguese a player in Portugal would
expect (the Portuguese interfaces of Windows, macOS, the Xbox and
PlayStation, and the European Portuguese editions of today's games are the
model), and keep your own choice consistent within your chunk. The spelling
is the 1990 orthographic agreement's, as Portugal writes it (`ação`,
`ideia`, `ótimo`, `atual`, `direção`, `objetivo`, `detetar`, `deteção`,
`receção`, `perspetiva`, `espetador`, `excecional`), keeping the consonants
Portugal still writes and pronounces (`contacto`, `facto`, `secção`,
`pacto`, `ficção`) and Portugal's accents (`económico`, `fenómeno`,
`género`, `génio`, `prémio`, `eletrónico`, `atómico`, `quilómetro`,
`anónimo`, `autónomo`, `bebé`, `ténue`, `câmara`).

The Brazilian pack (`docs/glossaries/pt-BR.md`) was translated first and
is the pack's nearest neighbour. Where it reads as Brazil writes, this pack
says it as Portugal does. Do not copy it: read the English, then write the
European Portuguese.

## 1. Voice and grammar

- Statements and hints (a full sentence): the present indicative, neutral
  and plain. "Settings were not saved." → `As definições não foram
  guardadas.` "The processor draws and scales the view." → `O processador
  desenha e dimensiona a imagem.`
- Instructions to the player: the formal imperative of Portuguese
  interfaces, the third person singular (`Clique`, `Selecione`, `Escolha`,
  `Prima`, `Introduza`, `Tente novamente mais tarde.`). Never `tu` and its
  forms (`clica`, `seleciona`, `teu`). Never `você`: leave the subject out,
  or recast; where a pronoun cannot be avoided write `si` (`para si`). `seu`,
  `sua` are the player's, with the article (`o seu jogo`, `a sua pasta`).
- Progressive forms: `a` and the infinitive, never the gerund. "Downloading"
  → `A transferir`, "Waiting for the host" → `A aguardar o anfitrião`,
  "Patrolling" → `A patrulhar`, "is copying" → `está a copiar`.
- Pronouns after the verb in a main clause (`O jogo reinicia-se.`,
  `Proteja-o.`, `Chama-se`), before it after a negation, a question word,
  `que`, `se`, `quando`, `já` and similar (`não se guarda`, `que se
  instala`). Never start a sentence with an unstressed pronoun. The future
  and conditional take mesoclisis only in the briefings' formal voice, and
  even there prefer a recast (`vai ser destruído` over `destruir-se-á`).
- `ter de`, not `ter que`. `Já não` for "no longer", not `não … mais`.
- Confirmation questions: `Pretende` and an infinitive. "Replace the game
  files?" → `Pretende substituir os ficheiros do jogo?` A short question
  that is a dialog's title may be a bare infinitive: `Sair do jogo?`
- Labels, buttons, menu items, setting names and headings: noun phrases or
  infinitives, no full stop, in sentence case (only the first word and
  names capitalized). "Open folder" → `Abrir pasta`, "Try again" →
  `Tentar novamente`, "Mouse wheel zoom" → `Zoom com a roda do rato`.
  Where the English is in capitals, so is the Portuguese (`OPÇÕES`,
  `SAIR`).
- Short status words: the participle, or `A` and the infinitive for
  something in progress, agreeing with what it describes, masculine
  singular when nothing says otherwise. "Installed" → `Instalado`,
  "Downloading" → `A transferir`, "Not found" → `Não encontrado`, "Failed"
  → `Falhou`, "Waiting" → `A aguardar`, "Ready" → `Pronto`, "Off" / "On" →
  `Desligado` / `Ligado`.
- Mission briefings and in-fiction messages (HQ talking to the Commander):
  a crisp military register. Orders in the imperative (`Leve as suas
  unidades até ao Portal e proteja-o.`), statements in the indicative, the
  Commander addressed as `Comandante`, the side's own forces as `as nossas
  forças`. No slang, no exclamations the English does not have.
- The briefings' fixed words: `MISSION` → `MISSÃO`, `PRIORITY` →
  `PRIORIDADE`, `PRIORITY CRITICAL` → `PRIORIDADE CRÍTICA`, `INFO FEED` →
  `INFORMAÇÕES`, `INTEL FEED` → `INFORMAÇÕES DOS SERVIÇOS SECRETOS`, `END`
  → `FIM`, `WARNING` → `ATENÇÃO`, `Suggestions:` → `Sugestões:`, `Battle
  Tactics:` → `Táticas de batalha:`, `Mission T01: …` → `Missão T01: …`
  with the missions table's name. CORE's own briefings speak as a machine:
  `INTELL-TAP:` → `ESCUTA-INTEL:`, `DO SO NOW.` → `EXECUTE AGORA.`, and
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
  í ó ô õ ú ç` and their capitals. Do not use `ª` or `º` (ordinals):
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
  plural (`{count} ficheiros`), as the English does.
- `{device}` and `{cloud}` are filled with this pack's `device` and `the
  cloud`, or with the system's own name for them (`iPad`, `iCloud`).
  Translate `device` as `dispositivo` and `the cloud` as `nuvem`, with no
  article, and write the sentences so either fills them: `neste {device}`,
  `em {cloud}`, `via {cloud}` (never `na {cloud}` or `da {cloud}`).
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
  Steam, GOG, iCloud, Windows, macOS, Linux, DirectX, DirectPlay: as
  written.
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
| the Arm/Core war | a guerra entre o ARM e o CORE |
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
| income / production | rendimento / produção |
| metal extractor (mex) | extrator de metal |
| metal maker | conversor de metal |
| solar collector | coletor solar |
| wind generator | gerador eólico |
| tidal generator | gerador maremotriz |
| fusion reactor / fusion power plant | reator de fusão / central de fusão |
| power plant | central (`central geotérmica`), never `usina` |
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
| team | equipa |
| kills / losses | abates / perdas |
| veteran / veterancy | veterano / experiência |
| victory / defeat | vitória / derrota |
| paused | em pausa (the title: PAUSA) |
| Tech Level 1 / 2 | Nível tecnológico 1 / 2 |
| Adv., Advanced (unit names) | Avançado, Avançada (after the noun) |
| build menu | menu de construção |
| control group (select groups) | grupo |
| selection, select | seleção, selecionar |
| waypoint | ponto de passagem |
| queue | fila |
| self-destruct | autodestruição |
| repair | reparação (noun), reparar (verb) |
| map | mapa |
| match, game (one played) | partida, jogo |
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
| Fire orders: Hold Fire / Return Fire / Fire At Will | Ordens de fogo: Cessar fogo / Ripostar / Fogo à vontade |
| Move orders: Hold Position / Maneuver / Roam | Ordens de movimento: Manter posição / Manobrar / Vaguear |
| On / Off (a unit) | Ligado / Desligado |
| Activate / Deactivate | Ativar / Desativar |
| Cloaked / Visible | Camuflado / Visível |
| Resurrect | Ressuscitar |
| arm (an order, on touch and controller rings) / ARM ORDER | preparar (a ordem) / PREPARAR |
| QUEUE / ADD / FORCE / CLEAR / STORE (touch) | FILA / ADICIONAR / FORÇAR / LIMPAR / GUARDAR |
| Patrolling / Guarding (builders) | A patrulhar / A proteger |

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
| watcher, spectator / watch | espetador / assistir |
| replay | repetição |
| recorder, recording | gravador, gravação |
| saved game / save / load | jogo guardado / guardar / carregar |
| Options | Opções |
| Settings | Definições |
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
| Cheats | Batotas |
| game speed | velocidade do jogo |
| Sound / Music / Volume / Movies | Som / Música / Volume / Vídeos |
| Credits | Créditos |
| Intro | Introdução |
| Restrictions | Restrições |
| SINGLE / MULTI / INTRO / EXIT (title screen) | UM JOGADOR / MULTIJOGADOR / ABERTURA / SAIR |
| On / Off (3.1c's sound toggles) | Sim / Não, as 3.1c's French and Italian say Oui and Sì |
| the game menu's Settings (OA settings) | Definições, or Defin. where it does not fit |
| Wind Speed / Gravity (briefing) | Vento / Gravidade |

## 7. Open Annihilation's interface

| English | Portuguese |
|---|---|
| Library | Biblioteca |
| mod | mod (masc., plural mods) |
| mod profile | perfil do mod |
| hacks, standard hacks (engine behaviour a mod switches on) | ajustes, ajustes predefinidos |
| map / map pack | mapa / pacote de mapas |
| language pack | pacote de idioma |
| package | pacote |
| expansion | expansão |
| base game | jogo base |
| registry (a server listing packages) | repositório |
| catalogue | catálogo |
| download (verb / noun) | transferir / transferência |
| install / update / remove / delete | instalar / atualizar, atualização / remover / eliminar |
| version / revision | versão / revisão |
| roll back | reverter |
| folder / file | pasta / ficheiro |
| archive (an .hpi, .ufo, .ccx or .gp3 file; a zip) | arquivo |
| game files / game folder / game archives | ficheiros do jogo / pasta do jogo / arquivos do jogo |
| device | dispositivo |
| free (space) | livre (`{size} free` → `{size} livres`) |
| screen / window / full screen | ecrã / janela / ecrã inteiro |
| zoom, zoom in / out | zoom, aproximar / afastar |
| graphics | gráficos |
| graphics card | placa gráfica |
| hardware acceleration | aceleração por hardware |
| vertical sync | sincronização vertical |
| anti-aliasing | anti-aliasing |
| frame rate / frame | taxa de fotogramas / fotograma |
| pixel | píxel (plural píxeis) |
| resolution | resolução |
| modern fonts | tipos de letra modernos |
| font / text size | tipo de letra / tamanho do texto |
| controller / trackpad / stick / gyro / D-pad | comando / trackpad / manípulo / giroscópio / botão direcional |
| control (a thing on screen the player uses) | controlo (plural controlos) |
| touch | toque |
| haptics | vibração |
| pointer | ponteiro |
| mouse / mouse wheel | rato / roda do rato |
| keyboard | teclado |
| press (a key, a button) | premir (`Prima Enter`) |
| type (text) | escrever, introduzir (`Introduza um nome`) |
| scroll | deslocar |
| show / hide | mostrar / ocultar |
| enable / disable | ativar / desativar |
| user | utilizador |
| password | palavra-passe |
| share | partilhar |
| manage | gerir |
| access (verb) | aceder |
| default | predefinido, predefinição (`Predefinição do sistema`) |
| preview | pré-visualização |
| log (a file of messages) | registo |
| Developer Mode | Modo de programador |
| Language / System default | Idioma / Predefinição do sistema |
| snap (click snap) | encaixe, encaixar (the click is drawn to the nearest target) |
| the host (of a shared game) | anfitrião |
| shared game / network play | partida em rede / jogo em rede |
| HUD | HUD |
| Unicode | Unicode |
| install ID | ID de instalação |
| demo | demo |
| content | conteúdo |
| key (keyboard) / key binding | tecla / atalho |
| app | aplicação |
| phone / tablet | telemóvel / tablet |

## 8. Unit names

Proper names stay in English, as written, as Portuguese editions of RTS
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
Plataforma de Reparação Aérea · Adv. Shipyard Estaleiro Avançado · Advanced
Torpedo Launcher Lançador de Torpedos Avançado · Adv. Vehicle Plant Fábrica
de Veículos Avançada · Alien Beacon Sinalizador Alienígena · Construction
Aircraft Aeronave de Construção · Construction Hovercraft Hovercraft de
Construção · Construction Kbot / KBot Kbot de Construção · Cloakable Fusion
Reactor Reator de Fusão Camuflável · Commander Comandante · Construction
Ship Navio de Construção · Construction Seaplane Hidroavião de Construção ·
Construction Vehicle Veículo de Construção · Decoy Commander Comandante
Chamariz · Implosion Device Dispositivo de Implosão · Dragon's Teeth Dentes
de Dragão · Floating Dragon's Teeth Dentes de Dragão Flutuantes · Energy
Storage Depósito de Energia · Floating Metal Maker Conversor de Metal
Flutuante · Fortification Wall Muralha de Fortificação · Fusion Reactor
Reator de Fusão · Fusion Power Plant Central de Fusão · Galactic Gate Portal
Galáctico · Geothermal Powerplant Central Geotérmica · Hovercraft Platform
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
Fusion Plant Central de Fusão Submarina · Underwater Metal Extractor
Extrator de Metal Submarino · Underwater Metal Storage Depósito de Metal
Submarino · Vehicle Plant Fábrica de Veículos · Wind Generator Gerador
Eólico · Hydration Plant Central de Hidratação · Fortitude Missile Defense
Defesa Antimísseis Fortitude · Krogoth Gantry Pórtico Krogoth · Mobile
Artillery Artilharia Móvel · Missile Frigate Fragata de Mísseis ·
Resurrection Kbot Kbot de Ressurreição.

Kept as written (proper names, codes and the like): the same list as the
Brazilian glossary's section 8, word for word (FARK, A.K., Gaat Gun,
Defender - NS, the M-numbered mines, Archer, Swatter … Informer,
Diplomat). A kept name takes the article of what it is: `o Flash` (a
tank), `a Big Bertha` (a cannon), `o Krogoth`.

Unit classes in descriptions: Bomber bombardeiro · Fighter caça · Stealth
Fighter caça furtivo · Strategic Bomber bombardeiro estratégico · Gunship
aeronave de ataque · Scout / Air Scout batedor / batedor aéreo · Radar
Plane avião-radar · Transport transporte (Air Transport transporte aéreo,
Transport Ship navio de transporte) · Battleship couraçado · Cruiser
cruzador · Destroyer contratorpedeiro · Frigate fragata · Submarine
submarino · Submarine Killer caça-submarinos · (Light) Carrier porta-aviões
(ligeiro) · Light / Medium / Heavy Tank tanque ligeiro / médio / pesado ·
Assault Tank tanque de assalto · Amphibious Tank tanque anfíbio · Hovertank
tanque hovercraft · Infantry Kbot Kbot de infantaria · Assault Kbot Kbot de
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
naval. "Light" in a class is `ligeiro`, as Portugal's armies say it; in a
unit's own name (Light Laser Tower) it stays `Leve`.

## 9. Width

European Portuguese runs about a quarter longer than English, as the
Brazilian does. Captions on 3.1c's fixed-size buttons (its menus' buttons,
tabs, short labels) must stay short: no longer than the Brazilian pack's
caption of the same button unless Portugal's word is longer, and then no
more than the English's letters and about a third. Prefer the shortest
natural wording for a button: `Iniciar` over `Iniciar campanha` when the
screen already says it, `Carregar` over `Carregar jogo`. Abbreviate with a
full stop only when nothing shorter is natural (`Avanç.`, `Descarr.`), and
never in a sentence. Sentences in dialogs and hints may be as long as they
need to be; the text-fit check measures Open Annihilation's own screens.
The pictures' captions (pictures.tdf) are one word each.

## 10. Keys

One word for each idea, in the key editor, the overlay, Settings › Controls,
Settings › Accessibility, Library › Keys and the install question. Sentence
case in a label (`Esquema de teclas`), as the rest of this file.

| English | Portuguese |
|---|---|
| key layout | esquema de teclas (`esquema` alone where the screen already says keys) |
| key editor | editor de teclas |
| action (a binding; also where English still says "command" for one) | ação |
| key binding | atalho |
| helper (a setting of the key editor) | auxiliar (plural auxiliares) |
| changes of your own | as suas alterações |
| clash | conflito |
| latch / latched | fixar / fixado |
| unbound (the filter) | Sem tecla |
| letter (of a key) | letra |
| place (of a key) | posição |
| hold to confirm | Mantenha premido para confirmar |
| hold (a key, a button) | manter premido |
| Clone (a layout) | Clonar |
| Share / Paste (a layout) | Partilhar / Colar |
| Sharing (the heading) | Partilha |
| primary (the selected unit the others follow) | principal |
| idle (builders, factories) | inativos, inativas |
| countdown | contagem decrescente |

Named keys stay as the keyboard prints them: Shift, Ctrl, Alt, Option, Esc,
Escape, Enter, Tab, Backspace, Delete, Insert, Home, End, Page Up, Page
Down, Caps Lock, F1–F12, Win. In a sentence, Space is `barra de espaços`;
the key's name alone is `Espaço`. Arrows are `Seta para cima`, `Seta para
baixo`, `Seta para a esquerda`, `Seta para a direita`. Numpad is `Teclado
numérico` (`Numpad add` → `Teclado numérico +`). Mouse buttons: `Botão
esquerdo`, `Botão direito`, `Botão do meio`. Wheel: `Roda para cima`, `Roda
para baixo`.

## 11. Brains, mutators and the later screens

| English | Portuguese |
|---|---|
| brain (a computer player's mind, installed from the Library) | cérebro (the Library's tab: Cérebros) |
| built-in player | jogador integrado |
| computer player | computador (3.1c's Computer); `jogador do computador` only where a sentence needs it |
| Rush / Turtle / Learned / Teaching (brain styles) | Rush / Defensivo / Treinado / Didático |
| mutator | mutador (the Library's tab and the button: Mutadores) |
| Fog of War | Nevoeiro de guerra |
| Full 3D Mode / Full 3D | Modo 3D completo / 3D completo |
| Basic / Full (hardware acceleration's choices) | Básico / Completo, the choices' names, also in sentences (`em Completo`, `Requer a aceleração por hardware em Completo.`) |
| Smooth motion | Movimento suave |
| New unit shadows | Novas sombras de unidades |
| overlay / Arrange overlays | sobreposição / Organizar sobreposições |
| badge | emblema |
| Accessibility | Acessibilidade (heading ACESSIBILIDADE) |
| Engine Limits | Limites do motor |
| Whiteboard (key bindings) | Quadro branco |
| Megamap | Megamapa |
| Watching (key bindings) | Espetador |
| world (a mod's world, the Library's filter) / WORLD | mundo / MUNDO (`Mundo: {tag} ({count})`) |
| tag / TAGS | etiqueta / ETIQUETAS |
| In use (the Library's pill) | Em uso |
| rev (short for revision) | rev. |
| Ready when you are (sample chat) | Quando quiser |
| camera (Full 3D) / orbit / pan | câmara / orbitar / deslocar |
| Mouse look | Olhar com o rato |
| Developer (key bindings) | Programador |
| view (the part of the map on screen) | vista (`centra a vista`, `Desloca a vista para cima`); `visão` only in `linha de visão` |
| seat (a player's place in a game) | lugar (`Lugar {n}`) |
| tab (a screen's tab) | separador |
| bookmark (a stored view) / marker (the whiteboard's) | marcador / marca |

## 12. Brazilian words this pack does not use

A quick check for a pack adapted beside the Brazilian one. Each word on the
left is Brazil's; write the right one.

| Brazil | Portugal |
|---|---|
| arquivo (a file) | ficheiro (`arquivo` is an archive) |
| baixar, download | transferir, transferência |
| salvar, salvo | guardar, guardado |
| tela, tela cheia | ecrã, ecrã inteiro |
| mouse | rato |
| usuário | utilizador |
| configurações | definições |
| compartilhar | partilhar |
| excluir | eliminar |
| equipe, time | equipa |
| controle (a controller / a control) | comando / controlo |
| analógico, direcional (a controller's) | manípulo, botão direcional |
| pressionar, apertar (a key) | premir |
| digitar | escrever, introduzir |
| rolar (the view, a list) | deslocar |
| exibir | mostrar |
| habilitar, desabilitar | ativar, desativar |
| padrão (a default) | predefinido, predefinição |
| desenvolvedor | programador |
| registro, registrar | registo, registar |
| contato, fato, seção | contacto, facto, secção |
| detectar, detecção, recepção | detetar, deteção, receção |
| câmera | câmara |
| usina | central |
| reparo | reparação |
| renda | rendimento |
| destróier, encouraçado | contratorpedeiro, couraçado |
| trapaças | batotas |
| espectador | espetador |
| revidar, vagar (orders) | ripostar, vaguear |
| leve (a light class) | ligeiro |
| você, para você | (no subject), para si |
| ter que | ter de |
| Baixando, Carregando (gerunds) | A transferir, A carregar |
| gerenciar, acessar | gerir, aceder |
| contagem regressiva | contagem decrescente |
| ocioso | inativo |
| quadro (a frame) | fotograma |
| placa de vídeo | placa gráfica |
| fonte (a typeface) | tipo de letra |
| celular | telemóvel |
| aplicativo | aplicação |
| senha | palavra-passe |
