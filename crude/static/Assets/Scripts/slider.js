let slides=document.querySelectorAll(".slide");
let currentSlide=0;
function changesSlide(){
    slides[currentSlide].classList.remove("active");
    currentSlide=(currentSlide+1)%slides.length;
    slides[currentSlide].classList.add("active");
}
setInterval(changesSlide, 3000);