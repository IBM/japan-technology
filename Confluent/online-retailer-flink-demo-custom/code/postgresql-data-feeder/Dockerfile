# Use Maven and JDK base image
FROM maven:3.9.9-eclipse-temurin-21

# Set the working directory inside the container
WORKDIR /opt/db_feeder_app

# Copy all the project files into the container's working directory
COPY . .

# Change to the subdirectory where the project is located
# WORKDIR /opt/learn-apache-flink-table-api-for-java-content/exercises

# Run Maven to clean and package the project
RUN mvn compile

# Specify the command to run the Java application
CMD ["mvn", "exec:java"]

