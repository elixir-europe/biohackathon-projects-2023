/** Elixir BioHackathon 2023 */
package com.elixir.biohackaton.ISAToSRA.sra.service;

import org.dom4j.Element;
import org.springframework.stereotype.Service;


@Service
public class SRAAnalysisXmlCreator {

  public void createENAAnalysisSetElement(
      final Element webinElement
      // TODO other parameters
      ) {
      final Element analysisSetElement = webinElement.addElement("ANALYSIS_SET");
      // TODO other things
  }
}
