/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.biosamples.service;

import com.elixir.biohackaton.ISAToSRA.model.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class BioSamplesAccessionsParser {
  public static final String CHARACTERISTIC_CATEGORY_ACCESSION =
      "#characteristic_category/accession";

  public Map<String, String> parseIsaFileAndGetBioSampleAccessions(
      final List<Study> studies, Map<String, String> typeToBioSamplesAccessionMap) {
    getSourceBioSampleAccession(studies, typeToBioSamplesAccessionMap);
    getChildBioSampleAccessions(studies, typeToBioSamplesAccessionMap);

    return typeToBioSamplesAccessionMap;
  }

  private void getChildBioSampleAccessions(
      final List<Study> studies, final Map<String, String> typeToBioSamplesAccessionMap) {
    try {
      final AtomicInteger counter = new AtomicInteger(0);

      studies.forEach(
          study -> {
            study
                .getMaterials()
                .getSamples()
                .forEach(
                    sample -> {
                      if (sample != null) {
                        String childSampleAccession = null;

                        for (final Characteristic characteristic : sample.getCharacteristics()) {
                          if (characteristic
                              .getCategory()
                              .getId()
                              .equalsIgnoreCase(CHARACTERISTIC_CATEGORY_ACCESSION)) {
                            childSampleAccession = characteristic.getValue().getAnnotationValue();
                          }
                        }

                        typeToBioSamplesAccessionMap.put(
                            "CHILD_" + counter.getAndIncrement(), childSampleAccession);
                      }
                    });
          });
    } catch (final Exception e) {
      throw new RuntimeException("Failed to parse ISA Json and get BioSamples accessions", e);
    }
  }

  private void getSourceBioSampleAccession(
      final List<Study> studies, final Map<String, String> typeToBioSamplesAccessionMap) {
    try {
      studies.forEach(
          study ->
              study
                  .getMaterials()
                  .getSources()
                  .forEach(
                      source -> {
                        final ArrayList<Characteristic> sourceCharacteristics =
                            source.getCharacteristics();

                        for (final Characteristic characteristic : sourceCharacteristics) {
                          if (characteristic
                              .getCategory()
                              .getId()
                              .contains(CHARACTERISTIC_CATEGORY_ACCESSION)) {
                            typeToBioSamplesAccessionMap.put(
                                "SOURCE", characteristic.getValue().getAnnotationValue());
                          }
                        }
                      }));
    } catch (final Exception e) {
      throw new RuntimeException("Failed to parse ISA Json and get BioSamples accessions", e);
    }
  }
}
