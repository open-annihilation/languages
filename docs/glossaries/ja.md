# Japanese (ja) glossary and style guide for Open Annihilation

One glossary, one voice. Every translator follows this file exactly. When a
term is listed here, use it as written, every time. When a term is not
listed, choose the natural modern Japanese a Japanese RTS player would
expect (the Japanese editions of StarCraft, Age of Empires and Command &
Conquer: Red Alert 3 are the model), and keep your own choice consistent
within your chunk.

## 1. Voice and grammar

- Statements and hints (a full sentence): です・ます.
  "Settings were not saved." → `設定を保存できませんでした。`
  "The processor draws and scales the view." → `プロセッサーが画面を描画し、拡大縮小します。`
- Instructions to the player in the interface: `〜してください`.
  "Try again later." → `しばらくしてからもう一度試してください。`
- Confirmation questions: `〜しますか？`
  "Replace the game files?" → `ゲームファイルを置き換えますか？`
- Labels, buttons, menu items, settings names, headings: noun phrases
  (体言止め), no です・ます, no closing `。`. "Mouse wheel zoom" →
  `マウスホイールでズーム`, "Restore Defaults" → `初期設定に戻す`,
  "Try again" → `再試行`. An action button takes the noun when Japanese
  software has one (`インストール`, `削除`, `更新`, `再試行`, `キャンセル`),
  and else the plain dictionary form, as Japanese software writes it
  (`閉じる`, `戻る`, `フォルダーを開く`).
- Short status words: `済み / 中 / 未〜` and bare nouns.
  "Installed" → `インストール済み`, "Downloading" → `ダウンロード中`,
  "Not found" → `見つかりません`, "Failed" → `失敗`, "Waiting" → `待機中`,
  "Off" → `オフ`, "On" → `オン`.
- Mission briefings and in-fiction messages (HQ talking to the Commander):
  military register, decided once. Orders end in `〜せよ`, statements in
  だ・である. "Take your units to the Gate and secure it." →
  `部隊を率いてゲートへ向かい、これを確保せよ。` "Core will have adapted as
  well." → `COREもまた適応しているはずだ。` The tips of the Battle Tactics
  briefings (Suggestions, Battle Tactics) keep だ・である: "press the 'A' key
  to bring up the Attack cursor" → `「A」キーを押すと攻撃カーソルが出る。`
  Headings in them are nouns: Suggestions → `助言`, Battle Tactics →
  `戦術`, INFO FEED / INTEL FEED → `情報`, END → `以上`, MISSION →
  `ミッション` (its code kept: `ミッション 1.0001ARME`, `ミッション T01: `),
  PRIORITY → `優先`, PRIORITY 1 → `優先度1`, PRIORITY CRITICAL → `最優先`,
  SPECIAL PRIORITY → `特別優先`, WARNING → `警告`, Emergency → `緊急事態`.
- CORE's briefings speak as a cold machine: INTELL-TAP → `情報傍受`, DO SO
  NOW. → `ただちに実行せよ。`, Arm vermin → `ARMの害虫ども`.
- The units' own speech and the message log (`Unit lost`, `Commander under
  attack`): short noun phrases or plain だ・である, never です・ます.
- Never あなた or 君. Leave the subject out, as Japanese does; if one is
  needed, use プレイヤー (interface) or コマンダー (fiction).
- English capitals (OPEN FOLDER, SETTINGS) have no Japanese equivalent:
  translate normally. Keep Latin acronyms and key names as written: SHIFT,
  Shift, CTRL, ALT, ESC, Esc, TCP, IP, CD, DirectPlay, GPU, fps, KB, MB, GB,
  HTTP, HTTPS, ID, HUD, AI.
- No spaces between Japanese words, and none between Japanese and a Latin
  word or a number (`2 GBのメモリ`, `ARMの部隊`, `MODを読み込む`). A space the
  English puts between a number and its Latin unit stays (`3.5 MB`,
  `60 fps`).
- Punctuation: Japanese punctuation in Japanese text, full-width:
  `、。「」（）！？：・〜`. A full sentence ends in `。`. English quotes
  " " and ' ' become `「」`. Parentheses are full-width `（）` around
  Japanese text and around a slot that sits in Japanese text
  (`（{size}）`). Keep `…` or `...` as the English writes it, `›` in menu
  paths (`設定 › ダウンロード`), and the separators `·`, `→`, `✓`, `✕`, `—`,
  `/` as the English has them. Never write `;` or `；` anywhere (the table
  format ends a value at `;`): split the sentence with `。` or use `、`.
- Digits are half-width (`3分`, `2倍`, `16x16`), counters follow the number
  with no space (`3個`, `5分`, `2倍`, `8人`).

## 2. Placeholders and numbers (hard rules)

- Every placeholder of the English stays, exactly as written: `{name}`,
  `{size}`, `{To}`, `{From}`, `%s`, `%d`, `%i`, `%.1f`, `%%`, `%1$s` and so
  on. Never translate, drop, add, or respell one.
- printf conversions (`%s`, `%d`, …) must stay in the same ORDER as in the
  English, because they are filled in that order. Reword the sentence
  around them if needed. `{name}` slots may move freely, and usually do:
  Japanese puts the object before the verb (`Remove {name}?` →
  `{name}を削除しますか？`).
- Particles after a slot need no care: `{name}を`, `{name}が`, `{name}は`,
  `{name}の`, `{name}から` read right whatever the value. A count takes its
  counter: `{count}個`, `{n}分`, `{count}件`.
- Every number written in digits in the English stays (`1/32`, `2x`,
  `3.1c`, `16x16`, `9 x 21`).
- Staged captions written with `|` (`Easy|Medium|Hard`): keep exactly the
  same number of `|` stages, each translated in order.
- A tab or line break never goes into a translation.

## 3. Names kept as written

- **ARM** and **CORE**, the two sides: always Latin capitals, whatever the
  English case (Arm, Core, ARM, CORE). `COREの部隊`, `ARMコマンダー`.
- Open Annihilation, OA, Core Prime (the service and registry), Total
  Annihilation, Total Annihilation: The Core Contingency, Total
  Annihilation: Battle Tactics (and The Core Contingency, Battle Tactics
  alone), Cavedog Entertainment, GT Interactive, Steam, GOG, Windows,
  macOS, Linux, DirectX, DirectPlay: as written.
- MOD in Latin capitals, as Japanese players write it (`MOD`, `MODを有効にする`).
- File names, folder names, extensions, keys, URLs, version strings
  (`3.1c`, `oamod.yaml`, `totala1.hpi`, `.oalang`): as written.

## 4. Fiction: places and names

Invented names in katakana, after the English sound, with `・` between the
words of a name; ordinary words translated.

| English | Japanese |
|---|---|
| Core Prime (the CORE home planet, in the fiction) | COREプライム |
| Empyrrean | エンピリアン |
| Galactic Gate / the Gate | 銀河ゲート / ゲート |
| Thalassean | タラシアン |
| Tergiverse IV | ターギバースIV |
| Barathrum | バラスラム |
| Rougpelt | ルーグペルト |
| Aqueous Minor | アクエウス・マイナー |
| Aegus | イーガス |
| Dump (moon of Core Prime) | ダンプ |
| Hydross | ハイドロス |
| Lusch | ラッシュ |
| Temblor | テンブラー |
| Gelidus | ジェリダス |
| Krogoth | クロゴス |
| Central Consciousness | 中央意識体 |
| Larab Harbor | ララブ港 |
| Bromid Maze | ブロミッド迷路 |
| Brooban's Isle | ブルーバン島 |
| Motien Ramp | モティエン斜路 |
| Xantippe's Abyss | ザンティッペの深淵 |
| Slolam Pilago | スロラム・ピラゴ |
| Isle Parche | パーチ島 |
| Vebreen Fleet | ヴェブリーン艦隊 |
| Landown's Interface | ランダウン断層 |
| the Abutment (Rougpelt) | アバットメント |
| Serpent (the life-form of Hydross) | サーペント |
| the Arm/Core war | ARMとCOREの戦争 |
| patterning (CORE's transfer of minds into machines) | パターニング |
| nanolathe, nanolathing | ナノ旋盤、ナノ旋盤による建造 |
| HQ, command | 司令部 |
| Crustal 12 (a crust plate of Barathrum, Core Prime and others) | 地殻プレート12 |
| the contingent / contingency Core Commander | COREの予備コマンダー |
| the Gauntlet (Aqueous Minor) | 死の海峡 |
| Nigh Pilago | ナイ・ピラゴ |
| Vebreen Atoll | ヴェブリーン環礁 |
| Central Plaza, Command Dome | 中央広場、司令ドーム |
| Aqueous Body 397, Port Complex .016 | 第397水域、港湾施設.016 |
| Scorpion (the life-form of Lusch) | スコーピオン |
| implosion device, the beacon | 爆縮装置、ビーコン |

## 5. Game terms

| English | Japanese |
|---|---|
| Commander | コマンダー |
| unit | ユニット |
| building, structure | 建物 |
| Kbot, KBot | Kボット |
| vehicle | 車両 |
| tank | 戦車 |
| aircraft, plane | 航空機 |
| ship | 艦船 (a class), 船 (in a name: 建設船) |
| submarine, sub | 潜水艦 |
| hovercraft | ホバークラフト |
| seaplane | 水上機 |
| amphibious | 水陸両用 |
| builder (a unit that builds) | 建設ユニット |
| factory, plant | 工場 |
| lab (Kbot Lab) | ラボ |
| shipyard | 造船所 |
| metal | 金属 |
| energy | エネルギー |
| resources | 資源 |
| storage | 貯蔵量 (amount), 貯蔵庫 (building) |
| income / production | 収入 / 生産量 |
| metal extractor (mex) | 金属抽出機 |
| metal maker | 金属変換機 |
| solar collector | 太陽光発電機 |
| wind generator | 風力発電機 |
| tidal generator | 潮力発電機 |
| fusion reactor / fusion power plant | 核融合炉 / 核融合発電所 |
| geothermal | 地熱 |
| radar | レーダー |
| sonar | ソナー |
| jammer (radar/sonar) | 妨害装置 (レーダー妨害装置, ソナー妨害装置) |
| line of sight, LOS | 視界 |
| cloak, cloaked, decloak | クローク, クローク中, クローク解除 |
| stealth | ステルス |
| wreck, wreckage, corpse | 残骸 |
| feature (rocks, trees, wrecks on a map) | 地形物 |
| laser | レーザー |
| plasma | プラズマ |
| missile / rocket | ミサイル / ロケット |
| artillery | 砲兵 (unit), 砲 (gun), 自走砲 (Mobile Artillery) |
| flak | 対空砲 |
| torpedo | 魚雷 |
| depth charge | 爆雷 |
| mine (land / sea) | 地雷 / 機雷 |
| nuke, nuclear missile | 核ミサイル |
| anti-nuke, missile defense | 核迎撃, ミサイル防衛 |
| EMP | EMP |
| D-Gun (Disintegrator Gun) | Dガン (ディスインテグレーター・ガン) |
| anti-air | 対空 |
| ally, alliance | 同盟 (a player: 同盟プレイヤー) |
| enemy | 敵 |
| team | チーム |
| kills / losses | 撃破 / 損失 |
| veteran / newbie | ベテラン / 新兵 |
| victory / defeat | 勝利 / 敗北 |
| paused | 一時停止 |
| Tech Level 1 / 2 | 技術レベル1 / 技術レベル2 |
| Adv., Advanced (unit names) | 上級 |
| build menu | 建設メニュー |
| control group (select groups) | グループ (グループ登録, グループ選択) |
| selection, select | 選択 |
| waypoint | 経由地点 |
| queue (orders, building) | 予約 |
| self-destruct | 自爆 |

### Orders (buttons and their states; also used in touch controls)

| English | Japanese |
|---|---|
| ATTACK | 攻撃 |
| MOVE | 移動 |
| STOP | 停止 |
| PATROL | 巡回 (patrolling: 巡回中) |
| DEFEND / GUARD | 護衛 (guarding: 護衛中) |
| RECLAIM | 回収 |
| REPAIR | 修理 |
| CAPTURE | 捕獲 |
| LOAD / UNLOAD (transports) | 搭載 / 降車 |
| ORDERS | 命令 |
| BUILD | 建設 |
| BLAST / D-GUN | Dガン |
| ASSIST | 支援 |
| QUEUE / ADD (touch) | 予約 / 追加 |
| Fire orders: Hold Fire / Return Fire / Fire At Will | 射撃命令: 射撃中止 / 反撃 / 自由射撃 |
| VISIBLE / CLOAKED (the cloak toggle) | 可視 / クローク中 |
| Move orders: Hold Position / Maneuver / Roam | 移動命令: 現在地を固守 / 機動 / 自由移動 |
| On / Off (a unit) | オン / オフ |
| Activate / Deactivate | 起動 / 停止 |
| Resurrect | 蘇生 |
| Patrolling / Guarding (builders) | 巡回中 / 護衛中 |

## 6. Menus and modes

| English | Japanese |
|---|---|
| Single Player | シングルプレイ |
| Multiplayer | マルチプレイ |
| Campaign | キャンペーン |
| Mission | ミッション |
| Briefing | ブリーフィング |
| Skirmish | スカーミッシュ |
| Battle Room | 対戦ルーム |
| Lobby / Lounge | ロビー / ラウンジ |
| host / join | ホスト / 参加 |
| player | プレイヤー |
| computer player, AI | コンピューター (3.1c's "Computer"), AI ("AI") |
| watcher, spectator / watch | 観戦者 / 観戦 |
| replay | リプレイ |
| recorder, recording | レコーダー, 録画 |
| saved game / save / load | セーブデータ / セーブ / ロード |
| Options | オプション |
| Settings | 設定 |
| Preferences | 環境設定 |
| Previous Menu / Back | 前のメニュー / 戻る |
| Main menu / Game menu | メインメニュー / ゲームメニュー |
| Exit, Quit | 退出 (leave a screen or a game), 終了 (quit the program) |
| Exit to the system | システムに戻る |
| Narration / No Narration (the briefing's toggle) | 音声あり / 音声なし |
| OK / Cancel / Done / Close / Apply | OK / キャンセル / 完了 / 閉じる / 適用 |
| Yes / No | はい / いいえ |
| Retry, Try again | 再試行 |
| Continue | 続行 |
| Easy / Medium / Hard | イージー / ノーマル / ハード |
| Help | ヘルプ |
| Chat | チャット |
| Cheats | チート |
| game speed | ゲーム速度 |
| Sound / Music / Volume / Movies | サウンド / 音楽 / 音量 / ムービー |
| Credits | クレジット |
| Intro | イントロ |

## 7. Open Annihilation's interface

| English | Japanese |
|---|---|
| Library | ライブラリ |
| mod | MOD |
| mod profile | MODプロファイル |
| hacks, standard hacks (engine behaviour a mod switches on) | ハック, 標準ハック |
| map / map pack | マップ / マップパック |
| language pack | 言語パック |
| expansion | 拡張パック |
| base game | ベースゲーム |
| registry (a server listing packages) | レジストリ |
| catalogue | カタログ |
| package | パッケージ |
| download / install / update / uninstall | ダウンロード / インストール / 更新 / アンインストール |
| remove / delete | 削除 |
| version / revision | バージョン / リビジョン |
| roll back | ロールバック |
| folder / file / archive | フォルダー / ファイル / アーカイブ |
| game files / game folder / game archives | ゲームファイル / ゲームフォルダー / ゲームアーカイブ |
| device | デバイス |
| free (space) | 空き (`{size} free` → `空き{size}`) |
| screen / window / full screen | 画面 / ウィンドウ / フルスクリーン |
| zoom, zoom in / out | ズーム, ズームイン / ズームアウト |
| graphics | グラフィック |
| hardware acceleration | ハードウェアアクセラレーション |
| vertical sync | 垂直同期 |
| anti-aliasing | アンチエイリアス |
| frame rate | フレームレート |
| resolution | 解像度 |
| modern fonts | モダンフォント |
| font / text size | フォント / 文字サイズ |
| controller / trackpad / stick / gyro / D-pad | コントローラー / トラックパッド / スティック / ジャイロ / 十字キー |
| touch | タッチ |
| haptics | 振動 |
| pointer | ポインター |
| Developer Mode | 開発者モード |
| Language / System default | 言語 / システムの設定 |
| snap (click snap) | スナップ |
| the host (of a shared game) | ホスト |
| shared game / network play | 共有ゲーム / ネットワーク対戦 |
| HUD | HUD |
| Unicode | Unicode |
| install ID | インストールID |
| demo | 体験版 |
| screenshot | スクリーンショット |
| saves (a folder) | セーブ |

## 8. Unit names

Generic names are translated; proper names are written in katakana. Use
these exactly, in units.tdf and wherever a unit is named (briefings, help,
messages).

Generic: Adv. Aircraft Plant 上級航空機工場 · Adv. Construction Aircraft
上級建設航空機 · Adv. Construction Kbot 上級建設Kボット · Advanced
Construction Sub 上級建設潜水艦 · Adv. Construction Vehicle 上級建設車両 ·
Adv. Kbot Lab 上級Kボットラボ · Aircraft Plant 航空機工場 · Advanced Radar
Tower 上級レーダー塔 · Advanced Sonar Station 上級ソナー基地 · Air Repair Pad
航空機修理パッド · Adv. Shipyard 上級造船所 · Advanced Torpedo Launcher
上級魚雷発射機 · Adv. Vehicle Plant 上級車両工場 · Alien Beacon 異星ビーコン ·
Construction Aircraft 建設航空機 · Construction Hovercraft 建設ホバークラフト
· Construction Kbot / KBot 建設Kボット · Cloakable Fusion Reactor
クローク式核融合炉 · Commander コマンダー · Construction Ship 建設船 ·
Construction Seaplane 建設水上機 · Construction Vehicle 建設車両 · Decoy
Commander デコイ・コマンダー · Implosion Device 爆縮装置 · Dragon's Teeth
竜の歯 · Floating Dragon's Teeth 浮遊式竜の歯 · Energy Storage
エネルギー貯蔵庫 · Floating Metal Maker 浮遊式金属変換機 · Fortification Wall
防壁 · Fusion Reactor 核融合炉 · Fusion Power Plant 核融合発電所 · Galactic
Gate 銀河ゲート · Geothermal Powerplant 地熱発電所 · Hovercraft Platform
ホバークラフト基地 · Kbot Lab Kボットラボ · L.L.T. L.L.T. · Light Laser Tower
軽レーザー塔 · Heavy Laser Tower 重レーザー塔 · Metal Maker 金属変換機 · Metal
Extractor 金属抽出機 · Area Mine 広域地雷 · Focused Mine 集中地雷 · HE Area
Mine HE広域地雷 · Precision Mine 精密地雷 · Nuclear Mine 核地雷 · Moho Metal
Maker モホ金属変換機 · Moho Mine モホ鉱山 · Metal Storage 金属貯蔵庫 ·
Seaplane Platform 水上機基地 · Radar Tower レーダー塔 · Solar Collector
太陽光発電機 · Sonar Station ソナー基地 · Shipyard 造船所 · Targeting
Facility 照準施設 · Tidal Generator 潮力発電機 · Torpedo Launcher 魚雷発射機 ·
Underwater Energy Storage 水中エネルギー貯蔵庫 · Underwater Fusion Plant
水中核融合発電所 · Underwater Metal Extractor 水中金属抽出機 · Underwater
Metal Storage 水中金属貯蔵庫 · Vehicle Plant 車両工場 · Wind Generator
風力発電機 · Hydration Plant 給水プラント · Fortitude Missile Defense
フォーティチュード・ミサイル防衛 · Krogoth Gantry クロゴス・ガントリー · Gaat
Gun ガート・ガン · Mobile Artillery 自走砲 · Missile Frigate
ミサイルフリゲート · Resurrection Kbot 蘇生Kボット · Defender - NS
ディフェンダー - NS · M-104, M-209, M-303, M-420, M-515, M-610 as written ·
FARK FARK · A.K. A.K.

Proper (katakana): Archer アーチャー · Swatter スワッター · Ambusher
アンブッシャー · Protector プロテクター · Pelican ペリカン · Anaconda アナコンダ ·
Annihilator アナイアレイター · Eraser イレイザー · Atlas アトラス · Eagle イーグル
· Millenium ミレニアム · Brawler ブロウラー · Big Bertha ビッグ・バーサ ·
Bulldog ブルドッグ · Colossus コロッサス · Triton トリトン · Conqueror
コンカラー · Stunner スタナー · Zipper ジッパー · Jeffy ジェフィー · Stingray
スティングレイ · Fido ファイドー · Freedom Fighter フリーダム・ファイター ·
Flakker フラッカー · Flash フラッシュ · Flea フリー · Guardian ガーディアン ·
Hammer ハンマー · Hawk ホーク · Sentinel センチネル · Jammer ジャマー · Jethro
ジェスロ · Lancet ランセット · Panther パンサー · Penetrator ペネトレーター ·
Marky マーキー · Luger ルガー · Maverick マーベリック · Merl マール · Wombat
ウォンバット · Tiny タイニー · Podger ポッジャー · Ranger レンジャー · Peeper
ピーパー · Phoenix フェニックス · Skeeter スキーター · Peewee ピーウィー ·
Defender ディフェンダー · Rocko ロッコ · Crusader クルセイダー · Samson サムソン
· Scarab スカラベ · Scorpion スコーピオン · Fibber フィバー · Albatross
アルバトロス · Seer シーア · Seahawk シーホーク · Tornado トルネード · Skimmer
スキマー · Retaliator リタリエイター · Escort エスコート · Shooter シューター ·
Spider スパイダー · Infiltrator インフィルトレーター · Sea Serpent
シーサーペント · Stumpy スタンピー · Lurker ラーカー · Piranha ピラニア · Bear
ベア · Thunder サンダー · Hulk ハルク · Invader インベーダー · Vulcan バルカン ·
Warrior ウォーリアー · Phalanx ファランクス · Zeus ゼウス · Slinger スリンガー ·
Gimp ギンプ · Rapier レイピア · Shredder シュレッダー · Vulture バルチャー ·
Warlord ウォーロード · Buzzsaw バズソー · The Can ザ・カン · Hive ハイヴ ·
Crasher クラッシャー · Executioner エクスキューショナー · Doomsday Machine
ドゥームズデイ・マシン · Deleter デリーター · Freaker フリーカー · Weasel
ウィーゼル · Thunderbolt サンダーボルト · Fink フィンク · Cobra コブラ ·
Stinger スティンガー · Instigator インスティゲーター · Goliath ゴリアテ ·
Dominator ドミネーター · Hunter ハンター · Hurricane ハリケーン · Intimidator
インティミデーター · Krogoth クロゴス · Leveler レベラー · Hedgehog ヘッジホッグ ·
Nixer ニクサー · Slasher スラッシャー · Spoiler スポイラー · Morty モーティ ·
Immolator イモレーター · Searcher サーチャー · Punisher パニッシャー · Pyro パイロ
· Raider レイダー (not レーダー, which is radar) · Reaper リーパー ·
Pulverizer パルヴァライザー · Roach ローチ · Enforcer エンフォーサー · Crock
クロック · Typhoon タイフーン · Copperhead カッパーヘッド · Voodoo ブードゥー ·
Scrubber スクラバー · Shadow シャドウ · Shark シャーク · Silencer サイレンサー ·
Phantom ファントム · Snapper スナッパー · Spectre スペクター · Parasite
パラサイト · Leviathan リヴァイアサン · Storm ストーム · Snake スネーク · Sumo
スモウ · Turtle タートル · Thud サッド · Titan タイタン · Toaster トースター ·
Neutron ニュートロン · Truck トラック · Envoy エンヴォイ · Valkyrie ヴァルキリー ·
Vamp ヴァンプ · Avenger アベンジャー · Viper ヴァイパー · Voyeur ヴォワイヤー ·
Informer インフォーマー · Diplomat ディプロマット.

Unit classes in descriptions: Bomber 爆撃機 · Fighter 戦闘機 · Stealth
Fighter ステルス戦闘機 · Strategic Bomber 戦略爆撃機 · Torpedo Bomber 雷撃機 ·
Gunship ガンシップ · Scout / Air Scout 偵察機 (air), 偵察車両 (ground) · Radar
Plane レーダー機 · Transport 輸送機 (air) / 輸送船 (sea) · Battleship 戦艦 ·
Cruiser 巡洋艦 · Destroyer 駆逐艦 · Frigate フリゲート · Submarine 潜水艦 ·
(Light) Carrier (軽)空母 · Light / Medium / Heavy Tank 軽戦車 / 中戦車 /
重戦車 · Amphibious Tank 水陸両用戦車 · Infantry Kbot 歩兵Kボット · Assault
Kbot 突撃Kボット · Artillery Kbot 砲兵Kボット · Missile Tower ミサイル塔 ·
Plasma Battery プラズマ砲台 · Energy Weapon エネルギー兵器 · Mine Layer
地雷敷設 · Radar Vehicle レーダー車両 · Produces Aircraft / Kbots / Vehicles /
Ships 航空機を生産 / Kボットを生産 / 車両を生産 / 艦船を生産 · Produces Energy
エネルギーを生産 · Produces Metal 金属を生産 · Extracts Metal 金属を抽出 ·
Increases Energy Storage エネルギー貯蔵量を増加 · Increases Metal Storage
金属貯蔵量を増加 · Indigenous Lifeform 原生生物.

## 9. Width

Kana and kanji are drawn full-width, at least 12 px each, as wide as the
Chinese pack's characters. Captions on 3.1c's fixed-size buttons (its menus'
buttons, tabs, short labels) must stay short: about as many characters as
the Chinese has, at most about 1.5 times. Katakana loanwords are longer
than the Chinese, so on a button prefer the kanji compound
(`攻撃`, `建設`, `巡回`, `設定`) and the shortest natural wording: `開始` over
`ゲームを開始`, `ロード` over `ゲームをロード` when the screen already says
"game", and drop a name's `・` where it is tight. Sentences in dialogs and
hints may be as long as they need to be.

Captions shortened for 3.1c's fixed-size spots: the battle room's Cmdr
column → `司令`, the briefing's narration toggle → `音声あり / 音声なし`,
Battle Tactics' campaign lengths Very Short / Short / Medium / Long →
`超短編 / 短編 / 中編 / 長編`, the order buttons' captions → the kanji
word and the hotkey letter in half-width parentheses (`攻撃(A)`), as
Japanese software marks its menus' keys.

## 10. Keys

One word for each idea, in the key editor, the overlay, Settings › Controls,
Settings › Accessibility, Library › Keys and the install question.

| English | Japanese |
|---|---|
| key layout | キー配置 |
| key editor | キーエディター |
| action (a binding; also where English still says "command" for one) | アクション |
| changes of your own | 自分の変更 |
| clash | 競合 |
| latch / latched | 固定 / 固定中 |
| letter (of a key) | 文字 |
| place (of a key) | 位置 |
| hold to confirm | 長押しで確定 |

Named keys as a Japanese keyboard prints them. Shift, Ctrl, Alt, Esc,
Escape, Tab, Enter, Backspace, Delete, Insert, Home, End, Page Up, Page Down,
Caps Lock, F1–F12 and Win stay Latin. The rest:

| English | Japanese |
|---|---|
| Space | スペース |
| Arrow up / down / left / right | 上矢印 / 下矢印 / 左矢印 / 右矢印 |
| Numpad | テンキー |
| Convert | 変換 |
| Non convert | 無変換 |
| Kana mode | かな |
| Intl yen | ¥ |
| Intl ro | ろ |
| Left / Right / Middle button | 左ボタン / 右ボタン / 中ボタン |
| Wheel up / down | ホイール上 / ホイール下 |
