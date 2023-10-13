import gradio as gr

demo = gr.load("baichuan-inc/Baichuan-13B-Chat", src="models")

demo.launch()
