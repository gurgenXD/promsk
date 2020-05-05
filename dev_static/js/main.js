(function($) {
    function FooterBottom() { 
        $('body').css('margin-bottom', $('.footer').outerHeight())
    };

    FooterBottom();
    window.addEventListener('resize', FooterBottom, false);  
})(jQuery);


(function($) {
    function FooterBottom1() { 
        $('.offcanvas-collapse').css('top', ($('.navbar').offset().top + $('.navbar').outerHeight(true) - $(window).scrollTop()));
    };

    FooterBottom1();
    window.addEventListener('scroll', FooterBottom1, false);  
})(jQuery);

$(document).ready(function(){
    $('.dropdown').on('show.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown("fast");
    });

    $('.dropdown').on('hide.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp("fast");
    });
});

$(document).ready(function(){
    $(function () {
        'use strict'
        $('[data-toggle="offcanvas"]').on('click', function () {
            $('.offcanvas-collapse').toggleClass('open');
            $('.navbar-toggler-icon').toggleClass('open');
        })
    })
});

$(document).ready(function(){
    function handleFirstTab(e) {
        if (e.keyCode === 9) {
            document.body.classList.add('user-is-tabbing');

            window.removeEventListener('keydown', handleFirstTab);
            window.addEventListener('mousedown', handleMouseDownOnce);
        }
    }

    function handleMouseDownOnce() {
        document.body.classList.remove('user-is-tabbing');

        window.removeEventListener('mousedown', handleMouseDownOnce);
        window.addEventListener('keydown', handleFirstTab);
    }

    window.addEventListener('keydown', handleFirstTab);
});

$(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 750) {
            $('.scroll-to-top').fadeIn(200);
        } 
        else {
            $('.scroll-to-top').fadeOut(200);
        }
    });
    $('.scroll-to-top').click(function(){
        $('html, body').animate({scrollTop : 0},300);
        return false;
    });
});

$(document).ready(function(){
    var $grid = $('.img-grid').masonry({
        itemSelector: 'figure',
        percentPosition: true
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress( function() {
        $grid.masonry();
    });  
});

(function() {
    'use strict';
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

function numberWithCommas(number) {
    var parts = number.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return parts.join(".");
}
$(document).ready(function() {
    $(".number").each(function() {
        var num = $(this).text();
        var commaNum = numberWithCommas(num);
        $(this).text(commaNum);
    });
});

(function($) {
    function NavbarScroll() {
        var scroll = $(window).scrollTop(),
            topbar = $('.top-bar').outerHeight();

        if(scroll > topbar){
            $('.navbar').addClass('fixed-top');
            $('.top-bar').css('margin-bottom','63px');
            $('.offcanvas-collapse').addClass('now-scrolling');
        } 
        else {
            $('.navbar').removeClass('fixed-top');
            $('.top-bar').css('margin-bottom','0');
            $('.offcanvas-collapse').removeClass('now-scrolling');
        }
    };

    NavbarScroll();
    window.addEventListener('scroll', NavbarScroll, false);  
})(jQuery);

$(document).ready(function(){
    if ($(".jumbotron").length) {
        $(".top-bar").removeClass("bg-dark");
        $(".navbar").removeClass("bg-dark");
    }
});

(function($) {
    function MtchHeight() { 
        if(window.matchMedia('(min-width: 576px)').matches){
            $(function() {
                $('.product-card .card-body a').matchHeight({
                    byRow: false
                });

                $('.news-item-big a').matchHeight({
                    byRow: false
                });
            });
        }

        else {
            $('.product-card .card-body a').matchHeight({
                byRow: true
            });

            $('.news-item-big a').matchHeight({
                byRow: true
            });
        };
    };

    MtchHeight();
    window.addEventListener('resize', MtchHeight, false);  
})(jQuery);

jQuery(function($){
    $(".phone-input").mask("+7 (999) 999-99-99",{placeholder:"_"});
});