var urlfield = document.getElementById('url');
var cobolbutton = document.getElementById('cobolbutton');
var javabutton = document.getElementById('javabutton');
var localbutton = document.getElementById('localbutton');

var MODE = {
  "TEST": 1,
  "Z": 2,
  "OPENSHIFT": 3
}

function checkurl() {
  if (validURL(urlfield.value)) {
    cobolbutton.style.opacity = 1;
    javabutton.style.opacity = 1;
  } else {
    cobolbutton.style.opacity = 0.3;
    javabutton.style.opacity = 0.3;
  }

  getMode();
}

function setRunMode(text) {
  var rm = document.getElementById('runmode');
  rm.innerHTML = text;
}

function getMode() {

  var url = "./mode";

  var http = new XMLHttpRequest();

  http.open("GET", url, true);

  http.onreadystatechange = function() {
    if (http.readyState == 4 && http.status == 200) {
      var patientdata = JSON.parse(http.responseText);
      console.log(http.responseText);
      var response = JSON.parse(http.responseText);
      var mode = parseInt(response.mode);

      switch (mode) {

        case MODE.TEST:
          highlightLocal();
          break;

        case MODE.Z:
          highlightCobol();
          break;

        case MODE.OPENSHIFT:
          highlightJava();
          break;

      }

    }
  }
  http.send(null);

}

getMode();

function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
    '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
  return !!pattern.test(str);
}

function highlightJava() {
  localbutton.classList.remove("settingsbuttonselected");
  cobolbutton.classList.remove("settingsbuttonselected");
  javabutton.classList.add('settingsbuttonselected');
  javabutton.style.opacity = 1;
  setRunMode('Currently reading data from a Java OpenShift microservice');
}


function chooseJava() {
  if (validURL(urlfield.value)) {
    highlightJava();
    setModeOnServer(MODE.OPENSHIFT);
    console.log('clicked java');
  }
}

function highlightCobol() {
  localbutton.classList.remove("settingsbuttonselected");
  javabutton.classList.remove("settingsbuttonselected");
  cobolbutton.classList.add('settingsbuttonselected');
  cobolbutton.style.opacity = 1;
  setRunMode('Currently reading data from a Cobol Z application');
}

function setModeOnServer(mode) {

  var url = "./mode";
  var params = "mode=" + mode + "&url=" + urlfield.value;

  var http = new XMLHttpRequest();

  http.open("POST", url + "?" + params, true);

  http.onreadystatechange = function() {
    if (http.readyState == 4 && http.status == 200) {

      // sessionStorage.removeItem(patientid);
      // sessionStorage.removeItem(patientusername);
      sessionStorage.setItem("patientUImode", mode);

      window.location = '/login.html';

    }
  }
  http.send(null);

}

function chooseCobol() {
  if (validURL(urlfield.value)) {
    setModeOnServer(MODE.Z);
    highlightCobol();
    console.log('clicked cobol');
  }
}

function highlightLocal() {
  localbutton.classList.add("settingsbuttonselected");
  javabutton.classList.remove("settingsbuttonselected");
  cobolbutton.classList.remove('settingsbuttonselected');
  setRunMode('Currently reading data from a Node OpenShift microservice - demo mode');
}

function chooseLocal() {
  setModeOnServer(MODE.TEST);
  highlightLocal();
  console.log('clicked local');
}
