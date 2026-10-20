// 純邏輯：停點計算（Node 可測）
(function () {
  const TOL = 0.5; // 捲動位置可能有小數；presenter 用的是精確目標值
  function nextStop(current, stops, dir) {
    if (dir > 0) return stops.find(s => s > current + TOL) ?? stops[stops.length - 1];
    for (let i = stops.length - 1; i >= 0; i--) if (stops[i] < current - TOL) return stops[i];
    return stops[0];
  }
  function progressIn(y, start, end) {
    return end <= start ? 1 : Math.min(1, Math.max(0, (y - start) / (end - start)));
  }
  const KEYS = { PageDown: 1, ArrowDown: 1, ArrowRight: 1, ' ': 1, PageUp: -1, ArrowUp: -1, ArrowLeft: -1 };
  function keyDir(key, shift) { return key === ' ' && shift ? -1 : KEYS[key] || 0; }
  // 畫面中心落在哪個區塊（每塊高 h）；都不在回 -1
  function containing(y, tops, h) {
    const c = y + h / 2;
    return tops.findIndex(t => c >= t && c < t + h);
  }
  const api = { nextStop, progressIn, keyDir, containing };
  if (typeof window !== 'undefined') (window.RS = window.RS || {}).stops = api;
  if (typeof module !== 'undefined') module.exports = api;
})();
