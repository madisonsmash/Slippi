var vm = new Vue({
    el: '#container',
    data: {
        files: [],
    },
    methods: {
        //add new item on top of stack
        getAllFiles: function () {
            var fs = require('fs');
            this.files = fs.readdirSync('/assets/photos/');
            console.log(this.files);
        },
        created() {
            $.getJSON('replay-data.json').then((data) => {
                this.files = data;
            });
        },
    },
});
