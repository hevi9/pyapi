function jq( myid ) {
    return "#" + myid.replace( /(:|\.|\[|\]|,)/g, "\\$1" );
}

// this is inefficient
function button_adjust_height() {
    "use strict";
    let height_max = 0;
    $(".btn").each(function() {
        if($(this).height() > height_max) {
            height_max = $(this).height();
        }
    });
    $(".btn").height(height_max);
}

function prepare() {
    "use strict";
    button_adjust_height();
    $(".scope").hide();
    $(jq(".scope")).show();
}


$(document).ready(function(){
    prepare();
    $(".node").click(function(){
    	$(".scope").hide(); // hide all scopes first
        let id = "";
        let sel = id + ".scope";
        console.log("show", sel);
        $(jq(sel)).show();
        for(let i of $(this).attr("id").split(".")) {
        	if(id == "") {
        		id = i;
        	} else {
        		id += "." + i;
        	}
            let sel = id + ".scope";
            console.log("show", sel);
            $(jq(sel)).show();
        };
        // show .doc scope as well
        sel = id + ".doc.scope";
        console.log("show", sel);
        $(jq(sel)).show();
    });
});
