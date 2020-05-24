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

    // Modal button assignments
    $("#new-course-btn").click(function () {
        $("#new-course-modal").modal("show");
    });

    $("#new-course-icon").click(function () {
        $("#new-course-modal").modal("show");
    });

    $("#new-test-btn").click(function () {
        $("#new-test-modal").modal("show");
    });

    $("#rename-test-btn").click(function () {
        $("#rename-test-modal").modal("show")
    })

    $("#manage-students-btn").click(function () {
        $("#manage-students-modal").modal("show");
    });

    $("#help").click(function () {
        $("#help-modal").modal("show");
    });

    // Admin test dropdown
    $(".dropdown-toggle").dropdown();

    // Always making the first nav tab and pane active on load
    $('.nav-item').first().addClass('active');
    $('.tab-pane').first().addClass('active show');

});

// Admin new question type selector
function newQuestionSelector(qType) {
    if (qType == 1) {
        $('#new-question-mcq').hide();
        $('#new-question-solution').show();
        $('#question-type').attr('value', 1);
        $('#new-question-form #question-description').css('height', '190px');
    }
    else if (qType == 2) {
        $('#new-question-mcq').show();
        $('#new-question-solution').show();
        $('#question-type').attr('value', 2);
        $('#new-question-form #question-description').css('height', '130px');
    }
    else if (qType == 3) {
        $('#new-question-mcq').hide();
        $('#new-question-solution').hide();
        $('#question-type').attr('value', 3);
        $('#new-question-form #question-description').css('height', '280px');
    }
};

// Test MCQ radio button selectiong recording -- NOT WORKING
function insertValueToHidden(selection) {
    $('#mcq_answer').attr('value', selection)
}

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



