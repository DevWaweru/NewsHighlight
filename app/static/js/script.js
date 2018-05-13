$(document).ready(function () {
    // This facilitates smooth scrolling using jQuery easing
    $('a.smooth-scroll[href*="#"]:not([href="#"])').click(function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: (target.offset().top - 48)
                }, 1000, "easeInOutExpo");
                return false;
            }
        }
    });
    // Closes responsive menu when a smooth scroll class is triggered
    // this is for small screens with small pixel widths
    $('.smooth-scroll').click(function () {
        $('.navbar-collapse').collapse('hide');
    });
    //Scroll to the top
    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#navMain',
        offset: 54
    });

    // Collapse Navbar when the scroll is triggered
    var navbarCollapse = function () {
        if ($("#navMain").offset().top > 100) {
            $("#navMain").addClass("navbar-shrink");
        } else {
            $("#navMain").removeClass("navbar-shrink");
        }
    };
    // Collapse the nav bar if page is not at the top
    navbarCollapse();
    // Collapse the navbar when there is scroll activity
    $(window).scroll(navbarCollapse);
});