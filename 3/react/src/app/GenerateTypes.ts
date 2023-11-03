/* Import Dependencies */
import { writeFileSync } from 'fs'
import { compileFromFile } from "json-schema-to-typescript";
import { resolve } from 'path';


/* Media */
const Media = async () => {
    writeFileSync('src/app/types/Media.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'media.json'), {}));
}

Media();

/* Occurrence */
const Occurrence = async () => {
    writeFileSync('src/app/types/Occurrence.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'occurrence.json'), {}));
}

Occurrence();

/* Organism */
const Organism = async () => {
    writeFileSync('src/app/types/Organism.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'organism.json'), {}));
}

Organism();

/* Taxon Name */
const TaxonName = async () => {
    writeFileSync('src/app/types/TaxonName.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'taxonName.json'), {}));
}

TaxonName();

/* Media */
const Taxon = async () => {
    writeFileSync('src/app/types/Taxon.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'taxon.json'), {}));
}

Taxon();

/* Virtual Reference Collection Metadata */
const VirtualReferenceCollectionMetaData = async () => {
    writeFileSync('src/app/types/VirtualReferenceCollectionMetaData.d.ts', await compileFromFile(resolve(
        __dirname, '../sources/dataModel', 'virtualReferenceCollectionMetaData.json'
    ), {}));
}

VirtualReferenceCollectionMetaData();

/* Virtual Reference Collection */
const VirtualReferenceCollection = async () => {
    writeFileSync('src/app/types/VirtualReferenceCollection.d.ts', await compileFromFile(resolve(__dirname, '../sources/dataModel', 'virtualReferenceCollection.json'), {}));
}

VirtualReferenceCollection();