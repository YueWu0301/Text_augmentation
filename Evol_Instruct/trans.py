base_instruction = "I want you act as a Employee Simulator.\r\n \
					Your objective is to simulate a employee, rewrite a given prompt in another way for text augmentation\r\n \
					Your rewriting cannot omit the non-text parts such as the table and code in #The Given Prompt#:. Also, please do not omit the input in #The Given Prompt#. \r\n \
					You SHOULD rewrite the given prompt using the following method: \r\n\
					{} \r\n\
					You should try your best not to make the #Rewritten Prompt# become verbose.\r\n\
					'#The Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#\r\n\
         			使用中文回答,直接出 rewritten prompt，其他都不要写"

def transtructure(instruction):
	prompt = base_instruction.format("Please generate prompt with the same meaning but different language structures according to #The Given Prompt# for text augmentation. \
    You can change sentence structure or reverse the order of the sentence")
	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
	prompt += "#Rewritten Prompt#:\r\n"
	return prompt

def transtyle(instruction):
	prompt = base_instruction.format("Please generate prompt with the same meaning but different language styles according to #The Given Prompt# for text augmentation. \
    The language style can be formal, informal, concise, detailed, professional, humorous, popular, etc. Randomly select one from the above styles")
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