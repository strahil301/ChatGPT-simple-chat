

# Install modules

```
# install a virtual environment
python -m venv .venv

# activate the virtual environment
.venv/Scripts/activate.bat

# install dependencies
pip install llama_index
pip install gradio

```


# Add key 

Open `app.py`

```
# replace wiht open api key
os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'

```

# Run application

In the terminal execute execute the following command:
```
python app.py
```

# Open the applications in the browser

Open the browser and enter the url:
Load `http://127.0.0.1:7860` in the browser

# Ask questions

```
What is the implication of covid on workspace?
What is your source?
Will the Earth be impacted by a colision with Mars?
```
