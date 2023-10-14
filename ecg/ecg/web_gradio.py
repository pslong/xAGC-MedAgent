import gradio as gr

import thought_chain

import baichuan_client

def agent_start(input):
    print(input)

    result = thought_chain.start_chain(input)

    print(result)

    wrappedInput = "你是一个专业的医生，需要你针对以下病人的心电图数据，做出一些专业的分析\n" + result
    wrappedOutput = baichuan_client.doRequest("Baichuan2-53B", wrappedInput)

    print(wrappedOutput)

    return result


iface = gr.Interface(
    fn=agent_start,
    inputs="text",
    outputs="text"
)

iface.launch(share=True)
