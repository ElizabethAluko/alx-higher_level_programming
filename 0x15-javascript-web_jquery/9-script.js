$(document).ready(function() {
  // Fetch the translation data from the URL
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
    // Extract the translation of "hello" from the fetched data
    var helloTranslation = data.hello;
    
    // Display the translation in the <div> with ID "hello"
    $('#hello').text(helloTranslation);
  });
});
