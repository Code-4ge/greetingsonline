document.getElementById('toggle').checked = false;

function classToggle(){
  const navs = document.querySelectorAll('.collapse')
  navs.forEach(nav => nav.classList.toggle('Navbar__ToggleShow'));
  if (document.getElementById('toggle').checked == true) {
    document.getElementById('toggl_label').innerHTML="&#10799;";
  } 
  else {
    document.getElementById('toggl_label').innerHTML="&#9776;";
  }
}

function Copy(){
  var text = window.location.href + "/" + encodeURIComponent(document.getElementById('name').innerText);
  navigator.clipboard.writeText(text).then(function() {
  console.log('Async: Copying to clipboard was successful!');
  alert("Copied successful")
  }, 
  function(err) {
  console.error('Async: Could not copy text: ', err);
  });
}

