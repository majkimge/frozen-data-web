import * as $ from "jquery"; // YOU NEED TO DELETE FIRST 3 LINES FROM .js FILE

// when document is ready
$(() => {
  // handle pressing enter
  $("#input-password" ).on("keypress", function(event) {
    if (event.key.toLowerCase() === "enter") {
      event.preventDefault();
      $("#button-login").trigger("click");
    }
  });
});

function login() {
  let username = $("#input-username").val() as string;
  let password = $("#input-password").val() as string;

  fetch("/login", {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({username: username, password: password})
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.success) {
      location.assign('/home');
    }
    else {
      $("#login-message").text(data.message);
      $("#input-password").val("");
    }
  });
  
}