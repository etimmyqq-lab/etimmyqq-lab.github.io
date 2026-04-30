# Search Console 圖解版操作手冊

適用網站：`https://etimmyqq-lab.github.io/`  
手冊更新日：`2026-04-30`

這份手冊不是教你所有 SEO 理論，而是教你怎麼用 `Google Search Console` 直接看出：

- 網站有沒有開始被 Google 看見
- 哪些查詢字開始帶來曝光
- 哪些頁面被收錄、哪些還沒
- `sitemap.xml` 有沒有正常幫 Google 找到頁面
- 某一頁為什麼沒有被收錄

你現在最常用到的 4 個區塊是：

- `Performance / 成效`
- `Page indexing / 網頁索引`
- `URL Inspection / 網址檢查`
- `Sitemaps / Sitemap`

參考官方文件：

- Performance reports  
  https://support.google.com/webmasters/answer/10268906
- Performance report (Search results)  
  https://support.google.com/webmasters/answer/7576553
- Page indexing report  
  https://support.google.com/webmasters/answer/7440203
- URL Inspection tool  
  https://support.google.com/webmasters/answer/9012289
- Inspect and troubleshoot a single page  
  https://support.google.com/webmasters/answer/12482179
- About Search Console data  
  https://support.google.com/webmasters/answer/96568

## 1. 先理解 Search Console 是看什麼

Search Console 主要回答的是：

```text
Google 有沒有看到你
Google 怎麼理解你的頁面
哪些頁面有出現在搜尋結果
哪些頁面沒有被收錄
```

它不是拿來看「有沒有人寄信」的。  
寄信、表單、互動，主要看 `GA4`。  
搜尋曝光、點擊、收錄，主要看 `Search Console`。

可以把兩者理解成：

```text
Search Console = 被 Google 看見了沒有
GA4 = 被看見之後，有沒有產生行動
```

## 2. 你這個網站最重要的檢查順序

對你現在這個網站，建議每週照這個順序看：

```text
1. Performance
2. Page indexing
3. URL Inspection
4. Sitemaps
```

原因很簡單：

```text
先看有沒有曝光
→ 再看哪些頁面沒被收錄
→ 再查單一頁為什麼有問題
→ 最後確認 sitemap 有沒有正常提交
```

## 3. Performance / 成效 要怎麼看

這是你最常打開的報表。

官方文件說明的重點指標包括：

- `Clicks`
- `Impressions`
- `CTR`
- `Average position`

你可以用這張圖理解：

```text
Impressions = 你的頁面被看到幾次
Clicks = 被點進來幾次
CTR = 看到了之後，有多少人點
Position = 平均大概排在哪裡
```

### 操作路徑

```text
Search Console
  → Performance
    → Search results
```

如果是中文介面，通常可以理解成：

```text
成效
  → 搜尋結果
```

### 你在這裡最該看什麼

先把上方這 4 個指標打開：

- `總點擊`
- `總曝光`
- `平均 CTR`
- `平均排名`

然後下面表格切 2 種看法：

- `Queries / 查詢`
- `Pages / 網頁`

## 4. 查詢怎麼看

查詢是最直接的市場回饋。

它會回答：

```text
別人用什麼字搜到你
哪些字開始有曝光
哪些字有曝光但沒點擊
```

### 圖解判讀

#### 狀況 A

```text
某查詢有曝光
但點擊很低
```

解讀：

- 你已經開始被看到了
- 但標題或描述不夠吸引人

先改：

- `title`
- `meta description`
- 頁面開頭第一屏

#### 狀況 B

```text
完全沒有查詢資料
```

解讀：

- 網站可能還很新
- 或頁面還沒被收錄
- 或目前真的還沒累積搜尋能見度

Google 官方說明提到，新站資料可能要花一週左右才開始出現。  
來源：`About Search Console data`

## 5. 網頁怎麼看

把維度切到 `Pages / 網頁`，你就能看到：

```text
哪一頁最先被 Google 看見
哪一頁曝光最多
哪一頁點擊最多
```

你現在最該盯的頁面：

- `/`
- `/cooperation.html`
- `/intake.html`
- `/services/enterprise-ai-consulting.html`
- `/services/claude-code-training.html`
- `/services/digital-transformation-consulting.html`

### 圖解判讀

#### 狀況 A

```text
首頁曝光高
服務頁曝光低
```

解讀：

- 品牌入口有被看到
- 但服務承接頁還沒被 Google 理解得夠清楚

先改：

- 補更多服務頁內鏈
- 補該主題文章
- 強化服務頁的標題與內容主題

#### 狀況 B

```text
文章曝光高
服務頁點擊低
```

解讀：

- 內容開始能帶流量
- 但商業承接頁還沒吃到足夠能見度

先改：

- 文章內導回服務頁
- 服務頁 FAQ
- 服務頁更明確的主題關鍵字

## 6. Page indexing / 網頁索引 怎麼看

這個報表是用來看：

```text
哪些頁面已收錄
哪些頁面未收錄
未收錄的原因是什麼
```

官方文件也特別提醒：

- 小站不一定要每天看這份報表
- 重點是你的重要頁面要有被索引

### 操作路徑

```text
Search Console
  → Page indexing
```

中文介面可以理解成：

```text
索引
  → 網頁
```

### 你怎麼看才有效

你不用先追求所有頁都綠。  
先檢查這些重要頁：

- 首頁
- 3 個服務頁
- 合作頁
- intake 頁

### 圖解理解

```text
Indexed = Google 已收錄
Not indexed = Google 尚未收錄
```

但 `Not indexed` 不一定是壞事。  
例如：

- 重複頁
- 404 頁
- 本來就不該收錄的頁

真正要緊的是：

```text
重要頁面不在 Indexed 裡
```

## 7. URL Inspection / 網址檢查 怎麼用

這是你最實用的單頁診斷工具。

官方文件提到，它可以做幾件事：

- 看 Google 索引裡的版本
- 測試 live URL
- 看能不能要求重新收錄
- 查 canonical

### 操作路徑

最上方搜尋列直接輸入完整網址：

```text
https://etimmyqq-lab.github.io/intake.html
```

或：

```text
https://etimmyqq-lab.github.io/services/enterprise-ai-consulting.html
```

### 你最常用的 3 個功能

#### 1. 看這頁有沒有在 Google 上

如果結果顯示：

```text
URL is on Google
```

意思是這頁可出現在搜尋中，但不保證一定會有排名。

#### 2. Test live URL

這是看「現在這一刻」的頁面狀態，不是只看 Google 先前索引版本。

適合用在：

- 你剛改完頁面
- 你懷疑 Google 抓到的版本太舊
- 你想確認頁面現在能不能被讀取

#### 3. Request indexing

適合用在：

- 新頁剛上線
- 重要頁剛更新
- 修正完索引問題之後

官方文件也提到：

- 重新索引可能要幾天到 1-2 週
- 不保證一定收錄
- 如果有很多頁要更新，`提交 sitemap` 通常更有效率

## 8. Sitemap 怎麼看

`sitemap.xml` 的角色不是保證排名，而是幫 Google 更快知道你有哪些頁面。

你站上的 sitemap 在：

- `https://etimmyqq-lab.github.io/sitemap.xml`

### 操作路徑

```text
Search Console
  → Sitemaps
```

在欄位輸入：

```text
sitemap.xml
```

或完整網址：

```text
https://etimmyqq-lab.github.io/sitemap.xml
```

### 你要看什麼

最重要的是：

```text
Submitted
Success
Last read
Discovered URLs
```

### 圖解判讀

#### 狀況 A

```text
Status = Success
```

代表 Google 已正常讀到 sitemap。

#### 狀況 B

```text
已提交，但長期沒更新
```

代表可能 sitemap 沒更新、沒被重新讀取，或站內新頁沒有被列進去。

這時先檢查：

- sitemap 是否包含新頁
- `<lastmod>` 是否更新

## 9. 單頁沒收錄時，怎麼查

你可以照這個順序：

```text
1. 用 URL Inspection 檢查該頁
2. 看它是不是已在 Google
3. 如果不是，做 Live Test
4. 看是不是 robots / noindex / canonical / 抓取問題
5. 修正後 Request indexing
```

這是你最常遇到的實戰流程。

適合檢查的頁面像：

- 新文章
- 新服務頁
- 新增的 `intake.html`

## 10. 每週檢查一次的標準流程

你每週只要照下面跑一次：

### 第一步：看搜尋成效

```text
Performance
  → 看總曝光
  → 看總點擊
  → 看查詢
  → 看頁面
```

### 第二步：看重要頁有沒有被收錄

```text
Page indexing
  → 先確認重要頁面是否已索引
```

### 第三步：抽查 2 到 3 個重要頁

```text
URL Inspection
  → 首頁
  → 一個服務頁
  → intake 頁
```

### 第四步：確認 sitemap 正常

```text
Sitemaps
  → 看 last read
  → 看 status
```

## 11. 你現在最重要的判讀重點

現階段最值得看的不是一堆細節，而是這 5 個問題：

1. 曝光有沒有慢慢增加
2. 哪些查詢開始出現
3. 重要頁有沒有收錄
4. 哪些頁面曝光高但點擊低
5. 新頁提交後有沒有被 Google 讀到

## 12. 和 GA4 怎麼搭配看

你可以用下面這張圖理解：

```text
Search Console
看：曝光、點擊、收錄

GA4
看：進表單、開始填、開信、複製摘要
```

串起來就是：

```text
Google 看見你
   ↓
使用者點進來
   ↓
進到 intake 頁
   ↓
產生詢問
```

所以你的實際判讀順序應該是：

```text
Search Console 先看有沒有被看見
GA4 再看被看見後有沒有行動
```

## 13. 最簡版結論

如果你今天只記 4 件事，記這個就夠：

```text
1. Performance 看曝光與查詢
2. Pages 看哪些頁面開始被看到
3. URL Inspection 查單頁收錄問題
4. Sitemaps 確認新頁有被 Google 發現
```

## 14. 對你這個網站最值得優先看的頁面

建議你固定追這幾頁：

- `https://etimmyqq-lab.github.io/`
- `https://etimmyqq-lab.github.io/cooperation.html`
- `https://etimmyqq-lab.github.io/intake.html`
- `https://etimmyqq-lab.github.io/services/enterprise-ai-consulting.html`
- `https://etimmyqq-lab.github.io/services/claude-code-training.html`
- `https://etimmyqq-lab.github.io/services/digital-transformation-consulting.html`

因為這幾頁才是真正和：

- 品牌曝光
- 服務承接
- 詢問轉換

最直接相關的頁面。

## 15. 下一步最值得補的東西

這份手冊之後，最值得補的是：

1. `每週檢查清單 one-page 版`
2. `首頁 / 服務頁 CTA 點擊追蹤`
3. `高曝光低 CTR 頁面的標題改寫清單`

因為你接下來真正要做的，不是只看報表，而是：

```text
根據 Search Console 的數字去調整頁面
再用 GA4 看調整後有沒有更會出 lead
```
