// ============================================================
// 昆廷老師網站需求表單 — Google Apps Script
// 使用方式：
//   1. 開啟目標 Google Sheet
//   2. 選單 → 擴充功能 → Apps Script
//   3. 貼上此程式碼（取代預設內容）
//   4. 儲存（Ctrl+S）
//   5. 右上角「部署」→「新增部署作業」
//      - 類型：網路應用程式
//      - 執行身分：我（Me）
//      - 存取權：所有人（Anyone）
//   6. 複製部署 URL，貼到 intake.html 的 SCRIPT_URL 變數
// ============================================================

var SHEET_NAME = '需求表單';
var NOTIFY_EMAIL = 'etimmyqq@gmail.com';

function doPost(e) {
  try {
    var p = e.parameter;
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName(SHEET_NAME);

    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
    }

    // 第一次使用時建立欄位標頭
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['時間戳記', '姓名', '聯絡方式', '身份', '主題', '最卡的事', '一個月期望改變', '補充背景']);
      sheet.setFrozenRows(1);
      sheet.getRange(1, 1, 1, 8).setFontWeight('bold');
    }

    sheet.appendRow([
      new Date(),
      p.name    || '',
      p.contact || '',
      p.identity || '',
      p.topic   || '',
      p.pain    || '',
      p.goal    || '',
      p.context || ''
    ]);

    // 通知信
    MailApp.sendEmail({
      to: NOTIFY_EMAIL,
      subject: '【新需求表單】' + (p.name || '訪客') + ' ｜ ' + (p.topic || '未填主題'),
      body: buildEmailBody(p)
    });

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function buildEmailBody(p) {
  return [
    '有人填了需求表單，以下是內容：',
    '',
    '姓名：'       + (p.name    || '未填'),
    '聯絡方式：'   + (p.contact || '未填'),
    '身份：'       + (p.identity || ''),
    '想談的主題：' + (p.topic   || ''),
    '',
    '【目前最卡的一件事】',
    p.pain || '未填',
    '',
    '【一個月內希望看到的改變】',
    p.goal || '未填',
    '',
    '【補充背景】',
    p.context || '未填',
    '',
    '---',
    '此信由 etimmyqq-lab.github.io/intake.html 自動發送'
  ].join('\n');
}
