import Config from "../config.json" assert { type: "json" };
import { BrokerProcessService } from "../process/process.service.js";
import { BrokerStatus } from "../status.type.js";

export class BiosamplesService {
  constructor(isaJson) {
    this.isaJson = isaJson;
    console.log(isaJson)
    this.processService = new BrokerProcessService();
  }

  async submit() {
    this.processService.setStatus(BrokerStatus.Running);
    return fetch(`${Config.biosamples.url}?webinjwt=${Config.biosamples.token}`, {
      method: "POST",
      body: JSON.stringify(this.isaJson),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => { this.processService.setStatus(BrokerStatus.Done); return response.json(); })
      .catch((error) => { this.processService.setStatus(BrokerStatus.Failed); throw error; });
  }
}
