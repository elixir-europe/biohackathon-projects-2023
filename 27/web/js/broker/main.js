import { EnaBroker } from "./ena.js";
import { BiosampleBroker } from "./biosample.js";

export class Broker {
  async submit(isaJson) {
    const biosampleBroker = new BiosampleBroker(isaJson);
    const updatedIsaJson = await biosampleBroker.updateIsaJson();

    const enaBroker = new EnaBroker(updatedIsaJson);
    const reciept = await enaBroker.submit();
    const pathIsaJson = enaBroker.mapToPathIsaJson(reciept);

    console.log(pathIsaJson);
  }
}
