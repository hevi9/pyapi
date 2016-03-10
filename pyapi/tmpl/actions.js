function jq( myid ) {
    return "#" + myid.replace( /(:|\.|\[|\]|,)/g, "\\$1" );
}

$(document).ready(function(){
    $(".node").click(function(){
    	$(".scope").hide();
        var id = "";
        var sel = id + ".scope";
        console.log("show", sel);
        $(jq(sel)).show();

        
        for(let i of $(this).attr("id").split(".")) {
        	if(id == "") {
        		id = i;
        	} else {
        		id += "." + i;
        	}
            var sel = id + ".scope";
            console.log("show", sel);
            $(jq(sel)).show();
        };
    });
});
