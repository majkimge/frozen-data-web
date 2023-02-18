function load_graphs() {
  fetch("/get-graphs", {
    method: 'GET',
    headers: { 'Accept': 'application/json' }
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        let container = document.getElementById("graph-container");
        for (let i = 0; i < data.graphs.length; i++) {
          let div = document.createElement("div");
          div.innerHTML = data.graphs[i];
          if (div.firstChild != null) {
          container?.appendChild(div.firstChild);}
        }

        nodeScriptReplace(container);
      }
      else {
        console.log("Error fetching graphs")
        console.log(data);
      }
    });
}

window.onload = () => {
  load_graphs();
};




//// THIS IS USED TO RERUN SCRIPTS
function nodeScriptReplace(node) {
  if ( nodeScriptIs(node) === true ) {
          node.parentNode.replaceChild( nodeScriptClone(node) , node );
  }
  else {
          var i = -1, children = node.childNodes;
          while ( ++i < children.length ) {
                nodeScriptReplace( children[i] );
          }
  }

  return node;
}
function nodeScriptClone(node){
  var script  = document.createElement("script");
  script.text = node.innerHTML;

  var i = -1, attrs = node.attributes, attr;
  while ( ++i < attrs.length ) {                                    
        script.setAttribute( (attr = attrs[i]).name, attr.value );
  }
  return script;
}

function nodeScriptIs(node) {
  return node.tagName === 'SCRIPT';
}