const vm=require('vm'),fs=require('fs');
const src=fs.readFileSync(process.argv[2],'utf8');
const P=new Proxy(function(){},{get:(t,k)=>k===Symbol.toPrimitive?()=>'' :(k==='length'?0:P),apply:()=>P,construct:()=>P,set:()=>true,has:()=>true});
const store={};
const ctx={console:{log(){},warn(){},error(){}},document:P,window:P,navigator:P,location:{hash:'',search:'',href:''},localStorage:{getItem:()=>null,setItem(){},removeItem(){}},addEventListener(){},setTimeout(){},setInterval(){},clearTimeout(){},clearInterval(){},requestAnimationFrame(){},fetch:()=>new Promise(()=>{}),matchMedia:()=>({matches:false,addEventListener(){}}),history:P,Notification:P,performance:{now:()=>0},screen:P,innerWidth:400,innerHeight:800};
ctx.self=ctx;ctx.globalThis=ctx;
vm.createContext(ctx);
const names=['EX','TIPS','GUIDE','GUIDE_SLUG','WORKOUTS','WARMUP','SEQ','SEQ_TITLE','MOB_AREAS','MOB_FEEL','MOB_POS','BODY_ZONES','LOAD_MAP','YOGA_POOL','YOGA_STYLE','YOGA_INT','EQK','CATS','EX_META','PH','OWN_ANIM','DAYS','SUPPS','MEALS','QUICK','BR_GOAL','BR_EV','BR_KIND','BR','BR_USE','PSY_KAT','PSY_USE','PSY_EV','PSY','PSY_HELP','SK_CAT','SK_LOAD','SKILLS','CK_AREAS','CK_LIGHT','CK_Q','TPL_CLS','EXAMPLES','GLOW_EX','REGEN_DAY','DEFAULT_SETTINGS'];
const code=src+require('fs').readFileSync(__dirname+'/extra.js','utf8')+'\n;try{globalThis.__OUT={'+names.map(n=>`${n}:(typeof ${n}!=='undefined'?${n}:null)`).join(',')+'}}catch(e){globalThis.__ERR=String(e)}';
try{vm.runInContext(code,ctx)}catch(e){console.error('RUNERR',e.message)}
if(!ctx.__OUT){console.error('no out',ctx.__ERR);process.exit(1)}
ctx.__OUT.EXTRA=ctx.__EXTRA||ctx.__ERR2;fs.writeFileSync(process.argv[3],JSON.stringify(ctx.__OUT,(k,v)=>typeof v==='function'?'[fn]':v,1));
for(const n of names){const v=ctx.__OUT[n];console.log(n,v==null?'NULL':Array.isArray(v)?'arr '+v.length:typeof v==='object'?'obj '+Object.keys(v).length:typeof v)}
