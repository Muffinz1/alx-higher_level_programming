/*api swap*/
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (data, textStatus) {
  $('DIV#character').text(data.name);
});
