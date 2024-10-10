package com.example.cqrsexample;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class KafkaProducer {
    private static final String TOPIC = "cqrs-topic";

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;

    public void sendMessage(BookDTO bookDTO){
        String message =
                "{\"bid\":" + "\"" + bookDTO.getBid() + "\""
                        + ", \"title\":" + "\"" + bookDTO.getTitle() +  "\""
                        + ", \"author\":" + "\"" + bookDTO.getAuthor() +  "\""
                        + ", \"category\":" + "\"" + bookDTO.getCategory() +  "\""
                        + ", \"pages\":" + "\"" + bookDTO.getPages() +  "\""
                        + ", \"price\":" + "\"" + bookDTO.getPrice() +  "\""
                        + ", \"published_date\":" + "\"" + bookDTO.getPublished_date().toString() +  "\""
                        + ", \"description\":" + "\"" + bookDTO.getDescription() +  "\""
                        + "}";
        System.out.println("Dto :" + message);
        kafkaTemplate.send(TOPIC, message);
    }
}