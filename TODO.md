# To do

## Portuguese (`pt-BR` and `pt-PT`)

Both packs are complete and check clean: every interface word of 0.8.9,
3.1c's texts, the units, the missions and the 175 briefings, fitting every
screen the text-fit check measures. These are what is left, most important
first. `python3 tools/screens.py <tag> …` (see
[adding a language, step 9](docs/new-language.md#9-look-at-it-in-the-game))
shows each problem on screen.

### 1. 3.1c's menu buttons draw a box for some Portuguese letters (engine; fixed for the next release)

**What the player sees** with engine 0.8.9. On 3.1c's own buttons and
labels, a box in place of a letter: `Opç□es` on the single-player menu,
`OP□□ES` and `Definiç□es` on the in-game menu, `Posiç□o` and
`Linha de vis□o` in the skirmish setup, `Sem narraç□o` on the briefing's
narration button, `Miss□o/mapa` in the load dialog, and in the European
pack `Tamanho do ecr□` in the visual options. The letters hit are ã, õ, Ã,
Õ, Ç, Â, Ê, Ô and À. Briefings, help and Open Annihilation's own screens
draw every letter.

**The cause.** 3.1c's menu fonts, `anims/hattfont12.GAF` and
`anims/hattfont11.GAF` (every copy: `totala1.hpi`, `ccdata.ccx`,
`btdata.ccx`, `rev31.gp3`), hold a box in those letters' Windows-1252
slots, the same picture as the font's frame 0. The engine's 3.1c screens
draw these fonts as FNT fonts read from their GAF
(`formats::fnt::parse_gaf`), and `frontend_renderer::fnt_font_characters`
counted such a font as an FNT font: every glyph a letter, at the FNT
fonts' slots, with no comparison to frame 0. So the boxes counted as
letters, and Ç took its box at `0xC7` instead of the real Ç in the DOS
slot `0x80`. The sprite paths (`gui_font_characters`, and gadget-render's
`font_characters` over `dialog_art.cpp`'s frames) were already right.

**The fix** is engine commit `a37729da`, for the release after 0.8.9:
`parse_gaf` marks its font `gaf_backed`, and `fnt_font_characters` reads
such a font as a GUI font, at the GUI fonts' slots and without the
glyphs that are frame 0's picture. A caption with such a letter is then
drawn whole in the modern fonts. `frontend-gadget-draw` covers a GUI
font whose placeholder glyphs equal glyph 0, and
`frontend-artless-draw-data` the installed fonts. With that build,
`tools/screens.py pt-PT` shows `Opções`, `Definições`, `Posição`,
`Linha de visão`, `Tamanho do ecrã`, `Missão/mapa:` and `Sem narração`
whole. `OPÇÕES` is on none of the pictures.

**Left:** the engine release that carries the fix. The packs need no
change.

### 2. A native speaker's reading

Neither pack has been read by a Brazilian or a Portuguese player. The
Brazilian pack's first revision was translated in one pass, and the words
of 0.8.5 to 0.8.9 in a second; the European pack was translated from the
English beside the Brazilian. Both follow their glossaries
(`docs/glossaries/pt-BR.md`, `docs/glossaries/pt-PT.md`). The choices made
with least certainty are under "Words to look at with native speakers".

## Words to look at with native speakers

The packs' translator was unsure of these, and gave reasons. Each line is
the English, the translation the pack uses, and why.

### Brazilian Portuguese (pt-BR)

- `Briefing` kept as a loanword, `Destróier`, `ABERTURA` for INTRO,
  `Sim`/`Não` for 3.1c's On/Off (as its French and Italian do), and
  `RECICLAR` for reclaim rather than `RECUPERAR`.
- The Serpent and the Scorpion left in English in the briefings, and every
  unit's proper name left in English (Peewee, Big Bertha) while the generic
  names are translated.
- "brain": cérebro, as the engine's German and French say it. Rush, Turtle,
  Learned and Teaching are Rush, Defensivo, Treinado and Didático.
- "seat" (a player's place): lugar. `vaga` is the other choice.
- "Held:" before a modifier's description: Segurada:. "hold" and "double"
  gestures: pressão longa, pressão dupla.
- "Bounce keys" and "Sticky modifiers": Teclas de ricochete and
  Modificadores aderentes. The systems' own names may differ.
- "Hold keys that latch": Teclas de segurar que fixam, which reads clumsily.
- The battle room's mutators button is Mutadores · desl. and Mutadores ·
  {count} lig.; Mutadores alone does not leave room for the state.
- "Turn every helper off": Desativar auxiliares, shortened to fit
  Settings › Accessibility.
- "Select Map": Escolher, as the map chooser's own button is too narrow for
  Escolher mapa.

### European Portuguese (pt-PT)

- The same choices as the Brazilian pack for the briefings, the unit names,
  INTRO, On/Off, RECICLAR and the brains.
- "view" (the part of the map on screen): vista, where the Brazilian pack
  says visão.
- "Return Fire" and "Roam": Ripostar and Vaguear.
- "Decoy Commander": Comandante Chamariz.
- "the Gauntlet" (Core mission 10): O Corredor de Fogo, since Corredor da
  Morte means death row in Portugal.
- "You", the score screen's row beside "AI Player": Jogador.
- "Seeking to attack / defend / guard / land": A ir atacar, A ir defender,
  A ir proteger, A ir aterrar.
- "Next": Seguinte, one letter longer than the Brazilian Próximo.
- "Antialias": Anti-aliasing, the loanword Portugal's players use.
- "Include in device backups": Incluir nas cópias de segurança, shortened
  to fit the game-files screen.
- "Hold keys that latch": Teclas de manter que fixam, which reads clumsily.
- "software centre": centro de software. "Edge scrolling": Deslocação pela
  margem.

### Japanese (ja)

- "brain": ブレイン, a loanword. A Japanese word for a computer player's mind
  did not read as the thing the Library installs.
- "computer player": コンピューター, as 3.1c's Computer. Spelling out
  「コンピュータープレイヤー」 would say the same thing twice beside ブレイン.
- Rush ラッシュ, Turtle 籠城, Learned 学習型, Teaching 指導型. Turtle is 籠城
  (holding a position), not タートル, which is also an animal.
- "Full 3D Mode": フル3Dモード. The label is フル3Dモードを許可.
- "Clone" (the key editor's Duplicate…, now Clone as New Layout…): クローン.
  複製 is the pack's old word for Duplicate, and a clone here is a key layout
  of the player's own. A player may still expect 複製.
- "WORLD", the Library heading over world tags, and "World: {tag} ({count})":
  ワールド and ワールド：{tag}（{count}）, parallel to タグ. The pack had no
  word for a mod's world.
- "Option", the name a Mac gives the Alt key: Alt, the key the pack and the
  glossary already name. A Mac's key is printed Option.
- "Ready when you are", the sample line in Arrange overlays' chat: 準備できたらどうぞ.
- The battle room's mutators button is ミューテ · オフ and ミューテ · {count}オン.
  ミューテーター does not fit on the button. The rest of the pack still says ミューテーター.
- "Paste Someone's Layout…": 他の人のキー配置を貼り付け…. 相手 would read as
  an opponent in a game.
- "New unit shadows": ユニットの新しい影, so it does not read as the shadows
  of new units.
- "rev", the English's short form ("{version} · rev {revision}" and the two
  like it): Rev., where "revision" spelt out stays リビジョン. リビジョン left no
  room for a mod's name in the Library's narrower list.

### Korean (ko)

- "brain": 브레인, a loanword, for the same reason as the Japanese.
- "computer player": 컴퓨터, as 3.1c's Computer.
- Rush 러시, Turtle 수비형, Learned 학습형, Teaching 교육용. Turtle is 수비형
  (a defensive style), not 거북, the animal.
- "Full 3D Mode": 완전 3D 모드, not 전체 ("whole"). The label is 완전 3D 모드 허용.
- "Clone": 복제, the same word the pack used for Duplicate…. Korean does not
  split the two, so the old translation moved with the English.
- "WORLD" and "World: {tag} ({count})": 월드 and 월드: {tag} ({count}),
  parallel to 태그. The pack had no word for a mod's world.
- "Option": Alt, the key the pack already names.
- "Ready when you are": 준비되면 말씀해 주세요.
- "helper": 보조, everywhere now. "Turn every helper off" said 도우미, as two
  of the old key counts did.
- "New unit shadows": 유닛의 새 그림자, so it does not read as a new unit's
  shadows.

### Russian (ru)

- "brain": мозг (and мозги on the Library's tab). As the engine's German and
  French do. Мозги can read a little colloquially.
- "computer player": компьютерный игрок, spelt out, because «встроенный
  компьютер» alone reads as hardware.
- Rush Раш, Turtle Оборона, Learned Обученный, Teaching Обучающий. Turtle is
  Оборона, not Черепаха, which is also a unit's name.
- "Full 3D Mode": полный 3D-режим. The label is Разрешить полный 3D-режим.
- "Clone": Клонировать, where Duplicate… was Дублировать…. The meaning moved
  from a duplicate to a layout of the player's own.
- "WORLD" and "World: {tag} ({count})": МИР (beside ТЕГИ) and Мир: {tag}
  ({count}). The pack had no word for a mod's world.
- "Option": Alt.
- "Ready when you are": По готовности, so the sample chat does not take a
  gender.
- The battle room's mutators button is Мутат. · выкл. and Мутат. · {count}.
  Мутаторы does not fit on the button. The rest of the pack still says мутаторы.
- "From {layout} · {n} keys and {m} helpers changed": Из {layout} · изменено
  клавиш: {n}, помощников: {m}. The counts take a colon, so they need no
  plural forms, and the layout's name follows Из as it is, as in Копия
  {layout} and На основе {layout}.
- "Sharing": Передача, the hacks' word for the area, now also the heading over
  the key editor's Share and Paste.
- "KEYS": КЛАВИШИ, in capitals beside КАРТЫ and ДОПОЛНЕНИЯ, now that it is also
  the key editor's header.
- "In use", the Library's pill: Выбрано, a short participle as the glossary
  has it, as Ukrainian's Обрано. Используется left no room for the pack's own
  name in the Library's narrower list.

### Ukrainian (uk)

- "brain": мозок (and мозки on the Library's tab). Мозки can read a little
  colloquially.
- "computer player": компʼютерний гравець, spelt out, because «вбудований
  компʼютер» alone reads as hardware.
- Rush Раш, Turtle Оборона, Learned Навчений, Teaching Навчальний. Turtle is
  Оборона, not Черепаха, which is also a unit's name.
- "Full 3D Mode": повний 3D-режим. The label is Дозволити повний 3D-режим.
- "Clone": Клонувати, where Duplicate… was Дублювати….
- "WORLD" and "World: {tag} ({count})": СВІТ (beside ТЕГИ) and Світ: {tag}
  ({count}).
- "Option": Alt.
- "Ready when you are": По готовності, so the sample chat does not take a
  gender.
- The battle room's mutators button is Мутат. · вимк. and Мутат. · {count}.
  Мутатори does not fit on the button. The rest of the pack still says мутатори.
- "From {layout} · {n} keys and {m} helpers changed": З {layout} · змінено
  клавіш: {n}, помічників: {m}, for the same reason as the Russian.
- "KEYS": КЛАВІШІ, in capitals beside МАПИ and ДОПОВНЕННЯ, now that it is also
  the key editor's header.

### Simplified Chinese (zh-Hans)

- "brain": 大脑, the mind, not a loanword. The pack already said 大脑 for the
  Library's Brains tab.
- "computer player": 电脑玩家, spelt out.
- Rush 速攻, Turtle 龟缩, Learned 学习, Teaching 教学. Turtle is the RTS
  sense of holing up, not 龟, the animal.
- "Full 3D Mode": 完整3D模式. The label is 允许完整3D模式.
- "Clone": 克隆, where Duplicate… was 复制…. A player may still expect 复制.
- "WORLD" and "World: {tag} ({count})": 世界 and 世界：{tag}（{count}）,
  parallel to 标签.
- "Option": Alt.
- "Ready when you are": 准备好了就说一声.
- "helper": 辅助, everywhere now. "Helpers act in every game" said 辅助键, but
  a helper is a setting, not a key.
- "Layouts", the heading in the key editor's More menu: 按键布局, the
  glossary's word, not 布局 alone.
