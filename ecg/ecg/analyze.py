import numpy as np
import pandas as pd
import json

def analyze_ecg_data(ecg_data):
    ecg_data = np.array(ecg_data)[0]  # Convert input to numpy array for easier manipulation
    classes = ['A', 'N', 'O', '~']

    results = {"Class": [], "Avg Probability": [], "Max Probability": [], "Min Probability": []}

    # Loop over each class
    for i, class_ in enumerate(classes):
        # Extract the data for this class
        class_data = ecg_data[:, i]

        # Compute metrics
        avg_prob = np.mean(class_data)
        max_prob = np.max(class_data)
        min_prob = np.min(class_data)

        # Store the results
        results["Class"].append(class_)
        results["Avg Probability"].append(f"{avg_prob * 100:.2f}%")
        results["Max Probability"].append(f"{max_prob * 100:.2f}%")
        results["Min Probability"].append(f"{min_prob * 100:.2f}%")

    # Convert the dictionary to a pandas DataFrame for a nicer tabular display
    results_df = pd.DataFrame(results)

    # Find the class with the highest average probability
    most_probable_class = results_df.loc[results_df['Avg Probability'].idxmax()]['Class']

    # Print the results
    print(results_df)
    print(f"The most probable class is: {most_probable_class}")

    return results_df, most_probable_class


def explain_heartbeat_data(input_dict, rhythm):
    input_data = json.loads(input_dict)
    translations = {
        "N": "正常窦性心律（Normal sinus rhythm）",
        "A": "心房颤动（AF rhythm）",
        "O": "其他心律（Other rhythm）",
        "~": "噪声记录（Noisy recording）"
    }

    keys = {
        "A": '0',
        "N": '1',
        "O": '2',
        "~": '3'
    }

    translation = translations.get(rhythm)
    if not translation:
        return "无法识别的心跳节奏类型: {}".format(rhythm)

    # Add description map
    description_map = {
        "N": "心脏的起搏和导航系统工作正常",
        "A": "一种常见的心律失常，表现为心房的快速不规则跳动。心房颤动可能导致血液淤积并形成血栓，这有可能引起卒中",
        "O": "除正常窦性心律和心房颤动以外的其他类型的心脏节奏。具体来说，它可以包括一系列的心律失常，比如窦性心动过速、窦性心动过缓、室上性早搏、室性早搏等",
        "~": "该段ECG数据质量较差，可能受到了设备噪声、肌电噪声或其他干扰信号的影响，使得心率不齐的类型无法得到确定",
    }

    if rhythm not in description_map:
        return "无法识别的心跳节奏类型: {}".format(rhythm)

    key = keys[rhythm]

    message = f"该用户的心电图 (ECG) 数据被分类为 '{translation}'， 这表示 {description_map[rhythm]}。"

    message += f"\n\n平均概率为 {input_data['Avg Probability'][key]}，最高概率为 {input_data['Max Probability'][key]}，最低概率为 {input_data['Min Probability'][key]}。"

    return message

