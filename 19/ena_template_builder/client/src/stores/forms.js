import { defineStore } from 'pinia'

const EXAMPLE_DATA = {
  study: [
    {
      "alias": "a_cool_study",
      "title": "a cool study",
      "study_type": "Whole Genome Sequencing",
      "new_study_type": "",
      "study_abstract": ""
    }
  ],
  experiment: [{
    "alias": "a_cool_experiment",
    "title": "cool experiment",
    "study_alias": "a_cool_study",
    "sample_alias": "a cool sample",
    "design_description": "",
    "library_name": "",
    "library_strategy": "WGS",
    "library_source": "GENOMIC",
    "library_selection": "RANDOM",
    "library_layout": "Paired",
    "insert_size": "",
    "library_construction_protocol": "",
    "platform": "ILLUMINA",
    "instrument_model": "454 GS"
  }],
  run: [{
    "alias": "my_cool_run",
    "experiment_alias": "my_cool_experiment",
    "file_name": "myrun.sra",
    "file_format": "sra"
  }],
  sample: [{
    "alias": "my_cool_sample",
    "title": "my cool sample",
    "taxon_id": "1234",
    "sample_description": "",
    "cell_type": "",
    "dev_stage": "",
    "germline": "",
    "tissue_lib": "",
    "tissue_type": "",
    "isolation_source": "",
    "lat_lon": "",
    "collected_by": "",
    "collection date": "2020-01-01",
    "geographic location (country and/or sea)": "Afghanistan",
    "geographic location (region and locality)": "",
    "identified_by": "",
    "environmental_sample": "",
    "mating_type": "",
    "sex": "",
    "lab_host": "",
    "host scientific name": "",
    "bio_material": "",
    "culture_collection": "",
    "specimen_voucher": "",
    "cultivar": "",
    "ecotype": "",
    "isolate": "",
    "sub_species": "",
    "variety": "",
    "sub_strain": "",
    "cell_line": "",
    "serotype": "",
    "serovar": "",
    "strain": ""
  }],
}

export const useFormStore = defineStore('formData', {
  state: () => ({
    'study': [],
    'experiment': [],
    'run': [],
    'sample': [],
  }),
  actions: {
    getFormData(formName) {
      if (formName) {
        return this[formName]
      }
      return {
        study: this.study,
        experiment: this.experiment,
        run: this.run,
        sample: this.sample,
      }
    },
    setFormData(formName, data) {
      this[formName] = data
    },
    loadExampleData() {
      this.study = EXAMPLE_DATA.study
      this.experiment = EXAMPLE_DATA.experiment
      this.run = EXAMPLE_DATA.run
      this.sample = EXAMPLE_DATA.sample
    }
  }
})
