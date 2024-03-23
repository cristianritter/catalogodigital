document.addEventListener("DOMContentLoaded", function() {
    const prevButton = document.querySelector(".carousel-prev");
    const nextButton = document.querySelector(".carousel-next");
    const slide = document.querySelector(".carousel-slide");
  
    let counter = 0;
    const slideCount = document.querySelectorAll(".carousel-slide img").length;
  
    nextButton.addEventListener("click", function() {
      if (counter < slideCount - 1) {
        counter++;
      } else {
        counter = 0;
      }
      slide.style.transform = `translateX(-${counter * 100}%)`;
    });
  
    prevButton.addEventListener("click", function() {
      if (counter > 0) {
        counter--;
      } else {
        counter = slideCount - 1;
      }
      slide.style.transform = `translateX(-${counter * 100}%)`;
    });
  });
  
  document.addEventListener("DOMContentLoaded", function() {
    const slide = document.querySelector(".carousel-slide");
    const images = document.querySelectorAll(".carousel-slide img");
    const container = document.querySelector(".carousel-container");
  
    let counter = 0;
    const slideCount = images.length;
    const intervalTime = 3000; // Tempo em milissegundos entre cada troca de imagem
  
    function nextSlide() {
      if (counter < slideCount - 1) {
        counter++;
      } else {
        counter = 0;
      }
      slide.style.transform = `translateX(-${counter * 100}%)`;
    }
  
    // Função para avançar para o próximo slide automaticamente
    function startSlide() {
      setInterval(() => {
        nextSlide();
      }, intervalTime);
    }
  
    // Inicia a troca automática de slides quando a página carrega
    startSlide();
  });
  