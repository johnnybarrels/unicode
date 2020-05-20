$(window).ready(function () {
    let sideNavWidth = $('.sidenav').css('width');
    $('.content-container').css('margin-left', sideNavWidth);

    $(window).on('resize', function () {
        let sideNavWidth = $('.sidenav').css('width');
        $('.content-container').css('margin-left', sideNavWidth);
    });

    $(".fa-caret-square-down").click(function () {
        $("#option-menu").toggle();
    });
    // $(".fa-times").click(function () {
    //     document.getElementById("option-menu").style.visibility = "hidden";
    // });


    $("#new-course-btn").click(function () {
        $("#new-course-modal").modal("show");
    });

    $("#new-test-btn").click(function () {
        $("#new-test-modal").modal("show");
    });

    $(".dropdown-toggle").dropdown();

}
);
