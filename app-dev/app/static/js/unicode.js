$(window).on('load', function () {
    let sideNavWidth = $('.sidenav').css('width');
    $('.content-container').css('margin-left', sideNavWidth);

    // Doesn't work on resize
}
)
