"use strict";

var app;
var a_block_no = document.getElementById("block_no").value;
var a_eventData = document.getElementById("eventData").value;

(function() {
    app = new Vue({
        el:'#app',
        data: {
            hash: '',
            nonce: '',
            block_no: a_block_no,
            eventData: a_eventData
        },
        methods: {
            fetchData: function() {
                axios
                    .get('/eventdata')
                    .then(response => {
                        this.eventData = response.data;
                    });
            },
            getHash: function() {
                var previous_hash = document.getElementById("previous_hash");
                axios
                    .get('/hash?eventData=' + this.eventData +
                         '&previous_hash=' + previous_hash.innerHTML)
                    .then(response => {
                        var data = response.data;
                        this.nonce = data[0];
                        this.hash = data[1];
                        var originalHash = document.getElementById("original_hash");
                        var hash_value = originalHash.innerHTML;
                        if (hash_value == '') {
                            originalHash.innerHTML = this.hash;
                        } else if (hash_value != this.hash) {
                            originalHash.style.backgroundColor = 'red';
                        } else {
                            originalHash.style.backgroundColor = "#e7e6e6";
                        }
                    });
            }
        }
    });
})();
