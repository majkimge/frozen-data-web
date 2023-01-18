async function logout() {
  await fetch("/logout");
  location.assign('/home');
}