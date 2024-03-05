import Config from "../config.json" assert { type: "json" };
import { BrokerProcessService } from "../process/process.service.js";
import { BrokerStatus } from "../status.type.js";

export class EnaBroker {
  constructor(isaJson) {
    this.isaJson = isaJson;
    this.processService = new BrokerProcessService();
  }

  async submit() {
    this.processService.setStatus(BrokerStatus.Running);
    return fetch(
      `${Config.ena.url}?webinUserName=${Config.ena.username}&webinPassword=${Config.ena.password}`,
      {
        method: "POST",
        body: this.isaJson,
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
      .then((response) => { this.processService.setStatus(BrokerStatus.Done); return response.json(); })
      .catch((error) => { this.processService.setStatus(BrokerStatus.Failed); throw error; });
  }

  mapToPathIsaJson(reciept) {
    // todo: map the reciept to the json linked here: https://gist.github.com/apriltuesday/f31df010acbeaa695dd0af4a8b8fe608#response
    return reciept;
  }
}
