function submitForm() {
            event.preventDefault();
            var form = document.getElementById('form');
            var formData = new FormData(form);
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/analyze', true);
            xhr.onload = function() {
                var data = JSON.parse(this.responseText);
                var results = document.getElementById('results');
                results.innerHTML = "<p>Word count: " + data.word_count + "</p><p>Punctuation count: " + data.punctuation_count + "</p>";
            }
            xhr.send(formData);
            return false;
            }