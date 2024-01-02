import { EnaBroker } from "./ena/ena.broker.js";
import { BrokerType } from "./broker.type.js";

export class Broker {
  async submit(isaJson, type) {
    switch (type) {
      case BrokerType.Ena:
        const enaBroker = new EnaBroker(isaJson);
        const reciept = await enaBroker.submit();
        const pathIsaJson = enaBroker.mapToPathIsaJson(reciept);

        console.log(pathIsaJson);
        break;
      case BrokerType.Metabolights:
        break;
    }
  }
}
