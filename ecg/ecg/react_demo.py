import requests  # type: ignore

import outlines.models as models
import outlines.text as text

import predict_ecg
import fake_predict_deep_ecg as predict_af
import load_user_info


@text.prompt
def build_reAct_prompt(question):
    """预测一下张三是否有心律不齐?
    Tho 1: 我需要获取张三的心电图数据
    Act 2: GetMatPath '张三'
    Obs 2: /home/ubuntu/aimodel/ecg/dev-N.json
    Tho 3: 我需要调用预测心律不齐函数
    Act 4: PredictEcg '/home/ubuntu/aimodel/ecg/dev-N.json'
    Obs 4: 该用户的心电图数据被分类为正常窦性心律, 这表示 心脏的起搏和导航系统工作正常。平均概率为 94.30%,最高概率为 96.60%,最低概率为 90.85% ...
    Tho 5: 张三的心电图数据预测结果为正常窦性心律,概率为94.30%, 这表示张三的心脏的起搏和导航系统一切正常
    Act 6: Finish '根据张三的心电图数据，可预测为正常窦性心律,概率为94.30%, 这表示张三的心脏的起搏和导航系统一切正常'
    {{ question }}
    """


@text.prompt
def add_mode(i, mode, result, prompt):
    """{{ prompt }}
    {{ mode }} {{ i }}: {{ result }}
    """

def predict_ecg_model(mat_path):
    return predict_ecg.predict(mat_path)

def get_mat_path(user_name):
    return load_user_info.getMatPath(user_name)

prompt = build_reAct_prompt("预测一下王五是否有心律不齐")

complete = models.text_completion.openai(
    "gpt-3.5-turbo", max_tokens=1024, temperature=1.0
)

for i in range(1, 10):
    mode = complete(prompt, is_in=["Tho", "Act"])
    prompt = add_mode(i, mode, "", prompt)

    print(mode)
    if mode == "Tho":
        thought = complete(prompt, stop_at="\n")
        prompt += f"{thought}"
        print(thought)
    elif mode == "Act":
        action = complete(prompt, is_in=["PredictEcg", "GetMatPath", "Finish"])
        prompt += f"{action} '"
        print(action)

        subject = complete(prompt, stop_at=["'"])  # Apple Computers headquartered
        subject = " ".join(subject.split()[:2])
        prompt += f"{subject}'"
        print(subject)

        if action == "GetMatPath":
            result = get_mat_path(subject)
            prompt = add_mode(i, "Obs", result, prompt)
        elif action == "PredictEcg":
            result = predict_ecg_model(subject)
            prompt = add_mode(i, "Obs", result, prompt)
        else:
            break

print(prompt)
