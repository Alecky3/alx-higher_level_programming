$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (res) {
    $('DIV#hello').text(res.hello);
  }
  );
}
);
