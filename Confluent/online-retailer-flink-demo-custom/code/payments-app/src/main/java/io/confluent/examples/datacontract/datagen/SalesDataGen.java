package io.confluent.examples.datacontract.datagen;

import io.confluent.examples.datacontract.pojo.avro.Sale;

import java.time.Instant;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Random;

public class SalesDataGen {

    private static final String CONF_CODE_CHAR_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    private static final int CONF_CODE_LENGTH = 8;

    private static int orderId = 3000;

    static int getRandomNumber(int max)
    {
        return new Random().nextInt(max);
    }

    public static String generateConfirmationCode() {
        StringBuilder code = new StringBuilder();
        Random random = new Random();
        for (int i = 0; i < CONF_CODE_LENGTH; i++) {
            int index = random.nextInt(CONF_CODE_CHAR_LIST.length());
            code.append(CONF_CODE_CHAR_LIST.charAt(index));
        }
        return code.toString();
    }

    public static String generateFakeCreditCardNumber() {
        Random random = new Random();
        StringBuilder cardNumber = new StringBuilder();

        // Generate the first digit (between 2 and 4)
        cardNumber.append(random.nextInt(3) + 2);

        // Generate the next 15 digits
        for (int i = 2 ; i < 17; i++) {
            cardNumber.append(random.nextInt(10));
            if (i % 4 == 0 && i != 16) {
                cardNumber.append("-");
            }
        }

        return cardNumber.toString();
    }

    public static String generateFakeExpirationDate() {
        Random random = new Random();
        // Generate a year between 1 and 4 years in the future
        int yearToAdd = 1 + random.nextInt(4);
        // Generate a month between 1 and 12
        int month = 1 + random.nextInt(12);

        // Get the current date
        LocalDate currentDate = LocalDate.now();
        // Calculate the expiration date
        LocalDate expirationDate = currentDate.plusYears(yearToAdd).withMonth(month);

        // Format the expiration date as MM/YY
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/yy");
        return expirationDate.format(formatter);
    }

    public static Sale getSale(int fail) {

        Sale order = new Sale();
        order.setOrderId(orderId++);
        order.setProductId(getRandomNumber(100));
        order.setCustomerId(getRandomNumber(50));
        order.setTs(Instant.ofEpochMilli(System.currentTimeMillis()));
        order.setCcNumber(generateFakeCreditCardNumber());
        order.setExpiration(generateFakeExpirationDate());
        order.setAmount((new Random().nextDouble())*1000);

        if (fail == 5) {
            order.setConfirmationCode("0");
        } else {
            order.setConfirmationCode(generateConfirmationCode());
        }

        

        return order;
    }
}
