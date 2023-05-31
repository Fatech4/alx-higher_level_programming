  // Add a click event listener to the div element with ID "add_item"
  $("#add_item").click(function() {
    // Create a new li element
    var newItem = $("<li>").text("Item");
    
    // Append the new li element to the ul element with class "my_list"
    $("ul.my_list").append(newItem);
  });
