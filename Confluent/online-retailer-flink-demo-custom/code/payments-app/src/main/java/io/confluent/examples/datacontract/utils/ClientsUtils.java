package io.confluent.examples.datacontract.utils;

import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.admin.NewTopic;

import java.io.*;
import java.util.Collections;
import java.util.Properties;
import java.util.concurrent.ExecutionException;

public class ClientsUtils {

    /**
     * Load configuration from environment variables (required).
     * Throws RuntimeException if required environment variables are not set.
     */
    public static Properties loadConfigFromEnv() {
        String bootstrapServers = System.getenv("BOOTSTRAP_SERVERS");

        // Validate required environment variables
        if (bootstrapServers == null || bootstrapServers.isEmpty()) {
            throw new RuntimeException("ERROR: Required environment variable BOOTSTRAP_SERVERS is not set.");
        }

        System.out.println("Loading Kafka configuration from environment variables");

        Properties cfg = new Properties();

        // Kafka connection settings
        cfg.put("bootstrap.servers", bootstrapServers);
        cfg.put("security.protocol", "SASL_SSL");
        cfg.put("sasl.mechanism", "PLAIN");

        String saslUsername = System.getenv("SASL_USERNAME");
        String saslPassword = System.getenv("SASL_PASSWORD");
        if (saslUsername == null || saslPassword == null) {
            throw new RuntimeException("ERROR: Required environment variables SASL_USERNAME and SASL_PASSWORD are not set.");
        }
        cfg.put("sasl.jaas.config", String.format(
            "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"%s\" password=\"%s\";",
            saslUsername, saslPassword));

        // Schema Registry settings
        String schemaRegistryUrl = System.getenv("SCHEMA_REGISTRY_URL");
        if (schemaRegistryUrl == null) {
            throw new RuntimeException("ERROR: Required environment variable SCHEMA_REGISTRY_URL is not set.");
        }
        cfg.put("schema.registry.url", schemaRegistryUrl);

        String srApiKey = System.getenv("SR_API_KEY");
        String srApiSecret = System.getenv("SR_API_SECRET");
        if (srApiKey == null || srApiSecret == null) {
            throw new RuntimeException("ERROR: Required environment variables SR_API_KEY and SR_API_SECRET are not set.");
        }
        cfg.put("basic.auth.credentials.source", "USER_INFO");
        cfg.put("schema.registry.basic.auth.user.info", srApiKey + ":" + srApiSecret);

        // AWS KMS settings for CSFLE (Client-Side Field Level Encryption)
        String awsAccessKeyId = System.getenv("AWS_ACCESS_KEY_ID");
        String awsSecretAccessKey = System.getenv("AWS_SECRET_ACCESS_KEY");
        if (awsAccessKeyId == null || awsSecretAccessKey == null) {
            throw new RuntimeException("ERROR: Required environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are not set.");
        }
        cfg.put("rule.executors._default_.param.access.key.id", awsAccessKeyId);
        cfg.put("rule.executors._default_.param.secret.access.key", awsSecretAccessKey);

        return cfg;
    }

    public static String createTopicIfNotExists(Properties props, String topicName) {
        AdminClient adminClient = AdminClient.create(props);
        boolean topicExists = false;
        try {
            // Replace possible spaces with - on the topic name
            topicName = topicName.replace(" ", "-");

            // Check if topic already exists
            topicExists = adminClient.listTopics().names().get().contains(topicName);
            if (!topicExists) {
                int partitions = new Integer(props.getProperty("num.partitions"));
                int replication = new Integer(props.getProperty("replication.factor"));
                NewTopic newTopic = new NewTopic(topicName, partitions, (short) replication);
                adminClient.createTopics(Collections.singletonList(newTopic)).all().get();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } finally {
            // Close the client
            adminClient.close();
        }
        return topicName;
    }

    public static int sizeof(Object obj) throws IOException {
        ByteArrayOutputStream byteOutputStream = new ByteArrayOutputStream();
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(byteOutputStream);
        objectOutputStream.writeObject(obj);
        objectOutputStream.flush();
        objectOutputStream.close();
        return byteOutputStream.toByteArray().length;
    }

    public static boolean isEven(int number) {
        // even
        return (number % 2) == 0;
    }

    public static void main(final String[] args) throws Exception {
        // This utility can be used to create topics using environment variable configuration
        if (args.length < 1) {
            System.out.println("Provide the topic name as an argument.");
            System.out.println("Configuration is loaded from environment variables.");
            System.exit(1);
        }
        try {
            Properties props = loadConfigFromEnv();
            createTopicIfNotExists(props, args[0]);
        } catch (Exception e) {
            System.out.println("Error in ClientsUtils.main method: " + e.getMessage());
        }
    }
}
