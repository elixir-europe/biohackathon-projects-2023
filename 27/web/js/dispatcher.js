// import "./broker/biosample.js";
// import { EnaBroker } from "./broker/ena.js";
// import { MetabolightsBroker } from "./broker/metabolights.js";

function filterIsaJsonByRepo(jsonContent, repoName) {
  let isa_json = JSON.parse(jsonContent);
  console.log(isa_json, 'isa JSON before');
  let newStudies = isa_json.studies.map((study) => {
    let assays =  study.assays.filter(assay => {
      return assay.comments.some((comment) =>
        comment.name === "target repository" && comment.value === repoName
      );
    });
    let newStudy = study;
    newStudy.assays = assays;
    if(assays.length < 1) return;
    return newStudy;
  }).filter(s => s !== undefined);
  let new_isa_json = {...isa_json}; //clone isa_json
  new_isa_json.studies = newStudies;
  console.log(new_isa_json, 'isa JSON after');
  // debugger;
  return new_isa_json;
}

function submitIsaJson(isa_json_text) {
  // 1. Read ISA JSON
  let isa_json = JSON.parse(isa_json_text);

  // 2. dispatch to BioSamples
  const bs_broker = BiosampleBroker(isa_json);
  const isa_json_update_bs = bs_broker.updateIsaJson();

  // 4. Split the ISA Json in different target repo
  // TODO use updated isa JSON instead of the original
  const enaIsaJson = filterIsaJsonByRepo(isa_json, 'ena')

  // 5. Dispatch to ENA
  const enaBroker = EnaBroker(enaIsaJson);
  const enaReceipt = enaBroker.submit(enaIsaJson);

  // 6. Parse ENA receipt

  // 7. Dispatch partial to Metabolights
  const metaboIsaJson = filterIsaJsonByRepo(isa_json, 'metabolights');
  const metaBroker = MetabolightsBroker(metaboIsaJson);

  // 8. Parse Metabolights receipt


  // 9. Update the BioSamples record with external links to the different repos

}
