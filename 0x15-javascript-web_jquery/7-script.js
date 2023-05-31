// Fetch the character data from the URL
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  // Extract the character name from the fetched data
  var characterName = data.name;
  
  // Display the character name in the <div> with ID "character"
  $('#character').text(characterName);
});
