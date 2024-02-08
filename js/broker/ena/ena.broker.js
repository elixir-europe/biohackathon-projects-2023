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

export function enaSubmit(name, password, json){

// Assuming you have the file data in a variable named jsonData
// Replace 'jsonData' with your actual variable holding the JSON data



fetch('https://a.cplantbox.com/isaena/submit?webinUserName='+name+'&webinPassword='+password, {
  method: 'POST',
  //mode: 'cors',
  headers: {
    
    'Content-Type': 'application/json',
    'accept': '*/*'
  },
  body: JSON.stringify(json)
})
.then((response) => response.text())
  // if (!response.ok) {
  //   throw new Error('Network response was not ok');
  // }
 

.then(data => {
  console.log('Success: ', data);
  enaReturn = data;
  document.getElementById("enaStatus").innerText="Returned";
  document.getElementById("enaText").innerText=enaReturn;
      document.getElementById("status_modal_button").click();
  // Handle the response data here
})
.catch(error => {
  console.error('Error:', error);
  // Handle errors here
});

}
window.enaSubmit = enaSubmit;
