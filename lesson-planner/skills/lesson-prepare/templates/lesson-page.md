# Lesson page template

Copy everything inside the `html` block below into a new `.html` file, then fill only the JSON data block.
Do not change the rest of the code.

````html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lesson</title>
<!--
  Lesson Planner by Menta: lesson page template.
  Fill ONLY the JSON inside <script id="lesson-data">. Everything else stays as is.
  Data shapes: skills/lesson-prepare/reference/exercise-types.md
-->
<style>
:root{
  --bg:#F3F7FC; --surface:#FFFFFF; --raised:#EAF2FB; --text:#13294B; --muted:#5B6B82; --line:#D6E1EE;
  --primary:#1E7BE6; --on-primary:#FFFFFF; --ok:#1F9D57; --ok-bg:#E3F5EA; --bad:#D93B3B; --bad-bg:#FBE6E6;
  --tr:#4A5E7A; --radius:14px; --gap:16px;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0D1726; --surface:#16233A; --raised:#1E2E4A; --text:#E8EEF7; --muted:#9AA9BF; --line:#2A3B58;
    --primary:#4B9BF5; --on-primary:#0D1726; --ok:#4CC782; --ok-bg:#163A2A; --bad:#F07171; --bad-bg:#3D1C22; --tr:#AFC0D8;
  }
}
:root[data-theme="dark"]{
  --bg:#0D1726; --surface:#16233A; --raised:#1E2E4A; --text:#E8EEF7; --muted:#9AA9BF; --line:#2A3B58;
  --primary:#4B9BF5; --on-primary:#0D1726; --ok:#4CC782; --ok-bg:#163A2A; --bad:#F07171; --bad-bg:#3D1C22; --tr:#AFC0D8;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:820px;margin:0 auto;padding:24px 16px 48px}
header.top{margin-bottom:20px}
h1{font-size:28px;line-height:1.2;margin:0 0 6px}
.meta{color:var(--muted);font-size:14px;display:flex;flex-wrap:wrap;gap:6px 14px}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 0}
button{font:inherit;cursor:pointer}
.btn{border:1px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:6px 14px;font-size:14px}
.btn:hover{border-color:var(--primary)}
.btn.primary{background:var(--primary);color:var(--on-primary);border-color:var(--primary)}
section.block{margin:28px 0 0}
.block-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;border-bottom:2px solid var(--line);padding-bottom:6px;margin-bottom:12px}
.block-head h2{font-size:20px;margin:0}
.block-head .min{color:var(--muted);font-size:13px;white-space:nowrap}
.ex{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:16px;margin:0 0 var(--gap)}
.ex-task{font-weight:600;margin:0 0 10px}
.tap{cursor:pointer;text-decoration:underline dotted var(--muted);text-underline-offset:4px}
.tr{display:none;color:var(--tr);font-size:14px;font-style:italic;margin:2px 0 4px}
.tr.on{display:block}
body.all-tr .tr{display:block}
ol.items{margin:0;padding-left:22px}
ol.items>li{margin:0 0 12px}
.gap{display:inline-block;min-width:80px;border:none;border-bottom:2px solid var(--primary);background:transparent;color:var(--text);font:inherit;padding:0 4px;text-align:center}
.gap.ok{border-color:var(--ok);background:var(--ok-bg)}.gap.bad{border-color:var(--bad);background:var(--bad-bg)}
.opts{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.opt{border:1px solid var(--line);background:var(--raised);color:var(--text);border-radius:10px;padding:6px 12px;font-size:15px}
.opt.ok{background:var(--ok-bg);border-color:var(--ok)}.opt.bad{background:var(--bad-bg);border-color:var(--bad)}
.chip.ok{border-color:var(--ok);background:var(--ok-bg)}
.chip{border:1px solid var(--line);background:var(--raised);color:var(--text);border-radius:8px;padding:4px 10px;margin:3px}
.built{min-height:38px;border:1px dashed var(--line);border-radius:10px;padding:4px;margin:6px 0}
.small{font-size:13px;color:var(--muted)}
.check{margin-left:6px}
.ans{display:none;color:var(--ok);font-size:14px;margin-top:4px}
body.show-ans .ans,.ans.on{display:block}
.reading{white-space:pre-line}
.pic{max-width:420px;margin:0 auto 12px}
.pic svg{width:100%;height:auto;display:block}
.dlg p{margin:0 0 6px}.dlg b{color:var(--primary)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
.picopt{border:2px solid var(--line);border-radius:12px;background:var(--surface);padding:6px;text-align:center}
.picopt svg{width:100%;height:auto;display:block}
.picopt.ok{border-color:var(--ok)}.picopt.bad{border-color:var(--bad)}
table.gt{border-collapse:collapse;width:100%;font-size:15px}
table.gt th,table.gt td{border:1px solid var(--line);padding:6px 10px;text-align:left}
table.gt th{background:var(--raised)}
.slide{border-left:4px solid var(--primary);padding:4px 0 4px 12px;margin:0 0 14px}
.slide h3{margin:0 0 4px;font-size:17px}
.mem{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:8px}
.memc{min-height:70px;border-radius:10px;border:1px solid var(--line);background:var(--primary);color:var(--on-primary);font-size:15px;padding:6px}
.memc.open{background:var(--raised);color:var(--text)}.memc.done{background:var(--ok-bg);color:var(--text);border-color:var(--ok)}
.label-wrap{position:relative;max-width:420px;margin:0 auto 10px}
.label-wrap svg{width:100%;height:auto;display:block}
.pin{position:absolute;transform:translate(-50%,-50%);width:26px;height:26px;border-radius:50%;background:var(--primary);color:var(--on-primary);font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center}
.card{border:1px solid var(--line);border-radius:12px;background:var(--raised);padding:10px;text-align:center;min-height:120px}
.card svg{width:100%;height:auto;max-width:160px}
.card .back{display:none}.card.flip .back{display:block}.card.flip .front-word{opacity:.6}
.host{color:var(--primary);font-weight:600}
textarea{width:100%;min-height:56px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--text);font:inherit;padding:8px}
select{font:inherit;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--text);padding:3px 6px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:0 0 8px}
.sortp{display:flex;gap:8px;align-items:flex-start;border:1px solid var(--line);border-radius:10px;padding:8px;margin:0 0 6px;background:var(--surface)}
.sortp .mv{display:flex;flex-direction:column;gap:2px}
.sortp.ok{border-color:var(--ok)}.sortp.bad{border-color:var(--bad)}
.footer-card{margin:36px 0 0;background:var(--raised);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;font-size:15px}
.footer-card a{color:var(--primary);font-weight:600;text-decoration:none}
.footer-card .addr{display:none}
.notes{background:var(--raised);border-radius:10px;padding:10px 12px;font-size:14px;color:var(--muted);margin-top:10px}
@media print{
  :root{--bg:#fff;--surface:#fff;--raised:#f3f3f3;--text:#000;--muted:#444;--line:#bbb;--primary:#000;--tr:#333}
  body{font-size:12pt}
  .toolbar,.check,.opts .hint-btn,.no-print{display:none!important}
  .ex{break-inside:avoid;border-color:#bbb}
  .tr{display:none!important}
  body.print-tr .tr{display:block!important}
  .ans{display:none!important}
  body.show-ans .ans{display:block!important}
  .gap{border-bottom:1px solid #000;min-width:110px}
  .memc{background:#fff!important;color:#000!important}
  .card .back{display:block}
  .footer-card .addr{display:inline}
  textarea{border:none;border-bottom:1px solid #000;border-radius:0;min-height:40px}
}
</style>
</head>
<body>
<main id="app"></main>

<script id="lesson-data" type="application/json">
{
  "title": "Example lesson",
  "language": "French",
  "level": "A2",
  "kind": "Core",
  "minutes": 60,
  "translate_to": "English",
  "ui": {},
  "blocks": []
}
</script>

<script>
(function(){
const D = JSON.parse(document.getElementById('lesson-data').textContent);
const UI = Object.assign({
  print:"Print / Save as PDF", printAns:"PDF with answers", answers:"Teacher answers", translations:"All translations",
  check:"Check", reset:"Reset", model:"Model answer", tapHint:"Tap a sentence to see its translation.",
  min:"min", level:"Level", focus:"Focus", kind:"Lesson", translate:"Translations", phrases:"Useful phrases",
  footer:"Enjoy interactive lessons like this? Join Menta to save each student's progress, teach over video calls, assign homework and more.",
  footerLink:"See your lesson live on Menta →", yourAnswer:"Your answer…", words:"words", start:"Start", choose:"choose…", required:"Use these words:"
}, D.ui || {});
document.title = D.title || 'Lesson';
/* Teacher style (from style-profile.json). Missing = Menta style above. */
const S = D.style || {};
const VARS = {bg:'--bg', surface:'--surface', raised:'--raised', text:'--text', muted:'--muted', line:'--line', primary:'--primary', on_primary:'--on-primary', translation:'--tr'};
for (const k in (S.colors||{})) if (VARS[k]) document.documentElement.style.setProperty(VARS[k], S.colors[k]);
if (S.colors) document.documentElement.setAttribute('data-theme', 'light');
if (S.font) document.body.style.fontFamily = S.font;
if (S.radius != null) document.documentElement.style.setProperty('--radius', S.radius + 'px');
if (D.lang_code) document.documentElement.lang = D.lang_code;

/* ---------- helpers ---------- */
function h(tag, props, ...kids){
  const el = document.createElement(tag);
  for (const k in (props||{})){
    const v = props[k];
    if (k === 'class') el.className = v;
    else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
    else if (k === 'html') el.innerHTML = v; /* only used for author-written SVG pictures */
    else el.setAttribute(k, v);
  }
  for (const c of kids.flat()){ if (c == null || c === false) continue; el.append(c.nodeType ? c : document.createTextNode(String(c))); }
  return el;
}
const norm = s => String(s||'').toLowerCase().replace(/[’`´]/g,"'").replace(/[.!?¡¿,;:]+$/,'').replace(/\s+/g,' ').trim();
const shuffle = a => { a = a.slice(); for (let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; };
function trPair(text, tr, tag){
  const wrap = h(tag||'div');
  const line = h('div', {class:'tr'}, tr||'');
  const main = h('span', tr ? {class:'tap', onclick:()=>line.classList.toggle('on')} : {}, text);
  wrap.append(main); if (tr) wrap.append(line);
  return wrap;
}
function pic(svg, cls){ return svg ? h('div', {class:cls||'pic', html:svg}) : null; }
function ans(text){ return h('div', {class:'ans'}, '✓ ' + text); }
function splitGap(sentence, answer){
  const i = sentence.toLowerCase().indexOf(String(answer).toLowerCase());
  if (i < 0) return [sentence + ' ', ''];
  return [sentence.slice(0,i), sentence.slice(i + answer.length)];
}
function task(ex){ return ex.task ? trPair(ex.task, ex.task_tr, 'div') : null; }
function mark(el, ok){ el.classList.remove('ok','bad'); el.classList.add(ok ? 'ok' : 'bad'); }

/* ---------- exercise renderers ---------- */
const R = {};

R.text = ex => h('div', {}, ex.title ? h('h3', {}, ex.title) : null, pic(ex.picture), h('div', {class:'reading'}, ex.body||''));

R.dialogue = ex => h('div', {class:'dlg'}, ex.title ? h('h3', {}, ex.title) : null,
  (ex.lines||[]).map(l => h('p', {}, h('b', {}, l.speaker + ': '), l.text)));

R.speaking = ex => h('ol', {class:'items'}, (ex.items||[]).map(it => {
  const a = h('div', {class:'ans'}, UI.model + ': ' + (it.model||''));
  return h('li', {}, trPair(it.q, it.tr),
    it.model ? h('button', {class:'btn check', onclick:()=>a.classList.toggle('on')}, UI.model) : null, a);
}));

R.test = ex => h('ol', {class:'items'}, (ex.items||[]).map(it => {
  const [pre, post] = splitGap(it.sentence, it.answer);
  const gap = h('span', {class:'gap'}, ' ');
  const opts = h('div', {class:'opts'}, shuffle([it.answer, ...(it.options||[])]).map(o =>
    h('button', {class:'opt', onclick:e => { const ok = o === it.answer; mark(e.target, ok); if (ok){ gap.textContent = o; mark(gap, true); } }}, o)));
  return h('li', {}, trPair(h('span', {}, pre, gap, post), it.tr), opts, ans(it.answer));
}));

R.gap_fill = ex => h('ol', {class:'items'}, (ex.items||[]).map(it => {
  const [pre, post] = splitGap(it.sentence, it.answer);
  const inp = h('input', {class:'gap', 'aria-label':'gap', size: Math.max(6, it.answer.length + 2)});
  const go = () => mark(inp, norm(inp.value) === norm(it.answer) || (it.accept||[]).some(a => norm(a) === norm(inp.value)));
  inp.addEventListener('keydown', e => { if (e.key === 'Enter') go(); });
  return h('li', {}, trPair(h('span', {}, pre, inp, it.hint ? ' (' + it.hint + ')' : '', post), it.tr),
    h('button', {class:'btn check', onclick:go}, UI.check), ans(it.answer));
}));

R.unscramble = ex => h('ol', {class:'items'}, (ex.items||[]).map(it => {
  const words = it.sentence.replace(/([.!?])$/,'').split(/\s+/);
  const end = (it.sentence.match(/[.!?]$/)||[''])[0];
  const built = h('div', {class:'built'}); const pool = h('div', {});
  const fill = () => { built.innerHTML=''; pool.innerHTML='';
    shuffle(words).forEach(w => pool.append(h('button', {class:'chip', onclick:e => { built.append(e.target); e.target.onclick = ev => { pool.append(ev.target); ev.target.onclick = null; }; }}, w))); };
  fill();
  const go = () => mark(built, norm([...built.children].map(b=>b.textContent).join(' ')) === norm(words.join(' ')));
  return h('li', {}, built, pool, it.tr ? trPair('🔤', it.tr) : null,
    h('button', {class:'btn check', onclick:go}, UI.check), h('button', {class:'btn check', onclick:()=>{built.classList.remove('ok','bad'); fill();}}, UI.reset),
    ans(it.sentence));
}));

R.classify = ex => {
  const cols = ex.columns||[];
  return h('div', {}, h('div', {class:'row small'}, cols.map((c,i) => trPair((i+1) + '. ' + c.title, c.tr, 'span'))),
    (ex.items||[]).map(it => h('div', {class:'row'}, trPair(it.text, it.tr, 'span'),
      cols.map((c,i) => h('button', {class:'opt', onclick:e => mark(e.target, i === it.column)}, c.title)),
      h('span', {class:'ans'}, '→ ' + (cols[it.column]||{}).title))));
};

R.sort_paragraphs = ex => {
  const list = h('div', {});
  const paras = (ex.paragraphs||[]).map((p,i) => ({p, i, tr:(ex.translations||[])[i]}));
  shuffle(paras).forEach(o => {
    const row = h('div', {class:'sortp'});
    row.dataset.i = o.i;
    row.append(h('div', {class:'mv no-print'},
      h('button', {class:'chip', onclick:()=>{ if (row.previousSibling) list.insertBefore(row, row.previousSibling); }}, '↑'),
      h('button', {class:'chip', onclick:()=>{ if (row.nextSibling) list.insertBefore(row.nextSibling, row); }}, '↓')),
      trPair(o.p, o.tr));
    list.append(row);
  });
  return h('div', {}, list, h('button', {class:'btn check', onclick:()=>[...list.children].forEach((r,k)=>mark(r, +r.dataset.i === k))}, UI.check),
    ans((ex.paragraphs||[]).map((p,i)=>(i+1)+'. '+p.slice(0,40)+'…').join('  ')));
};

R.paragraph_headings = ex => {
  const heads = shuffle([...(ex.paragraphs||[]).map(p=>p.heading), ...(ex.extra_headings||[])]);
  return h('div', {}, (ex.paragraphs||[]).map(p => {
    const sel = h('select', {onchange:e => mark(e.target, e.target.value === p.heading)}, h('option', {value:''}, UI.choose), heads.map(x => h('option', {value:x}, x)));
    return h('div', {class:'ex', style:'padding:10px'}, sel, h('div', {class:'reading'}, p.text), ans(p.heading));
  }));
};

R.picture_choice = ex => {
  const items = ex.items||[];
  if (ex.mode === 'fit'){
    return h('div', {}, trPair(ex.question, ex.question_tr), h('div', {class:'grid'},
      shuffle(items).map(o => h('button', {class:'picopt', html:o.svg, onclick:e => mark(e.currentTarget, !!o.correct)}))),
      ans('#' + (items.findIndex(o=>o.correct)+1) + ' (as written)'));
  }
  if (ex.mode === 'word_to_picture'){
    return h('ol', {class:'items'}, items.map(it => h('li', {}, trPair(it.word, it.tr),
      h('div', {class:'grid'}, shuffle(items).map(o => h('button', {class:'picopt', html:o.svg, onclick:e => mark(e.currentTarget, o === it)}))))));
  }
  return h('div', {class:'grid'}, items.map(it => {
    const sel = h('select', {onchange:e => mark(e.target, e.target.value === it.word)}, h('option', {value:''}, UI.choose), shuffle(items).map(o => h('option', {value:o.word}, o.word)));
    return h('div', {class:'picopt'}, pic(it.svg, ''), sel, ans(it.word));
  }));
};

R.memory_pairs = ex => {
  const pairs = (ex.pairs||[]).slice(0,5);
  const cards = shuffle(pairs.flatMap((p,i) => [{t:p.a, i}, {t:p.b, i}]));
  let open = [];
  const board = h('div', {class:'mem'}, cards.map(c => {
    const b = h('button', {class:'memc'}, '?');
    b.onclick = () => {
      if (b.classList.contains('done') || b.classList.contains('open') || open.length === 2) return;
      b.classList.add('open'); b.textContent = c.t; open.push([b,c]);
      if (open.length === 2){
        const [[b1,c1],[b2,c2]] = open;
        if (c1.i === c2.i){ b1.classList.add('done'); b2.classList.add('done'); open = []; }
        else setTimeout(() => { [b1,b2].forEach(x => { x.classList.remove('open'); x.textContent='?'; }); open = []; }, 900);
      }
    };
    return b;
  }));
  return h('div', {}, board, ans(pairs.map(p => p.a + ' = ' + p.b).join(' · ')));
};

R.label_picture = ex => {
  const labels = ex.labels||[];
  const wrap = h('div', {class:'label-wrap', html:ex.svg||''});
  labels.forEach((l,i) => wrap.append(h('div', {class:'pin', style:`left:${l.x*100}%;top:${l.y*100}%`}, String(i+1))));
  const opts = shuffle(labels.map(l=>l.text));
  return h('div', {}, wrap, labels.map((l,i) => {
    const ctl = ex.mode === 'type'
      ? h('input', {class:'gap', onchange:e => mark(e.target, norm(e.target.value) === norm(l.text))})
      : h('select', {onchange:e => mark(e.target, e.target.value === l.text)}, h('option', {value:''}, UI.choose), opts.map(o => h('option', {value:o}, o)));
    return h('div', {class:'row'}, h('b', {}, (i+1) + '.'), ctl, h('span', {class:'ans'}, l.text));
  }));
};

R.grammar_theory = ex => h('div', {}, (ex.slides||[]).map(s => h('div', {class:'slide'},
  h('h3', {}, trPair(s.header, s.header_tr, 'span')), trPair(s.text, s.text_tr),
  s.examples && s.examples.length ? h('ul', {}, s.examples.map(e => h('li', {}, trPair(e.text || e, e.tr, 'span')))) : null)));

R.grammar_table = ex => h('div', {}, ex.title ? h('h3', {}, ex.title) : null,
  h('div', {style:'overflow-x:auto'}, h('table', {class:'gt'},
    h('thead', {}, h('tr', {}, (ex.headers||[]).map(x => h('th', {}, x)))),
    h('tbody', {}, (ex.rows||[]).map(r => h('tr', {}, r.map(x => h('td', {}, x))))))));

R.cards = ex => h('div', {class:'grid'}, (ex.cards||[]).map(c => {
  const card = h('div', {class:'card'}, pic(c.svg, ''), h('div', {class:'front-word'}, h('b', {}, c.word)),
    h('div', {class:'back'}, h('div', {class:'tr on'}, c.tr||''), c.example ? h('div', {class:'small'}, c.example) : null));
  card.onclick = () => card.classList.toggle('flip');
  card.style.cursor = 'pointer';
  return card;
}));

R.incomplete_dialogue = ex => h('div', {}, (ex.lines||[]).map(l => {
  const guest = !l.text || l.text === '…' || l.text === '...';
  if (!guest) return h('p', {}, h('span', {class:'host'}, l.speaker + ': '), l.text, l.tr ? h('div', {class:'tr'}, l.tr) : null);
  const a = h('div', {class:'ans'}, UI.model + ': ' + (l.hint||''));
  return h('div', {style:'margin:0 0 10px'}, h('b', {}, l.speaker + ':'), h('textarea', {placeholder:UI.yourAnswer}),
    l.hint ? h('button', {class:'btn check', onclick:()=>a.classList.toggle('on')}, UI.model) : null, a);
}));

R.production_cards = ex => h('div', {}, (ex.cards||[ex]).map(c => h('div', {class:'slide'},
  trPair(c.role, c.role_tr), c.required_words ? h('div', {class:'small'}, UI.required + ' ',
    c.required_words.map(w => h('label', {style:'margin-right:10px'}, h('input', {type:'checkbox'}), ' ' + w))) : null)));

R.image_task = ex => {
  const p = h('div', {class:'ans'}, (ex.phrases||[]).join(' · '));
  return h('div', {}, pic(ex.svg), ex.phrases ? h('button', {class:'btn check', onclick:()=>p.classList.toggle('on')}, UI.phrases) : null, p);
};

R.match_pairs = ex => {
  const pairs = ex.pairs||[]; const bank = shuffle(pairs.map(p=>p.b));
  return h('div', {}, pairs.map(p => h('div', {class:'row'}, h('b', {style:'min-width:110px'}, p.a),
    h('select', {onchange:e => mark(e.target, e.target.value === p.b)}, h('option', {value:''}, UI.choose), bank.map(b => h('option', {value:b}, b))),
    h('span', {class:'ans'}, p.b))));
};

R.crossword = ex => h('ol', {class:'items'}, (ex.words||[]).map(w => {
  const boxes = [...w.answer].map(() => h('input', {class:'gap', maxlength:'1', style:'min-width:0;width:30px;margin:1px'}));
  boxes.forEach((b,i) => b.addEventListener('input', () => { if (b.value && boxes[i+1]) boxes[i+1].focus(); }));
  const go = () => mark(wrap, norm(boxes.map(b=>b.value).join('')) === norm(w.answer));
  const wrap = h('div', {class:'row'}, boxes);
  return h('li', {}, trPair(w.clue + ' (' + w.answer.length + ')', w.tr), wrap, h('button', {class:'btn check', onclick:go}, UI.check), ans(w.answer));
}));

R.constrained_text = ex => {
  const req = ex.required_words||[]; const min = ex.min_words||0, max = ex.max_words||9999;
  const count = h('span', {class:'small'}, '0 ' + UI.words);
  const chips = req.map(w => h('span', {class:'chip'}, w));
  const area = h('textarea', {placeholder:UI.yourAnswer, style:'min-height:140px'});
  area.addEventListener('input', () => {
    const n = (area.value.trim().match(/\S+/g)||[]).length;
    count.textContent = n + ' / ' + min + '–' + max + ' ' + UI.words;
    count.style.color = n >= min && n <= max ? 'var(--ok)' : 'var(--muted)';
    req.forEach((w,i) => { const used = area.value.toLowerCase().includes(w.toLowerCase()); chips[i].style.borderColor = used ? 'var(--ok)' : 'var(--line)'; chips[i].style.background = used ? 'var(--ok-bg)' : 'var(--raised)'; });
  });
  return h('div', {}, req.length ? h('div', {class:'row'}, chips) : null, area, count, ex.model ? h('div', {class:'ans'}, UI.model + ': ' + ex.model) : null);
};

R.story_telling = ex => {
  const secs = ex.seconds || 60; let left = secs, timer = null;
  const clock = h('b', {style:'font-size:28px'}, '1:00');
  const show = () => clock.textContent = Math.floor(left/60) + ':' + String(left%60).padStart(2,'0');
  show();
  const start = h('button', {class:'btn primary', onclick:() => { if (timer) return; left = secs; show(); timer = setInterval(() => { left--; show(); if (left <= 0){ clearInterval(timer); timer = null; } }, 1000); }}, UI.start);
  return h('div', {}, h('div', {class:'row'}, (ex.phrases||[]).map(p => { const c = h('button', {class:'chip'}, p); c.onclick = () => c.classList.toggle('ok'); return c; })),
    h('div', {class:'row', style:'margin-top:10px'}, clock, start));
};

/* ---------- page ---------- */
const app = document.getElementById('app');
const meta = [ [UI.level, D.level], [UI.kind, D.kind], [UI.focus, D.focus], [D.language], [D.minutes ? D.minutes + ' ' + UI.min : null], [UI.translate, D.translate_to] ]
  .filter(x => x[x.length-1]).map(x => h('span', {}, x.length > 1 ? x[0] + ': ' + x[1] : x[0]));
app.append(h('header', {class:'top'}, h('h1', {}, D.title), h('div', {class:'meta'}, meta),
  D.goal ? h('p', {}, D.goal) : null,
  h('div', {class:'small'}, UI.tapHint),
  h('div', {class:'toolbar'},
    h('button', {class:'btn', onclick:()=>document.body.classList.toggle('all-tr')}, UI.translations),
    h('button', {class:'btn', onclick:()=>document.body.classList.toggle('show-ans')}, UI.answers),
    h('button', {class:'btn', onclick:()=>{ document.body.classList.remove('show-ans'); window.print(); }}, UI.print),
    h('button', {class:'btn', onclick:()=>{ document.body.classList.add('show-ans'); window.print(); setTimeout(()=>document.body.classList.remove('show-ans'), 500); }}, UI.printAns))));

(D.blocks||[]).forEach((b, bi) => {
  const sec = h('section', {class:'block'}, h('div', {class:'block-head'}, h('h2', {}, (bi+1) + '. ' + b.name), b.minutes ? h('span', {class:'min'}, b.minutes + ' ' + UI.min) : null));
  (b.exercises||[]).forEach(ex => {
    const fn = R[ex.type];
    sec.append(h('div', {class:'ex'}, task(ex), fn ? fn(ex) : h('div', {class:'small'}, 'Unknown type: ' + ex.type),
      ex.teacher_note ? h('div', {class:'notes ans'}, ex.teacher_note) : null));
  });
  app.append(sec);
});

app.append(h('aside', {class:'footer-card'},
  UI.footer + ' ', h('a', {href:'https://menta-lms.com', target:'_blank', rel:'noopener'}, UI.footerLink + ' menta-lms.com'),
  h('span', {class:'addr'}, ' (https://menta-lms.com)')));
})();
</script>
</body>
</html>
````
