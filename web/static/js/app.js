function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
     results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
     console.log(results);
}

var prodId = getParameterByName('audio');
