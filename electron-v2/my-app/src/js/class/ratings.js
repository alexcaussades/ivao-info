const path = require("path");

class Rating {


  constructor(rating, type, option = "text") {
    this.rating = rating;
    this.type = type;
    this.option = option;
  }

  /** 
   * @param {string} rating - Rating
   * @param {string} type - Pilot or ATC
   * @param {string} option - text or img
   * @example getRating("1", "Pilot", "text") // => "FS1"
   * getRating("1", "Pilot", "img") // => "URL IMG"
   * getRating("1", "ATC", "text") // => "AS1"
   * getRating("1", "ATC", "img") // => "URL IMG"
   */

  getRating(rating, type, option) {
    if (type == "Pilot") {
      switch (rating) {
        case 1:
          let img = path.join(
            __dirname,
            "../../../src/img/ratings/pilots/2.webp"
          );
          let grade = "FS1";
          if (option == "img") {
            return img;
          } else {
            return grade;
          }
        case 2:
         let img1 = path.join(__dirname, "../../../src/img/ratings/pilots/3.webp");
         let grade1 = "FS2";
          if (option == "img") {
            return img1;
          } else {
            return grade1;
          }
        case 3:
          let img2 = path.join(__dirname, "../../../src/img/ratings/pilots/4.webp");
          let grade2 = "FS3";
          if (option == "img") {
            return img2;
          } else {
            return grade2;
          }
        case 4:
            let img3 = path.join(__dirname, "../../../src/img/ratings/pilots/5.webp");
            let grade3 = "PP";
            if (option == "img") {
                return img3;
            } else {
                return grade3;
            }
        case 5:
            let img4 = path.join(__dirname, "../../../src/img/ratings/pilots/6.webp");
            let grade4 = "SPP";
            if (option == "img") {
                return img4;
            } else {
                return grade4;
            }
        case 6:
            let img5 = path.join(__dirname, "../../../src/img/ratings/pilots/7.webp");
            let grade5 = "CP";
            if (option == "img") {
                return img5;
            } else {
                return grade5;
            }
        case 7:
            let img6 = path.join(__dirname, "../../../src/img/ratings/pilots/8.webp");
            let grade6 = "ATP";
            if (option == "img") {
                return img6;
            } else {
                return grade6;
            }
        case 8:
            let img7 = path.join(__dirname, "../../../src/img/ratings/pilots/9.webp");
            let grade7 = "SFI";
            if (option == "img") {
                return img7;
            } else {
                return grade7;
            }
        case 9:
            let img8 = path.join(__dirname, "../../../src/img/ratings/pilots/10.webp");
            let grade8 = "CFI";
            if (option == "img") {
                return img8;
            } else {
                return grade8;
            }
        default:
          return "OBS";
      }
    } else if (type == "ATC") {
      switch (rating) {
        case 2:
            let img = path.join(__dirname, "../../../src/img/ratings/atc/2.webp");
            let grade = "AS1";
            if (option == "img") {
                return img;
            } else {
                return grade;
            }
        case 3:
            let img1 = path.join(__dirname, "../../../src/img/ratings/atc/3.webp");
            let grade1 = "AS2";
            if (option == "img") {
                return img1;
            } else {
                return grade1;
            }
        case 4:
            let img2 = path.join(__dirname, "../../../src/img/ratings/atc/4.webp");
            let grade2 = "AS3";
            if (option == "img") {
                return img2;
            } else {
                return grade2;
            }
        case 5:
            let img3 = path.join(__dirname, "../../../src/img/ratings/atc/5.webp");
            let grade3 = "ADC";
            if (option == "img") {
                return img3;
            } else {
                return grade3;
            }
        case 6:
            let img4 = path.join(__dirname, "../../../src/img/ratings/atc/6.webp");
            let grade4 = "APC";
            if (option == "img") {
                return img4;
            } else {
                return grade4;
            }
        case 7:
            let img5 = path.join(__dirname, "../../../src/img/ratings/atc/7.webp");
            let grade5 = "ACC";
            if (option == "img") {
                return img5;
            } else {
                return grade5;
            }
        case 8:
            let img6 = path.join(__dirname, "../../../src/img/ratings/atc/8.webp");
            let grade6 = "SEC";
            if (option == "img") {
                return img6;
            } else {
                return grade6;
            }
        case 9:
            let img7 = path.join(__dirname, "../../../src/img/ratings/atc/9.webp");
            let grade7 = "SAI";
            if (option == "img") {
                return img7;
            } else {
                return grade7;
            }
        case 10:
            let img8 = path.join(__dirname, "../../../src/img/ratings/atc/10.webp");
            let grade8 = "CAI";
            if (option == "img") {
                return img8;
            } else {
                return grade8;
            }
        default:
          return "OBS";
      }
    }
  }
}

module.exports = Rating;
