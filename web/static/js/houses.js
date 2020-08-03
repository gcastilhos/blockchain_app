"use strict";

(function() {

    var _getHash = function(id) {
        axios
            .get('/hash?eventData=' + app.eventData[id] +
                 '&previous_hash=' + app.previous_hash[id])
            .then(response => {
                var data = response.data;
                app.$set(app.nonce, id, data[0]);
                app.$set(app.hash, id, data[1]);
                app.$set(app.active, id, (app.original_hash[id] != app.hash[id]));
                if (id < app.size - 1) {
                    app.$set(app.previous_hash, id + 1, app.hash[id]);
                    _getHash(id + 1);
                }
            });
    };

    var _fetchData = function() {
        axios
            .get('/eventdata')
            .then(response => {
                app.eventData = response.data;
            });
    };

    var _blockNoFormat = function(values) {
        var size = values.length;
        var new_values = new Array(size);
        for (var i = 0; i < size; i++) {
            new_values[i] = ("000" + values[i]).slice(-6);
        }   
        return new_values; 
    };

    var app = new Vue({
        el:'#app',
        data: {
            block_no: _blockNoFormat(sessionStorage.block_no.split(",")),
            hash: sessionStorage.hash_code.split(","),
            original_hash: sessionStorage.hash_code.split(","),
            previous_hash: sessionStorage.previous_hash.split(","),
            nonce: sessionStorage.nonce.split(","),
            eventData: sessionStorage.eventData.split(","),
            active: new Array(sessionStorage.size).fill(false),
            size: sessionStorage.size
        },
        methods: {
            fetchData: _fetchData,
            getHash: _getHash
        }
    });
})();
