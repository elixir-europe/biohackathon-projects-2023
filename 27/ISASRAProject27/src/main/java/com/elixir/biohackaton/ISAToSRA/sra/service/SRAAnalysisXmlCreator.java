/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.sra.service;

import com.elixir.biohackaton.ISAToSRA.model.Assay;
import com.elixir.biohackaton.ISAToSRA.model.DataFile;
import com.elixir.biohackaton.ISAToSRA.model.Study;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicReference;
import lombok.extern.slf4j.Slf4j;
import org.dom4j.Element;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class SRAAnalysisXmlCreator {
  private static final String DERIVED_FILE_KEY = "Derived Data File";

  private static final String CHECKSUM_KEY = "checksum";

  private static final String CHECKSUM_TYPE_KEY = "checksum type";

  public void createENAAnalysisSetElement(final Element webinElement, final List<Study> studies) {
    final Element analysisSetElement = webinElement.addElement("ANALYSIS_SET");

    studies.forEach(
        study ->
            study
                .getAssays()
                .forEach(assay -> convertAssayToAnalysisElement(assay, analysisSetElement)));
  }

  private void convertAssayToAnalysisElement(final Assay assay, final Element analysisSetElement) {
    final Element analysisElement = analysisSetElement.addElement("ANALYSIS");

    // TODO top level analysis attributes (including type)

    // Add samples
    assay
        .getMaterials()
        .getSamples()
        .forEach(
            sample -> {} // TODO
            );
    //add_element(analysis_elemt, 'SAMPLE_REF',
    //                        accession=sample_row.get('Sample Accession'),
    //                        label=sample_row.get('Sample ID'))

    // Add files
    final Element filesElement = analysisElement.addElement("FILES");
    assay.getDataFiles().forEach(dataFile -> convertDataFileToFileElement(dataFile, filesElement));
  }

  private void convertDataFileToFileElement(DataFile dataFile, Element filesElement) {
    // Analysis must use derived files
    if (!dataFile.getType().equalsIgnoreCase(DERIVED_FILE_KEY)) {
      return;
    }

    String filename = dataFile.getName();
    // TODO any way to get filetype (vcf, bam, etc.) besides extension? also what if files are
    // compressed?
    String filetype = dataFile.getName().substring(dataFile.getName().lastIndexOf('.'));

    // Files must have a checksum (stored in comments)
    AtomicReference<String> checksum = new AtomicReference<>();
    AtomicReference<String> checksumType = new AtomicReference<>();
    dataFile
        .getComments()
        .forEach(
            comment -> {
              if (comment.getName().equalsIgnoreCase(CHECKSUM_KEY)) {
                checksum.set(comment.getValue());
              } else if (comment.getName().equalsIgnoreCase(CHECKSUM_TYPE_KEY)) {
                checksumType.set(comment.getValue());
              }
            });

    if (Objects.isNull(checksum.get()) || Objects.isNull(checksumType.get())) {
      log.error("Checksum and checksum type not found");
    } else {
      Element fileElement = filesElement.addElement("FILE");
      fileElement.addAttribute("filename", filename);
      fileElement.addAttribute("filetype", filetype);
      fileElement.addAttribute("checksum_method", checksumType.get());
      fileElement.addAttribute("checksum", checksum.get());
    }
  }
}
