var app;

(function() {
    app = new Vue({
        el:'#app',
        data: {
            hash: '',
            nonce: a_nonce,
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
                axios
                    .get('/hash?block_no=' + this.block_no +
                         '&nonce=' + this.nonce +
                         '&eventData=' + this.eventData)
                    .then(response => {
                        this.hash = response.data;
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
