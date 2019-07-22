var vm = new Vue({
    el: '#container',
    data: {
        files: [],
    },
    mounted:function(){
        this.created();
    },
    methods: {
        //add new item on top of stack
        getAllFiles: function () {
            $.getJSON('map.json').then((data) => {
                this.files = data;
            });
            console.log(files);
        },
        created() {
            $.getJSON('map.json').then((data) => {
                this.files = data;
            });
        },
    },
});
