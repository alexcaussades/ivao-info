class Online {
  constructor(dateIVAO) {
    this.date = new Date();
    this.dateIVAO = new Date(dateIVAO);
    this.difference = this.date.getTime() - this.dateIVAO.getTime();
    this.dateDiff = new Date(this.difference);
    this.heure = this.dateDiff.getUTCHours();
    this.minutes = this.dateDiff.getMinutes();
    this.secondes = this.dateDiff.getSeconds();
  }

  getHeure() {
    if (this.heure < 10) {
      return "0" + this.heure;
    } else {
      return this.heure;
    }
  }

  getMinutes() {
    if (this.minutes < 10) {
      return "0" + this.minutes;
    } else {
      return this.minutes;
    }
  }

  getSecondes() {
    if (this.secondes < 10) {
      return "0" + this.secondes;
    } else {
      return this.secondes;
    }
  }

  getOnline() {
    return this.getHeure() + ":" + this.getMinutes() + ":" + this.getSecondes();
  }

}

module.exports = Online;