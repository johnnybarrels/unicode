
// ACE Code Editor

  // find each text area marked to have an editor
$('.code-editor').each(function() {
    var textarea = $(this);
    var mode = textarea.data('editor');
    // create the editor div
    var div = $('<div>', {
        'class': 'editor',
        'width': '100%',
        'height': '100%'
    }).insertBefore(textarea);
    // hide the original text area
    textarea.hide();
    // configure the editor
    var editor = ace.edit(div[0]);
    var session = editor.getSession();
    editor.setTheme("ace/theme/tomorrow_night_eighties");
    session.setValue(textarea.val());
    session.setMode('ace/mode/' + mode);
    session.setNewLineMode('unix');
    session.setTabSize(4);
    session.setUseSoftTabs(true);
    session.setUseWrapMode(true);
    // update the text area before submitting the form
    textarea.closest('form').submit(function() {
        textarea.val(editor.getSession().getValue());
    });
});

    // Old ACE method:
    // Works on anything with class="editor"

    // var editor;
    // $('.editor').each(function (index) {
    //     editor = ace.edit(this);
    //     editor.setTheme("ace/theme/tomorrow_night_eighties");
    //     editor.session.setMode("ace/mode/python");
    // });

