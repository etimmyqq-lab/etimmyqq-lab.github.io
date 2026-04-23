# 昆廷老師個人品牌網站 — 版本歷程

## [2026-04-23] 部署上線 https://etimmyqq-lab.github.io/

### 變更內容
- 新增 `site.config.json`（base_url + github_repo）
- 新增 `.gitignore`（排除 *.bak / outbox/ / OS / editor 檔案）
- 修改 `index.html` / `sitemap.xml` / `robots.txt` / `articles/2026-04-23-43a3f283.html`：填入實際 base_url
- 修改 `exposure/daily_pipeline.py`（在 auto-post 專案）：新增 `get_base_url()` 讀 site.config.json，讓未來新文章 canonical 與 sitemap 自動帶絕對 URL
- **修復 head marker bug**：原本 `<title><!-- BRAND:head_title -->...<!-- /BRAND:head_title --></title>` 會讓 title 變「含 marker 文字」（因為 `<title>` 與 `<meta content>` 內的 HTML 註解會被當成純文字）。改成 marker 在 element 外包整段：`<!-- BRAND:head_title --><title>...</title><!-- /BRAND:head_title -->`
  - `sync_from_brand_profile.py` 對應更新：head 7 個 marker（head_title/meta_description/meta_author/meta_keywords/og_title/og_description/og_site_name/twitter_title/twitter_description）的 value 改產完整 element 字串而非純文字

### 部署過程
1. 使用者提供 GitHub username `timmytsou`
2. 用 Playwright 開 https://github.com/new 發現登入帳號實際是 `etimmyqq-lab`（Google OAuth 自動登入）
3. 使用者選擇 A：接受 `etimmyqq-lab.github.io`
4. Playwright 自動填 repo name → Public → Create repository
5. 本地 git init / remote add / commit / push（Windows Git Credential Manager 自動認證）
6. 驗證 `Your site is live at https://etimmyqq-lab.github.io/`
7. 發現 title 顯示含 marker → 修 → 重 push
8. Pages rebuild 約 30 秒 → 最終驗證完成

### 驗證結果（live）
- https://etimmyqq-lab.github.io/ HTTP 200
- https://etimmyqq-lab.github.io/articles/2026-04-23-43a3f283.html HTTP 200
- `document.title` = `昆廷老師｜企業 AI 顧問．易經決策教練`（乾淨，無 marker）
- JSON-LD `name=昆廷老師`、`url=https://etimmyqq-lab.github.io`、`sameAs=[LinkedIn, YouTube, Threads]`、`knowsAbout=[8 個核心關鍵字]`
- canonical、og:title、hero 全正確

### 原因
- 使用者要求「你不是可以幫我操控網頁嗎，請直接幫我處理」→ 用 Playwright 自動化 GitHub 建 repo
- Head marker bug 是 HTML spec 的 subtle issue（title 是 raw text element、attribute value 也不 parse 註解），上線前一定要修

### 影響範圍
- 網站正式對外公開
- schema.org/Person 結構化資料上線，AI 爬蟲（Google/Claude/Perplexity/GPTBot）都可以抓到
- 下一次跑 daily-publish.bat 時，新文章的 canonical 與 sitemap URL 會自動帶 `https://etimmyqq-lab.github.io`

### 待使用者操作
1. **提交 sitemap 給 Google**：到 https://search.google.com/search-console → Add property `https://etimmyqq-lab.github.io` → 驗證 → Sitemaps → 提交 `/sitemap.xml`
2. **Rich Results Test**：https://search.google.com/test/rich-results 測 `https://etimmyqq-lab.github.io/` 驗證 JSON-LD 通過
3. 更新 LinkedIn / YouTube / Threads bio 的「個人網站」連結為 `https://etimmyqq-lab.github.io`
4. 等 7–14 天讓 Google 索引後，跑 weekly-report.bat 看 AI 可見度變化

## [2026-04-23] 一鍵發文 + 週報自動化（B + C 自動化）

### 變更內容
- 修改 `index.html`：articles-grid 加 `<!-- ARTICLES:auto -->` marker
- 新增 `articles/_template.html`：獨立文章頁模板（含 schema.org/Article JSON-LD、Open Graph、文章專用 CSS）
- 新增 `articles/2026-04-23-43a3f283.html`：首篇自動產出的文章（「客服可以完全交給 AI 嗎？」）
- 新增 `outbox/2026-04-23/`：本篇對應的多平台純文字檔
  - `_topic.txt`（本篇主題）
  - `linkedin.txt`、`threads.txt`、`youtube.txt`（直接複製貼）
  - `website.md`（長文原稿）
- 新增 `daily-publish.bat`：一鍵發文快捷，含審核 gate（自動開啟 outbox + 首頁讓你看 → 按 y 確認後才 git push）
- 新增 `weekly-report.bat`：一鍵週報 + 監測，產完自動開啟 .md 檔

### 流水線細節（daily-publish.bat → daily_pipeline.py）
1. 從 GEO 矩陣隨機挑未用長尾問題（去重池 `auto-post/data/used_long_tails.json`）
2. 呼叫模組 ③ `content_fanout.generate` 產 4 平台內容（約 76 秒）
3. 從 website 版擷取標題（截 45 字）+ 描述（去 md 格式、截 80 字）
4. 套用 `articles/_template.html` → 寫入 `articles/YYYY-MM-DD-{hash}.html`
5. 首頁 `<!-- ARTICLES:auto -->` 區塊插入新卡片（保留最新 6 張）
6. sitemap.xml 追加 article URL
7. `outbox/YYYY-MM-DD/` 輸出 3 平台純文字 + website.md
8. 記錄 `used_long_tails.json` 供下次去重

### 端到端測試結果
- 測試長尾：「客服可以完全交給 AI 嗎？客人會不會覺得沒溫度？」
- 總耗時：76 秒（Claude CLI 產 4 格式）
- 所有產出檔案都正確建立
- 首頁文章卡片、sitemap、outbox 都成功更新
- used_long_tails.json 追加 1 筆
- 文章頁 HTTP 200、schema.org/Article JSON-LD 正確嵌入

### 原因
- 使用者要求「B + C 自動化，只留審核」
- 內容生產全流程自動化（選題 → 產文 → 轉 HTML → 更新網站 → 輸出多平台文字）
- 審核 gate 設計：產完 → 自動開啟 outbox 與網站 → 等使用者按 y 才 git push
- 週報每週一次，自動比較趨勢 + 產下週建議主題清單

### 影響範圍
- auto-post 新增模組：`exposure/daily_pipeline.py`、`exposure/weekly_report.py`
- auto-post 新增資料檔（首次執行建立）：`data/used_long_tails.json`、`reports/YYYY-WW.md`
- personal-website 每次跑 daily-publish 會新增 1 篇 article、更新 index.html 與 sitemap.xml
- 不影響既有 auto-post 排程/佇列/發文流程

### 使用者後續動線
- 每天（或每週幾次）：雙擊 `daily-publish.bat` → 看 outbox 三份文字 → 按 y → 複製貼到 LinkedIn/Threads/YouTube
- 每週：雙擊 `weekly-report.bat` → 看 AI 曝光度變化 + 下週建議主題

## [2026-04-23] 聯絡資訊填入 + 4 錨點品牌套件 + 3 支 .bat 快捷

### 變更內容
- 修改 `index.html`：
  - 聯絡區 4 張卡片填入實際 URL（Email/LinkedIn/YouTube/Threads），加 `target="_blank"` + `rel="noopener"`
  - JSON-LD `sameAs` 填入 3 個社群 URL（GEO 關鍵，讓 AI 爬蟲建立跨平台實體關聯）
- 新增 `brand-kit.md`：一頁式「複製貼上」品牌套件
  - 4 錨點（個人網站 / LinkedIn / YouTube / Threads）的 headline / about / bio 素材
  - 每錨點獨立 checklist
  - 一致性檢核表（姓名 / Tagline / 頭銜 / 核心關鍵字 / 核心金句 5 項跨平台必須一致）
  - 動線建議（今晚 → 明天 → 後天 → 週末的 4 週漸進路徑）
- 新增 `sync.bat`：雙擊跑 dry-run + 實際同步（帶確認提示）
- 新增 `preview.bat`：雙擊啟動 http.server 8080 + 自動開瀏覽器
- 新增 `deploy.bat`：雙擊走完 git init / remote add / add / commit / push 全流程（首次會引導填 repo URL）

### 資料來源
- 聯絡資訊：使用者提供（etimmyqq@gmail.com / timmy-tsou / @entairoi / @timmy.tsou.tw）
- 4 錨點素材：`POST /api/exposure/authority-anchors/{linkedin|youtube|threads}/assets`
- 全部匯總自 `C:\claude\auto-post\data\authority_anchors.json`

### 原因
- 使用者把 3 個社群的真實 URL 給我，要順便填進 JSON-LD 與聯絡區
- 3 個錨點素材已在後端產出，需要匯出成使用者能直接「複製貼上到各平台」的格式
- 使用者偏好雙擊即跑的 Windows 批次檔（減少 CLI 操作）

### 影響範圍
- 聯絡區 UI 從 placeholder 變成可點擊的實際連結
- JSON-LD `sameAs` 現在含 3 個真實 URL → Google/Claude/Perplexity 爬蟲可建立昆廷老師跨平台實體
- 新增 3 支 .bat 讓日常操作無需開 cmd 視窗

### 待使用者操作
1. 依 `brand-kit.md` 順序更新 LinkedIn / YouTube / Threads 的 bio
2. 雙擊 `deploy.bat` 走部署流程（需先建 GitHub repo）
3. 部署後回 index.html 把 JSON-LD 的 `"url"` 填成實際網址

## [2026-04-23] 自動同步工具：sync_from_brand_profile.py

### 變更內容
- 新增 `sync_from_brand_profile.py`（純 Python stdlib，無第三方依賴）
  - 讀取：`C:\claude\auto-post\data\brand_profile.json`
  - 目標：`index.html` 中 `<!-- BRAND:xxx -->...<!-- /BRAND:xxx -->` 標記區段
  - 支援 17 個 marker 欄位（head_title / meta_* / og_* / twitter_* / jsonld / nav_brand / hero_* / about_* / footer_bio）
  - `--dry-run`：只顯示 diff 不寫檔
  - `--no-backup`：跳過 .bak 備份
  - 預設會寫 `index.html.bak`
  - **保留 JSON-LD 的 `url` 與 `sameAs`**（從現有 HTML 讀出合併）
  - 冪等：二次執行 0 changed
  - Windows cp950 友善：強制 stdout UTF-8 + 用 ASCII 符號
- 修改 `index.html`：加入 17 個 `<!-- BRAND:xxx -->` marker（手寫金句、核心主題、文章、聯絡方式、JSON-LD 的 url/sameAs **不加 marker**，保留手動維護權）
- 修改 `README.md`：新增「自動同步品牌資料」區塊與完整工作流說明

### 特殊處理
- `hero_title`（tagline）：自動在中文逗號後加 `<br>` 斷行
- `about_prose`：bio_long 按 `\n\n` 切段，第一段自動將前 4 核心關鍵字包 `<strong>`
- `hero_eyebrow` / `about_lede`：從 `platform_bios.website_about` 第一行「｜」後擷取
- `jsonld`：讀取現有 JSON-LD，更新 name/alternateName/description/jobTitle/knowsAbout，**保留** url/sameAs

### 原因
- 使用者預期品牌定位會隨時間演進，需要能把 `brand_profile.json` 的更新自動反映到網站
- 避免手動複製貼 → 容易漏同步、格式錯亂
- marker 設計確保工具只改該改的，不動手寫內容

### 影響範圍
- 新增檔案：`sync_from_brand_profile.py`、`index.html.bak`（首次執行時產生）
- 修改 `index.html`：加入 marker（向下相容，不影響顯示）
- 不影響部署流程；部署後填入的 canonical URL / JSON-LD url / sameAs 都會被保留

### 測試結果
- dry-run：17 markers 全偵測到
- 實際同步：5 changed（jsonld 欄位結構統一、og_description 改為完整 positioning_statement、twitter_title/description 改為 canonical 版本、about_prose 第一段 strong 位置校正）
- 冪等性驗證：二次執行 0 changed
- 預覽伺服器 HTTP 200，頁面正常渲染

## [2026-04-23] 專案初始化（Project Genesis）

### 變更內容
- 新增 `index.html`：單頁式主頁，含 5 個區塊
  - Hero（tagline「用易經卦牌，導你走進 AI 時代」+ 雙 CTA）
  - About（bio_long 完整呈現，含 4 個核心概念加粗）
  - 核心主題（4 張卡片，易經卦牌卡有 accent 色強調）
  - 方法論 callout（深藍漸層強調金句「AI 解決怎麼做，易經回答該不該做」）
  - 文章區（3 張 placeholder 卡）
  - 聯絡區（Email + LinkedIn/YouTube/Threads 卡片）
- `<head>` 嵌入：
  - **schema.org/Person JSON-LD**（GEO 最關鍵資料，讓 AI 建立人物實體）
  - Open Graph meta tags（profile type）
  - Twitter Card
  - canonical link
  - 完整 8 組核心關鍵字 meta keywords
- 新增 `assets/style.css`：#1F4E79 主色 + #C9A96E 東方金 accent，含響應式設計、sticky nav、noscript-safe 動畫
- 新增 `robots.txt`：明確允許 GPTBot / ClaudeBot / PerplexityBot / Google-Extended
- 新增 `sitemap.xml`：僅含首頁（未來新增文章時需同步更新）
- 新增 `.nojekyll`：關閉 GitHub Pages 的 Jekyll 處理
- 新增 `README.md`：完整部署指引（GitHub Pages / Vercel 兩種路徑 + 發佈後 3 處必改）
- 新增 `CLAUDE.md`：專案規範

### 資料來源
- 內容文字：`C:\claude\auto-post\data\brand_profile.json`（auto-post 曝光引擎模組 ①「品牌定位器」產生）
- schema.org JSON-LD：透過 `POST http://127.0.0.1:5500/api/exposure/authority-anchors/website/assets` 取得

### 原因
- 使用者採用融合敘事策略（方案 B）建立個人 AI 曝光度，需要一個權威錨點網站讓 AI 爬蟲建立人物實體關聯
- 個人網站在 GEO 策略中投報率最高（schema.org/Person + 高權重域名 + 完整段落）
- 既有曝光引擎模組 ③「內容裂變」產出的網站長文需要有地方發佈

### 影響範圍
- 新專案，無既有檔案被修改
- 與 auto-post 專案的關係：consumer（讀 brand_profile.json、呼叫 API 取得素材）
- 部署後需填入 3 處真實 URL（canonical / "url" / "sameAs"）

### 待使用者操作
1. 到 GitHub 建立 `<username>.github.io` repo
2. 依 README 步驟 `git push`
3. 填入真實 URL 三處後重新 push
4. 用 Google Rich Results Test 驗證 JSON-LD
5. 提交 sitemap.xml 給 Google Search Console
6. 回 auto-post 曝光引擎模組 ④ 勾選 checklist 項目
