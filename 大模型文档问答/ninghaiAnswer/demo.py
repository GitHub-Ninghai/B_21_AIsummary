import subprocess
import gradio as gr


def call_document_q_and_a(问题):
    # 使用subprocess来调用你的脚本，并指定encoding为utf-8
    result = subprocess.run(["python", "./Document_Q_And_A.py", "--user_question", 问题],
                            capture_output=True, text=True, encoding='utf-8', check=True)
    # 假设你的脚本的输出是标准的文本输出，我们直接返回这个输出
    return result.stdout
examples = [
    "B-21的供应商有哪些？\n","B-21发展时间线\n","本报告关于B-21的主要内容有哪些？\n"  # 这是一个示例问题，用户输入时会替换它,
]



# 创建一个Gradio界面
with gr.Interface(call_document_q_and_a, "text", "text",examples=examples,title="B-21问答") as i:
    i.launch()