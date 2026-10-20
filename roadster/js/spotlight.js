// 展間：亮點＋雷射說明卡＋巡覽
(function () {
  // 照片百分比座標 → object-fit:cover 下的框內像素座標
  function toScreen(natW, natH, boxW, boxH, x, y) {
    const s = Math.max(boxW / natW, boxH / natH);
    const w = natW * s, h = natH * s;
    return { left: (boxW - w) / 2 + x / 100 * w, top: (boxH - h) / 2 + y / 100 * h };
  }
  if (typeof module !== 'undefined') module.exports = { toScreen };
  if (typeof window === 'undefined') return;

  const ctls = [];

  function mount(stage) {
    const spots = RS.data.HOTSPOTS[stage.dataset.photo] || [];
    const img = stage.querySelector('img.base');
    const card = stage.querySelector('.card');
    const layer = stage.querySelector('.hotspots');
    const laser = document.createElement('div');
    laser.className = 'laser';
    layer.appendChild(laser);
    const btns = spots.map((s, i) => {
      const b = document.createElement('button');
      b.className = 'hot';
      b.setAttribute('aria-label', s.title);
      b.addEventListener('click', e => { e.stopPropagation(); open(i); });
      layer.appendChild(b);
      return b;
    });
    let pos = [], idx = -1;

    function layout() {
      if (!img.naturalWidth) return;
      pos = spots.map(s => toScreen(img.naturalWidth, img.naturalHeight, stage.clientWidth, stage.clientHeight, s.x, s.y));
      pos.forEach((p, i) => { btns[i].style.left = p.left + 'px'; btns[i].style.top = p.top + 'px'; });
      if (idx >= 0) placeCard(idx);
    }
    function placeCard(i) {
      const p = pos[i], W = stage.clientWidth, H = stage.clientHeight;
      const cw = card.offsetWidth, ch = card.offsetHeight;
      const right = p.left + 120 + cw < W - 16;
      const left = Math.max(16, right ? p.left + 120 : p.left - 120 - cw);
      card.style.left = left + 'px';
      card.style.top = Math.min(Math.max(16, p.top - ch / 2), H - ch - 16) + 'px';
      card.classList.toggle('from-left', !right);
      // 雷射：從亮點水平射到卡片邊緣
      const from = right ? p.left + 14 : left + cw, to = right ? left : p.left - 14;
      laser.style.left = from + 'px';
      laser.style.top = p.top + 'px';
      laser.style.width = Math.max(0, to - from) + 'px';
      laser.style.transformOrigin = right ? 'left' : 'right';
    }
    function open(i) {
      idx = i;
      card.innerHTML = `<h3>${spots[i].title}</h3><p>${spots[i].body}</p>`;
      btns.forEach((b, j) => b.classList.toggle('active', j === i));
      // 先收回再射出，換點時雷射重打一次
      card.classList.remove('open'); laser.classList.remove('on');
      placeCard(i);
      void laser.offsetWidth;
      card.classList.add('open'); laser.classList.add('on');
    }
    function close() {
      card.classList.remove('open'); laser.classList.remove('on');
      btns.forEach(b => b.classList.remove('active'));
    }
    stage.addEventListener('click', close);
    img.complete ? layout() : img.addEventListener('load', layout);
    addEventListener('resize', layout);

    const ctl = {
      stage,
      tourNext() { if (idx >= spots.length - 1) return false; open(idx + 1); return true; },
      tourPrev() { if (idx <= 0) return false; open(idx - 1); return true; },
      reset() { idx = -1; close(); },
      hasTour: () => spots.length > 0
    };
    ctls.push(ctl);
    return ctl;
  }

  RS.spotlight = { mount, all: () => ctls, toScreen };
})();
