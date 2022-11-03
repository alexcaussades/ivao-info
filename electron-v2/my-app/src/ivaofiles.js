const axios = require("axios");
const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";

//reupere les données de l'api
function ivaoDataAtcCallsing(value) {
  if (!value) return console.error("Manque Information Plateforme");
  axios({
    method: "get",
    url: dataIvao,
    responseType: "json",
  }).then(function (response) {
    response.data.clients.atcs.forEach((atc) => {
      if (atc.callsign == value) {
        console.log(atc.callsign);
      } else {
        //sortie du console.log en 1 resultat afficher
        return;
      }
    });
  });
}

// search atc callsign jocker string
function ivaoDataAtcCallsingJocker(value) {
  if (!value) return console.error("Manque Information Plateforme");
  axios({
    method: "get",
    url: dataIvao,
    responseType: "json",
  }).then(function (response) {
    response.data.clients.atcs.forEach((atc) => {
      if (atc.callsign.includes(value)) {
         let result = atc.callsign;
          return result;
      } else {
        //sortie du console.log en 1 resultat afficher
        return;
      }
    });
  });
}

// recherche des pilotes par postion atc aux depart de la plateforme
function searchPilotByAtcDeparture(value) {
  if (!value) return console.error("Manque Information Plateforme");
  axios({
    method: "get",
    url: dataIvao,
    responseType: "json",
  }).then(function (response) {
    response.data.clients.pilots.forEach((pilot) => {
      if (pilot.flightPlan.departureId == value) {
        console.log(
          pilot.callsign +
            " | " +
            pilot.flightPlan.level +
            " | " +
            pilot.flightPlan.aircraft.icaoCode
        );
      } else {
        //sortie du console.log en 1 resultat afficher
        return;
      }
    });
  });
}

//recherche des pilotes par position atc aux arrivé de la plateforme
function searchPilotByAtcArrival(value) {
  if (!value) return console.error("Manque Information Plateforme");
  axios({
    method: "get",
    url: dataIvao,
    responseType: "json",
  }).then(function (response) {
    response.data.clients.pilots.forEach((pilot) => {
      if (pilot.flightPlan.arrivalId == value) {
        console.log(
          pilot.callsign +
            " | " +
            pilot.flightPlan.level +
            " | " +
            pilot.flightPlan.aircraft.icaoCode
        );
      } else {
        //sortie du console.log en 1 resultat afficher
        return;
      }
    });
  });
}


module.exports = {
  ivaoDataAtcCallsing,
  ivaoDataAtcCallsingJocker,
  searchPilotByAtcDeparture,
  searchPilotByAtcArrival,
};
