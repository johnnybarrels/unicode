$(document).ready(function () {
    console.log('hello');
    $('#create-course-btn').click(function (event) {
        event.preventDefault();
        let url = "{{ url_for('create_course') }}";
        $.get(url, function (data) {
            $.post(url, data = $('#createCourseForm').serialize(), function (data) {
                if (data.status == 'ok') {
                    $('#new-course-modal').modal('hide');
                    location.reload();
                } else {
                    console.log('failed');
                }
            });
        });
    });
});             
