$(document).ready(function()
{
    function showHint(msg)
    {
        $a = $('<div class="row"><div class="alert alert-info">'
            +'<button type="button" class="close" data-dismiss="alert">&times;</button>'
            +msg
            +'</div></div>');
        $('.container').append($a);
    }
    
    function updatePage()
    {
         $.ajax('/gamestate', {'cache': false}).done(function(R)
        {
            var newroom = $.parseJSON(R);
        
            if(newroom.hint) showHint(newroom.hint);
        
            $('.roomname').html(newroom.name);
        
            var $log = $('pre');
        
            $log.append(newroom.gametext);
        
            var h = $log.height();
            $log.animate({'scrollTop': '+='+h}, 1000);
            $('#appendedInputButton').val('');
        });
    };

    function playerAction(s)
    {
    
        $.ajax('/pl_action/'+s, {'cache': false}).done(function()
        {
            updatePage();            
        });
    }

    $('.btn').click(function(e)
    {
        if(e.target.id == "newgame") return;
        text = $('#appendedInputButton').val();
        if(text === "new game" || text === "newgame") return;
        e.preventDefault();
        playerAction(text);
    });
    
    $('pre').html('');
    updatePage();
    
});