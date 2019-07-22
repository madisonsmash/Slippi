var vm = new Vue({
    el: '#container',
    data: {
        files: [],
        tag: "",
        searchdate: "",
    },
    mounted:function(){
        this.created();
    },
    methods: {
        pruneResults: function (game){
            if(this.searchdate.length != 0) {
                // if date doesn't match, don't display
                if(!this.searchdate.includes(game['searchdate'])){
                    return false;
                }
            }
            // if user is searching for a tag, check all tags in players
            if(this.tag.length != 0) {
                for(var i = 0; i < 4; i++){
                    if(game['players'][i] != null && game['players'][i]['tag'].includes(this.tag)){
                        return true;
                    }
                }
                return false;
            } else {
                return true;
            }
        },
        created: function () {
            $.getJSON('map.json').then((data) => {
                this.files = data;
            });
        },
    },
});
