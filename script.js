document.addEventListener("click", function () {
  const carousel = document.querySelector(".carousel");
  const prevButton = carousel.querySelector(".prev");
  const nextButton = carousel.querySelector(".next");
  const inner = carousel.querySelector(".carousel-inner");
  const items = carousel.querySelectorAll(".testimonial");
  const itemWidth = items[0].offsetWidth;

  let currentIndex = 0;

  prevButton.addEventListener("click", function () {
    if (currentIndex > 0) {
      currentIndex--;
      inner.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
    }
  });

  nextButton.addEventListener("click", function () {
    if (currentIndex < items.length - 1) {
      currentIndex++;
      inner.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
    }
  });
});
