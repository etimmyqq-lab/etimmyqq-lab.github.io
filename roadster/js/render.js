// 從 data.js 產生規格卡與時間軸（數字只有一個來源）
(function () {
  const { SPECS, TIMELINE } = RS.data;
  const fmt = (s, v) => v.toFixed(s.decimals);

  document.getElementById('specs').innerHTML = SPECS.map(s =>
    `<div class="spec" data-spec-id="${s.id}">
      <div class="num"><small>${s.prefix}</small><b>${fmt(s, s.value)}</b><span>${s.unit}</span></div>
      <p class="label">${s.label}</p><p class="sub">${s.sub}</p>
    </div>`).join('');

  document.getElementById('timeline').innerHTML = TIMELINE.map(t =>
    `<li class="tl-item">
      <img src="${t.img}" alt="${t.title}" loading="lazy">
      <p class="year">${t.year}</p><h3>${t.title}</h3><p>${t.body}</p>
    </li>`).join('');
})();
