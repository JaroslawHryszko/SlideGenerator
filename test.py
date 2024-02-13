import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, BartForConditionalGeneration, BartTokenizer

sentence = """It can be expensive to train ML models. First, the data has to be prepared and then the model must be trained. The first activity can consume large amounts of human resources, while
the latter activity can consume a lot of computing resources. Many organizations do not have access
to these resources."""

model_name = "Vamsi/T5_Paraphrase_Paws"
device = torch.device("cuda")
torch.cuda.manual_seed(2137)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
text =  "paraphrase: " + sentence + " </s>"
encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt").to(device)
input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)
outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    do_sample=True,
    top_k=220,
    top_p=1,
    early_stopping=True,
    num_return_sequences=1,
    encoder_no_repeat_ngram_size=4
)
for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)

input_sentence = line

model_name = 'eugenesiow/bart-paraphrase'
model = BartForConditionalGeneration.from_pretrained(model_name).to(device)
tokenizer = BartTokenizer.from_pretrained(model_name)
batch = tokenizer(input_sentence, return_tensors='pt').to(device)
generated_ids = model.generate(
    batch['input_ids'],
    max_length=256,
    do_sample=True,
    top_k=120,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=1,
    encoder_no_repeat_ngram_size=4
)
generated_sentence = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

tokenizer = AutoTokenizer.from_pretrained("shrishail/t5_paraphrase_msrp_paws")
model = AutoModelForSeq2SeqLM.from_pretrained("shrishail/t5_paraphrase_msrp_paws").to(device)

text =  "paraphrase: " + generated_sentence[0] + " </s>"
encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt").to(device)
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to(device)
outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    do_sample=True,
    top_k=120,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=1,
    encoder_no_repeat_ngram_size=4
)
for output in outputs:
    line2 = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)





print("1:" + sentence)
print("2:" + line)
print("3:" + generated_sentence[0])
print("4:" + line2)