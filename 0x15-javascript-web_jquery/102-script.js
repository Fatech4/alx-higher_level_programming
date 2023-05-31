  $(document).ready(function() {
    $("input#btn_translate").click(function() {
      // Get the language code entered by the user
      var languageCode = $("input#language_code").val();

      // Make an AJAX GET request to fetch the translation
      $.get("https://www.fourtonfish.com/hellosalut/hello/" + languageCode + "/", function(data, status) {
        // Display the translation in the div tag with ID "hello"
        $("div#hello").text(data.hello);
      });
    });
  });
