# Traditional Chinese (zh-Hant) glossary and style guide

One glossary, one voice. The pack starts from the Simplified Chinese pack
(`docs/glossaries/zh-Hans.md` and `zh-Hans/`) and says it as Taiwan writes
it: the terms differ, not only the character forms (軟體, not 软件 with its
strokes swapped). When a term is listed here, use it as written, every time.
When a term is not listed, keep the simplified pack's sentence and write
each character in the traditional form Taiwan uses for that word.

The face is Noto Sans CJK TC Bold (face 3, not the Hong Kong face). A
character both Chinese faces draw is still taken from this face, so the
regional form is Taiwan's.

## 1. Voice

- The player is 你. An instruction takes 請. A question takes 嗎？.
- 命令 stays the unit order. A key-binding action is 動作, not 命令.
- Labels, buttons and headings stay noun phrases, as the simplified pack
  writes them. Do not add 請 to a button.
- Mission briefings keep the simplified pack's register: HQ talking to the
  commander, 建議 for the suggestions, the colour codes `&Y`, `&R` and `&G`
  left where they are.
- Named keys stay Latin, as the keyboard prints them: Shift, Ctrl, Alt,
  Esc, Tab, Enter, F1–F12, Delete, Home, End, Page Up, Page Down, Win.
- ARM and CORE stay Latin capitals. Open Annihilation, OA, Core Prime,
  Total Annihilation and the expansion names stay as written. File names,
  extensions, URLs and version strings (`3.1c`, `totala1.hpi`, `.oalang`)
  stay as written.
- 橫掃千軍 is this game's Chinese name. Do not rename it.
- A place the simplified pack transliterated stays that spelling in
  traditional characters (叶恩巴库 becomes 葉恩巴庫). Do not invent a new
  spelling.

## 2. Placeholders and numbers

- Every placeholder stays, exactly: `{name}`, `{size}`, `%s`, `%d`, `%i`,
  `%.1f`, `%%` and the rest. Never translate, drop, add or respell one.
- printf conversions stay in the same order as the English. `{name}` may
  move.
- Digits stay digits (`1/32`, `3.1c`, `16x16`).
- A caption written with `|` keeps the same number of stages, in order.
- Never write `;`, `//` or a tab inside a value. The table format ends a
  value at `;`.

## 3. Taiwan terms

| English | Simplified pack | Traditional (Taiwan) |
|---|---|---|
| software | 软件 | 軟體 |
| network (computers) | 网络 | 網路 |
| the internet | 互联网 | 網際網路 |
| a learned network (a brain's) | 网络 | 神經網路 |
| information | 信息 | 資訊 |
| chat message | 聊天信息 | 聊天訊息 |
| message | 消息 | 訊息 |
| default | 默认 | 預設 |
| settings (the noun) | 设置 | 設定 |
| set up (a factory, a group, a path) | 设置 | 設置 |
| memory (RAM) | 内存 | 記憶體 |
| mouse | 鼠标 | 滑鼠 |
| screen | 屏幕 | 螢幕 |
| resolution | 分辨率 | 解析度 |
| disk | 磁盘 | 磁碟 |
| hard disk | 硬盘 | 硬碟 |
| disc | 光盘 | 光碟 |
| keyboard | 键盘 | 鍵盤 |
| server | 服务器 | 伺服器 |
| folder | 文件夹 | 資料夾 |
| file | 文件 | 檔案 |
| computer | 计算机 | 電腦 |
| dialog | 对话框 | 對話方塊 |
| copy | 复制 | 複製 |
| compatible | 兼容 | 相容 |
| online / offline | 在线 / 离线 | 線上 / 離線 |
| networked play | 联机 | 連線 |
| interface | 界面 | 介面 |
| log | 日志 | 日誌 |
| menu | 菜单 | 選單 |
| window | 窗口 | 視窗 |
| user | 用户 | 使用者 |
| link | 链接 | 連結 |
| load | 加载 | 載入 |
| save | 保存 | 儲存 |
| activate | 激活 | 啟用 |
| support | 支持 | 支援 |
| data | 数据 | 資料 |
| search | 搜索 | 搜尋 |
| paste / cut | 粘贴 / 剪切 | 貼上 / 剪下 |
| clipboard | 剪贴板 | 剪貼簿 |
| print | 打印 | 列印 |
| quit / exit | 退出 | 結束 |
| finish or leave | 结束或退出 | 結束或離開 |
| thread | 线程 | 執行緒 |
| port | 端口 | 連接埠 |
| driver | 驱动 | 驅動程式 |
| program | 程序 | 程式 |
| a sequence (自毀, 內爆) | 程序 | 程序 |
| uninstall | 卸载 | 解除安裝 |
| unload | 卸载 | 卸載 |
| Help (the button) | 帮助 | 說明 |
| help (the verb, a help file) | 帮助 / 帮助文件 | 幫助 / 說明檔案 |
| video recording, replay, film | 录像 | 錄影 |
| capture a movie | 录制影片 | 錄製影片 |
| movie | 影片 | 影片 |
| custom | 自定义 | 自訂 |
| shortcut (a file) | 快捷方式 | 捷徑 |
| shortcut key | 快捷键 | 快速鍵 |
| icon | 图标 | 圖示 |
| variable | 变量 | 變數 |
| queue | 队列 | 佇列 |
| laser | 激光 | 雷射 |
| quality | 质量 | 品質 |
| video (a setting) | 视频 | 視訊 |

Click stays the simplified pack's verbs, in traditional characters:
點按, 單擊, 點擊, 雙擊. Do not rewrite them as 按一下. The order-button
captions are two hanzi plus the letter (`卸載U`, `攻擊A`), and
`啟用|停用` stays two and two.

## 4. Characters that do not take the other traditional form

Unihan lists a second traditional form for these. The pack keeps the form
Taiwan writes for the word, and a phrase in section 3 covers the cases
that change.

| Stays | Changes, by the phrase |
|---|---|
| 干 in 干擾, 若干 | 乾燥, 乾脆, 乾旱 |
| 刮 in 搜刮 | (颳 is wind; the pack has none) |
| 后 as 後, except 皇后, 太后, 王后 | |
| 里 as 裡, except 公里, 海里, 英里 | |
| 面, 系 in 系統, 只 as "only" | 艦隻, 船隻; 關係, 聯繫 |
| 制 in 控制, 限制, 強制 | 製造, 製作, 複製, 繪製, 標誌 |
| 复 as 復 in 恢復, 修復 | 複雜, 重複, 複製; 覆蓋, 反覆 |
| 发 as 發 | 頭髮, 毛髮 |
| 卷 | 席捲, 捲起, 捲土重來 |
| 借 in 借調 | 藉助 |
| 舍 in 舍伍德 | 窮追不捨 |
| 游 is not a blanket 遊 | 遊戲, 遊擊, 漫遊, 遊玩, 遊騎兵 |
| 台 as 臺 | 颱風, 臺灣 |
| 松 as 鬆 in 鬆開, 輕鬆 | |
| 范 as 範 in 範圍 | |
| 斗 as 鬥 in 戰鬥 | 漏斗, 北斗 stay 斗 |
| 谷, 折, 征, 向, 蒙, 板, 曲, 表, 旋, 注 in 注意 | 註冊, 註釋, 備註 |

## 5. Unit names

Unit names are the simplified pack's names in the forms above. Ranger
(游骑兵导弹舰) is 遊騎兵導彈艦. A jammer stays 干擾 (橡皮擦雷達干擾機甲,
干擾者雷達干擾車), never 幹擾. A laser tower is 雷射塔 (刺鰩重型雷射塔,
輕型雷射塔).

## 6. The name in the language list

`name` is 繁體中文. Those four characters are already in the engine's
endonym face, `NotoSansCJKsc-Bold-Endonyms.otf`, so the list can draw the
name before the pack is installed. Locales are `zh-Hant`, `zh-TW`, `zh-HK`
and `zh-MO`. A bare `zh` stays with the Simplified pack.
