# Builder stage: Use gradle image to compile jar file
FROM gradle:jdk11 AS builder

WORKDIR /app

COPY . .
RUN ./gradlew build -x test -x spotlessApply --info --stacktrace "-Dorg.gradle.jvmargs=--add-exports jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED --add-exports jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED --add-exports jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED --add-exports jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED --add-exports jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED"

# Use a lightweight base image to run the jar file
FROM openjdk:11-jre-slim

ARG JAR_FILE=/app/build/libs/*.jar

# Copy the JAR file from the builder stage
COPY --from=builder ${JAR_FILE} app.jar

# Set the entry point for the application
ENTRYPOINT ["java", "-jar", "/app.jar"]
