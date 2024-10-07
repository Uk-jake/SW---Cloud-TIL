from kafka import KafkaConsumer
import json
class MessageConsumer:
   def __init__(self, broker, topic):
       self.broker = broker
       self.consumer = KafkaConsumer(
           topic,  # Topic to consume
           bootstrap_servers=self.broker,
           value_deserializer=lambda x: x.decode(
               "utf-8"
           ),  # Decode message value as utf-8
           group_id="my-group",  # Consumer group ID
           auto_offset_reset="earliest",  # Start consuming from earliest available message
           enable_auto_commit=True,  # Commit offsets automatically
       )
   def receive_message(self):
       try:
           for message in self.consumer:
               #print(message.value)
               result = json.loads(message.value)
               for k, v in result.items():
                   print(k, ":", result[k])
               print(result["name"])
               print(result["age"])
       except Exception as exc:
           raise exc
      
# 브로커와 토픽명을 지정한다.
broker = ["localhost:9092"]
topic = "exam-topic"
cs = MessageConsumer(broker, topic)
cs.receive_message()
