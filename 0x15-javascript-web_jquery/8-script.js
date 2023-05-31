$(function(){
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", 
	  function(data, status){
    $.each(data.results, function(i, item){
	$("ul#list_movies").append("<li>" + item.title + "</li>");
    });
  });
});
