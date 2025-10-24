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

/* ========== مدیریت منوی موبایل (جدید) ========== */
(function() {
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.getElementById('mobileNav');

  if (!navToggle || !navMenu) return;

  // ۱. باز و بسته کردن منوی اصلی (همبرگر)
  navToggle.addEventListener('click', function() {
    // کلاس .is-open را به منو اضافه/حذف می‌کند
    const isOpen = navMenu.classList.toggle('is-open');
    // ویژگی aria-expanded را برای دسترسی‌پذیری آپدیت می‌کند
    navToggle.setAttribute('aria-expanded', isOpen);
  });

  // ۲. مدیریت زیرمنوها در موبایل (با کلیک)
  const dropdownLinks = navMenu.querySelectorAll('.nav__item--dropdown > a');

  dropdownLinks.forEach(link => {
    link.addEventListener('click', function(event) {

      // فقط در حالت موبایل (زیر 992px) با کلیک کار کند
      if (window.innerWidth <= 992) {
        event.preventDefault();

        const dropdownContent = this.nextElementSibling; // .nav__dropdown
        const parentItem = this.parentElement; // .nav__item--dropdown

        // باز/بسته کردن زیرمنوی فعلی
        const isSubmenuOpen = parentItem.classList.toggle('is-open');
        dropdownContent.classList.toggle('is-open');

        // بستن بقیه زیرمنوهای باز
        if (isSubmenuOpen) {
            navMenu.querySelectorAll('.nav__item--dropdown.is-open').forEach(openItem => {
                if (openItem !== parentItem) {
                    openItem.classList.remove('is-open');
                    openItem.querySelector('.nav__dropdown').classList.remove('is-open');
                }
            });
        }
      }
    });
  });

})();