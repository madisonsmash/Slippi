var vm = new Vue({
    el: '#container',
    data: {
        main: [],
        files: [],
        tag: "",
        searchdate: "",
        displayhome: true,
        tourneyname: "",
    },
    mounted:function(){
        this.created();
    },
    methods: {
        pruneResults: function (game){
            // if user is searching for a tag, check all tags in players
            if(this.tag.length != 0) {
                for(var i = 0; i < 4; i++){
                    if(game['players'][i] != null && game['players'][i]['searchtag'].includes(this.tag.toUpperCase())){
                        return true;
                    }
                }
                return false;
            } else {
                return true;
            }
        },
        created: function () {
            $.getJSON('main.json').then((data) => {
                this.main = data;
                console.log(this.main);
            });
            $.getJSON('map.json').then((data) => {
                this.files = data;
            });
        },
        displayTournament: function(name) {
            this.displayhome = false;
            this.tourneyname = name;
        },
    },
});
