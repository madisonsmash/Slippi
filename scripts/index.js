var vm = new Vue({
    el: '#container',
    data: {
        files: [],
        stylesheet: "light-style.css",
        searchdate: "",
    },
    mounted:function(){
        this.created();
    },
    methods: {
        //add new item on top of stack
        getAllFiles: function () {
            console.log(this.files);
        },
        created: function () {
            $.getJSON('map.json').then((data) => {
                this.files = data;
                console.log(this.files)
            });
        },
    },
});
