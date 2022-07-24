# Sequence Diagram 
## Greeting Conversation

```mermaid
sequenceDiagram
    actor Alice
    participant Recorder
    participant STT
    participant RASA
    
    loop Recording time (5s)
        Alice->>+Recorder: "Hallo!"
    end
    Recorder->>+STT: Send formatted audio file
    Note over STT: Audio Conversion to text
    STT->>-RASA: Sends text
    Note over RASA: Tokenizer
    Note over RASA: Featurizers
    Note over RASA: DIETClassifier
    Note over RASA: EntityExtractor
    RASA-->>Alice: Send reply: "Guten Tag!"