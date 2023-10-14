from typing import Callable, List
import outlines.text as text

def google_search(query: str):
    """Google Search"""
    pass


def wikipedia_search(query: str):
    """Wikipedia Search"""
    pass

def predict_ecg_model():
    """predict_ecg_model"""
    pass

def predict_deep_ecg_model():
    """predict_deep_ecg_model"""
    pass



@text.prompt
def my_commands(tools: List[Callable]):
    """AVAILABLE COMMANDS:

    {% for tool in tools %}
    TOOL
    {{ tool | name }}, {{ tool | description }}, args: {{ tool | signature }}
    {{ tool | source }}
    {% endfor %}
    """

prompt = my_commands([google_search, wikipedia_search, predict_ecg_model, predict_deep_ecg_model])
print(prompt)


