function retrievePatientInformation() {

  if (!sessionStorage.getItem("patientid")) {
    console.log("Redirecting to login");
    window.location = '/login.html';
    return;
  }

  var url = "./info";
  var params = "id=" + sessionStorage.getItem("patientid");

  var http = new XMLHttpRequest();

  http.open("GET", url + "?" + params, true);

  http.onreadystatechange = function() {
    if (http.readyState == 4 && http.status == 200) {
      var patientdata = JSON.parse(http.responseText);
      console.log(http.responseText);
      fillUI(patientdata)
    }
  }
  http.send(null);
}

function retrieveDummyData() {
  var patientdata = {
    "personal": {
      "name": "Ralph DAlmeida",
      "age": 38,
      "gender": "male",
      "street": "34 Main Street",
      "city": "Toronto",
      "zipcode": "M5H 1T1"
    },
    "medications": ["Metoprolol", "ACE inhibitors", "Vitamin D"],
    "appointments": ["2018-01-15 1:00 - Dentist", "2018-02-14 4:00 - Internal Medicine", "2018-09-30 8:00 - Pediatry"]
  }
  fillUI(patientdata);
}

function fillUI(patientdata) {
  var patientname = document.getElementById('name');
  patientname.innerHTML = patientdata.personal.name;

  var patientdetails = document.getElementById('details');
  patientdetails.innerHTML = patientdata.personal.age + " years old";

  var patientstreet = document.getElementById('street');
  patientstreet.innerHTML = patientdata.personal.street;

  var patientcity = document.getElementById('city');
  patientcity.innerHTML = patientdata.personal.city;

  var patientzipcode = document.getElementById('zipcode');
  patientzipcode.innerHTML = patientdata.personal.zipcode;

  var appointments = document.getElementById('appointments');

  patientdata.appointments.forEach(function(appointment) {
    var box = document.createElement('div');
    box.className = 'boxitem';
    box.innerHTML = '<img class="stethascope" src="/images/stethascope.svg"><div class="boxitemlabel">' + appointment + '</div>'
    appointments.appendChild(box);
  })

  var medications = document.getElementById('medications');

  patientdata.medications.forEach(function(medication) {
    var box = document.createElement('div');
    box.className = 'boxitem';
    box.innerHTML = '<img class="beaker" src="/images/beaker.svg"><div class="boxitemlabel">' + medication + '</div>'
    medications.appendChild(box);
  })

  var patientlogout = document.getElementById('logout');
  patientlogout.innerHTML = sessionStorage.getItem("patientusername") + "/logout";
}
