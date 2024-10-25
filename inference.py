from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def load_model():
    """
    Load a pre-trained question generation model and tokenizer.

    This function uses the Hugging Face Transformers library to load a pre-trained 
    question generation model and tokenizer from a specified checkpoint.

    Parameters:
    None

    Returns:
    tokenizer (AutoTokenizer): The tokenizer for the loaded model.
    model (AutoModelForSeq2SeqLM): The loaded question generation model.
    """
    tokenizer = AutoTokenizer.from_pretrained("QGCheckpoint")
    model = AutoModelForSeq2SeqLM.from_pretrained("QGCheckpoint")
    return tokenizer, model


def generate_question(context):
    tokenizer,model=load_model()
    inputs = tokenizer.encode(context, return_tensors='pt')
    attention_mask = (inputs != tokenizer.pad_token_id).long() 
    outputs = model.generate(inputs, attention_mask=attention_mask, max_length=100, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)



def inference(context):
    _,model=  load_model()
    model.eval()
    questions = generate_question(context)
    return questions

    
   
  



