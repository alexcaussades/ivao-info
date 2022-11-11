const { shell, ipcRenderer } = require("electron");
const { Notification } = require("electron");
const os = require("os");

const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";

//recuperer le données du formulaire en reception des donées via submit de la test.html

ipcRenderer.on("plateform", (event, value) => {
  console.log(value);
});