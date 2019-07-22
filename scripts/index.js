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
        pruneResults: function (game){
            if(this.searchdate.length == 0) {
                return true;
            }
            return(this.searchdate.includes(game['searchdate']));
        },
        created: function () {
            $.getJSON('map.json').then((data) => {
                this.files = data;
            });
        },
    },
});
