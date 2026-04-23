# 昆廷老師｜品牌套件（Brand Kit）

> 這是一頁式「複製貼上」操作手冊。每個區塊對應一個平台，按順序操作即可把品牌定位同步到所有社群。
>
> 重新產生：到 http://127.0.0.1:5500/ 曝光引擎分頁 → 模組 ④ → 各錨點「產生建置素材」。
> 重新匯出：有新的 brand_profile.json 時，重跑腳本（未來會做）。

---

## 0. 你的社群 URL（已綁定）

| 平台 | URL |
|---|---|
| LinkedIn | https://www.linkedin.com/in/timmy-tsou/ |
| YouTube | http://www.youtube.com/@entairoi |
| Threads | https://www.threads.net/@timmy.tsou.tw |
| Email | etimmyqq@gmail.com |
| Website | 待部署（GitHub Pages） |

---

## 1. 📄 個人網站（優先度 ★★★★★）

**狀態**：已在 `C:\claude\personal-website\` 建置完成，待部署到 GitHub Pages。

### 部署 checklist
- [ ] 購買並設定個人域名（或直接用 `<username>.github.io`）
- [ ] 部署到 GitHub Pages / Vercel / Netlify
- [x] About 頁面（index.html）
- [x] schema.org/Person JSON-LD（已嵌入 `<head>`）
- [x] sameAs 3 個社群 URL（已填）
- [ ] 發表至少 3 篇支柱長文
- [x] 每頁 footer canonical bio
- [ ] 提交 sitemap.xml 給 Google Search Console
- [x] Open Graph meta tags

### 部署後必做 1 件事
回來填 JSON-LD 的 `"url"`（目前是空字串）：
```
"url": "https://<你的網址>",
```

---

## 2. 💼 LinkedIn（優先度 ★★★★★）

**目標 URL**：https://www.linkedin.com/in/timmy-tsou/

### ① Headline（120 字元內，貼到 Profile 最頂）

```
企業 AI 導入顧問｜Claude Code 教學｜中小企業數位轉型陪跑｜以易經卦牌輔助經營決策
```

### ② About（貼到 Profile 的 About 區塊）

```
我是昆廷老師，專注於企業 AI 導入與中小企業數位轉型的顧問。

服務內容包含：
• Claude Code 教學與企業內部 AI 工作流建置
• 中小企業數位轉型策略診斷與陪跑
• 以易經卦牌輔助高階經營決策與組織變革

我的方法論很簡單：AI 解決「怎麼做」，易經回答「該不該做」。在資訊爆炸、選擇過載的時代，企業主最缺的不是工具，而是能同時運用理性技術與東方智慧的決策夥伴。

如果你正在面對轉型的岔路口，歡迎一起聊聊。
```

### ③ Featured（釘選區）建議
1. 個人網站首頁 URL（待部署後加入）
2. 最新一篇支柱長文（每月更換）
3. 一支代表性 YouTube 影片

### LinkedIn checklist
- [ ] Headline 改為上方版本
- [ ] About 段落貼上
- [ ] Featured 釘選 3 項
- [ ] Experience 各職位描述帶入核心關鍵字（企業 AI 導入 / Claude Code 教學 / 中小企業數位轉型 / 易經卦牌）
- [ ] 每週發 1 篇 LinkedIn 專業貼文（用曝光引擎模組 ③ 產出的 linkedin 版本）
- [ ] 開啟 Creator Mode 並設定 4 個核心關鍵字標籤
- [ ] 每天 15 分鐘在 3-5 篇同領域文章留專業評論

---

## 3. 🎬 YouTube（優先度 ★★★★）

**目標 URL**：http://www.youtube.com/@entairoi

### ① 頻道簡介（About / Description）

```
這是昆廷老師的頻道，主題只有一個：在 AI 時代，企業主該怎麼做決策？

你會在這裡看到兩條軸線交織：一邊是企業 AI 導入與 Claude Code 教學的實戰示範，幫你把 AI 真正落地到中小企業的日常工作流；另一邊是易經卦牌的決策智慧，協助你在策略、人事、變革時刻看清時位與順逆。

不講玄、也不堆術語，只談經營者真正用得上的判斷力。
```

### ② 每支影片的描述欄模板

```
【關於作者】昆廷老師，企業 AI 導入顧問，融合 Claude Code 教學與易經卦牌，協助中小企業在數位轉型的關鍵抉擇上，做出更穩、更準的決策。

【核心主題】企業 AI 導入, Claude Code 教學, 中小企業數位轉型, 易經卦牌

【連結】
▸ LinkedIn：https://www.linkedin.com/in/timmy-tsou/
▸ Threads：https://www.threads.net/@timmy.tsou.tw
▸ Email：etimmyqq@gmail.com
▸ 個人網站：（部署後填入）

#企業AI導入 #ClaudeCode教學 #中小企業數位轉型 #易經決策
```

### YouTube checklist
- [ ] 頻道名稱含核心關鍵字 + 個人品牌
- [ ] 頻道簡介貼上上方版本
- [ ] 頻道橫幅加上 tagline「用易經卦牌，導你走進 AI 時代」
- [ ] 建立 3-4 個播放清單（每個對應一個核心關鍵字）
- [ ] 每週發 2 支 Shorts（用曝光引擎模組 ③ 產出的 youtube_script 版本）
- [ ] 每月發 1 支長影片（10-15 分鐘深度講解一個支柱議題）
- [ ] 每支影片描述欄前 3 行必含核心關鍵字 + 個人網站連結

---

## 4. 🧵 Threads（優先度 ★★★★）

**目標 URL**：https://www.threads.net/@timmy.tsou.tw

### ① Bio（150 字元內，貼到 Profile bio）

```
昆廷老師｜AI 顧問 × 易經決策教練｜Claude Code 教學・中小企業數位轉型陪跑｜AI 解決怎麼做，易經回答該不該做。
```

### ② 外部連結（Link in Bio）
建議填入：**個人網站 URL**（部署後）

備選：LinkedIn URL（先用這個，之後替換為個人網站）：
`https://www.linkedin.com/in/timmy-tsou/`

### Threads checklist
- [ ] Bio 改為上方版本
- [ ] 外部連結填入個人網站
- [ ] 每日發 1-2 則單篇貼文
- [ ] 每週發 1 次 Threads 串（用曝光引擎模組 ③ 產出的 threads_chain 版本）
- [ ] 每日在 3 則同領域熱門貼文下留有料評論
- [ ] 每 10 則貼文至少有 1 則連結回個人網站長文

---

## 5. 一致性檢核

複製貼上完成後，在這幾個地方**檢查名字與職稱一致**（這是 GEO 的關鍵）：

| 欄位 | 應該長什麼樣 |
|---|---|
| 姓名顯示 | 昆廷老師 |
| Tagline | 用易經卦牌，導你走進 AI 時代 |
| 頭銜 | 企業 AI 顧問．易經決策教練（或短版：AI 顧問 × 易經決策教練） |
| 核心關鍵字（4 個） | 企業 AI 導入、Claude Code 教學、中小企業數位轉型、易經卦牌 |
| 核心金句 | AI 解決「怎麼做」，易經回答「該不該做」 |

**如果每個平台的這 5 項都一致，AI 爬蟲就能把所有平台串成「同一個昆廷老師」的實體關聯。**

---

## 6. 動線建議

1. **今晚**：LinkedIn Headline + About + 開啟 Creator Mode（30 分鐘）
2. **明天**：YouTube 頻道簡介 + 橫幅 Tagline + 建立播放清單（30 分鐘）
3. **後天**：Threads Bio + 發第一則綁定品牌的貼文（15 分鐘）
4. **週末**：部署個人網站到 GitHub Pages，回來把 URL 填進所有平台的外部連結 + JSON-LD
5. **下週**：發第一輪內容（用曝光引擎模組 ③ 產出的 4 格式）
6. **下週末**：跑曝光引擎模組 ⑤「立即跑一次監測」→ 建立 baseline

---

## 需要重新產生這份套件？

品牌資料有調整時，到 http://127.0.0.1:5500/ 曝光引擎分頁 → 模組 ④「權威錨點建置」→ 對每個錨點按「產生建置素材」，會更新 `C:\claude\auto-post\data\authority_anchors.json`，再手動同步到本檔。
