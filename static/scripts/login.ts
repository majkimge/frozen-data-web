// when document is ready
window.onload = () => {
  // handle pressing enter
  document.getElementById("input-password")?.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Cancel the default action, if needed
      event.preventDefault();
      // Trigger the button element with a click
      document.getElementById("button-login")?.click();
    }
  });
};

function login() {
  let username = (document.getElementById("input-username") as HTMLInputElement)?.value as string;
  let password = (document.getElementById("input-password") as HTMLInputElement)?.value as string;

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
      const queryString = window.location.search;
      const urlParams = new URLSearchParams(queryString);
      let next = urlParams.get('next')
      if (next == null) {
        next = "/home";
      }
      location.assign(next);
    }
    else {
      (document.getElementById("login-message") as HTMLElement).innerText = data.message;
      (document.getElementById("input-password") as HTMLInputElement).value = "";
    }
  });
}