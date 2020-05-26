"use strict";

var app;
var a_eventData = document.getElementById("eventData").value.split(",");
var a_nonce =  document.getElementById("nonce").value.split(",");
var a_hash_code = document.getElementById("hash_code").value.split(",");
var a_original_hash = document.getElementById("hash_code").value.split(","); 
var a_previous_hash = document.getElementById("hash_code").value.split(","); 

(function() {

    function _getHash(id) {
        axios
            .get('/hash?eventData=' + app.eventData[id] +
                 '&previous_hash=' + app.previous_hash[id - 1])
            .then(response => {
                var data = response.data;
                app.$set(app.nonce, id, data[0]);
                app.hash[id] = data[1];
                for (var i = id; i < 7; i++) {
                    app.active[i] = (app.original_hash[id] != app.hash[id]);
                }
            });
    }

    function _fetchData() {
        axios
            .get('/eventdata')
            .then(response => {
                app.eventData = response.data;
            });
    }

    app = new Vue({
        el:'#app',
        data: {
            hash: a_hash_code,
            original_hash: a_original_hash,
            previous_hash: a_previous_hash,
            nonce: a_nonce,
            eventData: a_eventData,
            active: [false, false, false, false, false, false, false]
        },
        methods: {
            fetchData: _fetchData,
            getHash: _getHash
        }
    });
})();
