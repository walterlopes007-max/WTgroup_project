// ===== Transição de página (fade) =====
document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('page-enter');
  requestAnimationFrame(() => document.body.classList.add('page-enter-active'));

  // Fade-in dos elementos .fade-in
  const els = document.querySelectorAll('.fade-in');
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      }
    })
  }, {threshold:.18});
  els.forEach(el=>io.observe(el));

  // Marcar item ativo na navbar conforme URL
  const path = window.location.pathname.replace(/\/+$/,'/');
  document.querySelectorAll('.navbar-nav .nav-link').forEach(a=>{
    if(a.getAttribute('href') === path){ a.classList.add('active') }
  });
});
