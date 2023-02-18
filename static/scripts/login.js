// when document is ready
window.onload = function () {
    var _a;
    // handle pressing enter
    (_a = document.getElementById("input-password")) === null || _a === void 0 ? void 0 : _a.addEventListener("keypress", function (event) {
        var _a;
        // If the user presses the "Enter" key on the keyboard
        if (event.key === "Enter") {
            // Cancel the default action, if needed
            event.preventDefault();
            // Trigger the button element with a click
            (_a = document.getElementById("button-login")) === null || _a === void 0 ? void 0 : _a.click();
        }
    });
};
function login() {
    var _a, _b;
    var username = (_a = document.getElementById("input-username")) === null || _a === void 0 ? void 0 : _a.value;
    var password = (_b = document.getElementById("input-password")) === null || _b === void 0 ? void 0 : _b.value;
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
            document.getElementById("login-message").innerText = data.message;
            document.getElementById("input-password").value = "";
        }
    });
}
