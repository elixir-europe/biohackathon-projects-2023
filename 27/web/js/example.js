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
    const data= {accession:{path:["1", "2", "3"]}};
    return new Promise((resolve, reject) => {
        setTimeout(() => {
          if (success) {
            resolve(data);
          } else {
            reject('There was a problem with the server, please try again.');
          }
        }, 2000);
      });
  }


