// Exercise 2.3 Javascript file  //
// Read the instructions.html //

//some helpful debug code

$("#javascript_start").html("[OK] Started executing the javascript file");
$("#javascript_end").html("[WAITING]...this far we haven't reached the end... Maybe you should try FireBug?");

// ADD YOUR CODE BETWEEN THESE LINES //


$(function() {
    $('a[href$=".pdf"]').prop('class', 'pdf');
});

$(function() {//NOT with .pdf or .html
    $('a[href*="."]:not(a[href$=".pdf"]):not(a[href$=".html"]):not(a[href$="/"]):not(a[href$="link"])').prop('class', 'download');
});




// ADD YOUR CODE BETWEEN THESE LINES //

//some helpful debug code

$("#javascript_end").html("[OK] The end of your javascript file was reached. (meaning there were no huge errors) Hopefully your code works too! ");
