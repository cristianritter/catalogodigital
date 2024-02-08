// Seleciona o ícone de GPS clicável
const gpsIcon = document.getElementById('gpsIcon');

// Adiciona um evento de clique ao ícone de GPS
gpsIcon.addEventListener('click', function() {
    // Verifica se o navegador suporta a API de geolocalização
    if (navigator.geolocation) {
        // Obtém a localização do usuário
        navigator.geolocation.getCurrentPosition(function(position) {
            // Obtém as coordenadas de latitude e longitude
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            // Chama a função para converter as coordenadas em nome da cidade
            getCityName(latitude, longitude);
        });
    } else {
        // Caso o navegador não suporte a geolocalização
        alert('Seu navegador não suporta geolocalização.');
    }
});

// Função para obter o nome da cidade com base nas coordenadas de latitude e longitude
function getCityName(latitude, longitude) {
    // Cria uma nova instância do objeto XMLHttpRequest
    const xhr = new XMLHttpRequest();

    // Define a URL da API de geocodificação reversa
    const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`;

    // Configura a solicitação
    xhr.open('GET', url, true);

    // Define a função de retorno de chamada quando a solicitação for concluída
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            // Analisa a resposta JSON
            const response = JSON.parse(xhr.responseText);

            // Obtém o nome da cidade a partir da resposta
            const city = response.address.city;

            // Preenche o campo de entrada da cidade com o nome da cidade
            document.getElementById('cityInput').value = city;
        } else {
            // Se houver um erro na solicitação
            console.error('Erro ao obter os dados da cidade.');
        }
    };

    // Define a função de retorno de chamada para tratamento de erros
    xhr.onerror = function() {
        console.error('Erro de conexão.');
    };

    // Envia a solicitação
    xhr.send();
}
