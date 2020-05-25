"use strict";

var app;
var a_eventData = document.getElementById("eventData").value;

(function() {
    app = new Vue({
        el:'#app',
        data: {
            hash: '',
            nonce: '',
        },
        methods: {
            fetchData: function() {
                axios
                    .get('/eventdata')
                    .then(response => {
                        this.eventData = response.data;
                    });
            },
            getHash: function(id) {
                var previous_hash = document.getElementById("previous_hash_" + id).innerHTML;
                var eventData = document.getElementById("eventData_" + id).value;
                axios
                    .get('/hash?eventData=' + eventData +
                         '&previous_hash=' + previous_hash)
                    .then(response => {
                        var data = response.data;
                        var nonce = document.getElementById('nonce_' + id);
                        nonce.value = data[0];
                        var hash = data[1];
                        var hash_code = document.getElementById('hash_code_' + id);
                        hash_code.innerHTML = hash;
                        var originalHash = document.getElementById("original_hash_" + id);
                        var hash_value = originalHash.innerHTML;
                        if (hash_value == '') {
                            originalHash.innerHTML = hash;
                        } else if (hash_value != hash) {
                            originalHash.style.backgroundColor = 'red';
                        } else {
                            originalHash.style.backgroundColor = "#e7e6e6";
                        }
                    });
            }
        }
    });
})();
