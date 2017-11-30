$(document).ready(function () {

    // Get CSRF token as variable
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    let csrftoken = getCookie('csrftoken');


    // Like Dislike
    function like() {
        let like = $(this);
        let pk = like.data('id');
        let dislike = like.next();

        console.log('LIKEEEE');
        $.ajax({
            url : $(this).attr('send-to'),
            type : 'POST',
            data : { 'obj' : pk, csrfmiddlewaretoken: csrftoken},

            success : function (data) {
                like.find("[data-count='like']").text(data.likes);
                dislike.find("[data-count='dislike']").text(data.dislikes);
            }
        });

        return false;
    }

    function dislike() {
        let dislike = $(this);
        let pk = dislike.data('id');
        let like = dislike.prev();

        $.ajax({
            url : $(this).attr('send-to'),
            type : 'POST',
            data : { 'obj' : pk, csrfmiddlewaretoken: csrftoken },

            success : function (data) {
                dislike.find("[data-count='dislike']").text(data.dislikes);
                like.find("[data-count='like']").text(data.likes);
            }
        });

        return false;
    }

    //LIKE DISLIKE ONCLICK
    $(function() {
        $('[data-action="like"]').click(like);
        $('[data-action="dislike"]').click(dislike);
    });


    // Send comment

    $('#send-comment').on('submit', function (e) {
        e.preventDefault();
        let pk = $(this).attr('data-id');
        console.log($(this).find('input[name="text"]').val())
        $.ajax({
            url : $(this).attr('action'),
            type : 'POST',
            data : {'obj' : pk,
                    csrfmiddlewaretoken: csrftoken,
                    'text': $('#comment_text').val()
            },
            success: function (response) {
                if (response.error) {
                    alert('min comment len = 10 ;)')
                } else {
                    let comment = `<li><p><small>${response.user}</small></p><p>${response.text}</p></li><hr>`;
                    $('#comments').prepend(comment)
                }
            }
        })

    });


});


