import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,  BartForConditionalGeneration, BartTokenizer

def paraphrase_vamsi(input_sentence):
    device = torch.device("cuda")
    torch.cuda.manual_seed(2137)
    model_name = "Vamsi/T5_Paraphrase_Paws"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
    text = "paraphrase: " + input_sentence + " </s>"
    encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt").to(device)
    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)
    outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=500,
        do_sample=True,
        top_k=220,
        top_p=1,
        early_stopping=True,
        num_return_sequences=1,
        encoder_no_repeat_ngram_size=4
    )
    for output in outputs:
        line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return line

def paraphrase_eugene(input_sentence):
    device = torch.device("cuda")
    torch.cuda.manual_seed(2137)
    model_name = 'eugenesiow/bart-paraphrase'
    model = BartForConditionalGeneration.from_pretrained(model_name).to(device)
    tokenizer = BartTokenizer.from_pretrained(model_name)
    batch = tokenizer(input_sentence, return_tensors='pt').to(device)
    generated_ids = model.generate(
        batch['input_ids'],
        max_length=500,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=1,
        encoder_no_repeat_ngram_size=3
    )
    generated_sentence = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return generated_sentence[0]

def paraphrase_shail(input_sentence):
    device = torch.device("cuda")
    torch.cuda.manual_seed(2137)
    model_name = 'shrishail/t5_paraphrase_msrp_paws'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
    text = "paraphrase: " + input_sentence + " </s>"
    encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt").to(device)
    input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to(device)
    outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=500,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=1,
        encoder_no_repeat_ngram_size=6
    )
    for output in outputs:
        line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return line


input_sentence = """Black-box adversarial attacks involve the attacker exploring the model to determine its functionality 
and then building a duplicate model that provides similar functionality.  The attacker then uses a 
white-box approach to identify adversarial examples for this duplicate model.  As adversarial 
examples are generally transferable, the same adversarial examples will normally also work on the 
original model. """

vamsi = paraphrase_vamsi(input_sentence)
eugene = paraphrase_eugene(input_sentence)
shail = paraphrase_shail(input_sentence)

print("0: "+ input_sentence)
print("Vamsi: " + vamsi)
print("Eugene:" + eugene)
print("Shail:" + shail)
