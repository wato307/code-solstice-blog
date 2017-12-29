var mainContentObj = $("#contentWrapper")[0];
var originalTop = mainContentObj.getBoundingClientRect().top;
var lastTop = originalTop;
$(window).scroll(function(evt){
    var box = mainContentObj.getBoundingClientRect();
    if(box.top >= lastTop){
        $(".navbar").css("opacity", 1);
    }else{
        if(box.top>=0){
            $(".navbar").css("opacity", box.top/originalTop);
        }else{
            $(".navbar").css("opacity", 0);
        }
    }
    lastTop = box.top;
});