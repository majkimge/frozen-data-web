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
            alert(data.message);
        }
    });
}
