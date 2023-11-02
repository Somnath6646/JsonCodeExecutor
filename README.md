# **JsonCodeExecutor**

JsonCodeExecutor is a simple, intuitive tool that enables you to pose natural language questions to your JSON data. 

## **Setup**
1. Environment Configuration:

Before starting, ensure you have an .env file in the root directory of your project with the following content:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

2. Install the required packages:
```bash
pip install -r "requirements.txt"
```

3. Run the main script:
```bash
python3 main.py
```

## **How It Works**

Its actualy very simple.

### **1. Describing the JSON**

We all know that we can't fit a huge json in the context. So what i have done here is instead of directly interacting with large JSON data, JsonCodeExecutor uses the `describe_json` function. This function recursively traverses the JSON structure and provides a human-readable description. It identifies dictionaries (JSON objects), their key-value pairs, arrays (JSON lists), their elements, and other data types in the JSON.

**Example**:
```python
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling"]
}
```

When passed through `describe_json`, the output will be:
```
a JSON object which consists of the following keys and types:
- name: a value of type str
- age: a value of type int
- city: a value of type str
- hobbies: an array of a value of type str (all elements in the array have this type)
```

### **2. Generate the Required Code**

After generating this description, its attached in the prompt for GPT. GPT then crafts the necessary code to fetch the answer that you, the user, are looking for. 

## **Why JsonCodeExecutor?**

While searching for solutions to query JSON using natural language, I came across Langchain's JSON Agent [here](https://python.langchain.com/docs/integrations/toolkits/json). I found it cumbersome and unnecessarily complex. 

To demonstrate this, I've included an example of how Langchain's JSON Agent works in this repository. In comparison, you'll find JsonCodeExecutor to be a more straightforward solution which you can even debug yourself without having to memorize a new word or anything.
