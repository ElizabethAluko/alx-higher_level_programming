// Attach a click event handler to the <div> with ID "toggle_header"
$('#toggle_header').click(function() {
  // Toggle the class "red" and "green" on the <header> element
  $('header').toggleClass('red green');
});
