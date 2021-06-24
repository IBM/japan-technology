/* dependency setup */
process.env.UV_THREADPOOL_SIZE = 128;

var express = require("express");
var bodyParser = require('body-parser');
var log4js = require('log4js');
var logger = log4js.getLogger();
var backendApi = require("./backendApi")


logger.level = 'debug';
logger.debug("launching Example health endpoint");

/* end of dependency setup */

var port = process.env.PORT || 8080;

var app = express();

var MODE = {
  "TEST": 1,
  "Z": 2,
  "OPENSHIFT": 3
}

var CURRENTMODE = MODE.TEST;

var API_URL = ""

app.post('/mode', function(req, res) {
  logger.debug('called the mode endpoint with mode: ' + req.query.mode);
  logger.debug('called the mode endpoint with url: ' + req.query.url);
  CURRENTMODE = req.query.mode;
  API_URL = req.query.url;
  res.send({ "modes": MODE,
    "mode": CURRENTMODE
  });
});

app.get('/mode', function(req, res) {
  res.send({ "modes": MODE,
    "mode": CURRENTMODE
  });
});

app.get('/info', function(req, res) {

  logger.debug('called the information endpoint for ' + req.query.id);

  var patientdata;

  if (CURRENTMODE == MODE.TEST) {
    patientdata = {
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

    res.send(patientdata);
  } else {

    patientdata = {
      personal: {},
      medications: [],
      appointments: []
    }

    var patientInfo = backendApi.getPatientInfo(API_URL, req.query.id);
    var patientMedications = backendApi.getPatientMedications(API_URL, req.query.id);
    var patientAppointments = backendApi.getPatientAppointments(API_URL, req.query.id);

    patientInfo.then(function(patientInfoResult) {
      patientdata.personal = patientInfoResult;

      patientMedications.then(function(patientMedicationsResult) {
        patientdata.medications = patientMedicationsResult;

        patientAppointments.then(function(patientAppointmentsResult) {
          patientdata.appointments = patientAppointmentsResult;

          res.send(patientdata);
        })
      })
    })
  }

});

app.get('/measurements', function(req, res) {

  logger.debug('called the measurements endpoint for ' + req.query.id);

  var measurements;

  if (CURRENTMODE == MODE.TEST) {

  measurements = {
    smokerstatus: 'Former smoker',
    dia: 88,
    sys: 130,
    bmi: 19.74,
    bmirange: 'normal',
    weight: 54.42,
    height: 1.6603
  }

    res.send(measurements);
  }else{

  var patientMeasurements = backendApi.getPatientMeasurements(API_URL, req.query.id);

  patientMeasurements.then(function(patientMeasurementsResult) {
    measurements = patientMeasurementsResult;
    res.send(measurements);
  })
}

});

app.post('/login', function(req, res) {

  logger.debug('called the login endpoint for ' + req.query.username);

  var patientLogin = backendApi.patientLogin(API_URL, req.query.username, req.query.password);

  console.log(patientLogin)

  patientLogin.then(function(id) {


    console.log(id)
    res.send({
      id: id
    });


  })

})

// Bootstrap application settings
app.use(express.static('./public')); // load UI from public folder
app.use(bodyParser.json())

app.listen(port);
logger.debug("Listening on port ", port);
