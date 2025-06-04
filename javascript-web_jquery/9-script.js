$(document).ready(function() {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function(error) {
      console.log('Error fetching data:', error);
      $('#hello').text('Error loading translation');
    }
  });
});
