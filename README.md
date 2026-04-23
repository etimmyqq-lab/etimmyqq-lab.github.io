# 昆廷老師個人品牌網站

> 企業 AI 顧問．易經決策教練 — AI 曝光引擎的「權威錨點 #1」

靜態網站，零建置步驟，可直接部署到 GitHub Pages / Vercel / Netlify。

## 結構

```
personal-website/
├── index.html          # 主頁（單頁式：hero / about / topics / articles / contact）
├── assets/
│   └── style.css       # 色系 #1F4E79 × 東方金 #C9A96E
├── articles/           # 未來長文目錄（.html 或 .md）
├── .nojekyll           # 關閉 GitHub Pages 的 Jekyll 處理
├── robots.txt          # 給 AI 爬蟲（GPTBot / ClaudeBot / PerplexityBot）的允許指示
└── sitemap.xml
```

## ★ GEO 關鍵重點

`index.html` 的 `<head>` 含 **schema.org/Person JSON-LD**——這是讓 Claude / ChatGPT / Gemini / Perplexity 的爬蟲建立「昆廷老師」人物實體關聯的最核心資料。

部署後必做：**用 Google 的 Rich Results Test 驗證 JSON-LD 正確** → https://search.google.com/test/rich-results

---

## 部署到 GitHub Pages（推薦．免費．15 分鐘）

### 前置作業
1. 註冊 GitHub 帳號（若尚未有）
2. 在 GitHub 建立新 repo，取名 `<你的username>.github.io`（這樣會用 username 域名而不是 repo 名）
3. 本機打開 cmd / PowerShell

### 部署步驟

```bash
cd C:\claude\personal-website
git init
git add .
git commit -m "Initial commit: personal brand site"
git branch -M main
git remote add origin https://github.com/<你的username>/<你的username>.github.io.git
git push -u origin main
```

到 GitHub repo 頁面 → Settings → Pages → Source 選 `main` branch → Save
約 1-2 分鐘後 `https://<你的username>.github.io` 就會上線。

### 發佈後要改的 3 個地方

用 Edit 打開 `index.html`，搜尋並填入：

1. `<link rel="canonical" href="/">` → 改成完整 URL
2. 第 39 行左右 `"url": ""` → 填入你的網址
3. 第 42 行左右 `"sameAs": [""]` → 填入 LinkedIn / YouTube / Threads URL（陣列形式）

範例：
```json
"url": "https://kunting.github.io",
"sameAs": [
  "https://www.linkedin.com/in/kunting",
  "https://www.youtube.com/@kunting",
  "https://www.threads.net/@kunting"
]
```

### 自訂域名（可選）

若想用自己買的域名（如 `kunting.tw`）：
1. 在 repo 根目錄新增 `CNAME` 檔，內容單一行：`kunting.tw`
2. 到域名商（Gandi / Cloudflare / Namecheap）新增 DNS A/CNAME 指向 GitHub Pages

---

## 部署到 Vercel（更快，推薦度第二）

1. https://vercel.com/ 用 GitHub 登入
2. Import 這個 repo → 點 Deploy（不用設定，Vercel 自動偵測）
3. 預覽 URL 立刻產出，可綁定自訂域名

---

## 內容維護

### ⭐ 自動同步品牌資料（推薦）

```bash
# 同步（自動備份）
C:\claude\auto-post\venv\Scripts\python.exe sync_from_brand_profile.py

# 只看會改什麼，不實際寫檔
C:\claude\auto-post\venv\Scripts\python.exe sync_from_brand_profile.py --dry-run
```

**運作原理**：`index.html` 含有 `<!-- BRAND:xxx -->...<!-- /BRAND:xxx -->` 標記區段，工具只替換標記內容，**不會動你手寫的金句、核心主題卡片、文章、聯絡方式**。

**保留的區段**（手寫或部署時填的，工具不碰）：
- Hero 下方金句「AI 解決怎麼做…」
- 4 張核心主題卡片的描述
- 方法論 callout
- 3 張文章卡片
- 聯絡方式（Email / LinkedIn / YouTube / Threads URL）
- JSON-LD 的 `"url"` 與 `"sameAs"`（部署後你填的）

**會同步的區段**（從 `brand_profile.json` 衍生）：
- `<title>`、meta description、meta keywords
- Open Graph / Twitter Card 標題與描述
- schema.org/Person JSON-LD（name / alternateName / description / jobTitle / knowsAbout）
- 導覽列品牌名
- Hero eyebrow、大標題、CTA 按鈕
- About h2、About lede、About prose（4 段 bio_long，第一段自動加 `<strong>`）
- Footer bio

**完整工作流**（品牌定位調整 → 網站同步 → 部署）：
```
1. 到 http://127.0.0.1:5500/ 曝光引擎分頁 → 模組 ① 品牌定位器
2. 改表單 → 按「產生品牌定位」
3. cd C:\claude\personal-website
4. python sync_from_brand_profile.py --dry-run   # 預覽
5. python sync_from_brand_profile.py             # 實際同步
6. 瀏覽器刷新 http://127.0.0.1:8080/ 確認
7. git add . && git commit -m "update brand profile" && git push
```

### 新增文章
在 `articles/` 目錄下新增 `.html` 檔案，再到 `index.html` 的 `articles-grid` 區塊加一張卡片連到該文章。

文章本身可直接用 auto-post 曝光引擎的「內容裂變」產生的 `website` 格式——那已是完整 Markdown 長文，只要用一個簡單轉 HTML 工具（或手動貼）即可。

### 建議發文節奏
- 每週 1 篇支柱長文（1500–2500 字）
- 每篇文末加 canonical footer bio + 連結到其他平台

### 同步更新 Sitemap
每次新增文章後，手動編輯 `sitemap.xml` 加一筆 `<url>` 項目。

---

## 與 auto-post 曝光引擎的關係

這個網站是 auto-post 專案 `exposure` 模組中「**模組 ④ 權威錨點 - 個人網站**」的具體實作。

- 內容來源：`C:\claude\auto-post\data\brand_profile.json`
- 每次品牌定位更新後，可重新執行：
  ```bash
  curl -X POST http://127.0.0.1:5500/api/exposure/authority-anchors/website/assets
  ```
  取得新的 `about_html` / `schema_person_jsonld` / 其他素材，再手動同步到 `index.html`
- 勾選 auto-post 曝光引擎 → 模組 ④ → 網站 checklist 的各項，追蹤完成度

## 進度檢核清單（對應曝光引擎模組 ④）

- [ ] 購買並設定個人域名
- [ ] 部署到 GitHub Pages / Vercel / Netlify
- [ ] 放上 About 頁面（已完成，在 index.html）
- [ ] 加入 schema.org/Person JSON-LD（已完成，在 head）
- [ ] 發表至少 3 篇支柱長文
- [ ] 每頁 footer 放 canonical bio（已完成）
- [ ] 提交 sitemap.xml 給 Google Search Console
- [ ] 每篇文章加 Open Graph meta tags（index.html 已完成）

---

## 本地預覽

最簡：用任何靜態檔案伺服器開 `index.html` 即可，例如：
```bash
cd C:\claude\personal-website
python -m http.server 8080
```
瀏覽器打開 http://127.0.0.1:8080

也可以直接雙擊 `index.html` 在瀏覽器開啟（但 schema.org JSON-LD 的驗證必須透過 http 才能用 Rich Results Test）。
