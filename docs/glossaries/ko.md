# Korean (ko) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the natural modern Korean a Korean RTS player would expect
(StarCraft / Red Alert 3 Korean editions are the model), and keep your own
choice consistent within your chunk.

## 1. Voice and grammar

- Statements and hints (a full sentence): 합쇼체 `-습니다 / -ㅂ니다`.
  "Settings were not saved." → `설정을 저장하지 못했습니다.`
  "The processor draws and scales the view." → `프로세서가 화면을 그리고 크기를 조절합니다.`
- Instructions to the player in the interface: `-하세요`. "Try again later." → `나중에 다시 시도하세요.`
- Confirmation questions: `-하시겠습니까?` "Replace the game files?" → `게임 파일을 교체하시겠습니까?`
- Labels, buttons, menu items, settings names, headings: noun phrases, no
  sentence ending. "Open folder" → `폴더 열기`, "Try again" → `다시 시도`,
  "Mouse wheel zoom" → `마우스 휠 확대/축소`.
- Short status fragments: nominal endings `-됨 / -함 / -음 / 중`.
  "Installed" → `설치됨`, "Downloading" → `다운로드 중`, "Not found" →
  `찾을 수 없음`, "Failed" → `실패`, "Waiting" → `대기 중`.
- Mission briefings and in-fiction messages (HQ talking to the Commander):
  military register. Orders `-하십시오`, statements `-습니다`.
  "Take your units to the Gate and secure it." → `부대를 이끌고 관문으로 가서 관문을 확보하십시오.`
- Do not use 당신. Leave the subject out, as Korean does; if one is
  needed, use 플레이어 (interface) or 커맨더 (fiction).
- English capitals (OPEN FOLDER, SETTINGS) have no Korean equivalent:
  translate normally. Keep Latin acronyms and key names as written:
  SHIFT, CTRL, ALT, ESC, Esc, TCP, IP, CD, DirectPlay, GPU, fps, KB, MB, GB.
- Spacing (띄어쓰기) follows the standard rules. No space between a number
  and a counter (`3개`, `5분`, `2배`), a space before a Latin unit
  (`3.5 MB`, `60 fps`).
- Punctuation: half-width Western punctuation only (`. , ? ! : ( ) …`).
  Never use full-width `，。：；（）`. Never write `;` anywhere (the table
  format ends a value at `;`); split the sentence or use a comma instead.
  Keep `…` or `...` exactly as the English writes it. Quotes: “ ” for
  English " ", ‘ ’ for English ' '. Keep `·`, `→`, `✓`, `✕`, `—` as the
  English has them.

## 2. Placeholders and numbers (hard rules)

- Every placeholder of the English stays, exactly as written: `{name}`,
  `{size}`, `%s`, `%d`, `%i`, `%.1f`, `%%`, `%1$s` and so on. Never
  translate, drop, add, or respell one.
- printf conversions (`%s`, `%d`, …) must stay in the same ORDER as in the
  English, because they are filled in that order. Reword the Korean
  sentence around them if needed. `{name}` slots may move freely.
- Every number written in digits in the English stays in the Korean
  (`1/32`, `2x`, `3.1c`, `16x16`, `9 x 21`).
- Staged captions written with `|` (`Easy|Medium|Hard`): keep exactly the
  same number of `|` stages, each translated in order.
- Particles after a slot: the value's last sound is unknown, so prefer a
  wording that needs no batchim-dependent particle after the slot (`{name}:`,
  `{name}의`, `{name}에서`, `{name}에`, `{name}까지`, `{name}도`, `{n}개`), or
  restructure. Only as a last resort use the paired forms `을(를)`, `이(가)`,
  `은(는)`, `와(과)`, `(으)로`.
- A tab or line break never goes into a translation.

## 3. Names kept as written

- **ARM** and **CORE**, the two sides: always Latin capitals, whatever the
  English case (Arm, Core, ARM, CORE). `CORE 부대`, `ARM 커맨더`.
- Open Annihilation, OA, Core Prime (the service and registry), Total
  Annihilation, Total Annihilation: The Core Contingency, Total
  Annihilation: Battle Tactics, Cavedog Entertainment, GT Interactive,
  Steam, GOG, Windows, macOS, Linux, DirectX, DirectPlay: as written.
- File names, folder names, extensions, keys, URLs, version strings
  (`3.1c`, `oamod.yaml`, `totala1.hpi`, `.oalang`): as written.

## 4. Fiction: places and names

Transliterate invented names into Hangul (외래어 표기법); translate
ordinary words.

| English | Korean |
|---|---|
| Core Prime (the CORE home planet, in the fiction) | CORE 프라임 |
| Empyrrean | 엠피리언 |
| Galactic Gate / the Gate | 은하 관문 / 관문 |
| Thalassean | 탈라시안 |
| Tergiverse IV | 터지버스 IV |
| Barathrum | 바라스럼 |
| Rougpelt | 루그펠트 |
| Aqueous Minor | 아퀴어스 마이너 |
| Aegus | 이거스 |
| Dump (moon of Core Prime) | 덤프 |
| Hydross | 하이드로스 |
| Lusch | 러시 |
| Temblor | 템블러 |
| Gelidus | 젤리더스 |
| Krogoth | 크로고스 |
| Central Consciousness | 중앙 의식 |
| Larab Harbor | 라랍 항 |
| Bromid Maze | 브로미드 미로 |
| Brooban's Isle | 브루반 섬 |
| Motien Ramp | 모티엔 경사로 |
| Xantippe's Abyss | 잔티페의 심연 |
| Slolam Pilago | 슬롤람 필라고 |
| Isle Parche | 파르체 섬 |
| Vebreen Fleet | 베브린 함대 |
| the Arm/Core war | ARM과 CORE의 전쟁 |
| patterning (CORE's transfer of minds into machines) | 패터닝 |
| nanolathe, nanolathing | 나노 선반, 나노 건설 |

## 5. Game terms

| English | Korean |
|---|---|
| Commander | 커맨더 |
| unit | 유닛 |
| building, structure | 건물 |
| Kbot, KBot | K봇 |
| vehicle | 차량 |
| tank | 전차 |
| aircraft, plane | 항공기 |
| ship | 함선 |
| submarine, sub | 잠수함 |
| hovercraft | 호버크래프트 |
| seaplane | 수상기 |
| amphibious | 수륙양용 |
| builder (a unit that builds) | 건설 유닛 |
| factory, plant | 공장 |
| lab (Kbot Lab) | 연구소 |
| shipyard | 조선소 |
| metal | 금속 |
| energy | 에너지 |
| resources | 자원 |
| storage | 저장량 (amount), 저장고 (building) |
| income / production | 수입 / 생산량 |
| metal extractor (mex) | 금속 추출기 |
| metal maker | 금속 변환기 |
| solar collector | 태양열 집열기 |
| wind generator | 풍력 발전기 |
| tidal generator | 조력 발전기 |
| fusion reactor / fusion power plant | 핵융합로 / 핵융합 발전소 |
| geothermal | 지열 |
| radar | 레이더 |
| sonar | 소나 |
| jammer (radar/sonar) | 교란기 (레이더 교란기, 소나 교란기) |
| line of sight, LOS | 시야 |
| cloak, cloaked | 은폐, 은폐됨 |
| stealth | 스텔스 |
| wreck, wreckage, corpse | 잔해 |
| feature (rocks, trees, wrecks on a map) | 지형지물 |
| laser | 레이저 |
| plasma | 플라스마 |
| missile / rocket | 미사일 / 로켓 |
| artillery | 포병 (unit), 야포 (gun) |
| flak | 대공포 |
| torpedo | 어뢰 |
| depth charge | 폭뢰 |
| mine (land / sea) | 지뢰 / 기뢰 |
| nuke, nuclear missile | 핵미사일 |
| anti-nuke, missile defense | 핵 요격, 미사일 방어 |
| EMP | EMP |
| D-Gun (Disintegrator Gun) | D건 (디스인티그레이터 건) |
| anti-air | 대공 |
| ally, alliance | 동맹 |
| enemy | 적 |
| team | 팀 |
| kills / losses | 처치 / 손실 |
| veteran / veterancy | 베테랑 / 숙련도 |
| victory / defeat | 승리 / 패배 |
| paused | 일시 정지 |
| Tech Level 1 / 2 | 기술 레벨 1 / 기술 레벨 2 |
| Adv., Advanced (unit names) | 고급 |
| build menu | 건설 메뉴 |
| control group (select groups) | 부대 (부대 지정, 부대 선택) |
| selection, select | 선택 |
| waypoint | 경유지 |
| queue | 대기열 |
| self-destruct | 자폭 |

### Orders (buttons and their states; also used in touch controls)

| English | Korean |
|---|---|
| ATTACK | 공격 |
| MOVE | 이동 |
| STOP | 정지 |
| PATROL | 순찰 |
| DEFEND / GUARD | 호위 |
| RECLAIM | 회수 |
| REPAIR | 수리 |
| CAPTURE | 포획 |
| LOAD / UNLOAD (transports) | 탑재 / 하역 |
| ORDERS | 명령 |
| BUILD | 건설 |
| BLAST / D-GUN | D건 |
| ASSIST | 지원 |
| Fire orders: Hold Fire / Return Fire / Fire At Will | 사격 명령: 사격 금지 / 응사 / 자유 사격 |
| Move orders: Hold Position / Maneuver / Roam | 이동 명령: 위치 고수 / 기동 / 자유 이동 |
| On / Off (a unit) | 켜짐 / 꺼짐 |
| Activate / Deactivate | 활성화 / 비활성화 |
| Resurrect | 부활 |
| Patrolling / Guarding (builders) | 순찰 중 / 호위 중 |

## 6. Menus and modes

| English | Korean |
|---|---|
| Single Player | 싱글 플레이어 |
| Multiplayer | 멀티플레이어 |
| Campaign | 캠페인 |
| Mission | 미션 |
| Briefing | 브리핑 |
| Skirmish | 스커미시 |
| Battle Room | 대기실 |
| Lobby / Lounge | 로비 |
| host / join | 호스트 / 참가 |
| player | 플레이어 |
| computer player, AI | 컴퓨터 (3.1c's "Computer"), AI ("AI") |
| watcher, spectator / watch | 관전자 / 관전 |
| replay | 리플레이 |
| recorder, recording | 녹화 |
| saved game / save / load | 저장된 게임 / 저장 / 불러오기 |
| Options | 옵션 |
| Settings | 설정 |
| Preferences | 환경 설정 |
| Previous Menu / Back | 이전 메뉴 / 뒤로 |
| Main menu / Game menu | 메인 메뉴 / 게임 메뉴 |
| Exit, Quit | 나가기 (leave a screen), 종료 (quit the program) |
| Exit to the system | 시스템으로 나가기 |
| OK / Cancel / Done / Close / Apply | 확인 / 취소 / 완료 / 닫기 / 적용 |
| Retry, Try again | 다시 시도 |
| Continue | 계속 |
| Easy / Medium / Hard | 쉬움 / 보통 / 어려움 |
| Help | 도움말 |
| Chat | 채팅 |
| Cheats | 치트 |
| game speed | 게임 속도 |
| Sound / Music / Volume / Movies | 사운드 / 음악 / 볼륨 / 동영상 |
| Credits | 제작진 |
| Intro | 인트로 |

## 7. Open Annihilation's interface

| English | Korean |
|---|---|
| Library | 라이브러리 |
| mod | 모드 |
| mod profile | 모드 프로필 |
| hacks, standard hacks (engine behaviour a mod switches on) | 수정 항목, 표준 수정 항목 |
| map / map pack | 맵 / 맵 팩 |
| language pack | 언어 팩 |
| expansion | 확장팩 |
| base game | 기본 게임 |
| registry (a server listing packages) | 저장소 |
| catalogue | 목록 |
| download / install / update / remove / delete | 다운로드 / 설치 / 업데이트 / 제거 / 삭제 |
| version / revision | 버전 / 리비전 |
| roll back | 롤백 |
| folder / file / archive | 폴더 / 파일 / 아카이브 |
| game files / game folder / game archives | 게임 파일 / 게임 폴더 / 게임 아카이브 |
| device | 기기 |
| free (space) | 여유 공간 (`{size} free` → `여유 공간 {size}`) |
| screen / window / full screen | 화면 / 창 / 전체 화면 |
| zoom, zoom in / out | 확대/축소, 확대 / 축소 |
| graphics | 그래픽 |
| hardware acceleration | 하드웨어 가속 |
| vertical sync | 수직 동기화 |
| anti-aliasing | 안티에일리어싱 |
| frame rate | 프레임 레이트 |
| resolution | 해상도 |
| modern fonts | 최신 글꼴 |
| font / text size | 글꼴 / 텍스트 크기 |
| controller / trackpad / stick / gyro / D-pad | 컨트롤러 / 트랙패드 / 스틱 / 자이로 / 방향 패드 |
| touch | 터치 |
| haptics | 햅틱 |
| pointer | 포인터 |
| Developer Mode | 개발자 모드 |
| Language / System default | 언어 / 시스템 기본값 |
| snap (click snap) | 스냅 |
| the host (of a shared game) | 호스트 |
| shared game / network play | 멀티플레이 게임 / 네트워크 플레이 |
| HUD | HUD |
| Unicode | 유니코드 |
| install ID | 설치 ID |
| demo | 데모 |

## 8. Unit names

Generic names are translated; proper names are transliterated. Use these
exactly, in units.tdf and wherever a unit is named (briefings, help,
messages).

Generic: Adv. Aircraft Plant 고급 항공기 공장 · Adv. Construction Aircraft
고급 건설 항공기 · Adv. Construction Kbot 고급 건설 K봇 · Advanced
Construction Sub 고급 건설 잠수함 · Adv. Construction Vehicle 고급 건설 차량
· Adv. Kbot Lab 고급 K봇 연구소 · Aircraft Plant 항공기 공장 · Advanced Radar
Tower 고급 레이더 탑 · Advanced Sonar Station 고급 소나 기지 · Air Repair Pad
항공기 수리대 · Adv. Shipyard 고급 조선소 · Advanced Torpedo Launcher 고급
어뢰 발사기 · Adv. Vehicle Plant 고급 차량 공장 · Alien Beacon 외계 신호기 ·
Construction Aircraft 건설 항공기 · Construction Hovercraft 건설
호버크래프트 · Construction Kbot / KBot 건설 K봇 · Cloakable Fusion Reactor
은폐형 핵융합로 · Commander 커맨더 · Construction Ship 건설 함선 ·
Construction Seaplane 건설 수상기 · Construction Vehicle 건설 차량 · Decoy
Commander 미끼 커맨더 · Implosion Device 내파 장치 · Dragon's Teeth 용치 ·
Floating Dragon's Teeth 부유 용치 · Energy Storage 에너지 저장고 · Floating
Metal Maker 부유 금속 변환기 · Fortification Wall 방벽 · Fusion Reactor
핵융합로 · Fusion Power Plant 핵융합 발전소 · Galactic Gate 은하 관문 ·
Geothermal Powerplant 지열 발전소 · Hovercraft Platform 호버크래프트
플랫폼 · Kbot Lab K봇 연구소 · L.L.T. L.L.T. · Light Laser Tower 경레이저 탑 ·
Heavy Laser Tower 중레이저 탑 · Metal Maker 금속 변환기 · Metal Extractor
금속 추출기 · Area Mine 광역 지뢰 · Focused Mine 집중 지뢰 · HE Area Mine
고폭 광역 지뢰 · Precision Mine 정밀 지뢰 · Nuclear Mine 핵 지뢰 · Moho Metal
Maker 모호 금속 변환기 · Moho Mine 모호 광산 · Metal Storage 금속 저장고 ·
Seaplane Platform 수상기 플랫폼 · Radar Tower 레이더 탑 · Solar Collector
태양열 집열기 · Sonar Station 소나 기지 · Shipyard 조선소 · Targeting
Facility 표적 지정 시설 · Tidal Generator 조력 발전기 · Torpedo Launcher 어뢰
발사기 · Underwater Energy Storage 수중 에너지 저장고 · Underwater Fusion
Plant 수중 핵융합 발전소 · Underwater Metal Extractor 수중 금속 추출기 ·
Underwater Metal Storage 수중 금속 저장고 · Vehicle Plant 차량 공장 · Wind
Generator 풍력 발전기 · Hydration Plant 급수 시설 · Fortitude Missile
Defense 포티튜드 미사일 방어 · Krogoth Gantry 크로고스 갠트리 · Gaat Gun
가트 건 · Mobile Artillery 이동식 야포 · Missile Frigate 미사일 프리깃 ·
Resurrection Kbot 부활 K봇 · Defender - NS 디펜더 - NS · M-104, M-209, M-303,
M-420, M-515, M-610 as written · FARK FARK · A.K. A.K.

Proper (transliterated): Archer 아처 · Swatter 스와터 · Ambusher 앰부셔 ·
Protector 프로텍터 · Pelican 펠리컨 · Anaconda 아나콘다 · Annihilator
어나이얼레이터 · Eraser 이레이저 · Atlas 아틀라스 · Eagle 이글 · Millenium
밀레니엄 · Brawler 브롤러 · Big Bertha 빅 버사 · Bulldog 불도그 · Colossus
콜로서스 · Triton 트리톤 · Conqueror 컨커러 · Stunner 스터너 · Zipper 지퍼 ·
Jeffy 제피 · Stingray 스팅레이 · Fido 파이도 · Freedom Fighter 프리덤 파이터 ·
Flakker 플래커 · Flash 플래시 · Flea 플리 · Guardian 가디언 · Hammer 해머 ·
Hawk 호크 · Sentinel 센티널 · Jammer 재머 · Jethro 제스로 · Lancet 랜싯 ·
Panther 팬서 · Penetrator 페너트레이터 · Marky 마키 · Luger 루거 · Maverick
매버릭 · Merl 멀 · Wombat 웜뱃 · Tiny 타이니 · Podger 포저 · Ranger 레인저 ·
Peeper 피퍼 · Phoenix 피닉스 · Skeeter 스키터 · Peewee 피위 · Defender 디펜더
· Rocko 로코 · Crusader 크루세이더 · Samson 샘슨 · Scarab 스카라브 ·
Scorpion 스콜피온 · Fibber 피버 · Albatross 앨버트로스 · Seer 시어 · Seahawk
시호크 · Tornado 토네이도 · Skimmer 스키머 · Retaliator 리탈리에이터 ·
Escort 에스코트 · Shooter 슈터 · Spider 스파이더 · Infiltrator 인필트레이터 ·
Sea Serpent 시 서펀트 · Stumpy 스텀피 · Lurker 러커 · Piranha 피라냐 · Bear
베어 · Thunder 선더 · Hulk 헐크 · Invader 인베이더 · Vulcan 벌컨 · Warrior
워리어 · Phalanx 팰렁스 · Zeus 제우스 · Slinger 슬링어 · Gimp 김프 · Rapier
레이피어 · Shredder 슈레더 · Vulture 벌처 · Warlord 워로드 · Buzzsaw 버즈소 ·
The Can 더 캔 · Hive 하이브 · Crasher 크래셔 · Executioner 엑시큐셔너 ·
Doomsday Machine 둠스데이 머신 · Deleter 딜리터 · Freaker 프리커 · Weasel
위즐 · Thunderbolt 선더볼트 · Fink 핀크 · Cobra 코브라 · Stinger 스팅어 ·
Instigator 인스티게이터 · Goliath 골리앗 · Dominator 도미네이터 · Hunter 헌터
· Hurricane 허리케인 · Intimidator 인티미데이터 · Krogoth 크로고스 · Leveler
레벨러 · Hedgehog 헤지호그 · Nixer 닉서 · Slasher 슬래셔 · Spoiler 스포일러 ·
Morty 모티 · Immolator 이몰레이터 · Searcher 서처 · Punisher 퍼니셔 · Pyro
파이로 · Raider 약탈자 (not 레이더, which is radar) · Reaper 리퍼 ·
Pulverizer 펄버라이저 · Roach 로치 · Enforcer 인포서 · Crock 크록 · Typhoon
타이푼 · Copperhead 코퍼헤드 · Voodoo 부두 · Scrubber 스크러버 · Shadow 섀도 ·
Shark 샤크 · Silencer 사일런서 · Phantom 팬텀 · Snapper 스내퍼 · Spectre 스펙터
· Parasite 패러사이트 · Leviathan 리바이어선 · Storm 스톰 · Snake 스네이크 ·
Sumo 스모 · Turtle 터틀 · Thud 서드 · Titan 타이탄 · Toaster 토스터 · Neutron
뉴트론 · Truck 트럭 · Envoy 엔보이 · Valkyrie 발키리 · Vamp 뱀프 · Avenger
어벤저 · Viper 바이퍼 · Voyeur 보이어 · Informer 인포머 · Diplomat 디플로맷.

Unit classes in descriptions: Bomber 폭격기 · Fighter 전투기 · Stealth Fighter
스텔스 전투기 · Strategic Bomber 전략 폭격기 · Gunship 건십 · Scout / Air
Scout 정찰기 · Radar Plane 레이더 정찰기 · Transport 수송기 (air) / 수송선
(sea) · Battleship 전함 · Cruiser 순양함 · Destroyer 구축함 · Frigate 프리깃 ·
Submarine 잠수함 · (Light) Carrier (경)항공모함 · Light / Medium / Heavy Tank
경전차 / 중형 전차 / 중전차 · Amphibious Tank 수륙양용 전차 · Infantry Kbot
보병 K봇 · Artillery Kbot 포병 K봇 · Missile Tower 미사일 탑 · Plasma Battery
플라스마 포대 · Energy Weapon 에너지 무기 · Mine Layer 지뢰 부설 · Radar
Vehicle 레이더 차량 · Produces Aircraft / Kbots / Vehicles / Ships 항공기 /
K봇 / 차량 / 함선 생산 · Produces Energy 에너지 생산 · Produces Metal 금속
생산 · Increases Energy Storage 에너지 저장량 증가 · Increases Metal Storage
금속 저장량 증가 · Indigenous Lifeform 토착 생명체.

## 9. Width

Korean syllables are drawn full-width, at least 12 px each. Captions on
3.1c's fixed-size buttons (its menus' buttons, tabs, short labels) must stay
short: about as many syllables as the Chinese has characters, at most about
1.5 times. Prefer the shortest natural wording for a button: `시작` over
`시작하기`, `불러오기` over `게임 불러오기` when the screen already says
"game". Sentences in dialogs and hints may be as long as they need to be.

## 10. Keys

One word for each idea, in the key editor, the overlay, Settings › Controls,
Settings › Accessibility, Library › Keys and the install question.

| English | Korean |
|---|---|
| key layout | 키 배치 |
| key editor | 키 편집기 |
| action (a binding; also where English still says "command" for one) | 동작 |
| changes of your own | 내 변경 |
| clash | 충돌 |
| latch / latched | 고정 / 고정됨 |
| letter (of a key) | 글자 |
| place (of a key) | 위치 |
| hold to confirm | 길게 눌러 확인 |

Named keys as a Korean keyboard prints them. Shift, Ctrl, Alt, Esc, Escape,
Tab, Enter, Backspace, Delete, Insert, Home, End, Page Up, Page Down,
Caps Lock, F1–F12 and Win stay Latin. 한/영 stays 한/영.

| English | Korean |
|---|---|
| Space | 스페이스 |
| Arrow up / down / left / right | 위쪽 화살표 / 아래쪽 화살표 / 왼쪽 화살표 / 오른쪽 화살표 |
| Numpad | 숫자 키 |
| Left / Right / Middle button | 왼쪽 버튼 / 오른쪽 버튼 / 가운데 버튼 |
| Wheel up / down | 휠 위 / 휠 아래 |
