PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Drumless</title>
<style>
:root{--bg:#f5f5f5;--card:#fff;--text:#222;--mute:#777;--line:#e2e2e2;--accent:#3367d6;--err:#c0392b;--ok:#2e7d32}
@media(prefers-color-scheme:dark){:root{--bg:#131313;--card:#2b2b2b;--text:#eaeaea;--mute:#999;--line:#404040;--accent:#5a95f5;--err:#ff7b6b;--ok:#6fcf7a}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.4 system-ui,sans-serif}
main{max-width:760px;margin:0 auto;padding:16px}
h1{font-size:1.4rem;margin:8px 0 2px}.sub{color:var(--mute);margin:0 0 16px}
.card{background:var(--card);border-radius:8px;padding:14px;margin-bottom:12px;box-shadow:0 1px 3px #0002}
#drop{border:2px dashed var(--line);text-align:center;padding:28px 12px;cursor:pointer}
#drop.over{border-color:var(--accent)}
#drop small{display:block;color:var(--mute);margin-top:4px}
.acts{display:flex;gap:12px;align-items:center}
.row{display:flex;gap:8px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.st{font-size:.8rem;color:var(--mute)}.st.done{color:var(--ok)}.st.error{color:var(--err)}
.disc{width:100%;aspect-ratio:1;border-radius:50%;background:
 radial-gradient(circle,var(--card) 0 9%,#0004 9% 10%,transparent 10.5%),
 repeating-radial-gradient(circle,#0000 0 3px,#0000001a 3px 4px),
 conic-gradient(hsl(var(--h) 65% 48%),hsl(var(--h) 75% 70%),hsl(var(--h) 60% 38%),hsl(var(--h) 75% 66%),hsl(var(--h) 65% 48%))}
.disc.busy{opacity:.4}
#list{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
#list>.sub{grid-column:1/-1;margin:0}
.tile{position:relative;aspect-ratio:1;overflow:hidden;background:var(--card);border-radius:10px;padding:10px;display:flex;flex-direction:column;align-items:center;border:2px solid transparent;box-shadow:0 1px 3px #0002;min-width:0}
.tile .disc{width:58%;flex:none}
.tile.pick,.tile.bad{cursor:pointer}.tile.pick:hover{border-color:var(--line)}
.tile.sel{border-color:var(--accent)}
.tname{margin-top:6px;width:100%;font-size:.85rem;font-weight:600;line-height:1.2;text-align:center;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow-wrap:anywhere}
.tile .st{margin-top:2px;text-align:center}
.x{position:absolute;top:4px;right:6px;color:var(--mute);font-size:.9rem;padding:2px 4px}
#player .head{display:flex;gap:14px;align-items:center}
#pdisc{width:64px;flex:none}
.tt{flex:1;min-width:0}
.ptitle{font-size:1.15rem;font-weight:700;overflow-wrap:anywhere}
.pstem{color:var(--mute);font-size:.85rem}
.seg{display:grid;grid-template-columns:repeat(3,1fr);margin-top:16px;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.seg button{padding:10px 6px;font-weight:600;color:var(--mute);border-right:1px solid var(--line)}
.seg button:last-child{border-right:0}
.seg button.on{background:var(--accent);color:#fff}
.wavehead{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:16px;font-size:.85rem;color:var(--mute);font-variant-numeric:tabular-nums}
.zoom{display:flex;gap:6px}
.zoom button{border:1px solid var(--line);border-radius:6px;padding:4px 11px;color:var(--text);font-weight:600;line-height:1.2}
.zoom button:hover{text-decoration:none;border-color:var(--accent)}.zoom button:disabled{opacity:.35;cursor:default;border-color:var(--line)}
#wave,#ovw{display:block;width:100%;touch-action:none;user-select:none;border-radius:8px;background:color-mix(in srgb,var(--text) 5%,transparent)}
#wave{height:136px;margin-top:6px;cursor:pointer}
#ovw{height:34px;margin-top:6px;cursor:pointer}
#ovw[hidden]{display:none}
.transport{display:flex;justify-content:center;align-items:center;gap:28px;margin-top:8px}
#play{width:64px;height:64px;border-radius:50%;background:var(--accent);color:#fff;font-size:1.4rem}
.skip{color:var(--text);border:1px solid var(--line)!important;border-radius:20px;padding:8px 14px}
.loop{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap;margin-top:14px;font-size:.85rem;color:var(--mute);font-variant-numeric:tabular-nums}
.loop input,.loop select{background:transparent;color:var(--text);border:1px solid var(--line);border-radius:6px;padding:4px 6px;font:inherit}
.loop select{background:var(--card)}
.loop input{width:5.5em}.loop input:disabled{opacity:.55}
.skip.on{background:var(--accent);border-color:var(--accent)!important;color:#fff}
.rates{display:flex;gap:6px;align-items:center;margin-top:16px}
.rates span{color:var(--mute);font-size:.75rem;letter-spacing:.08em;margin-right:4px}
.rates button{flex:1;border:1px solid var(--line);border-radius:6px;padding:8px 0;color:var(--text);font-weight:600}
.rates button.on{background:var(--accent);border-color:var(--accent);color:#fff}
.seg button:hover,.rates button:hover,#play:hover,.skip:hover{text-decoration:none}
#play:hover{filter:brightness(1.12)}
#dl{margin-top:14px;font-size:.9rem}#dl summary{color:var(--accent);cursor:pointer}
#dl .links{flex-direction:column;gap:6px}
@keyframes spin{to{transform:rotate(360deg)}}
body.playing #pdisc{animation:spin 4s linear infinite}
#player{border:2px solid var(--accent)}
a,button{color:var(--accent);background:none;border:0;font:inherit;cursor:pointer;padding:0;text-decoration:none}
a:hover,button:hover{text-decoration:underline}
.links{display:flex;gap:14px;margin-top:8px;flex-wrap:wrap;font-size:.9rem}
.err{color:var(--err);font-size:.85rem;overflow-wrap:anywhere}
#logbar{position:fixed;left:0;right:0;bottom:0;background:var(--card);border-top:1px solid var(--line);box-shadow:0 -2px 6px #0002}
#logbar[hidden]{display:none}
#logbar .row{max-width:760px;margin:0 auto;padding:6px 16px;font-size:.85rem}
#logbar .row span{color:var(--mute);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#log{margin:0;height:11rem;overflow:auto;padding:0 16px 8px;font:12px/1.35 ui-monospace,monospace;white-space:pre-wrap;overflow-wrap:anywhere}
#logbar.min #log,#logbar.min #loghandle{display:none}
#loghandle{height:10px;cursor:ns-resize;touch-action:none;display:flex;align-items:center;justify-content:center}
#loghandle::after{content:"";width:40px;height:4px;border-radius:2px;background:var(--line)}
#loghandle:hover::after,#loghandle.drag::after{background:var(--mute)}
</style></head><body><main>
<h1>Drumless</h1><p class="sub">Upload a song, get it back without the drums. <span id="model"></span></p>
<div class="card" id="drop"><input id="file" type="file" accept="audio/*,.flac,.m4a,.opus" multiple hidden>
Drop songs here or click to choose<small>mp3, wav, flac, m4a, ogg … up to 500 MB each</small></div>
<div id="msg" class="err"></div>
<div class="card" id="player" hidden>
 <div class="head"><div class="disc" id="pdisc"></div>
  <div class="tt"><div class="ptitle" id="pname"></div><div class="pstem" id="pstem"></div></div>
  <span class="acts"><button id="pren">Rename</button><button id="pdel">Delete</button></span></div>
 <div class="seg" id="stems"><button data-stem="no_drums">Without drums</button><button data-stem="drums">Drums only</button><button data-stem="original">Original</button></div>
 <div class="wavehead"><span id="time">0:00 / 0:00</span><span class="zoom"><button id="zout" aria-label="Zoom out">−</button><button id="zin" aria-label="Zoom in">+</button><button id="zfit" title="Show the whole song">Fit</button><button id="zloop" title="Zoom to the loop section">Loop</button></span></div>
 <canvas id="wave"></canvas><canvas id="ovw" hidden></canvas>
 <div class="transport"><button class="skip" id="back">⏪ 10s</button><button class="skip" id="stop" aria-label="Stop" title="Stop and go back to the beginning">⏹</button><button id="play" aria-label="Play">▶</button><button class="skip" id="fwd">10s ⏩</button></div>
 <div class="loop"><button class="skip" id="repeat">⟳ Repeat track</button><button class="skip" id="loopsec">⇔ Loop section</button><span id="looptxt"></span></div>
 <div class="loop"><button class="skip" id="click" title="Click in place of the missing drums">♩ Click</button></div>
 <div class="loop" id="clickset" hidden>
  <select id="cmode" aria-label="What to set"><option value="start">start + BPM + beats</option><option value="end">end + BPM + beats</option><option value="span">start + end + beats</option></select>
  <label>start <input id="cstart" type="number" min="0" step="10"> ms</label><button id="cstartnow" title="Use the playhead">⌖</button>
  <label>end <input id="cend" type="number" min="0" step="10"> ms</label><button id="cendnow" title="Use the playhead">⌖</button>
  <label><input id="cbpm" type="number" min="20" max="400" step="0.1"> BPM</label>
  <label><input id="cbeats" type="number" min="1" max="10000" step="1"> beats</label>
  <label title="Beats of click before the music when you press play (0: none)">count-in <input id="ccount" type="number" min="0" max="16" step="1"> beats</label></div>
 <div class="rates" id="rates"><span>SPEED</span><button data-rate="50">50</button><button data-rate="60">60</button><button data-rate="70">70</button><button data-rate="80">80</button><button data-rate="90">90</button><button data-rate="100">100</button></div>
 <details id="dl"><summary>Download</summary><div class="links" id="plinks"></div></details>
</div>
<div id="list"></div>
</main>
<div id="logbar" hidden><div id="loghandle" title="Drag to resize"></div><div class="row"><span id="logname"></span><button id="logtoggle">Hide log</button></div><pre id="log"></pre></div>
<script src="/vendor/SignalsmithStretch.js"></script>
<script>
const $=s=>document.querySelector(s), esc=s=>s.replace(/[&<>"']/g,c=>"&#"+c.charCodeAt(0)+";");
const LABEL={queued:"Queued",separating:"Separating…",mixing:"Mixing…",done:"Done",error:"Failed",cancelled:"Cancelled"};
function elapsed(t){const s=Math.max(0,Math.round(Date.now()/1000-t));return Math.floor(s/60)+"m "+String(s%60).padStart(2,"0")+"s"}
const STEMS={no_drums:"Without drums",drums:"Drums only",original:"Original"};
const fmt=x=>{if(!isFinite(x))return"0:00";x=Math.floor(x);return Math.floor(x/60)+":"+String(x%60).padStart(2,"0")};
const hue=n=>{let h=0;for(const c of n)h=(h*31+c.charCodeAt(0))%360;return h};
const MIN_LOOP=0.5,MIN_VIEW=1,PPS=200; // PPS: peaks per second, as the server makes them
let tracks=[],cur=null,stem="no_drums",rate=1,dragging=false,repeat=false,loop={a:null,b:null,on:false};
let peaks=null,peakCache={},view={s:0,l:null},dirty=true,holdFollow=0; // view.l null: the whole song
try{rate=+localStorage.getItem("rate")||1;repeat=localStorage.getItem("repeat")==="1"}catch(e){}
// Playback. The song is decoded into memory and played through WebAudio, so the loop is gapless and the click runs on
// the same clock as the music. At 100% the buffer plays as it is; slower, it goes through Signalsmith Stretch (the pitch is kept).
// The engine keeps the song position `aPos` at context time `aOut`, advancing at `rate` and wrapping in the loop region; the
// playhead and the click times are worked out from that, not read back from the audio nodes.
const audio=(()=>{
  const FADE=0.005,LEAD=0.05;
  let ctx=null,buf=null,node=null,nodeBuf=null,nodeGain=null,kind=null,src=null,srcGain=null;
  let playing=false,aOut=Infinity,aPos=0,preT=Infinity,prePos=0,gen=0,loadGen=0,loopTimer=0,seekTimer=0,seekAt=0,prepP=Promise.resolve();
  const A={onplay:null,onpause:null,onended:null,onloadedmetadata:null,onanchor:null,preroll:null};
  const context=()=>ctx||(ctx=new (window.AudioContext||window.webkitAudioContext)());
  const region=()=>loop.on&&loop.a!==null?[loop.a,loop.b]:repeat&&buf?[0,buf.duration]:null;
  function posAt(tc){ // the song position at context time tc
    if(!buf)return 0;
    if(!playing||tc<=aOut)return aPos;
    let x=aPos+(tc-aOut)*rate;const r=region();
    if(r&&aPos<r[1]&&x>=r[1])x=r[0]+(x-r[0])%(r[1]-r[0]);
    return Math.min(x,buf.duration);
  }
  A.segments=(from,to)=>{ // [{t, p0, p1}]: from context time t the song plays from p0 to p1 (a loop gives several)
    const out=[];if(!playing||!buf||aOut===Infinity)return out;
    if(preT<aOut&&from<aOut){ // count-in: the click runs ahead of the music, which enters at aOut (the song position goes below 0 if the grid says so)
      const t0=Math.max(from,preT),t1=Math.min(to,aOut);
      if(t1>t0)out.push({t:t0,p0:prePos+(t0-preT)*rate,p1:prePos+(t1-preT)*rate,pre:true});
    }
    const r=region();let t=Math.max(from,aOut),p=aPos+(t-aOut)*rate;
    if(r&&aPos<r[1]&&p>=r[1])p=r[0]+(p-r[0])%(r[1]-r[0]);
    while(t<to){
      const end=r&&p<r[1]?r[1]:buf.duration,tEnd=t+(end-p)/rate;
      out.push({t,p0:p,p1:p+(Math.min(tEnd,to)-t)*rate});
      if(!(r&&p<r[1]&&tEnd<to))break;
      t=tEnd;p=r[0];
    }
    return out;
  };
  async function doPrepare(stretch){
    const c=context();
    if(c.state!=="running")await c.resume().catch(()=>{});
    if(!stretch)return;
    if(!node){
      node=await SignalsmithStretch(c);
      nodeGain=c.createGain();nodeGain.gain.value=0;node.connect(nodeGain).connect(c.destination);
    }
    if(nodeBuf!==buf){
      const b=buf;nodeBuf=null;
      await node.dropBuffers();
      await node.addBuffers(Array.from({length:b.numberOfChannels},(_,i)=>new Float32Array(b.getChannelData(i))));
      nodeBuf=b;
    }
  }
  const prepare=s=>prepP=prepP.catch(()=>{}).then(()=>doPrepare(s)); // one at a time
  function stopKind(k,at){ // fade the sound out from context time `at`
    if(k==="native"&&src){
      const s=src,g=srcGain;src=srcGain=null;
      g.gain.cancelScheduledValues(at);g.gain.setValueAtTime(1,at);g.gain.linearRampToValueAtTime(0,at+FADE);
      try{s.stop(at+FADE+0.01)}catch(e){}
    }else if(k==="stretch"&&node){
      const g=nodeGain.gain;g.cancelScheduledValues(at);g.setValueAtTime(1,at);g.linearRampToValueAtTime(0,at+FADE);
      node.schedule({output:at+FADE,active:false});
    }
  }
  async function restart(p,countIn){ // (re)start the sound at position p (default: where it is now) with the present settings; countIn: lead in with the click
    const my=++gen,next=rate===1?"native":"stretch";
    try{await prepare(next==="stretch")}
    catch(e){if(my===gen){$("#msg").textContent="Playback failed: "+(e.message||e);A.pause()}return}
    if(my!==gen||!playing||!buf)return;
    const c=ctx,tc=c.currentTime+LEAD;
    let q=p===undefined?posAt(tc):p;
    const r=region();if(loop.on&&r&&(q<r[0]||q>=r[1]))q=r[0]; // a section that is on starts inside it
    q=Math.max(0,Math.min(q,buf.duration-0.001));
    let ts=tc,pp=Infinity; // ts: when the music enters
    if(countIn&&A.preroll){const p0=A.preroll(q);if(p0!==null&&p0<q){pp=p0;ts=tc+(q-p0)/rate}}
    if(kind&&kind!==next)stopKind(kind,tc);
    if(next==="native"){
      if(kind==="native")stopKind("native",tc);
      const s=c.createBufferSource(),g=c.createGain();s.buffer=buf;
      if(r){s.loop=true;s.loopStart=r[0];s.loopEnd=r[1]}
      g.gain.setValueAtTime(0,ts);g.gain.linearRampToValueAtTime(1,ts+FADE);
      s.connect(g).connect(c.destination);s.start(ts,q);src=s;srcGain=g;
    }else{
      const g=nodeGain.gain;g.cancelScheduledValues(tc-FADE);
      if(kind==="stretch"){g.setValueAtTime(1,tc-FADE);g.linearRampToValueAtTime(0,tc)}
      g.setValueAtTime(0,ts);g.linearRampToValueAtTime(1,ts+FADE);
      node.schedule({output:ts,active:true,input:q,rate,semitones:0,loopStart:r?r[0]:0,loopEnd:r?r[1]:0});
    }
    kind=next;aPos=q;aOut=ts;preT=tc;prePos=pp;dirty=true;
    if(A.onanchor)A.onanchor(tc);
  }
  function finish(){ // ran off the end
    playing=false;aPos=buf.duration;aOut=Infinity;++gen;stopKind(kind,ctx.currentTime);kind=null;dirty=true;
    if(A.onended)A.onended();
  }
  setInterval(()=>{if(playing&&buf&&aOut<Infinity&&!region()&&posAt(ctx.currentTime)>=buf.duration-0.003)finish()},25);
  Object.defineProperties(A,{
    paused:{get:()=>!playing},ended:{get:()=>false},
    duration:{get:()=>buf?buf.duration:NaN},
    currentTime:{
      get:()=>ctx?posAt(ctx.currentTime-(ctx.outputLatency||0)):aPos,
      set(v){
        if(!buf)return;
        aPos=Math.max(0,Math.min(v,buf.duration));dirty=true;
        if(!playing)return;
        aOut=Infinity; // the playhead stays where it was put until the sound follows
        clearTimeout(seekTimer);seekTimer=setTimeout(()=>{seekAt=performance.now();restart(aPos)},Math.max(0,seekAt+40-performance.now()));
      }
    },
  });
  A.context=context;
  A.play=async()=>{
    if(!buf||playing)return;
    if(aPos>=buf.duration-0.01)aPos=0;
    playing=true;aOut=Infinity;dirty=true;
    if(A.onplay)A.onplay();
    await restart(aPos,true);
  };
  A.pause=()=>{
    if(!playing)return;
    const p=posAt(ctx.currentTime);++gen;clearTimeout(seekTimer);
    stopKind(kind,ctx.currentTime);kind=null;aPos=p;aOut=Infinity;playing=false;dirty=true;
    if(A.onpause)A.onpause();
  };
  A.applyLoop=()=>{ // the loop section or repeat changed: carry on in the new region
    if(!playing||aOut===Infinity)return; // a restart is already on its way
    clearTimeout(loopTimer);loopTimer=setTimeout(()=>restart(),60);
  };
  A.rateChanged=()=>{if(playing)restart()};
  A.unload=()=>{
    ++gen;++loadGen;clearTimeout(seekTimer);
    if(ctx)stopKind(kind,ctx.currentTime);
    kind=null;playing=false;buf=null;aPos=0;aOut=Infinity;nodeBuf=null;dirty=true;
    if(node)node.dropBuffers();
    if(A.onpause)A.onpause();
  };
  A.load=async(url,keep)=>{ // keep: a stem change in the same song, the position and play state stay
    const my=++loadGen;
    const r=await fetch(url);if(!r.ok)throw new Error("HTTP "+r.status);
    const data=await r.arrayBuffer();if(my!==loadGen)return;
    const b=await context().decodeAudioData(data);if(my!==loadGen)return;
    buf=b;
    if(keep)aPos=Math.min(aPos,b.duration);else{aPos=0;playing=false}
    dirty=true;
    if(A.onloadedmetadata)A.onloadedmetadata();
    if(keep&&playing)restart();
  };
  return A;
})();
function tile(t){
  const run=t.status==="separating"||t.status==="mixing",done=t.status==="done";
  const st=done?"":LABEL[t.status]+(t.status==="queued"&&t.position?` (#${t.position})`:"")+(run?" · "+elapsed(t.started):"");
  const x=run?`<button class="x" data-cancel="${t.id}" title="Cancel" aria-label="Cancel">✕</button>`:done?"":`<button class="x" data-del="${t.id}" title="Delete" aria-label="Delete">✕</button>`;
  const cls=["tile",done&&"pick",t.status==="error"&&"bad",t.id===cur&&"sel"].filter(Boolean).join(" ");
  return `<div class="${cls}" data-id="${t.id}" data-err="${esc(t.error||"")}" style="--h:${hue(t.name)}">${x}
   <div class="disc${done?"":" busy"}"></div><div class="tname">${esc(t.name)}</div><div class="st ${t.status}">${st}</div></div>`;
}
function setRate(r){
  rate=r;audio.rateChanged();
  document.querySelectorAll("#rates button").forEach(b=>b.classList.toggle("on",+b.dataset.rate===Math.round(r*100)));
  try{localStorage.setItem("rate",r)}catch(e){}
}
async function showStem(keepPos){
  const id=cur,sm=stem;
  loadPeaks();
  $("#pstem").textContent=STEMS[sm]+" · loading…";
  document.querySelectorAll("#stems button").forEach(b=>b.classList.toggle("on",b.dataset.stem===sm));
  try{await audio.load(`/files/${id}/${sm}`,keepPos)}
  catch(e){if(cur===id&&stem===sm)$("#msg").textContent="Could not load "+STEMS[sm]+": "+(e.message||e)}
  if(cur===id&&stem===sm)$("#pstem").textContent=STEMS[sm];
}
function select(id){
  const l=(tracks.find(t=>t.id===id)||{}).loop;
  loop=l?{a:l.a,b:l.b,on:!!l.on}:{a:null,b:null,on:false};updateLoopUi();
  cur=id;stem="no_drums";view={s:0,l:null};loadClick();
  for(const k in peakCache)if(!k.startsWith(id+"/"))delete peakCache[k];$("#player").hidden=false;
  $("#plinks").innerHTML=Object.entries(STEMS).map(([k,l])=>`<a href="/files/${id}/${k}?dl=1">${l}</a>`).join("");
  $("#dl").open=false;audio.unload();showStem(false);syncPlayer();
  $("#player").scrollIntoView({behavior:"smooth",block:"nearest"});
}
function syncPlayer(){
  const t=tracks.find(t=>t.id===cur);
  if(!t){if(cur){cur=null;audio.unload()}$("#player").hidden=true;return}
  $("#pname").textContent=t.name;$("#pdisc").style.setProperty("--h",hue(t.name));
}
const dur=()=>isFinite(audio.duration)?audio.duration:(peaks?peaks.length/PPS:0);
function vw(){ // the visible window, kept inside the song
  const d=dur(),l=view.l===null||view.l>=d?d:Math.max(Math.min(MIN_VIEW,d),view.l);
  return{s:Math.max(0,Math.min(view.s,Math.max(0,d-l))),l,d};
}
function setView(s,l){view={s,l};dirty=true;holdFollow=performance.now()+4000}
function zoomBy(f,focus){ // f above 1 zooms in; the song position at `focus` (0..1 across the view) stays under it
  const{s,l,d}=vw();if(!d)return;
  const nl=Math.min(d,Math.max(Math.min(MIN_VIEW,d),l/f));
  setView(s+focus*l-focus*nl,nl>=d?null:nl);
}
async function loadPeaks(){
  const id=cur,sm=stem,key=id+"/"+sm;
  if(peakCache[key]){peaks=peakCache[key];dirty=true;return}
  peaks=null;dirty=true;
  try{
    const r=await fetch(`/api/tracks/${id}/peaks/${sm}`);if(!r.ok)return;
    const a=new Uint8Array(await r.arrayBuffer());peakCache[key]=a;
    if(cur===id&&stem===sm){peaks=a;dirty=true}
  }catch(e){}
}
const wave=$("#wave"),ovw=$("#ovw"),wc=wave.getContext("2d"),oc=ovw.getContext("2d");
const css=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
function sizeOf(c){const r=c.getBoundingClientRect(),k=devicePixelRatio||1;
  const w=Math.round(r.width*k),h=Math.round(r.height*k);if(c.width!==w||c.height!==h){c.width=w;c.height=h}return{k,W:r.width,H:r.height}}
function colMax(a,t0,t1){ // loudest peak between two times, 0..1
  const i0=Math.floor(t0*PPS),i1=Math.min(a.length-1,Math.max(i0,Math.ceil(t1*PPS)-1));let m=0;
  for(let j=i0;j<=i1;j++)if(a[j]>m)m=a[j];return m/255;
}
function drawWave(){
  const{k,W,H}=sizeOf(wave),c=wc;c.setTransform(k,0,0,k,0,0);c.clearRect(0,0,W,H);
  const{s,l,d}=vw();if(!d||!W)return;
  const mute=css("--mute"),acc=css("--accent"),txt=css("--text"),line=css("--line");
  const xOf=t=>(t-s)/l*W,on=loop.on&&loop.a!==null,xa=on?xOf(loop.a):0,xb=on?xOf(loop.b):0;
  const Hw=H-16,mid=Hw/2;
  if(on){c.fillStyle=acc;c.globalAlpha=.14;const x0=Math.max(0,xa);c.fillRect(x0,0,Math.min(W,xb)-x0,Hw);c.globalAlpha=1}
  const n=Math.max(1,Math.floor(W/2.5)),cw=W/n;c.lineWidth=cw*0.7;c.lineCap="butt";
  if(!peaks){c.strokeStyle=line;c.lineWidth=2;c.beginPath();c.moveTo(0,mid);c.lineTo(W,mid);c.stroke()}
  else for(let i=0;i<n;i++){
    const t0=s+i*l/n;if(t0*PPS>=peaks.length)break;
    const x=(i+.5)*cw,half=Math.max(1,colMax(peaks,t0,s+(i+1)*l/n)*mid);
    c.strokeStyle=on&&x>=xa&&x<=xb?acc:mute;c.beginPath();c.moveTo(x,mid-half);c.lineTo(x,mid+half);c.stroke();
  }
  // time ruler
  const step=[1,2,5,10,15,30,60,120,300,600].find(v=>v/l*W>=80)||600;
  c.fillStyle=mute;c.strokeStyle=line;c.lineWidth=1;c.font="11px system-ui,sans-serif";
  for(let t=Math.ceil(s/step)*step;t<=s+l;t+=step){const x=Math.round(xOf(t))+.5;c.beginPath();c.moveTo(x,Hw);c.lineTo(x,Hw+4);c.stroke();c.fillText(fmt(t),x+3,H-3)}
  if(click.on){ // where the click's beats fall (the first one stronger); too close together to tell apart when zoomed out
    const g=60/click.bpm,s0=click.start/1000,px=g/l*W;
    if(px>=4){
      c.strokeStyle=css("--err");c.lineWidth=1;
      for(let i=Math.max(0,Math.ceil((s-s0)/g));i<click.beats;i++){
        const t=s0+i*g;if(t>s+l)break;
        const x=Math.round(xOf(t))+.5;c.globalAlpha=i?.55:1;c.lineWidth=i?1:2;
        c.beginPath();c.moveTo(x,0);c.lineTo(x,Hw);c.stroke();
      }
      c.globalAlpha=1;
    }
  }
  if(on)for(const x of[xa,xb]){
    if(x<-8||x>W+8)continue;
    c.strokeStyle=acc;c.fillStyle=acc;c.lineWidth=3;c.beginPath();c.moveTo(x,0);c.lineTo(x,Hw);c.stroke();
    for(const y of[8,Hw-8]){c.beginPath();c.arc(x,y,7,0,7);c.fill()}
  }
  const px=xOf(audio.currentTime);
  if(px>=0&&px<=W){c.globalAlpha=.9;c.strokeStyle=txt;c.lineWidth=2;c.beginPath();c.moveTo(px,0);c.lineTo(px,Hw);c.stroke();c.globalAlpha=1}
}
let ovBars=null;
function drawOvw(){
  const{s,l,d}=vw(),zoomed=d>0&&l<d-1e-6;ovw.hidden=!zoomed;if(!zoomed)return;
  const{k,W,H}=sizeOf(ovw),c=oc;c.setTransform(k,0,0,k,0,0);c.clearRect(0,0,W,H);
  const mute=css("--mute"),acc=css("--accent"),txt=css("--text"),mid=H/2,n=Math.max(1,Math.floor(W/2)),cw=W/n;
  if(peaks&&(!ovBars||ovBars.src!==peaks||ovBars.n!==n)){ // the whole song's bars only change with the peaks or the width
    ovBars={src:peaks,n,v:Array.from({length:n},(_,i)=>colMax(peaks,i*d/n,(i+1)*d/n))};
  }
  const x0=d?s/d*W:0,x1=d?(s+l)/d*W:W,on=loop.on&&loop.a!==null;
  if(on){c.fillStyle=acc;c.globalAlpha=.2;c.fillRect(loop.a/d*W,0,(loop.b-loop.a)/d*W,H);c.globalAlpha=1}
  c.lineWidth=cw*0.7;c.strokeStyle=mute;
  if(ovBars)ovBars.v.forEach((m,i)=>{const x=(i+.5)*cw,h=Math.max(1,m*mid);c.beginPath();c.moveTo(x,mid-h);c.lineTo(x,mid+h);c.stroke()});
  c.strokeStyle=txt;c.lineWidth=2;c.globalAlpha=.85;c.beginPath();c.moveTo(audio.currentTime/d*W,0);c.lineTo(audio.currentTime/d*W,H);c.stroke();
  c.globalAlpha=1;c.lineWidth=2;c.strokeRect(x0+1,1,Math.max(3,x1-x0-2),H-2);
}
function followPlayhead(){ // zoomed in and playing: turn the page when the playhead leaves the window
  if(audio.paused||dragging||performance.now()<holdFollow)return;
  const{s,l,d}=vw();if(l>=d-1e-6)return;
  const t=audio.currentTime;if(t<s||t>s+l)view={s:t-l*0.1,l:view.l};
}
let lastTime="";
function frame(){
  if(!$("#player").hidden&&(dirty||!audio.paused)){
    dirty=false;followPlayhead();drawWave();drawOvw();
    const t=fmt(audio.currentTime)+" / "+fmt(dur());if(t!==lastTime){lastTime=t;$("#time").textContent=t}
    const{l,d}=vw();$("#zin").disabled=!d||l<=Math.min(MIN_VIEW,d)+1e-6;$("#zout").disabled=$("#zfit").disabled=!d||l>=d-1e-6;$("#zloop").disabled=loop.a===null;
  }
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
new ResizeObserver(()=>{dirty=true}).observe(wave);
matchMedia("(prefers-color-scheme:dark)").addEventListener("change",()=>{dirty=true});
function updateLoopUi(){
  $("#loopsec").classList.toggle("on",loop.on);$("#repeat").classList.toggle("on",repeat);
  $("#looptxt").textContent=loop.a===null?"":loop.on?fmt(loop.a)+" – "+fmt(loop.b)+" · drag the handles":"saved "+fmt(loop.a)+" – "+fmt(loop.b);
}
function saveLoop(){
  if(loop.a===null||!cur)return;
  const body={a:loop.a,b:loop.b,on:loop.on},t=tracks.find(t=>t.id===cur);
  if(t)t.loop=body;
  fetch("/api/tracks/"+cur+"/loop",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)}).catch(()=>{});
}
async function refresh(){
  try{
    const d=await (await fetch("/api/tracks")).json();
    $("#model").textContent="Model: "+d.model.replace(/\.(yaml|ckpt)$/,"");
    tracks=d.tracks;
    const sig=JSON.stringify([cur,d.tracks.map(t=>[t.id,t.name,t.status,t.position])]);
    if(sig!==refresh.sig||d.tracks.some(t=>t.status==="separating"||t.status==="mixing")){
      $("#list").innerHTML=d.tracks.map(tile).join("")||'<p class="sub">No tracks yet.</p>';refresh.sig=sig;
    }
    syncPlayer();
  }catch(e){}
}
audio.onloadedmetadata=()=>{
  const d=audio.duration;
  if(loop.a!==null&&isFinite(d)){loop.b=Math.min(loop.b,d);loop.a=Math.max(0,Math.min(loop.a,loop.b-MIN_LOOP));updateLoopUi()}
  dirty=true;
};
// Click: a metronome you set by hand where the drums are missing (e.g. a drums-only intro). A grid is start, BPM and
// number of beats (end = the last beat); you give any three of start/end/BPM/beats (`mode` says which) and the fourth is worked out.
// Saved per song.
const CLICK_DEFAULT={start:0,bpm:120,beats:32,mode:"start",on:false,countin:0};
let click={...CLICK_DEFAULT},clickEnd=0,clickLast=0,clickNodes=[];
const gapMs=()=>60000/click.bpm;
function loadClick(){
  const c=(tracks.find(t=>t.id===cur)||{}).click;
  click=c?{start:c.start,bpm:c.bpm,beats:c.beats,mode:c.mode||"start",on:!!c.on,countin:c.countin||0}:{...CLICK_DEFAULT};
  updateClickUi();
}
function updateClickUi(){
  clickEnd=click.start+(click.beats-1)*gapMs();
  dirty=true;$("#click").classList.toggle("on",click.on);$("#clickset").hidden=!click.on;
  $("#cmode").value=click.mode;
  $("#cstart").value=Math.round(click.start);$("#cend").value=Math.round(clickEnd);
  $("#cbpm").value=+click.bpm.toFixed(2);$("#cbeats").value=click.beats;$("#ccount").value=click.countin;
  // the one that is worked out can't be typed into
  $("#cstart").disabled=$("#cstartnow").disabled=click.mode==="end";
  $("#cend").disabled=$("#cendnow").disabled=click.mode==="start";
  $("#cbpm").disabled=click.mode==="span";
}
function saveClick(){
  if(!cur)return;
  const t=tracks.find(t=>t.id===cur);if(t)t.click={...click};
  fetch("/api/tracks/"+cur+"/click",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(click)}).catch(()=>{});
}
function readClick(){
  const m=$("#cmode").value,s=+$("#cstart").value,e=+$("#cend").value,b=+$("#cbpm").value,n=Math.round(+$("#cbeats").value),cn=Math.round(+$("#ccount").value);
  let c=null;
  if(!(cn>=0&&cn<=16))cn=click.countin;
  if(n>=1&&n<=10000){
    if(m==="start"&&s>=0&&b>=20&&b<=400)c={start:s,bpm:b,beats:n};
    else if(m==="end"&&b>=20&&b<=400&&e-(n-1)*60000/b>=0)c={start:e-(n-1)*60000/b,bpm:b,beats:n};
    else if(m==="span"&&n>=2&&s>=0&&e>s&&(n-1)*60000/(e-s)>=20&&(n-1)*60000/(e-s)<=400)c={start:s,bpm:(n-1)*60000/(e-s),beats:n};
  }
  if(c){click={...c,start:Math.round(c.start),bpm:+c.bpm.toFixed(4),mode:m,on:click.on,countin:cn};saveClick()}
  updateClickUi(); // an invalid entry puts the saved values back
}
// The click is scheduled on the engine's clock: for the stretch of song about to sound (the loop's passes included),
// every beat that falls in it is started at the moment that position plays.
const CLICK_LOOK=0.15;
audio.onanchor=tc=>{ // the sound was repositioned: forget the clicks scheduled after it, start over from here
  clickLast=tc;clickNodes=clickNodes.filter(n=>{if(n.when<=tc)return true;try{n.g.disconnect()}catch(e){}return false});
};
// Count-in: the N grid beats before the position playback starts from (the grid carries on backwards past its start,
// and past 0:00: the click then plays alone). The beat that falls on the start itself is the music's own.
audio.preroll=q=>{
  if(!click.on||!click.countin)return null;
  const gap=60/click.bpm,s0=click.start/1000,m=Math.ceil((q-s0)/gap-1e-9);
  return m>click.beats?null:s0+(m-click.countin)*gap; // not once the grid has ended
};
function tick(){
  if(!click.on||audio.paused)return;
  const c=audio.context(),now=c.currentTime,to=now+CLICK_LOOK,from=Math.max(clickLast,now);
  clickNodes=clickNodes.filter(n=>n.when>now-0.1);
  if(to<=from)return;
  clickLast=to;
  const gap=60/click.bpm,s0=click.start/1000;
  for(const sg of audio.segments(from,to)){
    for(let i=Math.max(sg.pre?-Infinity:0,Math.ceil((sg.p0-s0)/gap-1e-9));i<click.beats;i++){ // a count-in runs on the grid extended backwards
      const sp=s0+i*gap;if(sp>=sg.p1)break;
      const when=sg.t+(sp-sg.p0)/rate;
      const o=c.createOscillator(),g=c.createGain();o.frequency.value=1500;
      g.gain.setValueAtTime(0.0001,when);g.gain.exponentialRampToValueAtTime(0.5,when+0.002);g.gain.exponentialRampToValueAtTime(0.0001,when+0.06);
      o.connect(g).connect(c.destination);o.start(when);o.stop(when+0.07);clickNodes.push({when,g});
    }
  }
}
setInterval(tick,25);
$("#click").onclick=()=>{
  click.on=!click.on;
  if(click.on)audio.context().resume();
  updateClickUi();saveClick();
};
["#cmode","#cstart","#cend","#cbpm","#cbeats","#ccount"].forEach(k=>$(k).onchange=readClick);
$("#cstartnow").onclick=()=>{$("#cstart").value=Math.round(audio.currentTime*1000);readClick()};
$("#cendnow").onclick=()=>{$("#cend").value=Math.round(audio.currentTime*1000);readClick()};
function snapToLoop(){ // with the section on, playback starts inside it
  if(!loop.on||loop.a===null)return;
  const t=audio.currentTime;if(t<loop.a||t>=loop.b)audio.currentTime=loop.a;
}
audio.onplay=audio.onpause=audio.onended=()=>{
  const p=!audio.paused;
  document.body.classList.toggle("playing",p);
  $("#play").textContent=p?"❚❚":"▶";$("#play").setAttribute("aria-label",p?"Pause":"Play");
};
async function refreshLog(){
  try{
    const d=await (await fetch("/api/log")).json();
    const bar=$("#logbar"),pre=$("#log");
    bar.hidden=!d.id;
    // Leave room at the bottom of the page so the panel never covers the last card.
    document.body.style.paddingBottom=d.id?bar.offsetHeight+"px":"";
    if(!d.id)return;
    $("#logname").textContent="Log · "+d.name;
    const stick=pre.scrollTop+pre.clientHeight>=pre.scrollHeight-24;
    const text=d.lines.join("\n");
    if(pre.textContent!==text){pre.textContent=text;if(stick||refreshLog.id!==d.id)pre.scrollTop=pre.scrollHeight}
    refreshLog.id=d.id;
  }catch(e){}
}
// Drag the handle on the panel's top edge to resize the log; the height is remembered.
const logH=()=>$("#log").getBoundingClientRect().height;
function setLogH(px){
  px=Math.max(60,Math.min(px,innerHeight*0.8));
  $("#log").style.height=px+"px";
  document.body.style.paddingBottom=$("#logbar").offsetHeight+"px";
  return px;
}
try{const h=+localStorage.getItem("logH");if(h)setLogH(h)}catch(e){}
$("#loghandle").onpointerdown=e=>{
  const handle=e.currentTarget,y0=e.clientY,h0=logH();let h=h0;
  handle.setPointerCapture(e.pointerId);handle.classList.add("drag");e.preventDefault();
  handle.onpointermove=m=>{h=setLogH(h0+y0-m.clientY)};
  handle.onpointerup=handle.onpointercancel=()=>{
    handle.onpointermove=handle.onpointerup=handle.onpointercancel=null;handle.classList.remove("drag");
    try{localStorage.setItem("logH",Math.round(h))}catch(e){}
  };
};
$("#logtoggle").onclick=()=>{
  const bar=$("#logbar");bar.classList.toggle("min");
  $("#logtoggle").textContent=bar.classList.contains("min")?"Show log":"Hide log";
  document.body.style.paddingBottom=bar.offsetHeight+"px";
};
async function upload(files){
  for(const f of files){
    const fd=new FormData();fd.append("file",f);
    $("#msg").textContent=`Uploading ${f.name}…`;
    const r=await fetch("/api/upload",{method:"POST",body:fd});
    if(!r.ok){const j=await r.json().catch(()=>({}));$("#msg").textContent=`${f.name}: ${j.detail||r.status}`;return}
  }
  $("#msg").textContent="";refresh();
}
const drop=$("#drop");
drop.onclick=()=>$("#file").click();
$("#file").onchange=e=>{upload([...e.target.files]);e.target.value=""};
drop.ondragover=e=>{e.preventDefault();drop.classList.add("over")};
drop.ondragleave=()=>drop.classList.remove("over");
drop.ondrop=e=>{e.preventDefault();drop.classList.remove("over");upload([...e.dataTransfer.files])};
async function del(id){
  if(!confirm("Delete this track and its files?"))return;
  await fetch("/api/tracks/"+id,{method:"DELETE"});refresh.sig=null;refresh();
}
$("#list").onclick=async e=>{
  const id=e.target.dataset.del,cid=e.target.dataset.cancel;
  if(id)return del(id);
  if(cid){if(confirm("Cancel processing this track?")){await fetch("/api/tracks/"+cid+"/cancel",{method:"POST"});refresh.sig=null;refresh()}return}
  const bad=e.target.closest(".bad");
  if(bad){$("#msg").textContent=bad.querySelector(".tname").textContent+": "+(bad.dataset.err||"failed");return}
  const row=e.target.closest(".pick");
  if(row&&row.dataset.id!==cur){select(row.dataset.id);refresh.sig=null;refresh()}
};
$("#pdel").onclick=()=>del(cur);
$("#pren").onclick=async()=>{
  const t=tracks.find(t=>t.id===cur);if(!t)return;
  const n=prompt("Rename track",t.name);
  if(!n||!n.trim()||n.trim()===t.name)return;
  const r=await fetch("/api/tracks/"+cur+"/rename",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:n.trim()})});
  if(!r.ok){const j=await r.json().catch(()=>({}));$("#msg").textContent="Rename: "+(j.detail||r.status)}
  refresh.sig=null;refresh();
};
$("#stems").onclick=e=>{const k=e.target.dataset.stem;if(k&&k!==stem){stem=k;showStem(true)}};
$("#rates").onclick=e=>{const r=e.target.dataset.rate;if(r)setRate(r/100)};
$("#play").onclick=()=>audio.paused?audio.play():audio.pause();
$("#stop").onclick=()=>{audio.pause();audio.currentTime=0};
$("#back").onclick=()=>{audio.currentTime=Math.max(0,audio.currentTime-10)};
$("#fwd").onclick=()=>{audio.currentTime=Math.min(audio.duration||1e9,audio.currentTime+10)};
const pts=new Map();let g=null;
const pos=e=>{const r=wave.getBoundingClientRect();return{x:e.clientX-r.left,y:e.clientY-r.top,W:r.width}};
const timeAtX=x=>{const v=vw();return Math.max(0,Math.min(v.d,v.s+x/wave.getBoundingClientRect().width*v.l))};
wave.onpointerdown=e=>{
  if(!dur())return;
  wave.setPointerCapture(e.pointerId);const p=pos(e);pts.set(e.pointerId,p);dragging=true;e.preventDefault();
  if(pts.size===1)g={x0:p.x,y0:p.y,moved:false,mode:null,pinched:false,off:0,lastX:p.x};
  else{g.pinched=true;g.mode="pinch";const[a,b]=[...pts.values()];g.dist=Math.hypot(a.x-b.x,a.y-b.y);g.cx=(a.x+b.x)/2}
};
wave.onpointermove=e=>{
  if(!pts.has(e.pointerId)||!g)return;
  const p=pos(e);pts.set(e.pointerId,p);const v=vw();
  if(pts.size>=2){ // two fingers: zoom around the middle between them, and follow it when it moves
    const[a,b]=[...pts.values()],dist=Math.max(1,Math.hypot(a.x-b.x,a.y-b.y)),cx=(a.x+b.x)/2;
    const nl=Math.min(v.d,Math.max(Math.min(MIN_VIEW,v.d),v.l*g.dist/dist));
    setView(v.s+g.cx/p.W*v.l-cx/p.W*nl,nl>=v.d?null:nl);g.dist=dist;g.cx=cx;return;
  }
  if(g.pinched)return; // one finger left over from a pinch does nothing
  if(!g.moved){
    if(Math.abs(p.x-g.x0)<6&&Math.abs(p.y-g.y0)<6)return;
    g.moved=true;
    const on=loop.on&&loop.a!==null,xa=on?(loop.a-v.s)/v.l*p.W:0,xb=on?(loop.b-v.s)/v.l*p.W:0;
    const da=Math.abs(g.x0-xa),db=Math.abs(g.x0-xb),h=da<=db?"a":"b",dh=Math.min(da,db);
    if(on&&dh<=28){g.mode=h;g.off=(h==="a"?xa:xb)-g.x0} // landed on a handle: it moves, and does not jump to the finger
    else g.mode=v.l<v.d-1e-6?"pan":"seek";
  }
  if(g.mode==="a"||g.mode==="b"){
    const t=Math.max(0,Math.min(v.d,v.s+(p.x+g.off)/p.W*v.l));
    if(g.mode==="a")loop.a=Math.min(t,loop.b-MIN_LOOP);else loop.b=Math.max(t,loop.a+MIN_LOOP);
    dirty=true;updateLoopUi();audio.applyLoop();
  }else if(g.mode==="pan"){setView(v.s-(p.x-g.lastX)/p.W*v.l,view.l);g.lastX=p.x}
  else if(g.mode==="seek")audio.currentTime=timeAtX(p.x);
};
wave.onpointerup=wave.onpointercancel=e=>{
  if(!pts.delete(e.pointerId))return;
  if(pts.size>0)return;
  if(g&&e.type==="pointerup"&&!g.moved&&!g.pinched)audio.currentTime=timeAtX(pos(e).x); // a tap seeks
  if(g&&(g.mode==="a"||g.mode==="b"))saveLoop();
  g=null;dragging=false;dirty=true;
};
wave.addEventListener("wheel",e=>{
  if(!dur())return;e.preventDefault();const p=pos(e),v=vw();
  if(e.shiftKey||Math.abs(e.deltaX)>Math.abs(e.deltaY)){if(v.l<v.d-1e-6)setView(v.s+(e.deltaX||e.deltaY)/p.W*v.l,view.l)}
  else zoomBy(Math.exp(-e.deltaY*(e.ctrlKey?0.01:0.0015)),p.x/p.W);
},{passive:false});
// The overview strip (shown when zoomed in): tap or drag to move the window.
let ovDrag=false;
const ovGo=e=>{const r=ovw.getBoundingClientRect(),v=vw();setView((e.clientX-r.left)/r.width*v.d-v.l/2,view.l)};
ovw.onpointerdown=e=>{ovw.setPointerCapture(e.pointerId);ovDrag=true;ovGo(e)};
ovw.onpointermove=e=>{if(ovDrag)ovGo(e)};
ovw.onpointerup=ovw.onpointercancel=()=>{ovDrag=false};
const zoomButton=f=>{const v=vw(),t=audio.currentTime;zoomBy(f,t>=v.s&&t<=v.s+v.l?(t-v.s)/v.l:0.5)};
$("#zin").onclick=()=>zoomButton(2);
$("#zout").onclick=()=>zoomButton(0.5);
$("#zfit").onclick=()=>setView(0,null);
$("#zloop").onclick=()=>{if(loop.a===null)return;const pad=(loop.b-loop.a)*0.15;setView(loop.a-pad,loop.b-loop.a+2*pad)};
$("#loopsec").onclick=()=>{
  const d=audio.duration;if(!cur||!isFinite(d))return;
  if(loop.on)loop.on=false;
  else{
    if(loop.a===null){ // first use: a section starting at the playhead, 10% of the song long
      const span=Math.min(d,Math.max(4,d*0.1));loop.a=Math.max(0,Math.min(audio.currentTime,d-span));loop.b=loop.a+span;
    }
    loop.on=true;snapToLoop();
  }
  updateLoopUi();dirty=true;saveLoop();audio.applyLoop();
};
$("#repeat").onclick=()=>{
  repeat=!repeat;updateLoopUi();audio.applyLoop();
  try{localStorage.setItem("repeat",repeat?"1":"0")}catch(e){}
};
$("#plinks").onclick=()=>{$("#dl").open=false};
document.addEventListener("keydown",e=>{
  if(e.code==="Space"&&cur&&!["INPUT","BUTTON","SUMMARY","TEXTAREA"].includes(e.target.tagName)){e.preventDefault();$("#play").click()}
});
setRate(rate);updateLoopUi();updateClickUi();
refresh();refreshLog();setInterval(refresh,3000);setInterval(refreshLog,2000);
</script></body></html>
"""
