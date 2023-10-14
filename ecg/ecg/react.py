import requests  # type: ignore

import outlines.models as models
import outlines.text as text


@text.prompt
def build_reAct_prompt(question):
    """预测一下张三是否有心率不齐?
    Tho 1: 我需要调用预测心率不齐函数
    Act 2: PredictEcg '张三'
    Obs 3: 该用户的心电图 (ECG) 数据被分类为 '正常窦性心律（Normal sinus rhythm）'， 这表示 心脏的起搏和导航系统工作正常。平均概率为 94.30%，最高概率为 96.60%，最低概率为 90.85%。 ...
    Act 4: Finish "张三的心电图 (ECG) 数据预测为 '正常窦性心律（Normal sinus rhythm）'，概率为94.30%, 这表示张三的心脏的起搏和导航系统一切正常"
    预测一下李四是否有心率不齐?
    Tho 1: 我需要调用预测心率不齐函数
    Act 2: PredictEcg '李四'
    Obs 3: 该用户的心电图 (ECG) 数据被分类为 '心房颤动（AF rhythm）'， 这是一种常见的心律失常，表现为心房的快速不规则跳动。心房颤动可能导致血液淤积并形成血栓，这有可能引起卒中。平均概率为 95.60%，最高概率为 97.30%，最低概率为 91.85%。 ...
    Act 4: Finish "李四的心电图 (ECG) 数据预测为 '心房颤动（AF rhythm）'，概率为95.60%, 这表示李四出现心律失常，表现为心房的快速不规则跳动。心房颤动可能导致血液淤积并形成血栓，这有可能引起卒中"
    {{ question }}
    """


@text.prompt
def add_mode(i, mode, result, prompt):
    """{{ prompt }}
    {{ mode }} {{ i }}: {{ result }}
    """


def search_wikipedia(query: str):
    url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={query}&origin=*"
    response = requests.get(url)
    page = response.json()["query"]["pages"]
    return ".".join(list(page.values())[0]["extract"].split(".")[:2])


prompt = build_reAct_prompt("Where is Apple Computers headquarted? ")

complete = models.text_completion.openai(
    "gpt-3.5-turbo", max_tokens=128, temperature=1.0
)

for i in range(1, 10):
    mode = complete(prompt, is_in=["Tho", "Act"])
    prompt = add_mode(i, mode, "", prompt)

    if mode == "Tho":
        thought = complete(prompt, stop_at="\n")
        prompt += f"{thought}"
    elif mode == "Act":
        action = complete(prompt, is_in=["Search", "Finish"])
        prompt += f"{action} '"

        subject = complete(prompt, stop_at=["'"])  # Apple Computers headquartered
        subject = " ".join(subject.split()[:2])
        prompt += f"{subject}'"

        if action == "Search":
            result = search_wikipedia(subject)
            prompt = add_mode(i, "Obs", result, prompt)
        else:
            break

print(prompt)
