$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/?' + $.param({ lang: $('INPUT#language_code').val() }), function (res) {
      $('DIV#hello').html(res.hello);
    });
  });
});
