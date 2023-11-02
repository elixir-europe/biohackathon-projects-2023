FROM openjdk:11
VOLUME /tmp
EXPOSE 8042
ARG JAR_FILE=build/libs/ISASRAProject27-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
