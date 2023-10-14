import random

def predict():
    output = random.choices(
        population=[True, False],
        weights=[0.999, 0.001], # 这里具体的权重你可以根据需要调整
        k=1
    )

    print(output[0])

    if (output[0] == True) :
        return "有房颤"
    else:
        return "无房颤"
