const slides = document.querySelectorAll('.slide');
const prev = document.querySelector('.nav.prev');
const next = document.querySelector('.nav.next');
let current = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle('active', i === index);
  });
}

prev.addEventListener('click', () => {
  current = (current - 1 + slides.length) % slides.length;
  showSlide(current);
});

next.addEventListener('click', () => {
  current = (current + 1) % slides.length;
  showSlide(current);
});

showSlide(current);
