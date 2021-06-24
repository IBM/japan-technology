var request = require('request');
// var API_URL = "https://api.us.apiconnect.ibmcloud.com/spbodieusibmcom-kenishia/sb/";

function getPatientInfo(url, patientID) {
	return new Promise(function(resolve, reject) {
		request(url + "getInfo/patients/" + patientID, function (error, response, body) {
	 		if (!error && response.statusCode == 200) {

				body = JSON.parse(body);

	    		var patientInfo = {
					      name: body["HCCMAREA"]["CA_PATIENT_REQUEST"]["CA_FIRST_NAME"] + " " + body["HCCMAREA"]["CA_PATIENT_REQUEST"]["CA_LAST_NAME"],
					      age: getAge(body["HCCMAREA"]["CA_PATIENT_REQUEST"]["CA_DOB"]),
					      street: body["HCCMAREA"]["CA_PATIENT_REQUEST"]["CA_ADDRESS"],
					      city: body["HCCMAREA"]["CA_PATIENT_REQUEST"]["CA_CITY"],
					      zipcode: body["HCCMAREA"]["CA_PATIENT_REQUEST"]["CA_POSTCODE"]
				};
				return resolve(patientInfo);
	  		} else {
	  			return resolve({});
	  		}
	  	});
	})
}

function getPatientMedications(url, patientID) {
	return new Promise(function(resolve, reject) {
		request(url + "getInfo/prescription/" + patientID, function (error, response, body) {
			var medications = [];
	 		if (!error && response.statusCode == 200) {
	 			body = JSON.parse(body);

	 			try {
					var medicationData = body["GETMEDO"]["CA_LIST_MEDICATION_REQUEST"]["CA_MEDICATIONS"];
				} catch(e) {
					return resolve(medications);
				}

	 			for (var i = 0, len = medicationData.length; i < len; i++) {
					if (medications.indexOf(medicationData[i]["CA_DRUG_NAME"]) === -1) {
						medications.push(medicationData[i]["CA_DRUG_NAME"]);
					}		
	 			}

				return resolve(medications);
	  		} else {
	  			return resolve(medications);
	  		}
	  	});
	})
}

function getPatientAppointments(url, patientID) {
	return new Promise(function(resolve, reject) {
		request(url + "appointments/list/" + patientID, function (error, response, body) {
			var appointments = [];
	 		if (!error && response.statusCode == 200) {

				body = JSON.parse(body);
				 
				var appointmentsData = body["ResultSet Output"]

	 			for (var i = 0, len = appointmentsData.length; i < len; i++) {
					appointments.push(appointmentsData[i]["APPT_DATE"].trim() + " " + appointmentsData[i]["APPT_TIME"].trim().replace(".",":").substring(0,5) + " - " + appointmentsData[i]["MED_FIELD"].trim());
				}
				return resolve(appointments);
	  		} else {
	  			return resolve(appointments);
	  		}
	  	});
	})
}

function getPatientMeasurements(url, patientID) {
	return new Promise(function(resolve, reject) {
		request(url + "listObs/" + patientID, function (error, response, body) {
			var measurements = {};
	 		if (!error && response.statusCode == 200) {
	 			body = JSON.parse(body);

	 			var measurementsData = body["ResultSet Output"]

	 			for (var i = 0, len = measurementsData.length; i < len; i++) {
	 				switch(measurementsData[i][["DESCRIPTION"]]) {
	 					case "Tobacco smoking status NHIS":
	 						if (!measurements.smokerstatus) {
	 							measurements.smokerstatus = measurementsData[i]["CHARACTERVALUE"];
	 						}
	 						break;
	 					case "Body Height":
	 						if (!measurements.height) {
	 							measurements.height = measurementsData[i]["NUMERICVALUE"]/100;
	 						}
	 						break;
	 					case "Body Weight":
	 						if (!measurements.weight) {
	 							measurements.weight = measurementsData[i]["NUMERICVALUE"];
	 						}
	 						break;
	 					case "Body Mass Index":
	 						if (!measurements.bmi) {
		 						measurements.bmi = measurementsData[i]["NUMERICVALUE"];

		 						if (measurements.bmi < 18.5) {
		 							measurements.bmirange = "underweight";
		 						} else if (measurements.bmi <= 24.9) {
		 							measurements.bmirange = "normal";
		 						} else if (measurements.bmi <= 29.9) {
		 							measurements.bmirange = "overweight";
		 						} else {
		 							measurements.bmirange = "obese";
		 						}
		 					}
	 						break;
	 					case "Systolic Blood Pressure":
	 						if (!measurements.sys) {
	 							measurements.sys = measurementsData[i]["NUMERICVALUE"];
	 						}
	 						break;
	 					case "Diastolic Blood Pressure":
	 						if (!measurements.dia) {
	 							measurements.dia = measurementsData[i]["NUMERICVALUE"];
	 						}
	 						break;
	 				}
	 			}

				return resolve(measurements);
	  		} else {
	  			return resolve(measurements);
	  		}
	  	});
	})
}

function patientLogin(url, username, password) {
	return new Promise(function(resolve, reject) {
		request.post({url: url + "login/user", json: {"UID":username,"PASS":password}}, function (error, response, body) {
			if (!error && response.statusCode == 200) {
				if (body["ResultSet Output"].length > 0) {
					resolve(body["ResultSet Output"][0]["PATIENTID"]);
				} else {
					resolve(undefined);
				}
			} else {
				return resolve(undefined);
			}
		});
	})
}

function getAge(dateString)
{
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var month = today.getMonth() - birthDate.getMonth();
    if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}

module.exports.getPatientInfo = getPatientInfo;
module.exports.getPatientMedications = getPatientMedications;
module.exports.getPatientAppointments = getPatientAppointments;
module.exports.getPatientMeasurements = getPatientMeasurements;
module.exports.patientLogin = patientLogin;
