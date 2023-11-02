/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.sra.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlElementWrapper;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlProperty;
import lombok.Data;

@JsonPropertyOrder({
  "alias",
  "accession",
  "status",
  "centerName",
  "holdUntilDate",
  "externalAccession"
})
@Data
public class ReceiptObject {

  @JsonPropertyOrder({"accession", "type"})
  @JsonIgnoreProperties(ignoreUnknown = true)
  @Data
  public static class ExternalAccession {
    @JacksonXmlProperty(localName = "accession", isAttribute = true)
    private String id;

    @JacksonXmlProperty(localName = "type", isAttribute = true)
    private String db;
  }

  @JacksonXmlProperty(localName = "alias", isAttribute = true)
  private String alias;

  @JacksonXmlProperty(localName = "accession", isAttribute = true)
  private String accession;

  @JacksonXmlProperty(localName = "status", isAttribute = true)
  private String status;

  @JacksonXmlProperty(localName = "centerName", isAttribute = true)
  private String centerName;

  @JacksonXmlProperty(localName = "holdUntilDate", isAttribute = true)
  private String holdUntilDate;

  @JacksonXmlProperty(localName = "EXT_ID")
  @JacksonXmlElementWrapper(useWrapping = false)
  private ExternalAccession externalAccession;
}
