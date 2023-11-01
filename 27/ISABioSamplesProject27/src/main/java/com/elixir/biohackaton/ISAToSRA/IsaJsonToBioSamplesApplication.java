/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA;

import com.elixir.biohackaton.ISAToSRA.biosamples.service.BioSampleSubmissionCreator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class IsaJsonToBioSamplesApplication implements ApplicationRunner {
  @Autowired BioSampleSubmissionCreator BioSampleSubmissionCreator;

  public static void main(final String[] args) {
    SpringApplication.run(IsaJsonToBioSamplesApplication.class, args);
  }

  @Override
  public void run(final ApplicationArguments args) throws Exception {
    this.BioSampleSubmissionCreator.performSubmissionToBioSamplesAndEna(args);
  }
}
