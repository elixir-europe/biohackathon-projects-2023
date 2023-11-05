/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.sra.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlElementWrapper;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlProperty;
import java.util.List;
import lombok.Data;

@JsonPropertyOrder({"infoMessages", "errorMessages"})
@Data
public class Messages {
  @JsonProperty("info")
  @JacksonXmlElementWrapper(useWrapping = false)
  @JacksonXmlProperty(localName = "INFO")
  private List<String> infoMessages;

  @JsonProperty("error")
  @JacksonXmlElementWrapper(useWrapping = false)
  @JacksonXmlProperty(localName = "ERROR")
  private List<String> errorMessages;
}
