/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.biosamples.service;

import com.elixir.biohackaton.ISAToSRA.model.IsaJson;
import com.elixir.biohackaton.ISAToSRA.model.Study;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class BioSampleSubmissionCreator {
  @Autowired private BioSamplesSubmitter bioSamplesSubmitter;
  @Autowired private ObjectMapper objectMapper;

  public void performSubmissionToBioSamplesAndEna(ApplicationArguments args) throws Exception {
    String webinToken;
    String isaJsonFilePath;

    objectMapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);

    // Mandatory command line arguments
    if (args.getOptionNames().contains("webinJwt")) {
      webinToken = args.getOptionValues("webinJwt").iterator().next();
    } else {
      throw new RuntimeException("Webin Authentication Token is not provided");
    }

    if (args.getOptionNames().contains("isaJsonFilePath")) {
      isaJsonFilePath = args.getOptionValues("isaJsonFilePath").iterator().next();
    } else {
      throw new RuntimeException("ISA-Json file is not provided");
    }

    final Path path = Paths.get(isaJsonFilePath);
    final List<String> lines = Files.readAllLines(path);
    final String isaJsonString = String.join("\n", lines);
    final IsaJson isaJson = this.objectMapper.readValue(isaJsonString, IsaJson.class);
    final List<Study> studies = getStudies(isaJson);

    this.bioSamplesSubmitter.createBioSamples(studies, webinToken);

    System.out.println(
        this.objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(isaJson));
  }

  public List<Study> getStudies(final IsaJson isaJson) {
    try {
      return isaJson.getInvestigation().getStudies();
    } catch (final Exception e) {
      log.info("Failed to parse ISA JSON and get studies", e);
    }

    return null;
  }
}
