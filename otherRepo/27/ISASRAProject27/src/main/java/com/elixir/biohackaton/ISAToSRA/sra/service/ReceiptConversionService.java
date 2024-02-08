/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.sra.service;

import com.elixir.biohackaton.ISAToSRA.sra.model.Receipt;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import com.fasterxml.jackson.dataformat.xml.ser.ToXmlGenerator;
import org.springframework.stereotype.Service;

@Service
public class ReceiptConversionService {
  private final XmlMapper xmlMapper = new XmlMapper();
  private final ObjectMapper jsonMapper = new ObjectMapper();

  public ReceiptConversionService() {
    setupJsonMapper();
    setupXmlMapper();
  }

  private void setupJsonMapper() {
    jsonMapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
    jsonMapper.configure(SerializationFeature.INDENT_OUTPUT, true);
    jsonMapper.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS, false);
  }

  private void setupXmlMapper() {
    xmlMapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
    xmlMapper.enable(SerializationFeature.INDENT_OUTPUT);
    xmlMapper.configure(ToXmlGenerator.Feature.WRITE_XML_DECLARATION, true);
  }

  public String convertReceiptXmlToJson(String xml) {
    return writeReceiptJson(readReceiptXml(xml));
  }

  public String writeReceiptJson(Receipt receipt) {
    return writeJson(receipt, "receipt");
  }

  private String writeJson(Object obj, String type) {
    try {
      return jsonMapper.writeValueAsString(obj);
    } catch (Exception ex) {
      throw new RuntimeException(type, ex);
    }
  }

  public Receipt readReceiptXml(String xml) {
    return readXml(xml, Receipt.class, "receipt");
  }

  private <T> T readXml(String xml, Class<T> cls, String type) {
    try {
      return xmlMapper.readValue(xml, cls);
    } catch (Exception ex) {
      throw new RuntimeException(type, ex);
    }
  }
}
