function load_graphs() {
  fetch("/get-graphs", {
    method: 'GET',
    headers: {'Accept': 'application/json' }
  })
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  });
}

window.onload = () => {
  load_graphs();
};