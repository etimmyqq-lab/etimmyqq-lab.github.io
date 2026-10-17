// 昆廷老師線下課程網站：A/B 兩版共用的動態引擎
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

// ---- 文字解碼：亂碼逐字定格成正確文字 ----
const GLYPHS = '01<>/{}[]#$%AI_=+*';
function decode(el) {
  const target = el.dataset.text || (el.dataset.text = el.textContent);
  if (reduce) { el.textContent = target; return; }
  const start = performance.now(), dur = 700 + target.length * 18;
  (function step(t) {
    const k = clamp((t - start) / dur);
    el.textContent = [...target].map((c, i) =>
      c === ' ' || i / target.length < k ? c : GLYPHS[(Math.random() * GLYPHS.length) | 0]).join('');
    if (k < 1) requestAnimationFrame(step);
  })(start);
}

// ---- 進場 + 解碼（捲到才觸發） ----
const io = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  e.target.classList.add('in');
  if (e.target.matches('[data-decode]')) decode(e.target);
  io.unobserve(e.target);
}), { threshold: .2 });
document.querySelectorAll('.io, [data-decode]').forEach(el => io.observe(el));

// ---- 捲動運鏡：進度 → 畫格；data-frames 留空 = 尚未生成的暫代段落 ----
const scrubs = [...document.querySelectorAll('.scrub')].map(sec => {
  const canvas = sec.querySelector('canvas'), ctx = canvas && canvas.getContext('2d');
  const dir = sec.dataset.frames, count = +sec.dataset.count || 0, frames = [];
  const s = { sec, canvas, ctx, dir, count, frames, loaded: false, last: -1 };
  s.load = () => {                                    // 捲到附近才開始下載
    if (s.loaded || !dir) return; s.loaded = true;
    const order = [];                                 // 先粗後細：每 4 張先抓 1 張
    for (let i = 0; i < count; i += 4) order.push(i);
    for (let i = 0; i < count; i++) if (i % 4) order.push(i);
    order.forEach(i => {
      const im = new Image();
      im.src = `${dir}/f${String(i + 1).padStart(3, '0')}.webp`;
      if (i === 0) im.onload = () => { s.last = -1; };
      frames[i] = im;
    });
  };
  s.beats = [...sec.querySelectorAll('.beat')].map(el => {
    el.querySelectorAll('.split').forEach(h => {
      h.innerHTML = h.innerHTML.split(/(<br>)/).map(part => part === '<br>' ? part :
        `<span class="ln">${[...part].map(c => `<span class="ch">${c}</span>`).join('')}</span>`).join('');
    });
    return { el, a: +el.dataset.in, b: +el.dataset.out, chars: [...el.querySelectorAll('.ch')], subs: [...el.querySelectorAll('.kicker, p, .row')] };
  });
  return s;
});

function sizeCanvases() {
  const dpr = Math.min(devicePixelRatio || 1, 2);
  scrubs.forEach(s => { if (s.canvas) { s.canvas.width = innerWidth * dpr; s.canvas.height = innerHeight * dpr; s.last = -1; } });
}
function drawFrame(s, i) {
  const ok = j => s.frames[j] && s.frames[j].complete && s.frames[j].naturalWidth;
  let k = i;                                          // 還沒載到的畫格 → 用最近一張已載入的
  for (let d = 0; d < s.count; d++) {
    if (ok(i - d)) { k = i - d; break; }
    if (ok(i + d)) { k = i + d; break; }
  }
  const im = s.frames[k]; if (!im || !im.naturalWidth) return;
  const c = s.canvas, sc = Math.max(c.width / im.naturalWidth, c.height / im.naturalHeight);
  const w = im.naturalWidth * sc, h = im.naturalHeight * sc;
  s.ctx.drawImage(im, (c.width - w) / 2, (c.height - h) / 2, w, h);
  s.last = i;
}
function paintBeat(bt, p) {
  const span = .14;
  const enter = bt.a <= 0 ? 1 : clamp((p - bt.a) / span);
  const leave = bt.b >= 1 ? 0 : clamp((p - (bt.b - span)) / span);
  bt.el.style.visibility = enter > 0 && leave < 1 ? 'visible' : 'hidden';
  const n = bt.chars.length || 1;
  bt.chars.forEach((c, i) => {
    const e = clamp(enter * 1.6 - (i / n) * .6), l = clamp(leave * 1.6 - (i / n) * .6), v = e * (1 - l);
    c.style.opacity = v;
    c.style.filter = v < 1 ? `blur(${(1 - v) * 10}px)` : 'none';
    c.style.transform = `translate3d(${l * -30}px,${(1 - e) * 30}px,0)`;
  });
  bt.subs.forEach(x => { const v = clamp(enter * 2 - 1) * (1 - leave); x.style.opacity = v; x.style.transform = `translateY(${(1 - v) * 14}px)`; });
}

// ---- 視差層：data-depth ----
const layers = [...document.querySelectorAll('[data-depth]')];

const nav = document.querySelector('.nav'), dock = document.querySelector('.dock');
function tick() {
  const y = scrollY, vh = innerHeight;
  nav && nav.classList.toggle('solid', y > vh * .5);
  dock && dock.classList.toggle('show', y > vh * .8 && y < document.documentElement.scrollHeight - vh * 1.6);

  scrubs.forEach(s => {
    const r = s.sec.getBoundingClientRect();
    if (r.top < vh * 2.5) s.load();
    if (r.bottom < 0 || r.top > vh) return;
    const p = clamp(-r.top / Math.max(1, r.height - vh));
    if (s.dir) { const f = Math.round(p * (s.count - 1)); if (f !== s.last) drawFrame(s, f); }
    s.beats.forEach(bt => paintBeat(bt, p));
    s.sec.style.setProperty('--p', p.toFixed(3));
  });

  if (!reduce) layers.forEach(l => {
    const r = l.parentElement.getBoundingClientRect();
    if (r.bottom < 0 || r.top > vh) return;
    const c = (r.top + r.height / 2 - vh / 2) / vh;
    l.style.transform = `translate3d(0,${c * +l.dataset.depth * 200}px,0)`;
  });
  requestAnimationFrame(tick);
}
sizeCanvases();
addEventListener('resize', sizeCanvases);
requestAnimationFrame(tick);

// 方案按鈕 → 預選表單方案
document.querySelectorAll('[data-plan]').forEach(a => a.addEventListener('click', () => {
  const sel = document.querySelector('select[name=topic]'); if (sel) sel.value = a.dataset.plan;
}));

// ---- 報名表：沿用既有需求表單的 Google Apps Script ----
const SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbz5FGQnKtRHw4_XQNzEu38jdm9OymVi95nZmbtOsJ0qwXIh2bBIclcpWiz9deErZBpj/exec';
document.querySelectorAll('form.form').forEach(form => form.addEventListener('submit', async e => {
  e.preventDefault();
  const btn = form.querySelector('button'), msg = form.querySelector('.msg');
  btn.disabled = true; msg.textContent = '送出中…';
  try {
    await fetch(SCRIPT_URL, { method: 'POST', mode: 'no-cors', body: new URLSearchParams(new FormData(form)) });
    form.reset(); msg.textContent = '收到了，開課資訊確定後我會第一時間通知你。';
  } catch {
    msg.textContent = '送出失敗，請改用 LINE 或 Email 聯絡我。';
  } finally { btn.disabled = false; }
}));
