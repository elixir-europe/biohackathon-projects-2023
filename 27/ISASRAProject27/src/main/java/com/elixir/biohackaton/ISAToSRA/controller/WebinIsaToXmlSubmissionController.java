/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.controller;

import static org.springframework.http.MediaType.APPLICATION_JSON_VALUE;
import static org.springframework.http.MediaType.APPLICATION_XML_VALUE;

import com.elixir.biohackaton.ISAToSRA.biosamples.service.BioSamplesAccessionsParser;
import com.elixir.biohackaton.ISAToSRA.model.Investigation;
import com.elixir.biohackaton.ISAToSRA.model.IsaJson;
import com.elixir.biohackaton.ISAToSRA.model.Study;
import com.elixir.biohackaton.ISAToSRA.sra.service.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import lombok.extern.slf4j.Slf4j;
import org.dom4j.Document;
import org.dom4j.DocumentHelper;
import org.dom4j.Element;
import org.dom4j.io.OutputFormat;
import org.dom4j.io.XMLWriter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
public class WebinIsaToXmlSubmissionController {
  @Autowired private BioSamplesAccessionsParser bioSamplesAccessionsParser;

  @Autowired private WebinStudyXmlCreator webinStudyXmlCreator;

  @Autowired private WebinExperimentXmlCreator webinExperimentXmlCreator;

  @Autowired private WebinProjectXmlCreator webinProjectXmlCreator;

  @Autowired private WebinRunXmlCreator webinRunXmlCreator;

  @Autowired private WebinHttpSubmissionService webinHttpSubmissionService;

  @Autowired private ObjectMapper objectMapper;

  @Autowired private ReceiptConversionService receiptConversionService;

  @ApiResponses(
      value = {
        @ApiResponse(responseCode = "200", description = "Ok"),
        @ApiResponse(responseCode = "401", description = "Unauthorized"),
        @ApiResponse(responseCode = "403", description = "Forbidden"),
        @ApiResponse(responseCode = "400", description = "Bad request"),
        @ApiResponse(responseCode = "408", description = "Request Timeout"),
        @ApiResponse(responseCode = "415", description = "Unsupported media type")
      })
  @PostMapping(
      value = "/submit",
      consumes = {APPLICATION_JSON_VALUE, APPLICATION_XML_VALUE})
  public String performSubmissionToEna(
      @RequestBody final String submissionPayload,
      @RequestParam(value = "webinUserName") String webinUserName,
      @RequestParam(value = "webinPassword") String webinPassword)
      throws Exception {
    if (webinUserName == null) {
      throw new RuntimeException("Webin Authentication username is not provided");
    }

    if (webinPassword == null) {
      throw new RuntimeException("Webin Authentication password is not provided");
    }

    final IsaJson isaJson = this.objectMapper.readValue(submissionPayload, IsaJson.class);
    final List<Study> studies = getStudies(isaJson);
    final Map<String, String> typeToBioSamplesAccessionMap =
        this.bioSamplesAccessionsParser.parseIsaFileAndGetBioSampleAccessions(
            studies, new HashMap<>());

    final Document document = DocumentHelper.createDocument();
    final Element webinElement = startPreparingWebinV2SubmissionXml(document);
    final String randomSubmissionIdentifier = String.valueOf(Math.random());

    this.webinStudyXmlCreator.createENAStudySetElement(
        webinElement, studies, randomSubmissionIdentifier);

    final Map<Integer, String> experimentSequenceMap =
        this.webinExperimentXmlCreator.createENAExperimentSetElement(
            typeToBioSamplesAccessionMap, webinElement, studies, randomSubmissionIdentifier);

    this.webinRunXmlCreator.createENARunSetElement(
        webinElement, studies, experimentSequenceMap, randomSubmissionIdentifier);
    this.webinProjectXmlCreator.createENAProjectSetElement(
        webinElement, getInvestigation(isaJson), randomSubmissionIdentifier);

    final OutputFormat format = OutputFormat.createPrettyPrint();
    final XMLWriter writer = new XMLWriter(System.out, format);

    writer.write(document);

    final String receiptXml =
        webinHttpSubmissionService.performWebinSubmission(
            webinUserName, document.asXML(), webinPassword);

    return receiptConversionService.convertReceiptXmlToJson(receiptXml);
  }

  public List<Study> getStudies(final IsaJson isaJson) {
    try {
      return isaJson.getInvestigation().getStudies();
    } catch (final Exception e) {
      log.info("Failed to parse ISA JSON and get studies", e);
    }

    return null;
  }

  public Investigation getInvestigation(final IsaJson isaJson) {
    try {
      return isaJson.getInvestigation();
    } catch (final Exception e) {
      log.info("Failed to parse ISA JSON and get studies", e);
    }

    return null;
  }

  private static Element startPreparingWebinV2SubmissionXml(Document document) {
    final Element webinElement = document.addElement("WEBIN");
    final Element submissionElement = webinElement.addElement("SUBMISSION");
    final Element actionsElement = submissionElement.addElement("ACTIONS");
    final Element actionElement = actionsElement.addElement("ACTION");

    actionElement.addElement("ADD");

    return webinElement;
  }
}
