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
    // $('.nav-item').first().addClass('active');
    // $('.tab-pane').first().addClass('active show');

    // function returnToPreviousPage() {
    //     window.history.back();
    // }

    // $('#createCourseForm').submit(function () {
    //     if (confirm("Are you sure?" == false)) {
    //         returnToPreviousPage()
    //     }
    // });

});

// function confirmForm() {
//     if (!confirm("Are you sure?")) {
//         return false
//     }
// }

// Admin new question type selector
function newQuestionSelector(qType) {
    if (qType == 1) {
        $('#new-question-mcq').hide();
        $('#new-question-solution').show();
        $('#solution-textbox').show();
        $('#solution-mcq').hide()
        $('#question-type').attr('value', 1);
        $('#new-question-form #question-description').css('height', '190px');
    }
    else if (qType == 2) {
        $('#new-question-mcq').show();
        $('#new-question-solution').show();
        $('#solution-textbox').hide();
        $('#solution-mcq').show()
        $('#question-type').attr('value', 2);
        $('#new-question-form #question-description').css('height', '50px');
    }
    else if (qType == 3) {
        $('#new-question-mcq').hide();
        $('#new-question-solution').hide();
        $('#question-type').attr('value', 3);
        $('#new-question-form #question-description').css('height', '280px');
    }
};

function validatePassword() {
    var validator = $("#registration-form").validate({
        rules: {
            password_again: {
                equalTo: "#password"
            }
        },
        messages: {
            password_again: "Passwords do not match"
        }
    });
}

// function validatePassword() {
//     confirm("are you sure?");
//     var pswd = $('#password').attr('value');
//     var pswd_rpt = $('#password_again').attr('value');
//     if (pswd != pswd_rpt) {
//         alert("The passwords do not match!");
//         $('#password_again').focus();
//         $('#password_again').closest('form').preventDefault();
//         return;
//     }
// }

// Storing value of MCQ radio button submission
function insertValueToHidden(loop_index, i) {
    mcq_index_str = "#mcq-form-" + loop_index.toString() + " #mcq-answer";
    console.log(mcq_index_str);
    $(mcq_index_str).attr('value', ['a', 'b', 'c', 'd'][i - 1])
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



