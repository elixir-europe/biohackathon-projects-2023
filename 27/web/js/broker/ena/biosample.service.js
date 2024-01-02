import Config from "./config.json" assert { type: "json" };

export class BiosampleService {
  constructor(isaJson) {
    this.isaJson = isaJson;
  }

  async updateIsaJson() {
    return fetch(`${Config.biosample.url}?webinjwt=${Config.biosample.token}`, {
      method: "POST",
      body: JSON.stringify(this.isaJson),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }
}
