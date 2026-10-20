// 規格、熱點、時間軸。數字只放 spec §6.4 查得到來源的；極速版本歸屬不明，先不放。
(function () {
  const SRC_REVEAL = 'Tesla 2026-10-15 發表會；Top Gear、Teslarati 報導';

  const SPECS = [
    { id: 'acc-performance', value: 1.6, decimals: 1, prefix: '<', unit: '秒', label: 'Performance 版 0–96 km/h', sub: '雙座道路版，就已經比多數超跑快', source: SRC_REVEAL },
    { id: 'acc-thrust', value: 0.9, decimals: 1, prefix: '<', unit: '秒', label: 'Thrust 版 0–96 km/h', sub: '加上冷氣體推進，直接噴出去', source: SRC_REVEAL },
    { id: 'acc-rocket', value: 0.59, decimals: 2, prefix: '<', unit: '秒', label: 'Rocket 版 0–96 km/h', sub: '單座、邀請制，眨一下眼就到了', source: SRC_REVEAL },
    { id: 'demo', value: 0.81, decimals: 2, prefix: '', unit: '秒', label: '發表會現場實測', sub: '推進器輔助，現場真的跑給你看', source: SRC_REVEAL },
    { id: 'range', value: 483, decimals: 0, prefix: '>', unit: 'km', label: '續航（官方宣稱）', sub: '超過 300 英里，跑得快也跑得遠', source: SRC_REVEAL }
  ];

  const HOTSPOTS = {
    front: [
      { id: 'headlight', x: 63, y: 52, title: '隱藏式頭燈', body: '頭燈藏在車頭的折角裡，平常只看到一道細光，亮起來才知道它在那。' },
      { id: 'glass', x: 50, y: 37, title: '金色玻璃座艙', body: '整片包覆的暖棕色玻璃，從車頭一路延伸上去，像戰鬥機座艙罩。' },
      { id: 'lightbar', x: 50, y: 58, title: '貫穿式燈條', body: '一條光橫過整個車頭，是新 Roadster 最好認的臉。' }
    ],
    doors: [
      { id: 'gullwing', x: 38, y: 30, title: '鷗翼門', body: '車門往上掀開，像翅膀一樣。上下車有儀式感，停車場也不怕卡到隔壁車。' },
      { id: 'cabin', x: 50, y: 42, title: '雙座座艙', body: 'Performance 跟 Thrust 都是雙座；Rocket 版直接變單座。' },
      { id: 'hood', x: 50, y: 72, title: '俐落車頭', body: '幾乎沒有多餘的線條，一刀切出來的折面，光打上去層次超乾淨。' }
    ],
    rear: [
      { id: 'taillight', x: 66, y: 64, title: '貫穿式尾燈', body: '紅色尾燈一路拉到底，後面的人只會記得這條紅線。' },
      { id: 'nozzle', x: 81, y: 61, title: '車尾圓孔', body: '車尾這幾個圓孔，位置跟官方推進影片對得上；細節官方還沒講清楚。' },
      { id: 'plate', x: 83, y: 47, title: 'RDSTR', body: '官方照片上的車牌就寫 RDSTR，連車牌都在玩梗。' }
    ],
    suspension: [
      { id: 'spring', x: 55, y: 45, title: '金色避震彈簧', body: '官方特寫放在最顯眼位置，金色彈簧配黑色機構，連看不到的地方都在講究。' },
      { id: 'arm', x: 68, y: 55, title: '懸吊連桿', body: '輪子跟車身之間靠這組連桿控制，加速快到 1 秒內，懸吊要撐得住才行。' },
      { id: 'tire', x: 88, y: 75, title: '高性能輪胎', body: '再大的馬力最後都要靠這四塊胎皮抓地。' }
    ],
    fans: [
      { id: 'suction', x: 52, y: 50, title: '吸力系統（位置示意）', body: '官方說底盤有吸力系統，把車子往地面吸，過彎更穩。這張是官方影片的 X 光底盤畫面，熱點只標大概位置。' },
      { id: 'corner', x: 28, y: 22, title: '四個角的懸吊', body: '從正上方看，四個輪子的懸吊機構清清楚楚。' }
    ],
    thrust: [
      { id: 'coldgas', x: 45, y: 22, title: '冷氣體推進', body: 'Thrust 版的選配：噴出高壓冷氣體推車子前進，不是火箭燃燒，是真的「噴出去」。畫面來自官方測試影片。' }
    ]
  };

  const TIMELINE = [
    { year: '2008', title: '第一代 Roadster', body: 'Tesla 的第一台車，證明電動車也可以很快、很帥。', img: 'assets/img/hist-2008.jpg' },
    { year: '2017', title: '第二代預告', body: '在 Semi 發表會最後突然登場，全場暴動。', img: 'assets/img/hist-2017.jpg' },
    { year: '2018', title: '送上太空', body: 'Falcon Heavy 首飛，把一台 Roadster 和 Starman 送進太陽軌道。', img: 'assets/img/hist-starman.jpg' },
    { year: '2026', title: '正式發表', body: '10 月 15 日在德州 Waco 附近亮相，現場跑出 0.81 秒。', img: 'assets/img/rear.jpg' },
    { year: '2028', title: '預計量產', body: '馬斯克說 2028 年量產。這次，大家都在等。', img: 'assets/img/doors.jpg' }
  ];

  const data = { SPECS, HOTSPOTS, TIMELINE };
  if (typeof window !== 'undefined') (window.RS = window.RS || {}).data = data;
  if (typeof module !== 'undefined') module.exports = data;
})();
