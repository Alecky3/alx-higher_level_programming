$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (res) {
  $('DIV#character').text(res.name);
}
);
