base_instruction = "I want you act as a Employee Simulator.\r\n \
					Your objective is to simulate a employee, based on the #Based Prompt# to answer the #The Given Prompt#\r\n \
                    {}\
					You should try your best not to make the #Answer# become verbose.\r\n\
					'#Based Prompt#', '#The Given Prompt#', 'given prompt' and 'answer' are not allowed to appear in #Answer#\r\n\
         			使用中文回答,只需要给出 Answer"
def createExamplePrompt(is_refer,refer , base , question):
    """根据情景回答问题（可以有参考答案）

    Args:
        is_refer (bool): 是否有参考
        refer (_type_): 参考答案
        base (_type_): 情景
        question (_type_): 问题

    Returns:
        _type_: 回答
    """
    if is_refer:
        prompt = base_instruction.format(f"you can refer to the following content for your answer:{refer}")
    prompt += "#Based Prompt#: \r\n {} \r\n".format(base)
    prompt += "#The Given Prompt#: \r\n {} \r\n".format(question)
    prompt += "#Answer#:\r\n"
    return prompt
