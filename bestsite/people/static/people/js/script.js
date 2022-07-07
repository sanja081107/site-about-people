var ProjectListPage = {
    init: function() {
        this.$container = $('.project-container');
        this.render();
        this.bindEvents();
    },

    render: function() {

    },

    bindEvents: function() {
        $('.btn-favorite', this.$container).on('click', function(e) {
            console.log('Hola');
            e.preventDefault();

            var self = $(this);
            var url = $(this).attr('href');
            $.getJSON(url, function(result) {
                if (result.success) {
                    $('.glyphicon-star', self).toggleClass('active');
                }
            });

            return false;
        });
    }
};

$(document).ready(function() {
    ProjectListPage.init();
});