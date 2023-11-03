/* Import Dependencies */
import { writeFileSync } from 'fs'
import { compileFromFile } from "json-schema-to-typescript";
import { resolve } from 'path';


/* Media */
const Media = async () => {
    writeFileSync('./types/Media.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'media.json'), {}));
}

Media();

/* Occurrence */
const Occurrence = async () => {
    writeFileSync('./types/Occurrence.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'occurrence.json'), {}));
}

Occurrence();

/* Organism */
const Organism = async () => {
    writeFileSync('./types/Organism.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'organism.json'), {}));
}

Organism();

/* Taxon Name */
const TaxonName = async () => {
    writeFileSync('./types/TaxonName.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'taxonName.json'), {}));
}

TaxonName();

/* Media */
const Taxon = async () => {
    writeFileSync('./types/Taxon.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'taxon.json'), {}));
}

Taxon();

/* Virtual Reference Collection Metadata */
const VirtualReferenceCollectionMetaData = async () => {
    writeFileSync('./types/VirtualReferenceCollectionMetaData.d.ts', await compileFromFile(resolve(
        __dirname, '../sources/dataModel', 'virtualReferenceCollectionMetaData.json'
    ), {}));
}

VirtualReferenceCollectionMetaData();

/* Virtual Reference Collection */
const VirtualReferenceCollection = async () => {
    writeFileSync('./types/VirtualReferenceCollection.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'virtualReferenceCollection.json'), {}));
}

VirtualReferenceCollection();