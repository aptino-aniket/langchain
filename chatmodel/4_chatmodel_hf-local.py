from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline



llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen3-0.6B",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 1024,
        "temperature": 0.7,
    }
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Hello, how are you?")

print(result.content)