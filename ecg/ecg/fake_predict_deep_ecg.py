import random

def predict():
    output = random.choices(
        population=[True, False],
        weights=[0.999, 0.001], # 这里具体的权重你可以根据需要调整
        k=1
    )

    return output[0]
