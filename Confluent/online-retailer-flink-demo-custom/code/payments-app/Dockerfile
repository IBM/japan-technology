# Use Maven and JDK base image
FROM maven:3.9.9-eclipse-temurin-21-alpine

# Set the working directory inside the container
WORKDIR /opt/payments_app

# 1) Copy only the pom to leverage Docker layer cache for dependencies
COPY pom.xml .
# Pre-fetch dependencies to speed up subsequent builds
RUN mvn -q -T 1C -DskipTests dependency:go-offline

# 2) Copy the application sources
COPY src ./src

# 3) Compile the project (generates Avro POJOs and compiles sources)
RUN mvn -q -T 1C compile

# 4) Run the Java application via Maven exec plugin
CMD ["mvn", "exec:java"]

