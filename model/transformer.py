from transformers import pipeline

class Pipelines:
    def __init__(self):
        self.english = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

        _polish_model = "eevvgg/PaReS-sentimenTw-political-PL"
        self.polish = pipeline("sentiment-analysis", model=_polish_model, tokenizer=_polish_model)

sentiment_analyzer = Pipelines()