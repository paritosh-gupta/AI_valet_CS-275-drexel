/**
 * Created by paritosh on 2/21/15.
 */
var accessToken = "54019354670c497d93bc7f54eb92895c";
var subscriptionKey = "bc83b78d-00be-46f0-bf45-fb563b397624";
var baseUrl = "https://api.api.ai/v1/";
$(document).ready(function() {
    $("#input").keypress(function(event) {
        if (event.which == 13) {
            event.preventDefault();
            send();
        }
    });
    $("#rec").click(function(event) {
        switchRecognition();
    });
});
var recognition;
function startRecognition() {
    recognition = new webkitSpeechRecognition();
    recognition.onstart = function(event) {
        updateRec();
    };
    recognition.onresult = function(event) {
        var text = "";
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            text += event.results[i][0].transcript;
        }
        setInput(text);
        stopRecognition();
    };
    recognition.onend = function() {
        stopRecognition();
    };
    recognition.lang = "en-US";
    recognition.start();
}
function stopRecognition() {
    if (recognition) {
        recognition.stop();
        recognition = null;
    }
    updateRec();
}
function switchRecognition() {
    if (recognition) {
        stopRecognition();
    } else {
        startRecognition();
    }
}
function setInput(text) {
    $("#input").val(text);
    send();
}
function updateRec() {
    $("#rec").text(recognition ? "Stop" : "Speak");
}
function send() {
    var text = $("#input").val();
    postToPython("/Process",{json: text});
}
function postToPython(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.
// The rest of this code assumes you are not using a library.
// It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);
    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);
            form.appendChild(hiddenField);
        }
    }
    document.body.appendChild(form);
    form.submit();
}
function setResponse(val) {
    $("#response").text(val);
}
