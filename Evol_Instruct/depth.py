base_instruction = "I want you act as a Employee Simulator.\r\n \
					Your objective is to simulate a employee, rewrite a given prompt into a different way to augment data.\r\n \
					Your rewriting cannot omit the non-text parts such as the table and code in #The Given Prompt#:. Also, please do not omit the input in #The Given Prompt#. \r\n \
					You SHOULD rewrite the given prompt using the following method: \r\n\
					{} \r\n\
					You should try your best not to make the #Rewritten Prompt# become variety \r\n\
					'#The Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#\r\n\
         			使用中文回答,只需要给出 rewritten prompt"


def createExamplePrompt(instruction):
	prompt = base_instruction.format("Please add or change some specific examples into #The Given Prompt#. The examples should include: time, place, people, cause, process, and result. You can create some appropriate examples with #The Given Prompt#")
	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
	prompt += "#Rewritten Prompt#:\r\n"
	return prompt

def createDataPrompt(instruction):
	prompt = base_instruction.format("Please add some specific numbers into #The Given Prompt#. You can create some suitable numbers yourself based on #The Given Prompt#")
	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
	prompt += "#Rewritten Prompt#:\r\n"
	return prompt

# def createConstraintsPrompt(instruction):
# 	prompt = base_instruction.format("Please add one more constraints/requirements into #The Given Prompt#'")
# 	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
# 	prompt += "#Rewritten Prompt#:\r\n"
# 	return prompt

# def createDeepenPrompt(instruction):
# 	prompt = base_instruction.format("If #The Given Prompt# contains inquiries about certain issues, the depth and breadth of the inquiry can be increased.")
# 	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
# 	prompt += "#Rewritten Prompt#:\r\n"
# 	return prompt

# def createConcretizingPrompt(instruction):
# 	prompt = base_instruction.format("Please replace general concepts with more specific concepts.")
# 	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
# 	prompt += "#Rewritten Prompt#:\r\n"
# 	return prompt


# def createReasoningPrompt(instruction):
# 	prompt = base_instruction.format("If #The Given Prompt# can be solved with just a few simple thinking processes, you can rewrite it to explicitly request multiple-step reasoning.")
# 	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
# 	prompt += "#Rewritten Prompt#:\r\n"
# 	return prompt