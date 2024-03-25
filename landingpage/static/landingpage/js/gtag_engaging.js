    document.getElementById('chamar-no-whatsapp-button').addEventListener('click', function() 
    {
        // Envia um evento personalizado para o Google Analytics quando o botão é clicado
        gtag('event', 'clique_em_chamar_no_whats', {
            'event_category': 'clique_em_chamar_no_whats',
            'event_label': 'clique_em_chamar_no_whats Clicado'
        });
    });