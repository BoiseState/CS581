// Jordan's card generator. Run: node make-cards.js
// Emits card-01.svg .. card-05.svg from cards.json.
// Deliberately no human likeness anywhere: each card gets a procedural sigil
// derived from a hash of the actor name, so the art is determined by the data.
const fs = require('fs');
const cards = JSON.parse(fs.readFileSync('cards.json', 'utf8'));

const TIER = {
  'nation-state-tier-1': { ink:'#e8453c', name:'NATION-STATE · TIER 1', bg:'#1a0d0d', accent:'#ff6b5e' },
  'nation-state-tier-2': { ink:'#e8873c', name:'NATION-STATE · TIER 2', bg:'#1a140d', accent:'#ffab5e' },
  'criminal':            { ink:'#9b6bd6', name:'CRIMINAL',             bg:'#140d1a', accent:'#c79bf0' },
  'hacktivist':          { ink:'#3ca8e8', name:'HACKTIVIST (claimed)', bg:'#0d151a', accent:'#6bc7ff' },
};

const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function hash(s){ let h=2166136261; for(const c of s){ h^=c.charCodeAt(0); h=Math.imul(h,16777619);} return h>>>0; }

// Procedural sigil: rotationally symmetric polygon burst seeded by the actor name.
function sigil(seed, accent){
  let h = seed, out = '', rnd = () => ((h = Math.imul(h ^ (h>>>15), 2246822507) >>> 0) / 4294967296);
  const arms = 6 + Math.floor(rnd()*4);
  for (let i=0;i<arms;i++){
    const a = (360/arms)*i, r1 = 46+rnd()*30, r2 = 78+rnd()*44, w = 5+rnd()*13;
    out += `<g transform="rotate(${a.toFixed(1)} 0 0)">`
        +  `<path d="M ${-w} ${-r1} L 0 ${-r2} L ${w} ${-r1} Z" fill="${accent}" opacity="${(0.32+rnd()*0.5).toFixed(2)}"/>`
        +  `</g>`;
  }
  const rings = 2 + Math.floor(rnd()*2);
  for (let i=0;i<rings;i++) out += `<circle r="${(26+i*17).toFixed(0)}" fill="none" stroke="${accent}" stroke-width="${(0.8+rnd()*1.6).toFixed(1)}" opacity="0.5"/>`;
  out += `<circle r="9" fill="${accent}" opacity="0.85"/>`;
  return out;
}

// Naive word wrap for SVG <text> since tspan has no flow.
function wrap(text, max){
  const words=String(text).split(/\s+/), lines=[]; let cur='';
  for(const w of words){ if((cur+' '+w).trim().length>max){ lines.push(cur.trim()); cur=w; } else cur+=' '+w; }
  if(cur.trim()) lines.push(cur.trim());
  return lines;
}

cards.forEach((c, idx) => {
  const t = TIER[c.capability_tier] || TIER['criminal'];
  const n = String(idx+1).padStart(2,'0');
  const aka = c.aka.slice(0,2).join(' · ');
  const cannot = wrap(c.what_this_card_cannot_tell_you, 64).slice(0,6);
  const sectors = wrap(c.sector_targeting.join(' · '), 46).slice(0,2);

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 1050" width="750" height="1050" role="img" aria-label="Threat actor card: ${esc(c.actor)}">
<defs>
  <linearGradient id="g${n}" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="${t.bg}"/><stop offset="1" stop-color="#07090c"/>
  </linearGradient>
  <clipPath id="art${n}"><rect x="42" y="150" width="666" height="380" rx="6"/></clipPath>
</defs>
<rect width="750" height="1050" rx="22" fill="url(#g${n})"/>
<rect x="14" y="14" width="722" height="1022" rx="14" fill="none" stroke="${t.ink}" stroke-width="2.5" opacity="0.75"/>
<rect x="26" y="26" width="698" height="998" rx="9" fill="none" stroke="${t.accent}" stroke-width="0.8" opacity="0.3"/>

<text x="42" y="74" font-family="Georgia,serif" font-size="40" font-weight="bold" fill="#f2f6fa">${esc(c.actor)}</text>
<text x="42" y="104" font-family="monospace" font-size="14" fill="${t.accent}" opacity="0.9">${esc(aka)}</text>
<rect x="42" y="118" width="${Math.min(560, 12+t.name.length*9.4)}" height="24" rx="12" fill="${t.ink}" opacity="0.22"/>
<text x="54" y="135" font-family="monospace" font-size="12.5" font-weight="bold" fill="${t.accent}" letter-spacing="1.4">${esc(t.name)}</text>
<text x="708" y="74" text-anchor="end" font-family="monospace" font-size="34" fill="${t.ink}" opacity="0.5">#${n}</text>

<rect x="42" y="150" width="666" height="380" rx="6" fill="#05070a" stroke="${t.accent}" stroke-width="0.8" opacity="0.95"/>
<g clip-path="url(#art${n})"><g transform="translate(375 340) scale(1.55)">${sigil(hash(c.actor), t.accent)}</g></g>
<text x="56" y="518" font-family="monospace" font-size="10" fill="${t.accent}" opacity="0.45">SIGIL: PROCEDURAL · NOT A LIKENESS · NO PERSON DEPICTED</text>

<line x1="42" y1="558" x2="708" y2="558" stroke="${t.accent}" stroke-width="1" opacity="0.4"/>
<text x="42" y="590" font-family="monospace" font-size="11" fill="#7a8fa6" letter-spacing="1.2">SIGNATURE TTP</text>
<text x="42" y="616" font-family="Georgia,serif" font-size="19" fill="#f2f6fa">${esc(wrap(c.signature_ttp.technique,52)[0])}</text>
${wrap(c.signature_ttp.technique,52)[1] ? `<text x="42" y="640" font-family="Georgia,serif" font-size="19" fill="#f2f6fa">${esc(wrap(c.signature_ttp.technique,52)[1])}</text>` : ''}
<rect x="42" y="654" width="${Math.min(420, 18+String(c.signature_ttp.mitre_ics_id).length*8.6)}" height="26" rx="4" fill="${t.ink}" opacity="0.2"/>
<text x="53" y="672" font-family="monospace" font-size="13" font-weight="bold" fill="${t.accent}">${esc(c.signature_ttp.mitre_ics_id)}</text>

<text x="42" y="718" font-family="monospace" font-size="11" fill="#7a8fa6" letter-spacing="1.2">SECTOR TARGETING</text>
${sectors.map((l,i)=>`<text x="42" y="${740+i*21}" font-family="Georgia,serif" font-size="15" fill="#dce8f4">${esc(l)}</text>`).join('\n')}
<text x="430" y="718" font-family="monospace" font-size="11" fill="#7a8fa6" letter-spacing="1.2">FIRST OBSERVED</text>
${wrap(c.first_observed,32).slice(0,3).map((l,i)=>`<text x="430" y="${740+i*21}" font-family="Georgia,serif" font-size="15" fill="#dce8f4">${esc(l)}</text>`).join('\n')}

<line x1="42" y1="800" x2="708" y2="800" stroke="${t.accent}" stroke-width="1" opacity="0.4"/>
<text x="42" y="828" font-family="monospace" font-size="11" fill="#7a8fa6" letter-spacing="1.2">WHAT THIS CARD CANNOT TELL YOU</text>
${cannot.map((l,i)=>`<text x="42" y="${850+i*19}" font-family="Georgia,serif" font-size="14" fill="#b9cbdd" opacity="0.95">${esc(l)}</text>`).join('\n')}

<line x1="42" y1="958" x2="708" y2="958" stroke="${t.accent}" stroke-width="0.8" opacity="0.3"/>
<text x="42" y="980" font-family="monospace" font-size="10.5" fill="#7a8fa6">CONFIDENCE: ${esc(String(c.confidence).toUpperCase())}</text>
${wrap('PROVENANCE: '+c.provenance, 96).slice(0,2).map((l,i)=>`<text x="42" y="${998+i*15}" font-family="monospace" font-size="9.5" fill="#5f7a90">${esc(l)}</text>`).join('\n')}
<text x="708" y="1010" text-anchor="end" font-family="monospace" font-size="9.5" fill="#4a6070">CS 581 · W2 · J. REYES</text>
</svg>`;
  fs.writeFileSync(`card-${n}.svg`, svg);
  console.log(`card-${n}.svg  ${c.actor}  (${c.capability_tier})`);
});
