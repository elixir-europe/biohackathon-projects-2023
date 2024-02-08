function metabolightsSubmit(input_json) {
    // const rawResponse = await fetch('https://httpbin.org/post', {
    //   method: 'POST',
    //   headers: {
    //     'Accept': 'application/json',
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify({a: 1, isaJson: input_json})
    // });

    // const response = await rawResponse.json();
    
    // console.log(response);
    // return response

    const success=1;
    const data= {
      "targetRepository": "ena",
      "receipt": {"a":"b"},
      "accessions": [
         {
            "path": [{"key": "investigation"}],
            "value": "PRJEB100893"
         },
         {
            "path": [
               {"key": "investigation"}, 
               {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}}
           ],
            "value": "ERP201308"
         },
         {
           "path": [
               {"key": "investigation"}, 
               {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}},
               {"key": "assays", "where": {"key": "@id", "value": "#assay/18_20_21"}}
           ],
           "value": "ERR9668871"
         },
         {
           "path": [
               {"key": "investigation"}, 
               {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}},
               {"key": "assays", "where": {"key": "@id", "value": "#assay/18_20_21"}},
               {"key": "materials"},
               {"key": "otherMaterials", "where": {"key": "@id", "value": "#other_material/332"}}
           ],
           "value": "ERX9222846"
         },
         {
           "path": [
               {"key": "investigation"}, 
               {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}},
               {"key": "assays", "where": {"key": "@id", "value": "#assay/18_20_21"}},
               {"key": "materials"},
               {"key": "otherMaterials", "where": {"key": "@id", "value": "#other_material/333"}}
           ],
           "value": "ERX9222847"
         }
      ]
   };
    return new Promise((resolve, reject) => {
        setTimeout(() => {
          if (success) {
            resolve(data);
            document.getElementById("biosamplesloading").className="spinner-border text-primary d-none";
            
            setTimeout(() => {
              document.getElementById("ENAloading").className="spinner-border text-primary d-none";

              setTimeout(() => {

                document.getElementById("metabolightsloading").className="spinner-border text-primary d-none";

              },3000)

            },3000)


          } else {
            reject('There was a problem with the server, please try again.');
          }
        }, 2000);
      });
  }


