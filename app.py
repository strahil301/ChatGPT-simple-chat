import os
os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'

from llama_index import SimpleDirectoryReader, VectorStoreIndex, LLMPredictor, PromptHelper, StorageContext, load_index_from_storage
import gradio as gr

"""
    the function reads the documents in /docs folder
    parses the pdfs
    breaks them down into chunks
    sends the data to ChatGPT to create vectors
    stores the vectors in the /storage folder
"""
def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 0.2
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    # llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = VectorStoreIndex.from_documents(documents,prompt_helper=prompt_helper)
    index.storage_context.persist()

    return index


""" 
    the function receives a query as plain text 
    loads the context vector from the /storage folder
    sends the context and the query to chatGPT
    returns the result as plain text 
"""
def chatbot(input_text):
    # index = GPTSimpleVectorIndex.load_from_disk('index.json')
    storage_context = StorageContext.from_defaults(persist_dir='./storage')
    index = load_index_from_storage(storage_context)
    # response = index.query(input_text, response_mode="compact")
    response = index.as_query_engine().query(input_text)

    return response

# gr is a simple out-of-box chatbot client, that invokes the supplied function, when a question is submitted 
iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="My AI Chatbot")

# index = construct_index("docs")
iface.launch(share=True)