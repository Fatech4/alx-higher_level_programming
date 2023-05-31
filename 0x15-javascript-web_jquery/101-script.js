  $(document).ready(function() {
    // Add item to the list
    $("div#add_item").click(function() {
      var newItem = $("<li>").text("Item");
      $("ul.my_list").append(newItem);
    });

    // Remove last item from the list
    $("div#remove_item").click(function() {
      $("ul.my_list li:last-child").remove();
    });

    // Clear the entire list
    $("div#clear_list").click(function() {
      $("ul.my_list").empty();
    });
  });
