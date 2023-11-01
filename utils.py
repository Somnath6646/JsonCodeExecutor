import json
import openai
from termcolor import colored
import sys
import os
from io import StringIO
from dotenv import load_dotenv
import re
import subprocess
import sys
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def describe_json(json_obj, depth=0):
    indent = '  ' * depth
    description = ''

    if isinstance(json_obj, dict):
        description += "a JSON object which consists of the following keys and types:\n"
        common_keys = None

        if all(isinstance(val, dict) for val in json_obj.values()):
            common_keys = set(json_obj.values().__iter__().__next__().keys())
            for val in json_obj.values():
                common_keys &= set(val.keys())

        for key, value in json_obj.items():
            description += f"{indent}- {key}: {describe_json(value, depth+1)}"
            if common_keys and isinstance(value, dict):
                description += f"{indent}  All JSON objects in this level share the same keys: {', '.join(common_keys)}.\n"

    elif isinstance(json_obj, list):
        description += "an array of "
        if not json_obj:  # If the list is empty
            description += "no items\n"
        elif all(isinstance(item, dict) for item in json_obj):
            common_keys = set(json_obj[0].keys()) if json_obj else set()
            for item in json_obj:
                common_keys &= set(item.keys())

            if common_keys:
                description += f"JSON objects with a common structure. The structure is as follows:\n"
                description += describe_json(json_obj[0], depth+1)
            else:
                for index, item in enumerate(json_obj):
                    description += f"{indent}- Item {index+1}: {describe_json(item, depth+1)}"
        else:
            description += f"{describe_json(json_obj[0], depth+1)} (all elements in the array have this type)\n"

    else:
        description += f"a value of type {type(json_obj).__name__}\n"

    return description



def generate_response(prompt, model="gpt-4", max_tokens=1000):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0,
        stream=True,
    )
    answer = ""
    res=""
    answer = ""
    
    for event in response:
      if "content" in res:
        print(colored(res["content"], "yellow"), end='', flush=True)   
        answer = answer+res["content"]
        
        
      event_text = event['choices'][0]['delta']  
      res = event_text

    return answer


def execute_api_code(code):
    # Redirect stdout to capture print output
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        exec(code, globals())
        output = sys.stdout.getvalue()
    finally:
        # Restore the original stdout
        sys.stdout = original_stdout

    return output





def get_imported_libraries(code):
    # Regular expression to match 'import xyz' or 'from xyz import ...'
    matches = re.findall(r'(?:import|from)\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*)*)', code)
    libraries = [match.split(',')[0].strip() for match in matches]
    return libraries

def is_installed(library):
    result = subprocess.run([sys.executable, "-m", "pip", "show", library], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # If the command was successful, the library is installed
    return result.returncode == 0


def install_library(library):
    subprocess.run([sys.executable, "-m", "pip", "install", library])

def install_missing_libraries(code):
    libraries = get_imported_libraries(code)
    for library in libraries:
        if not is_installed(library):
            print()
            print(f"Installing {library}...")
            install_library(library)
            print(f"{library} installed!")
        else:
            print(f"{library} is already installed.")




