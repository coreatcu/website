var infographic = ""
function setInfographic(newInfographic){
    infographic = newInfographic + "/" + newInfographic;
    console.log(infographic);
}

$(function() {
  // $("#stage").load('static/img/infographic/about/about-core.svg', function(response) {
  $("#stage").load('../static/img/infographic/' + infographic + ".svg", function(response) {
    $(this).addClass("svgLoaded");

    if (!response) { // Error loading SVG
      $(this).html('Error loading SVG. Be sure you are running from a the http protocol (not locally) and have read <strong><a href="http://tympanus.net/codrops/?p=13831#the-javascript">this important part of the tutorial</a></strong>');
    }

    cursor();

    $("#google_icon").on("click", function() {
        inactivate();
        $("#google_icon").css({opacity: "1.0"});
        $("#google_bubbles").css({opacity: "1.0"});
    });

    $("#twitter_icon").on("click", function() {
        inactivate();
        $("#twitter_icon").css({opacity: "1.0"});
        $("#twitter_bubbles").css({opacity: "1.0"});
    });

    $("#uber_icon").on("click", function() {
        inactivate();
        $("#uber_icon").css({opacity: "1.0"});
        $("#uber_bubbles").css({opacity: "1.0"});
    });

    $("#impulse_icon").on("click", function() {
        inactivate();
        $("#impulse_icon").css({opacity: "1.0"});
        $("#impulse_bubbles").css({opacity: "1.0"});
    });

    $("#facebook_icon").on("click", function() {
        inactivate();
        $("#facebook_icon").css({opacity: "1.0"});
        $("#facebook_bubbles").css({opacity: "1.0"});
    });


    function cursor() {
      $("#google_icon,#twitter_icon,#uber_icon,#impulse_icon,#facebook_icon").css({ cursor: "hand" });
    }

    function inactivate() {
      $("#google_icon,#twitter_icon,#uber_icon,#impulse_icon,#facebook_icon").css({ opacity: '0.5',
                                                                   WebkitTransition : 'opacity .25s ease-in-out',
        MozTransition    : 'opacity .25s ease-in-out',
        MsTransition     : 'opacity .25s ease-in-out',
        OTransition      : 'opacity .25s ease-in-out',
        transition       : 'opacity .25s ease-in-out'});
        $("#google_bubbles,#twitter_bubbles,#uber_bubbles,#impulse_bubbles,#facebook_bubbles").css({ opacity: '0.5',
        WebkitTransition : 'opacity .25s ease-in-out',
        MozTransition    : 'opacity .25s ease-in-out',
        MsTransition     : 'opacity .25s ease-in-out',
        OTransition      : 'opacity .25s ease-in-out',
        transition       : 'opacity .25s ease-in-out'});
    }
  });
});