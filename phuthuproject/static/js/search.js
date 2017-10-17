search.js
$('#search-form').submit(function(e){
$.post('/search/', $(this).serialize(), function(data){
$('.dk').html(data);
});
e.preventDefault();
});
