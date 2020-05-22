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

    $("#new-course-icon").click(function () {
        $("#new-course-modal").modal("show");
    });

    $("#new-test-btn").click(function () {
        $("#new-test-modal").modal("show");
    });

    $("#manage-students-btn").click(function () {
        $("#manage-students-modal").modal("show");
    });

    $(".dropdown-toggle").dropdown();

    $('#mcq-option-1').click(function () {
        $("#new-question-mcq")
    });

    // ACE Code Editor
    var editor;
    $('.editor').each(function (index) {
        editor = ace.edit(this);
        editor.setTheme("ace/theme/tomorrow_night_eighties");
        editor.session.setMode("ace/mode/python");
    });
});

function newQuestionSelector(qType) {
    if (qType == 1) {
        $('#new-question-mcq').hide();
        $('#new-question-solution').show();
        $('#question-type').attr('value', 1)
    }
    else if (qType == 2) {
        $('#new-question-mcq').show();
        $('#new-question-solution').show();
        $('#question-type').attr('value', 2)
    }
    else if (qType == 3) {
        $('#new-question-mcq').hide();
        $('#new-question-solution').hide();
        $('#question-type').attr('value', 3)
    }
};

// $('nav-add-tab').click(function () {
//     if ($('#mcq-option-1').hasClass('active')) {
//         console.log('Hello')
//         $('#new-question-mcq').hide()
//         $('#new-question-solution').show()
//     };

//     if ($('#mcq-option-2').hasClass('active')) {
//         $('#new-question-mcq').show()
//         $('#new-question-solution').show()
//     };

//     if ($('#mcq-option-3').hasClass('active')) {
//         $('#new-question-mcq').hide()
//         $('#new-question-solution').hide()
//     };
// })



