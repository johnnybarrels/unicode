$(window).ready( function () {
    let sideNavWidth = $('.sidenav').css('width');
    $('.content-container').css('margin-left', sideNavWidth);

    $(window).on('resize', function() {
        let sideNavWidth = $('.sidenav').css('width');
        $('.content-container').css('margin-left', sideNavWidth);
    });
}
);
