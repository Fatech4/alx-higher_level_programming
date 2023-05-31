  $(document).ready(function() {
    function fetchTranslation() {
      // Get the language code entered by the user
      var languageCode = $("input#language_code").val();

      // Make an AJAX GET request to fetch the translation
      $.get("https://www.fourtonfish.com/hellosalut/hello/" + languageCode + "/", function(data, status) {
        // Display the translation in the div tag with ID "hello"
        $("div#hello").text(data.hello);
      });
    }

    $("input#btn_translate").click(function() {
      fetchTranslation();
    });

    $("input#language_code").keypress(function(event) {
      if (event.which === 13) { // Check if Enter key is pressed
        fetchTranslation();
        event.preventDefault();
      }
    });
  });
