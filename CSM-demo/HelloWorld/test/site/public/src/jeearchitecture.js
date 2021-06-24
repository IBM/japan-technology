var generalInfo = {
  title: "Software Architecture",
  subtitle: "An Open Source Case Study",
  description: "This is an experimental project, and open source reference architecture for modernizing a traditional data system, with modern cloud technology.",
  technologies: ["RH OpenShift Kubernetes Service","RH OpenShift Source to Image", "Compose for MySQL", "OpenLiberty"],
  pattern: ""
}

var modernAppInfo = {
  title: "Writing a Modern Web UI using existing System Z application",
  subtitle: "Agile UI development",
  description: "In this pattern, we show how to rapidly prototype a new web UI built on Node JS, using HTML5 technology, surfacing traditional data in fresh ways. ",
  technologies: ["IBM Z", "IBM Cloud Private", "IBM API Connect"],
  pattern: ""
}

var analyticsInfo = {
  title: "A health data analytics app that integrates with historic data",
  subtitle: "Creating a full stack big data app",
  description: "In this pattern, we build a full stack containerized application that delves into big data, using Node JS and the Watson Data Platform.",
  technologies: ["IBM Z", "IBM Cloud Kubernetes Service", "IBM API Connect"],
  pattern: ""
}

var syntheaInfo = {
  title: "Conditioning data on ZOS",
  subtitle: "Data preparation from Synthea",
  description: "In this pattern, we look at tips and tricks for conditioning big sets of generated data for storage on Db2/zOS.",
  technologies: ["IBM Z", "IBM Db2"],
  pattern: ""
}

var mlInfo = {
  title: "Machine learning with big data and zOS",
  subtitle: "Jupiter Notebooks and zOS",
  description: "In this pattern, we look at tips and tricks for working with data science and Db2/zOS.",
  technologies: ["IBM Z", "IBM Db2"],
  pattern: ""
}

var apiInfo = {
  title: "Connecting zOS with API Connect",
  subtitle: "Jupiter Notebooks and zOS",
  description: "In this pattern, we show how to liberate mainframe data with hybrid integration.",
  technologies: ["IBM Z", "IBM Db2"],
  pattern: ""
}

var chosenpattern = null;

var c = document.getElementById("canvas");

var AQUA = "#00ABC0";
var NAVY = "#0F4C81";
var AQUALIGHT = "#99DDE5";
var EXTRALIGHT = "#CCEEF2";
var HIGHLIGHT = "#FF7CA8";
var HIGHFILL = "#FFE2EC";
var HIGHCOMPONENTFILL = "#FFB6CF";

var LOWFILL = "#e5f6f8";
var LOWSTROKE = "#cceef2";
var LOWFONT = "#99dde5";

var HIGHLIGHTED = 0;
var DIMMED = 1;
var NORMAL = 2;

var DIMMEDORANGE = "fef3ee";

if (c != undefined) {
  var ctx = c.getContext("2d");
  drawDefault();
  ctx.lineWidth = 1;
}


function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
  ctx.stroke();
  ctx.lineWidth = 1.5;
  ctx.fillStyle = "#0F4C81";
  ctx.font = 'bold 12px sans-serif';
  ctx.fillText("Classic Patient System", 5, 20);
  ctx.fillText("Modernized on Cloud", 435, 20);
}

function drawDefault(source) {
  clearCanvas();
  displayInfo(generalInfo)



  drawModernized(HIGHLIGHTED)
  drawMonolith(DIMMED)

  // drawContainerServicePattern(NORMAL);
}

function drawModernized(state) {
  drawContainer("OpenShift Kube S2I", state);
  drawDB(state);
  drawLiberty("OpenShift Kubernetes Service", state)
  drawConnections(state);
}

function drawMonolith(state) {
  drawWebsphere(state);
  drawDB2(state);
  drawSynthea(state);
  drawClassicConnections(state);
}

function drawDB(state) {
  var label = "IBM Cloud";
  drawSubsystem(355, 310, 200, 100, label, state);
  drawComposeForMySQL(state);
}

function drawS2I() {
  drawContainer("OpenShift Kube S2I", HIGHLIGHTED);
  drawLiberty("OpenShift Kubernetes Service", DIMMED);
  drawMonolith(DIMMED);
  drawConnections(DIMMED);
  drawDB(DIMMED);
}

function drawOpenShiftLiberty() {
  drawContainer("OpenShift Kube S2I", DIMMED);
  drawLiberty("OpenShift Kubernetes Service", HIGHLIGHTED);
  drawMonolith(DIMMED);
  drawConnections(HIGHLIGHTED);
  drawDB(HIGHLIGHTED)
}

function drawClassicReference() {
  drawMonolith(HIGHLIGHTED);
  drawModernized(DIMMED);
}

function drawModernizedReference() {
  drawMonolith(DIMMED);
  drawModernized(HIGHLIGHTED);
}

function openpattern() {

  if (chosenpattern != null) {

    switch (chosenpattern.id) {

      case 'patientrecords':
        window.open('https://developer.ibm.com/patterns/transform-load-big-data-csv-files-Db2-zos-database/');
        break;

      case 'apimanagement':
        break;

      case 'frontend':
        window.open('https://github.com/IBM/Example-health-patient-records');
        break;

      case 'ml':
        window.open('https://developer.ibm.com/patterns/machine-learning-using-synthesized-patient-health-records/');
        break;

      case 'analytics':
        window.open('https://github.com/IBM/Example-health-analytics');
        break;

      default:
        break;
    }
  }
}


function drawContainerServicePattern(source) {

  if (chosenpattern == null || chosenpattern != source) {

    if (chosenpattern != null) {
      clearSelectedborder(chosenpattern);
    }

    chosenpattern = source;

    clearCanvas();
    console.log('analytics app');
    drawContainer("OpenShift Kube S2I", HIGHLIGHTED);
    drawNodeApp("Kubernetes", DIMMED);

    drawPatientRecords(HIGHLIGHTED);
    drawCobolProcessing(HIGHLIGHTED);

    drawSynthea(DIMMED);
    displayInfo(analyticsInfo);

    ctx.strokeStyle = HIGHLIGHT;
    ctx.beginPath();

    ctx.moveTo(175, 240);
    ctx.lineTo(240, 220);

    /* API CONNECT TO ZOS CONNECT */

    connectAnalytics();

    ctx.stroke();

    setSelectedborder(source);

  } else {
    clearSelectedborder(source);

    chosenpattern = null;
    drawDefault();
  }
}

function setSelectedborder(source) {
  source.style.border = "1px solid " + HIGHLIGHT;
}

function clearSelectedborder(source) {
  source.style.border = "1px solid white";
}

function drawConnections(state) {
  ctx.strokeStyle = AQUA;

  switch (state) {

    case HIGHLIGHTED:
      ctx.fillStyle = HIGHCOMPONENTFILL;
      ctx.strokeStyle = HIGHLIGHT

      break;

    case NORMAL:
      ctx.fillStyle = AQUA;
      break;

    case DIMMED:
      ctx.fillStyle = LOWFILL;
      ctx.strokeStyle = LOWSTROKE;
      break;

    default:
      ctx.fillStyle = AQUALIGHT;
      break;
  }

  ctx.beginPath();
  // connectAPItoPatientUI();
  // connectAPItoZOS();
  // connectAnalytics();
  connectPatientsToBL();
  connectBLToDB();

  // connectDataPlatform();
  ctx.stroke();
}

function drawClassicConnections(state) {
  ctx.strokeStyle = AQUA;

  switch (state) {

    case HIGHLIGHTED:
      ctx.fillStyle = HIGHCOMPONENTFILL;
      ctx.strokeStyle = HIGHLIGHT
      break;

    case NORMAL:
      ctx.fillStyle = AQUALIGHT;
      break;

    case DIMMED:
      ctx.fillStyle = LOWFILL;
      ctx.strokeStyle = LOWSTROKE;
      break;

    default:
      ctx.fillStyle = AQUALIGHT;
      break;
  }

  ctx.beginPath();
  connectSyntheaToDB();
  connectWebSphereToDB();
  ctx.stroke();
}

function connectPatientsToBL() {
  ctx.moveTo(450, 140);
  ctx.lineTo(450, 190);
}

function connectBLToDB() {
  ctx.moveTo(450, 270);
  ctx.lineTo(450, 320);
}

function connectAPItoZOS() {
  ctx.moveTo(175, 240);
  ctx.lineTo(240, 220);
}

function connectAPItoPatientUI() {
  ctx.moveTo(240, 140);
  ctx.lineTo(170, 120);
}

function connectSyntheaToDB() {
  ctx.moveTo(100, 260);
  ctx.lineTo(100, 310);
}

function connectWebSphereToDB() {
  ctx.moveTo(100, 180);
  ctx.lineTo(100, 230);
}

function connectDataPlatform() {
  ctx.moveTo(385, 410);
  ctx.lineTo(175, 360);
}

function connectAnalytics() {
  ctx.moveTo(320, 220);
  ctx.lineTo(385, 240);
}

function drawPatientRecords(state) {
  drawComponent(25, 340, "Patient Records - Db2", state);
}

function drawSynthea(state) {
  drawIsland(5, 300, 200, 50, "Synthea - Data Generation", state);
}

function drawDB2(state) {
  drawIsland(5, 220, 200, 50, "DB2 - Patient Data", state);
}

function drawAPIConnect(state) {
  drawIsland(230, 130, 100, 100, "API Connect", state);
}

function drawCobolProcessing(state) {
  drawComponent(25, 280, "Cobol processing", state);
}

function drawAnalyticsUI(state) {
  drawComponent(375, 90, "Patient UI - Node JS", state);
}

function drawAnalyticsApp(state) {
  drawComponent(375, 150, "Analytics App - Node JS", state);
}

function drawAnalyticsAPI(state) {
  drawComponent(375, 210, "Analytics API - Node JS", state);
}

function drawDataLake(state) {
  drawComponent(375, 220, "Business Logic - Liberty", state);
}

function drawComposeForMySQL(state) {
  drawComponent(375, 350, "Compose for MySQL", state);
}

function displayInfo(info) {

  var title = document.getElementById("archtitle");
  title.innerHTML = info.title;

  // var subtitle = document.getElementById("subtitle");
  // subtitle.innerHTML = info.subtitle;

  var description = document.getElementById("description");
  description.innerHTML = info.description;

  var techlist = document.getElementById("techlist");
  techlist.innerHTML = ""

  info.technologies.forEach(function(technology) {

    var li = document.createElement('li');
    li.innerHTML = technology;
    techlist.appendChild(li);
  })
}


function drawIsland(x, y, width, height, label, state) {

  switch (state) {

    case HIGHLIGHTED:
      ctx.fillStyle = HIGHCOMPONENTFILL;
      ctx.strokeStyle = HIGHLIGHT

      break;

    case NORMAL:
      ctx.fillStyle = AQUALIGHT;
      break;

    case DIMMED:
      ctx.fillStyle = LOWFILL;
      ctx.strokeStyle = LOWSTROKE;
      break;

    default:
      ctx.fillStyle = AQUALIGHT;
      break;
  }

  ctx.fillRect(x, y, width, height);
  ctx.strokeRect(x, y, width, height);
  if (state === DIMMED) {
    ctx.fillStyle = LOWFONT
  } else {
    ctx.fillStyle = NAVY
  }
  ctx.font = 'bold 11px sans-serif';
  ctx.fillText(label, x + 10, y + height / 1.8);
}

function drawComponent(x, y, label, state) {

  var height = 40;
  var width = 160;

  switch (state) {

    case HIGHLIGHTED:
      ctx.fillStyle = HIGHCOMPONENTFILL;
      ctx.strokeStyle = HIGHLIGHT;
      break;

    case NORMAL:
      ctx.fillStyle = AQUALIGHT;
      break;

    case DIMMED:
      ctx.fillStyle = LOWFILL;
      break;

    default:
      ctx.fillStyle = AQUALIGHT;
      break;
  }

  ctx.fillRect(x, y, width, height);
  ctx.strokeRect(x, y, width, height);
  if (state === DIMMED) {
    ctx.fillStyle = LOWFONT
  } else {
    ctx.fillStyle = NAVY
  }
  ctx.font = 'bold 11px sans-serif';
  ctx.fillText(label, x + 10, y + 25);
}

function drawNodeApp(label, state) {
  drawSubsystem(5, 50, 200, 100, label, state);
  drawComponent(25, 90, "Patient UI - Node JS", state);
}

function drawContainer(label, state) {
  drawSubsystem(355, 50, 200, 100, label, state);
  drawAnalyticsUI(state)

}

function drawLiberty(label, state) {
  drawSubsystem(355, 180, 200, 100, label, state);
  drawDataLake(state);
}

function setColors(state) {

  switch (state) {

    case HIGHLIGHTED:
      ctx.fillStyle = HIGHFILL;
      ctx.strokeStyle = HIGHLIGHT
      break;

    case NORMAL:
      ctx.fillStyle = EXTRALIGHT;
      ctx.strokeStyle = AQUA;
      break;

    case DIMMED:
      ctx.fillStyle = LOWFILL;
      ctx.strokeStyle = LOWSTROKE;
      break;

    default:
      ctx.fillStyle = EXTRALIGHT;
      ctx.strokeStyle = AQUA
      break;
  }
}

function drawSubsystem(x, y, width, height, label, state) {

  setColors(state);

  var cs = ctx.strokeStyle;

  ctx.fillRect(x, y, width, height);
  fillStripes(ctx, x, y, width, height)
  ctx.strokeStyle = cs;
  ctx.strokeRect(x, y, width, height);

  if (state === DIMMED) {
    ctx.fillStyle = LOWFONT
  } else {
    ctx.fillStyle = NAVY
  }

  ctx.font = 'bold 11px sans-serif';
  ctx.fillText(label, x + 20, y + 25);
}

function drawWebsphere(state) {
  var label = "Websphere";
  drawSubsystem(5, 50, 200, 140, label, state);
  drawComponent(25, 90, "Patient UI - JSP", state);
  drawComponent(25, 130, "Business Logic - JEE", state);
}
