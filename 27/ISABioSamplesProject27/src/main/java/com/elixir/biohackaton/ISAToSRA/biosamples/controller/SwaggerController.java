/** Elixir BioHackathon 2022 */
package com.elixir.biohackaton.ISAToSRA.biosamples.controller;

import io.swagger.v3.oas.annotations.Hidden;
import java.io.IOException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SwaggerController {
  @GetMapping("/")
  @Hidden
  public void swagger(HttpServletRequest request, HttpServletResponse response) throws IOException {
    String swaggerURL = request.getContextPath() + "/swagger-ui.html";
    response.sendRedirect(swaggerURL);
  }
}
