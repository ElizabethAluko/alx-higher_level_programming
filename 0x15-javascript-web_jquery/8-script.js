// Fetch the movie data from the URL
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  // Get the movie results from the fetched data
  var movies = data.results;
  
  // Iterate over each movie and create <li> elements for their titles
  $.each(movies, function(index, movie) {
    // Create a new <li> element with the movie title
    var listItem = $('<li>').text(movie.title);
    
    // Append the <li> element to the <ul> with ID "list_movies"
    $('#list_movies').append(listItem);
  });
});
