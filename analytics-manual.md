# 網站曝光與詢問追蹤手冊

這份手冊是給 `https://etimmyqq-lab.github.io/` 使用的，重點放在你目前已經上線的曝光與詢問追蹤機制：

- `GA4`
- `Google Search Console`
- `需求表單 intake.html`
- `服務頁 / 合作頁 / 首頁` 的 CTA 承接

## 1. 目前已經完成的項目

網站現在已經有這些基礎：

- 首頁、作者頁、合作方式頁、3 個服務頁、文章群
- `robots.txt`
- `sitemap.xml`
- `canonical`
- `Open Graph / Twitter Card`
- GA4 追蹤碼：`G-3KEGWS9929`
- 需求表單頁：[intake.html](C:/claude/personal-website/intake.html)

需求表單頁目前可追蹤 4 個事件：

- `view_intake_page`
- `intake_form_start`
- `generate_lead`
- `copy_intake_summary`

## 2. 每個事件代表什麼

### `view_intake_page`

代表有人進入需求表單頁。  
這是最上層的「有沒有走到詢問入口」指標。

### `intake_form_start`

代表訪客開始動手填表。  
這比單純進頁更接近真實意圖，可以拿來判斷頁面內容是否有讓人願意往下走。

### `generate_lead`

代表訪客點了「整理後直接開信」。  
這是目前最接近實際詢問的核心事件。

### `copy_intake_summary`

代表訪客把摘要複製走。  
這通常表示對方可能要改用 LINE、手動寄信，或先帶回去整理，不一定會立刻成交，但意圖偏高。

## 3. 在 GA4 怎麼看

登入 `Google Analytics 4` 後，先看這幾個位置。

### 即時看法

路徑：

`報表 -> 即時`

你可以用它確認：

- 自己剛剛觸發的事件有沒有進來
- `view_intake_page` 是否正常出現
- `generate_lead` 和 `copy_intake_summary` 是否有被收進去

### 事件看法

路徑：

`報表 -> 互動 -> 事件`

重點看：

- 哪個事件次數最多
- `view_intake_page -> intake_form_start -> generate_lead` 的落差有多大

你可以這樣解讀：

- `view_intake_page` 很高，但 `intake_form_start` 很低  
  代表表單頁有流量，但文案或入口動機不夠強。

- `intake_form_start` 有起來，但 `generate_lead` 很低  
  代表使用者願意填，但最後沒有送出，通常是 CTA、信任感或填寫負擔要調整。

- `copy_intake_summary` 高於 `generate_lead`  
  代表有些人想先保留資訊，不一定是壞事，但可以考慮未來加更低摩擦的聯絡方式。

## 4. 哪些事件建議設成轉換

目前最建議的轉換事件是：

- `generate_lead`

次要觀察事件：

- `copy_intake_summary`
- `intake_form_start`

原因很簡單：

- `generate_lead` 最接近實際詢問
- `copy_intake_summary` 是高意圖輔助訊號
- `intake_form_start` 是中段意圖，不適合當最終轉換，但很適合看表單是否卡住

## 5. 在 GA4 設定轉換的做法

路徑：

`管理 -> 事件`

找到：

- `generate_lead`

把它標記成轉換事件。

如果之後你想放寬，也可以再把：

- `copy_intake_summary`

一起標成次級轉換。

## 6. Google Search Console 要看什麼

Search Console 不是看「有沒有寄信」，而是看「你有沒有被搜尋到」。

先看這 3 個區塊：

### 成效

路徑：

`成效 -> 搜尋結果`

重點看：

- `總點擊`
- `總曝光`
- `平均 CTR`
- `平均排名`

然後切兩種維度：

- `查詢`
- `頁面`

### 查詢怎麼看

查詢能回答：

- 別人用什麼字找到你
- 哪些字開始有曝光
- 哪些字曝光高但點擊低

如果某些詞已經有曝光，但點擊低：

- 優先改 `title`
- 改 `meta description`
- 讓頁面更直接回答搜尋意圖

### 頁面怎麼看

頁面能回答：

- 哪一頁開始被 Google 看見
- 是首頁、服務頁還是文章最先起來

你現在最該盯的是：

- 首頁
- `services/enterprise-ai-consulting.html`
- `services/claude-code-training.html`
- `services/digital-transformation-consulting.html`
- `intake.html`

## 7. 每週固定檢查一次就好

建議每週固定看一次，不要每天看。

每週看這 6 件事：

1. `Search Console` 哪些查詢開始有曝光
2. 哪些頁面 CTR 明顯偏低
3. 哪個服務頁最會把流量帶去 `intake.html`
4. `view_intake_page` 和 `generate_lead` 的差距
5. `copy_intake_summary` 是否異常偏高
6. 哪一篇文章最常帶人進服務頁

## 8. 如果數字不好，先怎麼判斷

### 情境 A：搜尋曝光低

優先做：

- 補新文章
- 補服務頁內鏈
- 調整標題更貼近搜尋詞

### 情境 B：服務頁有流量，但很少進表單

優先做：

- 強化服務頁 CTA
- 補案例與信任證據
- 把「適合誰、不適合誰」講更清楚

### 情境 C：進表單的人不少，但很少開信

優先做：

- 減少填寫壓力
- 讓按鈕更明確
- 補一句「填完不等於正式預約，只是先整理需求」

### 情境 D：複製摘要高，但開信低

優先做：

- 未來可加 LINE / 表單工具 / Calendly
- 也可能代表使用者偏向先私下整理，不一定是壞訊號

## 9. 你現在最重要的 KPI

現階段不要看太多數字，先盯這 4 個就夠：

- `Search Console 曝光數`
- `服務頁 CTR`
- `view_intake_page`
- `generate_lead`

這 4 個數字對你現在最有意義，因為它們對應的是：

- 有沒有被看到
- 有沒有被點進來
- 有沒有進入詢問入口
- 有沒有產生實際詢問動作

## 10. 下一步最值得補的追蹤

如果你要再往前走，建議下一批補這些事件：

- 首頁 CTA 點擊
- 合作頁 CTA 點擊
- 各服務頁 CTA 點擊
- 文章內文導向服務頁的點擊

這樣你就能知道：

- 哪一個入口最會帶出詢問
- 哪一種主題最容易轉成 lead
- 首頁、服務頁、文章，誰真正有貢獻

## 11. 建議的工作順序

先做：

1. 在 GA4 裡確認 4 個事件都有進來
2. 把 `generate_lead` 設成轉換
3. 每週固定看一次 Search Console

再做：

1. 補首頁 / 服務頁 CTA 點擊事件
2. 看哪個服務頁最有機會先拉出 lead
3. 針對高曝光低 CTR 的頁面改標題與描述

最後才做：

1. 更進階報表
2. 更多事件拆分
3. 更細的內容分眾

## 12. 這份手冊對應的實際檔案

- [intake.html](C:/claude/personal-website/intake.html)
- [index.html](C:/claude/personal-website/index.html)
- [cooperation.html](C:/claude/personal-website/cooperation.html)
- [services/enterprise-ai-consulting.html](C:/claude/personal-website/services/enterprise-ai-consulting.html)
- [services/claude-code-training.html](C:/claude/personal-website/services/claude-code-training.html)
- [services/digital-transformation-consulting.html](C:/claude/personal-website/services/digital-transformation-consulting.html)
- [sitemap.xml](C:/claude/personal-website/sitemap.xml)

如果之後有新增事件，直接把這份手冊一起更新，不要讓站上追蹤和文件脫節。
