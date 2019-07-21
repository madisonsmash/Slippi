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
            console.log(files);
        },
        created() {
            $.getJSON('map.json').then((data) => {
                this.files = data;
            });
        },
    },
});
