/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.sra.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlElementWrapper;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlProperty;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlRootElement;
import java.util.List;
import lombok.Data;

@JacksonXmlRootElement(localName = "RECEIPT")
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonPropertyOrder({
  "success",
  "receiptDate",
  "submissionFile",
  "analyses",
  "experiments",
  "runs",
  "samples",
  "studies",
  "projects",
  "submission",
  "messages",
  "actions"
})
@Data
public class Receipt {
  @JacksonXmlProperty(localName = "success", isAttribute = true)
  private boolean success;

  @JacksonXmlProperty(localName = "receiptDate", isAttribute = true)
  private String receiptDate;

  @JacksonXmlElementWrapper(localName = "ANALYSIS", useWrapping = false)
  @JacksonXmlProperty(localName = "ANALYSIS")
  private List<ReceiptObject> analyses;

  @JacksonXmlElementWrapper(localName = "EXPERIMENT", useWrapping = false)
  @JacksonXmlProperty(localName = "EXPERIMENT")
  private List<ReceiptObject> experiments;

  @JacksonXmlElementWrapper(localName = "RUN", useWrapping = false)
  @JacksonXmlProperty(localName = "RUN")
  private List<ReceiptObject> runs;

  @JacksonXmlElementWrapper(localName = "SAMPLE", useWrapping = false)
  @JacksonXmlProperty(localName = "SAMPLE")
  private List<ReceiptObject> samples;

  @JacksonXmlElementWrapper(localName = "STUDY", useWrapping = false)
  @JacksonXmlProperty(localName = "STUDY")
  private List<ReceiptObject> studies;

  @JacksonXmlElementWrapper(localName = "PROJECT", useWrapping = false)
  @JacksonXmlProperty(localName = "PROJECT")
  private List<ReceiptObject> projects;

  @JacksonXmlProperty(localName = "SUBMISSION")
  private ReceiptObject submission;

  @JacksonXmlProperty(localName = "MESSAGES")
  @JacksonXmlElementWrapper(useWrapping = false)
  private Messages messages;

  @JacksonXmlProperty(localName = "ACTIONS")
  @JacksonXmlElementWrapper(useWrapping = false)
  private List<String> actions;
}
