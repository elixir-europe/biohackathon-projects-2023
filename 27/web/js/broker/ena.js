import { ena as Config } from "./config.json";

export class EnaBroker {
  constructor(isaJson) {
    this.isaJson = isaJson;
  }

  async submit() {
    return fetch(
      `${Config.url}?webinUserName=${Config.username}&webinPassword=${Config.password}`,
      {
        method: "POST",
        body: this.isaJson,
      }
    );
  }

  mapToPathIsaJson(reciept) {}
}
