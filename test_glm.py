import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"

tokenizer = AutoTokenizer.from_pretrained("THUDM/glm-4v-9b", trust_remote_code=True)

query = 'describe this image'
image = Image.open("test.png").convert('RGB')
inputs = tokenizer.apply_chat_template([{"role": "user", "image": image, "content": query}],
                                       add_generation_prompt=True, tokenize=True, return_tensors="pt",
                                       return_dict=True)  # chat mode

inputs = inputs.to(device)
print(inputs)

model = AutoModelForCausalLM.from_pretrained(
    "THUDM/glm-4v-9b",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=False,
    trust_remote_code=True
).to(device).eval()


gen_kwargs = {"max_length": 1024, "do_sample": True, "top_k": 1}

with torch.no_grad():
    outputs = model.generate(**inputs, **gen_kwargs)
    print("Outputs:", outputs)
    outputs = outputs[:, inputs['input_ids'].shape[1]:]
    print("Reshape Outputs:", outputs)
    print(tokenizer.decode(outputs[0]))

