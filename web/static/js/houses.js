"use strict";

var app;
var a_eventData = sessionStorage.eventData.split(",");
var a_nonce = sessionStorage.nonce.split(",");
var a_hash_code = sessionStorage.hash_code.split(",");
var a_original_hash = a_hash_code.slice();
var a_previous_hash = a_hash_code.slice();

(function() {

    function _getHash(id) {
        axios
            .get('/hash?eventData=' + app.eventData[id] +
                 '&previous_hash=' + app.previous_hash[id - 1])
            .then(response => {
                var data = response.data;
                app.$set(app.nonce, id, data[0]);
                app.hash[id] = data[1];
                app.$set(app.active, id, (app.original_hash[id] != app.hash[id]));
                if (id < 7) {
                    app.previous_hash[id] = app.hash[id];
                    _getHash(id + 1);
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
            active: new Array(7).fill(false)
        },
        methods: {
            fetchData: _fetchData,
            getHash: _getHash
        }
    });
})();
