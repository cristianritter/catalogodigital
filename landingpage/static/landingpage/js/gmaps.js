function carregarMapa() {
    var gmapsLink = document.getElementById("google-map-container").getAttribute("data-gmaps-link");
    var iframe = document.createElement("iframe");
    iframe.setAttribute("src", gmapsLink);
    iframe.setAttribute("width", "100%");
    iframe.setAttribute("height", "200");
    document.getElementById("google-map-container").appendChild(iframe);
    document.getElementById("map-button").style.display = "none";
    document.getElementById("directions-button").style.display = "inline-block"; // Exibir o botão Obter Direções
}
