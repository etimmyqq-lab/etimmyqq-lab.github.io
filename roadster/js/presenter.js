// 遙控簡報筆：PageDown/PageUp/方向鍵/空白鍵 → 分段推進；滑鼠一動就回自由模式
(function () {
  const { nextStop, keyDir, containing } = RS.stops;
  let target = null, moving = false, anchor = null;

  const absTop = el => Math.round(el.getBoundingClientRect().top + scrollY);
  const stageAt = y => RS.spotlight.all().find(c => Math.abs(Math.min(absTop(c.stage.parentElement), maxY()) - y) < 2);
  const maxY = () => document.documentElement.scrollHeight - innerHeight;
  const setMode = m => { document.body.dataset.mode = m; };

  function go(y) {
    target = y;
    RS.spotlight.all().forEach(c => c.reset()); // 離開的展間收起卡片，進入的展間從頭巡覽
    moving = true;
    RS.scroll.animateTo(y).then(() => { if (target === y) moving = false; });
  }

  function onKey(e) {
    if (e.key === 'F5') return e.preventDefault(); // 簡報筆的「開始」鍵，別讓它重新整理
    const dir = keyDir(e.key, e.shiftKey);
    if (!dir && e.key !== 'Home' && e.key !== 'End') return;
    e.preventDefault();
    setMode('present');
    anchor = null;
    // 動畫中再按：以「上一次的目標」繼續推進，不看目前捲到哪
    if (!moving || target === null) target = Math.round(scrollY);
    const stops = RS.scroll.getStops();
    if (e.key === 'Home') return go(stops[0]);
    if (e.key === 'End') return go(stops[stops.length - 1]);
    // 用滾輪停在展間中間再按：先對齊這個展間，不要直接跳過它的巡覽
    if (!moving) {
      const tops = RS.spotlight.all().map(k => Math.min(absTop(k.stage.parentElement), maxY()));
      const i = containing(target, tops, innerHeight);
      if (i >= 0 && Math.abs(tops[i] - target) >= 2) return go(tops[i]);
    }
    const c = stageAt(target);
    if (c && (dir > 0 ? c.tourNext() : c.tourPrev())) return;
    const y = nextStop(target, stops, dir);
    if (y !== target) go(y);
  }

  function onMouse(e) {
    if (document.body.dataset.mode !== 'present') return;
    if (!anchor) { anchor = { x: e.clientX, y: e.clientY }; return; }
    if (Math.hypot(e.clientX - anchor.x, e.clientY - anchor.y) > 8) setMode('free');
  }

  function init() {
    addEventListener('keydown', onKey);
    addEventListener('mousemove', onMouse, { passive: true });
  }
  RS.presenter = { init };
})();
