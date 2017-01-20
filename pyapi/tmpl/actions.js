function jq(myid) {
    return "#" + myid.replace(/(:|\.|\[|\]|,)/g, "\\$1");
}


function prepare() {
    "use strict";
    $(".scope").hide();
    $(jq(".scope")).show();
}


function show_scope() {
    "use strict";
    $(".scope").hide();
    let id_path = this.id.split(".");
    let path = id_path.slice(0,-1);
    path.push("scope");
    let sel = path.join(".");
    console.log("show", sel);
    $(jq(sel)).show();
}

$(document).ready(function () {
    prepare();
    $(".nodenav").click(show_scope);
});
