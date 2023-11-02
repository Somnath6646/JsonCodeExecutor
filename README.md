# **JsonCodeExecutor**

JsonCodeExecutor is a simple, intuitive tool that enables you to pose natural language questions to your JSON data. 

## **Setup**
1. Install the required packages:
```bash
pip install -r "requirements.txt"
```

2. Run the main script:
```bash
python3 main.py
```

## **How It Works**

At the heart of JsonCodeExecutor is a unique approach to understanding and querying JSON structures:

### **1. Describing the JSON**

Instead of directly interacting with large JSON data, JsonCodeExecutor uses the `describe_json` function. This function recursively traverses the JSON structure and provides a human-readable description. It identifies dictionaries (JSON objects), their key-value pairs, arrays (JSON lists), their elements, and other data types in the JSON.

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

After generating this description, it's presented as a prompt to GPT. GPT then crafts the necessary code to fetch the answer that you, the user, are looking for. 

## **Why JsonCodeExecutor?**

While searching for solutions to query JSON using natural language, I came across Langchain's JSON Agent [here](https://python.langchain.com/docs/integrations/toolkits/json). I found it cumbersome and unnecessarily complex. 

To demonstrate this, I've included an example of how Langchain's JSON Agent works in this repository. In comparison, you'll find JsonCodeExecutor to be a more straightforward solution which you can even debug yourself without having to memorize a new word or anything.
