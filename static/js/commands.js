$(document).ready(function()
{
    //for performance
    var $TEXTBOX = $('pre');
    var $ACTIONBAR = $('#appendedInputButton');

    function showHint(msg)
    {
        $a = $('<div class="row"><div class="alert alert-info">'
            +'<button type="button" class="close" data-dismiss="alert">&times;</button>'
            +msg
            +'</div></div>');
        $('.hintbar').prepend($a);
    }
    
    function postChanges(R)
    {
        var newroom = $.parseJSON(R);
        
        if(newroom.hint) showHint(newroom.hint);
        
        $('.roomname').text(newroom.name, 750);
        
        $TEXTBOX.append(newroom.gametext);
        pageDown();
        $ACTIONBAR.val('');
    }
    
    function updatePage(newroom)
    {
        //multiple ajax calls were harming performance
        if(newroom)
        {
            postChanges(newroom);
            return;
        }
    
         $.ajax('/gamestate').done(function(R)
        {
            postChanges(R);
        });
    };

    function playerAction(s)
    {
    
        $.ajax('/pl_action/'+s+'/True').done(function(R)
        {
            updatePage(R);            
        });
    }
    
    function pageUp()
    {
            var h = $TEXTBOX.height();
            $TEXTBOX.animate({'scrollTop': '-='+h}, 750);
    }
    
    function pageDown()
    {
            var h = $TEXTBOX.height();
            $TEXTBOX.animate({'scrollTop': '+='+h}, 750);
    }
    
    function arrowUp()
    {
            var h = $TEXTBOX.height();
            $TEXTBOX.animate({'scrollTop': '-='+h/3}, 100);
    }
    
    function arrowDown()
    {
        var h = $TEXTBOX.height();
        $TEXTBOX.animate({'scrollTop': '+='+h/3}, 100);
    }

    $('.btn').click(function(e)
    {
        if(e.target.id == "newgame") return;
        text = $ACTIONBAR.val();
        if(text === "new game" || text === "newgame") return;
        e.preventDefault();
        playerAction(text);
    });
    
    $ACTIONBAR.keydown(function(e)
    {
        if(e.which == 33) pageUp();
        else if(e.which == 34) pageDown();
        else if(e.which == 38) arrowUp();
        else if(e.which == 40) arrowDown();
    });
    
    $TEXTBOX.text('');
    updatePage();
    
});