// 捲動敘事：開場影片 scrub、數字跳動、背景片段、停點與平滑捲動
(function () {
  const { progressIn } = RS.stops;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hero = document.getElementById('hero');
  const sticky = hero.querySelector('.sticky');
  const video = document.getElementById('heroVideo');
  const absTop = el => el.getBoundingClientRect().top + scrollY;
  const heroRange = () => { const s = absTop(hero); return [s, s + hero.offsetHeight - innerHeight]; };

  // ── 開場 scrub ──
  let ticking = false;
  function applyHero() {
    ticking = false;
    const [s, e] = heroRange();
    const p = progressIn(scrollY, s, e);
    sticky.style.setProperty('--p', p.toFixed(4));
    if (video.duration) video.currentTime = p * (video.duration - 0.05);
  }
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(applyHero); } };

  // ── 進出視窗 ──
  function watch(el, threshold, onIn, onOut) {
    new IntersectionObserver(([en]) => en.isIntersecting ? onIn() : onOut && onOut(), { threshold }).observe(el);
  }

  function countUp() {
    for (const s of RS.data.SPECS) {
      const b = document.querySelector(`.spec[data-spec-id="${s.id}"] b`);
      if (reduced) { b.textContent = s.value.toFixed(s.decimals); continue; }
      const t0 = performance.now();
      const step = now => {
        const k = Math.min(1, (now - t0) / 1200), ease = 1 - Math.pow(1 - k, 3);
        b.textContent = (s.value * ease).toFixed(s.decimals);
        if (k < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }
  }

  function perfClips() {
    const clips = [...document.querySelectorAll('#perf video.bg')];
    let i = 0;
    clips.forEach(v => v.addEventListener('ended', () => {
      clips[i].classList.remove('on');
      i = (i + 1) % clips.length;
      clips[i].currentTime = 0;
      clips[i].classList.add('on');
      clips[i].play().catch(() => {});
    }));
    watch(document.getElementById('perf'), 0.2,
      () => clips[i].play().catch(() => {}), () => clips.forEach(v => v.pause()));
  }

  // ── 停點與平滑捲動 ──
  function getStops() {
    const [s, e] = heroRange();
    const ys = [s, (s + e) / 2, e];
    document.querySelectorAll('.sec:not(#hero), .stage-wrap').forEach(el => ys.push(Math.round(absTop(el))));
    const max = document.documentElement.scrollHeight - innerHeight;
    return [...new Set(ys.map(y => Math.min(Math.round(y), max)))].sort((a, b) => a - b);
  }

  let anim = null;
  function animateTo(y) {
    if (anim) anim.done();
    const from = scrollY, dy = y - from;
    const dur = reduced ? 0 : Math.min(1600, Math.max(600, 400 + Math.abs(dy) * 0.35));
    return new Promise(resolve => {
      const me = { done: () => { if (anim === me) anim = null; resolve(); } };
      anim = me;
      const t0 = performance.now();
      const step = now => {
        if (anim !== me) return;
        const k = dur ? Math.min(1, (now - t0) / dur) : 1;
        const ease = k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
        scrollTo(0, from + dy * ease);
        k < 1 ? requestAnimationFrame(step) : me.done();
      };
      requestAnimationFrame(step);
    });
  }
  // 使用者自己滾輪／觸控就中斷自動捲動
  ['wheel', 'touchstart'].forEach(ev => addEventListener(ev, () => anim && anim.done(), { passive: true }));

  function init() {
    addEventListener('scroll', onScroll, { passive: true });
    addEventListener('resize', onScroll);
    video.addEventListener('loadedmetadata', applyHero);
    applyHero(); // 中段重新整理時，影片直接對到目前捲軸位置
    watch(document.getElementById('perf'), 0.35, countUp);
    perfClips();
    const items = document.querySelectorAll('#story .tl-item');
    watch(document.getElementById('story'), 0.25, () => items.forEach((el, i) => setTimeout(() => el.classList.add('on'), reduced ? 0 : i * 220)));
    const endV = document.querySelector('#end video');
    watch(document.getElementById('end'), 0.2, () => endV.play().catch(() => {}), () => endV.pause());
  }

  RS.scroll = { init, getStops, animateTo };
})();
