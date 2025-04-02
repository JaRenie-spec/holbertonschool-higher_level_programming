document.addEventListener('DOMContentLoaded', function() {
  const languageCodeSelect = document.getElementById('language_code');
  const translateButton = document.getElementById('btn_translate');
  const helloDiv = document.getElementById('hello');

  translateButton.addEventListener('click', function() {
    const languageCode = languageCodeSelect.value;

    if (languageCode) {
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          helloDiv.textContent = data.hello;
        })
        .catch(error => {
          console.error('Error fetching translation:', error);
          helloDiv.textContent = 'Sorry, something went wrong.';
        });
    } else {
      helloDiv.textContent = 'Please select a language code.';
    }
  });
});
