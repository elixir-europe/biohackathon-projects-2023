import { BrokerStatus } from "../status.type.js";

export class BrokerProcessService {
    constructor() {
        this.status = BrokerStatus.None;
        this.items = [];
    }

    addItem(item) {
        this.items.push(item);
    }

    removeItem(item) {
        this.items = this.items.filter(i => i != item);
    }

    setStatus(status) {
        this.status = status;
        const brokerEvent = new CustomEvent("broker", { detail: { status: this.status } });
        this.items.forEach((item) => { item.dispatchEvent(brokerEvent); });
    }
}