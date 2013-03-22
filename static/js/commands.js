$(document).ready(function()
{
    function showHint(msg)
    {
        $a = $('<div class="alert span8">'
            +'<button type="button" class="close" data-dismiss="alert">&times;</button>'
            +msg
            +'</div>');
        $('.container').append($a);
    }

    function nextRoom(s)
    {
    
        $.ajax('/pl_action/'+s).done(function(R)
        {
            var newroom = $.parseJSON(R);
            
            if(newroom.hint) showHint(newroom.hint);
            
            $('.roomname').html(newroom.name);
           
            var $log = $('pre');
            
            $log.append('\n  > '+s+'\n');
            $log.append('\n'+newroom.name+'\n');
            $log.append(newroom.description);
            
            var h = $log.height()
            $log.animate({'scrollTop': '+='+h}, 1000);
            $('#appendedInputButton').val('');
            
            if(newroom.gameover)
            {
                $('form').hide();
                $newgame = $('<a href="/newgame"><button type="submit" id="newgame" class="btn btn-inverse">Play Again?</button></a>');
                $('.container').append($newgame);
            }
            
        });
    }

    $('.btn').click(function(e)
    {
        if(e.target.id == "newgame") return;
        text = $('#appendedInputButton').val();
        if(text === "new game" || text === "newgame") return;
        e.preventDefault();
        //TODO: This id sucks, find a better way to handle it
        nextRoom(text);
    });
    
});