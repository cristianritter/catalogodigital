window.onload = function() {
    var highQualityImageUrl = document.getElementById("background-image").getAttribute("highQualityImageUrl");   
    var lazyImages = document.querySelectorAll("img.lazy-load");
    var img = new Image();
    img.onload = function() {
        document.querySelector('#masthead .background-image').style.backgroundImage = 'url(' + highQualityImageUrl + ')';
    };
    img.src = highQualityImageUrl; 
    lazyImages.forEach(function(lazyImage) {
        lazyImage.src = lazyImage.dataset.src;
        lazyImage.classList.remove("lazy-load");
    });  
};