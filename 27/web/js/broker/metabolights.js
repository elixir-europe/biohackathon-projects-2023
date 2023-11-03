import { metabolights as Config } from "./config.json"

export class MetabolightsBroker {
  constructor(isaJson) {
    this.isaJson = isaJson;
  }

  async submit() {
    return fetch(
      `${Config.url}?userName=${Config.username}&password=${Config.password}`,
      {
        method: "POST",
        body: this.isaJson,
      }
    );
  }
}
