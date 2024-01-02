import Config from "./config.json" assert { type: "json" };
import { BiosampleService } from "./biosample.service.js";

export class EnaBroker {
  constructor(isaJson) {
    this.isaJson = isaJson;
  }

  async submit() {
    const updatedIsaJson = await new BiosampleService(isaJson).updateIsaJson();
    return fetch(
      `${Config.ena.url}?webinUserName=${Config.ena.username}&webinPassword=${Config.ena.password}`,
      {
        method: "POST",
        body: updatedIsaJson,
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
  }

  mapToPathIsaJson(reciept) {
    // todo: map the reciept to the json linked here: https://gist.github.com/apriltuesday/f31df010acbeaa695dd0af4a8b8fe608#response
    return reciept;
  }
}
