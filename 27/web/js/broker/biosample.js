import { biosample as Config } from "./config.json";

export class BiosampleBroker {
  constructor(isaJson) {
    this.isaJson = isaJson;
  }

  async updateIsaJson() {
    return fetch(`${Config.url}?webinjwt=${Config.token}`, {
      method: "POST",
      body: this.isaJson,
    });
  }
}

export function updateExternalLinks(){

}
