// Shared runtime for design canvases.
// 1) renders preview lookalikes for live CTA blocks
// 2) when URL hash is #dump, writes slice geometry JSON into <pre id="__out"> for build.py
(function(){
  function btnHTML(d){
    return '<a style="display:inline-block;padding:18px 40px;border-radius:999px;background:'+(d.btnbg||'#BD2629')+';color:'+(d.btncolor||'#fff')+
      ';font:700 17px/20px DM Sans,Arial,sans-serif;text-decoration:none;letter-spacing:.2px">'+d.label+' &nbsp;&rarr;</a>';
  }
  document.querySelectorAll('.live[data-kind=button]').forEach(function(el){
    el.style.background=el.dataset.bg; el.style.textAlign='center';
    el.style.padding=(el.dataset.pad||'8px 0 40px');
    el.innerHTML=btnHTML(el.dataset)+(el.dataset.note?'<p style="margin:14px 0 0;font:500 13px/18px DM Sans,Arial,sans-serif;color:'+(el.dataset.notecolor||'#8A857E')+'">'+el.dataset.note+'</p>':'');
  });
  function lines(){
    var root=document.getElementById('email'); var R=root.getBoundingClientRect();
    document.querySelectorAll('.deco-line').forEach(function(l){
      var a=document.getElementById(l.dataset.from).getBoundingClientRect(), b=document.getElementById(l.dataset.to).getBoundingClientRect();
      var top=a.top+a.height/2-R.top, bot=b.top+b.height/2-R.top;
      l.style.top=(top-(+l.dataset.pre||0))+'px'; l.style.height=(bot-top+(+l.dataset.pre||0)+(+l.dataset.post||0))+'px';
      l.style.left=(a.left+a.width/2-R.left-1)+'px';
    });
  }
  lines(); if(document.fonts) document.fonts.ready.then(lines); window.addEventListener('load',lines);
  function dump(){
    var out=[]; var root=document.getElementById('email');
    Array.prototype.forEach.call(root.children,function(el){
      if(el.classList.contains('deco')) return;
      var r=el.getBoundingClientRect();
      if(el.classList.contains('live')){
        out.push({type:'live',kind:el.dataset.kind,bg:el.dataset.bg,label:el.dataset.label||'',href:el.dataset.href||'',
          note:el.dataset.note||'',notecolor:el.dataset.notecolor||'',pad:el.dataset.pad||'8px 0 40px',btnbg:el.dataset.btnbg||'',btncolor:el.dataset.btncolor||'',
          html:el.dataset.kind==='text'?el.innerHTML:'', y:r.top+scrollY,h:r.height});
      } else {
        out.push({type:'img',name:el.dataset.name||'slice',alt:el.dataset.alt||'',href:el.dataset.href||'',y:r.top+scrollY,h:r.height,bg:el.dataset.bg||''});
      }
    });
    var pre=document.createElement('pre'); pre.id='__out'; pre.textContent=JSON.stringify({total:root.getBoundingClientRect().height,items:out});
    document.body.appendChild(pre);
  }
  if(location.hash==='#dump'){ (document.fonts?document.fonts.ready:Promise.resolve()).then(function(){ setTimeout(dump,300); }); }
})();
