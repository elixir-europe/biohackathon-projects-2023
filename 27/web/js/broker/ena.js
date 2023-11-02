import { ena } from "./config.json";

class EnaActions {
  static Add = new EnaActions("ADD");
  static Modify = new EnaActions("MODIFY");
  static Validate = new EnaActions("VALIDATE");
  static Cancel = new EnaActions("CANCEL");
  static Receipt = new EnaActions("RECEIPT");
  static Hold = new EnaActions("HOLD");
  static Release = new EnaActions("RELEASE");

  constructor(name) {
    this.name = name;
  }

  get list() {
    return [
      EnaActions.Add,
      EnaActions.Modify,
      EnaActions.Validate,
      EnaActions.call,
      EnaActions.Cancel,
      EnaActions.Receipt,
      EnaActions.Hold,
      EnaActions.Release,
    ];
  }
}

class EnaElements {
  static Study = new EnaElements("STUDY");
  static Project = new EnaElements("PROJECT");
  static Sample = new EnaElements("SAMPLE");
  static Experiment = new EnaElements("EXPERIMENT");
  static Run = new EnaElements("RUN");
  static Analysis = new EnaElements("ANALYSIS");

  constructor(name) {
    this.name = name;
  }

  get list() {
    return [
      EnaElements.Study,
      EnaElements.Project,
      EnaElements.Sample,
      EnaElements.Experiment,
      EnaElements.Run,
      EnaElements.Analysis,
    ];
  }
}

export class EnaBroker {
  constructor(isaJson) {
    this.isaJson = isaJson;
  }

  async submit() {
    return fetch(ena.url, {
      body: { action: EnaActions.Add, isaJson: this.isaJson },
      headers: {},
    });
  }

  parseReciept(xmlReciept) {
    function getAccession(element) {
      element.getAttribute("accession");
    }

    let responseJson = {
      targetRepository: "ena",
      receipt: xmlReciept,
      accessions: [],
    };

    const parser = new DOMParser();
    const reciept = parser
      .parseFromString(xmlReciept)
      .getElementsByTagName("RECEIPT")
      .item(0);
    const success =
      String(reciept.getAttribute("success")).toLowerCase() === "true";
    if (!success) throw "Submission is failed.";

    for (const element of reciept.children) {
      let accession = {
        path: [],
        value: getAccession(element),
      };
      switch (element.nodeName) {
        case EnaElements.Study.name:
          accession.path = [];
          break;
        case EnaElements.Project.name:
          accession.path = [];
          break;
        case EnaElements.Sample.name:
          accession.path = [];
          break;
        case EnaElements.Experiment.name:
          accession.path = [];
          break;
        case EnaElements.Analysis.name:
          accession.path = [];
          break;
      }
      responseJson.accessions.push(accession);
    }
  }

  updateIsaJson() {}
}
