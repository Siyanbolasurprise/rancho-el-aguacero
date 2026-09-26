(()=>{const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
// header
const h=$('header.site');const onS=()=>h&&h.classList.toggle('scrolled',scrollY>40);addEventListener('scroll',onS,{passive:true});onS();
const b=$('.burger'),l=$('.links');b&&b.addEventListener('click',()=>{const o=l.classList.toggle('open');b.textContent=o?'✕':'☰';b.setAttribute('aria-expanded',o)});
// reveal
const io=new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting&&(e.target.classList.add('in'),io.unobserve(e.target))),{threshold:.12});
$$('.rv').forEach(el=>io.observe(el));
// lightbox
const lb=$('#lightbox');$$('[data-zoom]').forEach(img=>img.addEventListener('click',()=>{if(!lb)return;const full=lb.querySelector('img');full.src=img.dataset.full||img.src;full.alt=img.alt;lb.classList.add('open')}));
lb&&lb.addEventListener('click',()=>lb.classList.remove('open'));addEventListener('keydown',e=>e.key==='Escape'&&lb&&lb.classList.remove('open'));
// UTM preserve
const utm={};new URLSearchParams(location.search).forEach((v,k)=>{if(k.startsWith('utm_'))utm[k]=v});
$$('a[href*="wa.me"]').forEach(a=>{try{const u=new URL(a.href);Object.entries(utm).forEach(([k,v])=>u.searchParams.set(k,v));const src=u.searchParams.get('text')||'';if(src)a.href=u.toString()}catch{}});
// analytics stub
window.raTrack=(ev,data={})=>{window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:ev,...data,utm});};
// track key clicks
$$('[data-track]').forEach(el=>el.addEventListener('click',()=>window.raTrack(el.dataset.track,{page:location.pathname})));
// newsletter + generic lead forms
$$('form[data-lead]').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();let ok=true;
$$('[required]',f).forEach(i=>{const bad=!i.value.trim()||(i.type==='email'&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(i.value));i.setAttribute('aria-invalid',bad);const er=i.closest('.field')?.querySelector('.err');if(er)er.style.display=bad?'block':'none';if(bad)ok=false});
if(!ok)return;window.raTrack('lead_submit',{form:f.dataset.lead});
const done=f.parentElement.querySelector('.form-done')||document.createElement('p');
done.className='form-done notice';done.textContent=f.dataset.done||'Thank you. We will be in touch.';
f.replaceWith(done);}));
// FAQ filter
const q=$('#faqSearch');q&&q.addEventListener('input',()=>{const v=q.value.toLowerCase();$$('#faqList details').forEach(d=>{d.style.display=d.textContent.toLowerCase().includes(v)?'':'none'})});
// gallery filter
$$('[data-filter]').forEach(btn=>btn.addEventListener('click',()=>{$$('[data-filter]').forEach(x=>x.classList.remove('clay'));btn.classList.add('clay');
const v=btn.dataset.filter;$$('#galleryGrid figure').forEach(f=>{f.style.display=(v==='all'||f.dataset.cat===v)?'':'none'});}));
// ---- booking widget ----
const bw=$('#booking');if(bw){const lang=bw.dataset.lang||'en';
const T=lang==='es'?{need:'Elige alojamiento y fechas para ver el total.',dep:'Anticipo',total:'Total estimado',confirm:'Confirmar solicitud de reserva',ok:'¡Solicitud recibida! Te contactaremos por email y WhatsApp para confirmar y procesar el anticipo de forma segura.',ref:'Referencia'}:{need:'Choose lodging and dates to see your total.',dep:'Deposit',total:'Estimated total',confirm:'Request to book',ok:'Request received! We will contact you by email and WhatsApp to confirm and securely process the deposit.',ref:'Reference'};
const acc=$('#bAcc'),ci=$('#bIn'),co=$('#bOut'),g=$('#bGuests'),sum=$('#bSum');
const rates={house:14500,cabin:2800,camp:350};const fmt=n=>'$'+n.toLocaleString(lang==='es'?'es-MX':'en-US')+' MXN';
function calc(){const a=acc.value;let nights=0;if(ci.value&&co.value){nights=Math.round((new Date(co.value)-new Date(ci.value))/86400000);}if(!a||!(nights>0)){sum.innerHTML=`<p class="lede" style="font-size:16px">${T.need}</p>`;return null}
const per=rates[a]||0;const tot=per*nights;const dep=Math.round(tot*.3);
sum.innerHTML=`<p class="meta">${nights} night(s) × ${fmt(per)}</p><p class="price">${T.total}: ${fmt(tot)}</p><p>${T.dep} (30%): <b>${fmt(dep)}</b></p><p class="j-meta">Secure your reservation · remaining balance before check-in</p>`;return{tot,dep,nights}}
acc.addEventListener('change',calc);ci.addEventListener('change',calc);co.addEventListener('change',calc);
bw.addEventListener('submit',e=>{e.preventDefault();const r=calc();const req=$$('[required]',bw);let ok=true;
req.forEach(i=>{const bad=!i.value.trim();i.style.borderColor=bad?'#9c3d2e':'';if(bad)ok=false});if(!ok||!r){calc();return}
const ref='REA-'+Date.now().toString(36).toUpperCase();window.raTrack('booking_completed',{ref,total:r.tot});
$('#bookForm').style.display='none';const d=$('#bookDone');d.style.display='block';
d.querySelector('.ref').textContent=T.ref+': '+ref;});
}
})();
