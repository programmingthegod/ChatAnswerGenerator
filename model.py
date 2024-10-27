from transformers import T5ForConditionalGeneration, T5Tokenizer

class AnswerGenerator:
    def __init__(self, model_name='t5-small'):
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)

    def generate_answer(self, question, context):
        input_text = f"question: {question} context: {context}"
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model.generate(input_ids)
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer

# Initialize the model
answer_generator = AnswerGenerator()
