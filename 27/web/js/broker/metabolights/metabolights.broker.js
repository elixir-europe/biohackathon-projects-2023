import Config from "../config.json" assert { type: "json" };
import { BrokerProcessService } from "../process/process.service.js";
import { BrokerStatus } from "../status.type.js";
import { Data } from "./matabolights.data.js";

export class MetabolightsBroker {
    constructor(isaJson) {
        this.isaJson = isaJson;
        this.processService = new BrokerProcessService();
    }

    async submit() {
        this.processService.setStatus(BrokerStatus.Running);
        return new Promise((resolve) => resolve(Data))
            .then((response) => { this.processService.setStatus(BrokerStatus.Done); return response; })
            .catch((error) => { this.processService.setStatus(BrokerStatus.Failed); throw error; });
    }
}
