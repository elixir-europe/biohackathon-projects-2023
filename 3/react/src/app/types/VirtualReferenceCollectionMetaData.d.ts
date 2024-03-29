/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

/**
 * A numeric, textual value, or reference such as an IRI, that can be used to uniquely identify the object to which it is attached
 */
export type ReferenceCollectionIdentifier = string;
/**
 * A role played by a Person in the context of an entity such as an ObjectGroup, OrganisationalUnit or RecordLevel
 */
export type Creator = string;
/**
 * A role played by a Person in the context of an entity such as an ObjectGroup, OrganisationalUnit or RecordLevel
 */
export type Maintainer = string;
/**
 * Information about rights held in and over the resource
 */
export type CopyrightLicense = string;
/**
 * A person or organization owning or managing rights over the resource
 */
export type CopyrightOwner = string;
/**
 * A name given to the resource
 */
export type Title = string;
/**
 * An account of the resource
 */
export type Description = string;
/**
 * The geographic location from which objects associated with the ObjectGroup were collected, or where an Event took place
 */
export type Area = string[];
/**
 * A higher taxon (e. g., a genus, family, or order) at the level of the genus or higher, that covers all taxa that are the primary subject of the resource (which may be a media item or a collection)
 */
export type IncludedTaxaDescription = string;
/**
 * A language of the resource
 */
export type Language = string;
/**
 * Date on which the resource was changed
 */
export type LastUpdate = string;

export interface VirtualReferenceCollectionMetaData {
  referenceCollectionID: ReferenceCollectionIdentifier;
  creator?: Creator;
  maintainer?: Maintainer;
  copyrightLicense?: CopyrightLicense;
  copyrightOwner?: CopyrightOwner;
  title: Title;
  description?: Description;
  area?: Area;
  includedTaxaDescription?: IncludedTaxaDescription;
  language?: Language;
  lastUpdate: LastUpdate;
  [k: string]: unknown;
}
