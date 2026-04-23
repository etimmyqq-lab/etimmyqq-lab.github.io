# CLAUDE.md — 昆廷老師個人品牌網站

## 專案概覽

靜態個人品牌網站。純 HTML + CSS，無建置步驟、無 JS 框架依賴，可直接部署到 GitHub Pages / Vercel / Netlify。

**定位**：auto-post 曝光引擎「權威錨點 #1」——讓 AI 爬蟲（Claude / ChatGPT / Gemini / Perplexity）能透過 schema.org/Person JSON-LD 建立「昆廷老師」人物實體關聯。

## 專案路徑
`C:\claude\personal-website\`

## 技術堆疊
- 純 HTML5 / CSS3
- Google Fonts（Noto Sans TC + Noto Serif TC）
- 色系：#1F4E79（主）× #C9A96E（東方金 accent）
- 無 JS 框架、無 CDN 依賴（除了 Google Fonts）
- **schema.org/Person JSON-LD** 嵌入 `<head>`（GEO 關鍵）

## 檔案結構

```
personal-website/
├── index.html          # 單頁式主頁
├── assets/style.css    # 全部樣式
├── articles/           # 文章目錄（未來擴充）
├── .nojekyll           # 關閉 GitHub Pages Jekyll
├── robots.txt          # 明允許 AI 爬蟲
├── sitemap.xml
├── README.md           # 部署指引
├── CLAUDE.md           # 本文件
└── version.md          # 變更記錄
```

## 內容來源
所有文字內容皆來自 `C:\claude\auto-post\data\brand_profile.json`（由 auto-post 曝光引擎模組 ① 產生）。

修改原則：**不要手改 index.html 的文字內容**，應先更新 brand_profile.json，再重新呼叫曝光引擎 API 取得最新素材，然後同步到 index.html。

## 與 auto-post 曝光引擎的整合

```
auto-post/exposure (Port 5500)
    ↓ (brand_profile.json)
    ↓ (authority_anchors.generate_assets('website'))
    ↓
personal-website/index.html
    ↓ (git push)
    ↓
GitHub Pages → https://<user>.github.io
    ↓
AI 爬蟲讀 schema.org/Person JSON-LD → 建立人物實體
```

## Claude Code 操作規範

### 修改原則
1. 先讀 `version.md` 了解當前狀態
2. 完成任一實質性變更後寫入 `version.md`
3. 新增文章時同步更新 `sitemap.xml`
4. 修改 JSON-LD 後提醒使用者用 Google Rich Results Test 驗證

### 不要做的事
- 不要加 JavaScript 框架（React / Vue / Alpine 等）——這站要保持純靜態
- 不要加追蹤碼（GA / 像素）除非使用者明確要求
- 不要改動色系變數（--primary, --accent）除非使用者要求

### 色系規範
```css
--primary: #1F4E79;       /* 主色，標題、按鈕 */
--primary-dark: #15395a;  /* hover */
--primary-light: #2E6CA8;
--accent: #C9A96E;        /* 東方金，呼應易經 */
```

## 部署方式（依使用者偏好）
1. GitHub Pages（預設）
2. Vercel
3. Netlify

部署前必須確認：`<link rel="canonical">` / `"url"` / `"sameAs"` 三處已填入真實 URL。
