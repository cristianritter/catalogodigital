window.addEventListener('DOMContentLoaded', event => {

    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    var carregarMapa = function () {
        var iframe = document.createElement("iframe");
        iframe.setAttribute("src", "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3468.0310528904797!2d-51.01371158831997!3d-29.631841339516633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95193fbe62929801%3A0xfb885bf48d7148d6!2sAJR%20Cutelaria!5e0!3m2!1sen!2sbr!4v1703100728491!5m2!1sen!2sbr");
        iframe.setAttribute("title", "mapa google maps");
        document.getElementById("google-map-container").appendChild(iframe);
    }

    navbarShrink();
    carregarMapa()
                  
    document.addEventListener('scroll', navbarShrink);

    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

