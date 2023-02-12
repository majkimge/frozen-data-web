function load_graphs() {
    fetch("/get-graphs", {
        method: 'GET',
        headers: { 'Accept': 'application/json' }
    })
        .then(function (response) { return response.json(); })
        .then(function (data) {
        console.log(data);
    });
}
window.onload = function () {
    load_graphs();
};
