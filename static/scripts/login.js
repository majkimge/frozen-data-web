"use strict";
exports.__esModule = true;
var $ = require("jquery"); // YOU NEED TO DELETE FIRST 3 LINES FROM .js FILE
// when document is ready
$(function () {
    // handle pressing enter
    $("#input-password").on("keypress", function (event) {
        if (event.key.toLowerCase() === "enter") {
            event.preventDefault();
            $("#button-login").trigger("click");
        }
    });
});
function login() {
    var username = $("#input-username").val();
    var password = $("#input-password").val();
    alert(username + password);
    fetch("/login", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({ username: username, password: password })
    })
        .then(function (response) { return response.json(); })
        .then(function (data) {
        if (data.success) {
            location.assign('/home');
        }
        else {
            $("#login-message").text(data.message);
            $("#input-password").val("");
        }
    });
}
