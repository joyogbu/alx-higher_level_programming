$(document).ready(function() {
    let value = $('INPUT#language_code').val();
    $('INPUT#language_code').on("focus", function(data) {
        $.post('https://www.fourtonfish.com/hellosalut/hello/', {lang: value}, function() {
            alert($('DIV#hello').text(data));
        });
    });
    $('INPUT#btn_translate').on("click", fynction() {
        $('INPUT#language_code').trigger("focus");
    });
});
