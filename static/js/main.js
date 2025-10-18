// اسلایدر افقی بسیار ساده
(function(){
  const track = document.getElementById('sliderTrack');
  if(!track) return;

  const prev = document.querySelector('.slider__btn--prev');
  const next = document.querySelector('.slider__btn--next');

  const step = () => track.clientWidth * 0.8;

  prev?.addEventListener('click', () => track.scrollBy({left: -step(), behavior: 'smooth'}));
  next?.addEventListener('click', () => track.scrollBy({left:  step(), behavior: 'smooth'}));

  // اسکرول خودکار
  let auto = setInterval(()=> track.scrollBy({left: step(), behavior:'smooth'}), 4000);
  track.addEventListener('mouseenter', ()=> clearInterval(auto));
  track.addEventListener('mouseleave', ()=> auto = setInterval(()=> track.scrollBy({left: step(), behavior:'smooth'}), 4000));
})();
