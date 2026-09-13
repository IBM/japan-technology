FROM confluentinc/cp-kafka-connect:7.5.0

RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:2.4.2

ENV CONNECT_PLUGIN_PATH=/usr/share/java,/usr/share/confluent-hub-components

# Made with Bob
