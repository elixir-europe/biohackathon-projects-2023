FROM openjdk:11
VOLUME /tmp
EXPOSE 8032
ARG JAR_FILE=build/libs/ISABioSamplesProject27-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
