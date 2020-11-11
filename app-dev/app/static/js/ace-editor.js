
// ACE Code Editor

// Find each text area marked to have a code editor
$('.code-editor').each(function () {
    var textarea = $(this);
    var editorID = textarea.attr('id');
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

    editor.setOptions({
        fontFamily: 'Menlo, Consolas, Monaco, monospace',
        fontSize: '15px'
    })

    if (editorID == 'static-editor') {
        editor.setReadOnly(true);
        editor.container.style.pointerEvents = "none"
        editor.renderer.$cursorLayer.element.style.opacity = 0
        editor.renderer.setStyle("disabled", true)
        // editor.blur()
        editor.setOptions({
            highlightActiveLine: false,
            highlightGutterLine: false,
            showFoldWidgets: false
        })

    } else {
        // update the text area before submitting the form
        textarea.closest('form').submit(function () {
            textarea.val(editor.getSession().getValue());
        });
    }
});