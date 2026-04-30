# GA4 圖解版操作手冊

適用網站：`https://etimmyqq-lab.github.io/`  
GA4 代碼：`G-3KEGWS9929`  
手冊更新日：`2026-04-30`

這份是給你自己操作用的圖解版，不講太多理論，重點是：

- 怎麼確認網站有沒有收到資料
- 怎麼看需求表單的 4 個事件
- 怎麼把最重要的事件當成核心轉換指標
- 每週該看哪幾個畫面

對應事件：

- `view_intake_page`
- `intake_form_start`
- `generate_lead`
- `copy_intake_summary`

參考官方文件：

- Realtime report  
  https://support.google.com/analytics/answer/9271392
- About events  
  https://support.google.com/analytics/answer/9322688
- Key events / conversions  
  https://support.google.com/analytics/answer/13965727
- Creating conversions  
  https://support.google.com/analytics/answer/14710559

## 1. 先理解你現在在追什麼

你這個網站的詢問路徑，可以先簡化成下面這張圖：

```text
首頁 / 服務頁 / 合作頁
          ↓
      intake.html
          ↓
  開始填表 intake_form_start
          ↓
  點開信 generate_lead
          ↓
     真正送出詢問
```

另一條輔助路徑：

```text
intake.html
    ↓
copy_intake_summary
    ↓
使用者改用 LINE / 手動寄信 / 先內部整理
```

你現在最重要的不是看「總流量漂不漂亮」，而是看：

```text
有沒有走進 intake 頁
→ 有沒有開始填
→ 有沒有點開信
```

## 2. 第一次檢查：資料有沒有進來

先自己做一次測試：

1. 打開網站首頁
2. 點進 `需求表單`
3. 隨便填幾個欄位
4. 點一次 `整理後直接開信`
5. 再回來點一次 `複製需求摘要`

然後到 GA4 看：

```text
左側選單
Reports
  → Realtime
```

你要看到的是這條路：

```text
進到 Realtime
   ↓
找 Event count by Event name
   ↓
確認下面幾個事件有出現
   - view_intake_page
   - intake_form_start
   - generate_lead
   - copy_intake_summary
```

如果你有看到，就代表前端追蹤有正常送到 GA4。

## 3. Realtime 畫面怎麼看

截至 `2026-04-30`，Google 官方說明的進法是：

```text
Sign in to Google Analytics
  → Reports
  → Realtime
```

你的實際判讀順序建議長這樣：

```text
Realtime
  先看現在有沒有活躍使用者
      ↓
  再看 Event count by Event name
      ↓
  確認 intake 相關事件是否有進來
```

你只要先盯這一塊：

```text
Event count by Event name
```

圖解理解：

```text
如果看到：
view_intake_page = 有
intake_form_start = 有
generate_lead = 有

表示目前這條路是通的。
```

```text
如果只看到：
view_intake_page = 有
intake_form_start = 沒有

表示有人進表單頁，但沒有開始填。
通常是文案、信任感、或表單第一屏不夠有動機。
```

## 4. 事件報表怎麼看

當你不是在測試，而是要看一週表現時，去這裡：

```text
Reports
  → Engagement / 互動
      → Events / 事件
```

如果 GA4 中文介面翻譯略不同，也不用緊張，核心就是：

```text
報表
  → 互動
    → 事件
```

進去後你會看到很多事件名稱。  
你要先找這 4 個：

- `view_intake_page`
- `intake_form_start`
- `generate_lead`
- `copy_intake_summary`

你可以把它想成漏斗：

```text
view_intake_page
        ↓
intake_form_start
        ↓
generate_lead
```

### 圖解判讀

#### 狀況 A

```text
view_intake_page 高
intake_form_start 低
generate_lead 更低
```

解讀：

- 有流量進表單
- 但第一段沒有把人留下來

先改：

- 表單開頭文案
- 第一屏說明
- CTA 附近的信任句

#### 狀況 B

```text
view_intake_page 高
intake_form_start 高
generate_lead 低
```

解讀：

- 人願意填
- 但最後不想按開信

先改：

- 按鈕文案
- 表單欄位負擔
- 補一句「這不是正式預約，只是先整理需求」

#### 狀況 C

```text
copy_intake_summary 高
generate_lead 低
```

解讀：

- 使用者有意圖
- 但偏好先複製走，不一定當下寄出

先改：

- 未來加 LINE
- 或加更低摩擦的聯絡方式

## 5. 關鍵事件和轉換，現在怎麼理解

這裡要講清楚，因為 GA4 近年的命名有調整。

根據 Google 官方文件，截至 `2026-04-30`：

- 在 Analytics 裡，重要行為主要叫 `Key events`
- 如果你要跟 Google Ads 串更一致的廣告轉換衡量，才會再建立 `Conversions`

所以你現在最實用的做法是：

```text
先把 generate_lead 當成你的核心成功事件
```

實務上你可以這樣理解：

```text
網站經營判讀
→ 先看 generate_lead

廣告投放優化
→ 再處理 conversion 對接
```

## 6. 你在 GA4 裡最該盯的事件

優先順序建議如下：

### 第一層：最重要

- `generate_lead`

這是最接近「真的有人要來詢問」的事件。

### 第二層：輔助高意圖

- `copy_intake_summary`

這代表對方有很高機率不是隨便看看。

### 第三層：過程指標

- `intake_form_start`
- `view_intake_page`

它們不是最終成果，但很適合幫你找卡點。

## 7. 怎麼快速檢查單一事件

如果你今天只想看 `generate_lead`，可以用這種思路：

```text
Reports
  → Events
    → 找 generate_lead
```

你要回答的是 3 個問題：

1. 一週內有沒有成長
2. 哪些日期特別高或特別低
3. 它和 `view_intake_page` 的差距大不大

最簡單的圖解判斷：

```text
如果：
view_intake_page = 100
generate_lead = 8

你現在的表單詢問率大約就是 8%
```

不需要一開始就追求完美，只要這個比例能逐步變高，就表示網站承接能力在進步。

## 8. 每週例行檢查流程

每週只要照這個順序跑一次：

### 第一步

```text
Search Console
  → 看曝光
  → 看點擊
  → 看哪些頁面開始被搜到
```

### 第二步

```text
GA4 Realtime
  → 快速確認事件仍正常
```

### 第三步

```text
GA4 Events
  → 看 intake 4 個事件這週表現
```

### 第四步

回答下面 4 題：

1. 哪個入口最會把人帶到 `intake.html`
2. 進表單的人，有多少開始填
3. 開始填的人，有多少按開信
4. 哪個主題的內容最可能帶出詢問

## 9. 你的事件要怎麼和頁面一起看

你現在網站的主要承接頁面有：

- [index.html](C:/claude/personal-website/index.html)
- [cooperation.html](C:/claude/personal-website/cooperation.html)
- [services/enterprise-ai-consulting.html](C:/claude/personal-website/services/enterprise-ai-consulting.html)
- [services/claude-code-training.html](C:/claude/personal-website/services/claude-code-training.html)
- [services/digital-transformation-consulting.html](C:/claude/personal-website/services/digital-transformation-consulting.html)
- [intake.html](C:/claude/personal-website/intake.html)

你可以用下面這張圖理解：

```text
首頁 / 合作頁 / 服務頁
        ↓
    intake.html
        ↓
   generate_lead
```

所以未來如果你要再補追蹤，最值得優先加的是：

```text
首頁 CTA 點擊
合作頁 CTA 點擊
服務頁 CTA 點擊
文章導到服務頁的點擊
```

這樣你就能知道：

- 是首頁最會帶表單
- 還是合作頁最會帶表單
- 還是某一個服務頁其實最能收詢問

## 10. 你自己測試時的標準流程

每次改完頁面，可以用這個 5 分鐘流程驗證：

```text
1. 打開首頁
2. 點進需求表單
3. 填一段測試文字
4. 點開信
5. 點複製摘要
6. 打開 GA4 Realtime
7. 看事件有沒有出現
```

如果都有出現，這次改動通常就安全。

## 11. 常見誤解

### 誤解 1

```text
GA4 沒立刻看到完整資料 = 壞了
```

不是。  
官方文件也提到，完整報表常常不是即時全部到位；即時驗證先看：

- `Realtime`
- `DebugView`

### 誤解 2

```text
流量高 = 詢問一定會高
```

不是。  
你現在更該看的是：

```text
流量是否進到 intake
→ 進到 intake 後是否真的產生 generate_lead
```

### 誤解 3

```text
copy_intake_summary 不算成果
```

也不對。  
它不是最終成果，但對你的站型來說，這是高意圖訊號。

## 12. 最簡版結論

如果你今天只記 3 件事，記這個就夠：

```text
1. Realtime 看事件有沒有進來
2. Events 看 view_intake_page → generate_lead 的落差
3. 每週把 generate_lead 當成最重要的核心指標
```

## 13. 建議下一步

這份圖解版手冊看完之後，最值得補的是：

1. `首頁 CTA 點擊事件`
2. `合作頁 CTA 點擊事件`
3. `服務頁 CTA 點擊事件`

因為現在你已經能看到：

```text
人到了 intake 後有沒有行動
```

下一步要補的是：

```text
人到底是從哪個入口被推進 intake 的
```

這會讓你的判讀從「有沒有詢問」提升成「哪個入口最會產生詢問」。
