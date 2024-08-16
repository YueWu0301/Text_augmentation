import json
import random

from openai_access import call_chatgpt
# from depth import createConstraintsPrompt, createDeepenPrompt, createConcretizingPrompt, createReasoningPrompt
from depth import createDataPrompt , createExamplePrompt
from trans import transtyle , transtructure
from breadth import createBreadthPrompt
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


def getevolprompt(instruction, type):
    """
    输入instruction 以及增广类型
    返回变换之后的文字
    
    """
    if type=='example' :
        return createExamplePrompt(instruction)
    elif type == 'data':
        return createDataPrompt(instruction)
    elif type == 'style':
        return transtyle(instruction)
    elif type == 'structure' :
        return transtructure(instruction)
    elif type == 'bread' :
        return createBreadthPrompt(instruction)
    else:
        print('use con,deep,concret,reason,bread plz')




one_1_t = []
one_1_t.append(
    '思维敏捷、逻辑强：粤海大区有遗留费用。他给我讲；遗留费用后，没有原来的负债了。从费用管控和销售策略上，一步一步实现。\
沟通很舒服：\
爱学习：看过他会议的笔记本，看过他理开会记录，都理的很清楚。一年一个本。记了要点和核心动作。\
舰长班积极发言。出差还带着书籍。\
不停的培训团队：日常跟兄弟上讲思想文化跟分工，会放个黑板讲。\
-----有待提升---\
客户在产品的销售策略和导向上应该更强一些。eg：子公司的业绩导向完成上给的指导意见少。\
需要参与大区总、运营总的行销会议。\
'
)
one_1_t.append('优势：表达能力强，非常愿意表达，愿意展现自己。善于与人沟通。情商也很高。\
说教的多，谈思想谈未来，宏观的多。\
有待发展：从战略要转到打法，从策略到动作上转变。实战业务需要进一步的打磨，向进攻导向性转移，加强夺冠的坚决信心。增长点，突破口的挖掘很关键。需要攻坚克难的锚点。\
建议：建议更多的参与实际的业务。eg：大的闭环跑一边就更了解。')

one_1_t.append('间接共事有7-8年，关于重点客户工作对接，垂直直营的对接。粤海是最大的分子公司，重客的对接。\
年轻，比较有冲劲，对目标执着，A老师干劲儿足。对组织文化认可度很高。\
粤海大区整个业务导向，每年超百达成，重客粤海是第一批，体量最大，分子公司比较多。在垂直三年基础上，大区配合上，唯一一个亮丽的交付。自己做了很多内部创新，注重团队文化搭建，经常在一起聊对团队文化上，有自己的想法。粤海做一个研发的中心，跟总部对接，区别于其他大区总自我的追求。总部可以考虑在那边布局。在本职工作以外去思考。\
执行力也很好，粤海大区历练下，协同也挺强的。客户关系和协调性做的都很好。')

one_1_t.append('19年到粤海大区总，大区品类行销，通过领导对上汇报，对下工作安排上，汇报工作的整理。储备RBU之后，由领导安排去海南实习三个月RBU经理，正式转岗位1月粤西RBU，例会，回大区面对面正式汇报。从1月到粤北。把各个省区数量增加，做了区域整合。有的转岗有的离职。\
工作认真，对事情执着，对员工思想认知统一，经常做思想指导，把控整体方向。领导有方有策略。举例：固定时间做工作以外，思想上统一，以行业、区域机会点做分析，大环境做讲解，在公司企业文化讲解。统一公司要求，五年战略和大区的未来规划。直管层级上所有人统一认知，明确粤海的发展方向。学习上发一些书，引导员工学习。中间通过几次会议，下午开会到第二天早上，形成统一认知，统一目标。私下点对点的帮扶，询问，近期重点工作和问题，对应的讲解和指导建议。项目安排后，通过自己去走访市场，发现工作是否落地，整个环节做闭环管理跟进，在群里分享优秀的案例，各个区域注意的几个方面，告诉我们机会点在哪。\
提升点：细节的管理，需要充分的授权，跟客户沟通之后，上传下达解决基础的东西，有些资源掌握在省区。能明确下来像分子公司的资源，市场整合某个资源的授权，不要卡的太死。领导追的事情比较急，会觉得繁琐，下面会觉得重复做了。可以再精简。简单的量的问题，大家按照整个去追踪，领导会追的更急更细一些。与职能的沟通，职能管控严格，来回反复沟通，增加沟通成本。')


one_1_t.append('【优势】外箱型，爱学习爱沟通，爱向上沟通，及时的平行部门沟通。爱总结，唉分享，表达能力强。\
主动跟平行大区，跟领导沟通，表达能力也好。\
笔记记的很好。\
【待发展】\
1. 它的团队，换行政换的比较频繁，行销也换的频繁。是你要求高还是什么？\
不能把自己的人培养。要互相适应。\
2. 解决问题的能力又待提升，多给客户解决问题。不能光讲大道理。')

one_1_t.append('年龄不大，有想法，敢于表达，善于和团队互动。跟大家组成团队去做事情。')


four_1_1_t = []
four_1_1_t.append('垂直发展到第二年瓶颈期，会务实给出建议，整个大区KA经理，垂直经营人才。在困境中给过很多建议。也是这样去做的，做活大区实体化。与大区融为一体。流程上给大区减负。给业务提出有效的建议。')
four_1_1_t.append('通过拜访现有经销商，认知其他企业，搜集行业信息。带着团队去拜访华为，可口可乐，进入工厂销售团队和行销做互动。外部经济人口，尼尔森数据，让大家人知道我们行业的情况。刺激团队更有信心达成目标，教导有方法。通过各个职能部门近期汇报，做整合。看出与竞品的差距，大家明确整体的盘子有多少，如何能够抢占更多份额。参考竞品动作，整合销管和行销、渠道各个节点资源，根据资源要求行程大区内部的方案。')
four_1_1_t.append('可以做职能负责人。\
它想做事业部老总（但是它缺乏领导力，不能光有行政命令，干销售得有些匪气，不能只是让它怕你，要有些领导魅力）')


four_2_1_t = []
four_2_1_t.append('下面的人整体评价，不是老的大区总的风格，能够跟团队打成一片，比较带动大家的积极性，把大家尽头鼓起来。我们大区总有职业理想和追求的人。')

four_2_2_t = []
four_2_2_t.append('粤海大区留人难。人员的流动与大区的流动有关系。大区的整体文化有关联。\
没有业绩很难生存，粤海生存成本高，做不出业绩活不下去。\
中层的管理风格偏严厉。导致离职率高。\
--------\
他从预算管理上着手（授权子公司自负盈亏），终端执行上强化')
four_2_2_t.append('团队信心比较足，在压力大的情况下，积极推动销量。疫情风控的原因，并没有放弃不完成量的想法。明确目标要达成，对着目标去推进。统一思想，明确机会点，算出目标。拆分各个职能分担多少量，明确下来后去完成。')


four_3_1_t = []
four_3_1_t.append('对自我的时间管理很好，每天早上读书听书，每周运动健身很规律，每周爬山。')


four_3_2_t = []
four_3_2_t.append('以前大区管理统一意识的次数不多，现在做了思想统一，提出六本计划，让员工有奔头。除了涨薪涨工资，自己要获得额外的物质，每年给自己定一个小目标。团队更有动力。')

four_4_1_t = []
four_4_1_t.append('每个人如何做的更好，经常做疏导，到了某一个阶段区域压力很大，觉得自己不合适做BU经理，去疏导和讲解一下机会和问题点，如何解决协助。')

four_4_2_t = []
four_4_2_t.append('与粤海这块，需要A站台，需要大区行销运营做大节大庆的时候，能够达成一致。')

four_5_1_t = []
four_5_1_t.append('例会会用粤海举例，在粤海从来没有这样的投诉，各部门与核心部门开月度例会，其他部门的策略做沟通，大家在会上达成共识。大家借力发力，一直做的比较好的。\
华润万家拖欠账款，与A总跑万家，约到高层，帮助客户把账款往回要。大区冲到前线去零售商催账款。')

four_5_2_t = []
four_5_2_t.append('坚定立场一起推进，销售都很难，从销管资源有限，也没有更多资源支持大区。')

six_1_t = []
six_1_t.append('让牛人绽放：\
培养出很多人都输送出。目前两个人对接身上，与我们做过三年的交流，粤海的KA,继任者的培养，未来可以向大区总发展。')
six_1_t.append('·+诚信+消费者\
-让牛人绽放')



num = 100

text_list = [one_1_t , four_1_1_t , four_2_1_t,four_2_2_t,four_3_1_t,four_3_2_t,four_4_1_t,four_4_2_t,four_5_1_t,four_5_2_t,six_1_t]
name_list = ['one_1_t' , 'four_1_1_t' , 'four_2_1_t','four_2_2_t','four_3_1_t','four_3_2_t','four_4_1_t','four_4_2_t','four_5_1_t','four_5_2_t','six_1_t']


  
def augment(types, num, instruction, index1):
    """
    输入增广选择types 增广数量 num=1  要增广的 instruction
    返回一个augment 的结果 是一个{}
    """
    type = random.choice(types)
    selected_evol_prompt = getevolprompt(instruction , type)
    evol_instruction = call_chatgpt(selected_evol_prompt)
    return {"type":type,"evol_prompt":evol_instruction, 'index':index1}
def process_task(index, text):
    results = []
    for x in range(num):  # 假设 num 是要重复的次数
        print(x)
        text1 = random.choice(text)
        index1 = text.index(text1)
        aug = augment(types=['style', 'structure', 'bread'], num=1, instruction=text1, index1=index1)
        results.append(aug)
    file_path = f'result_1_t/{name_list[index]}.json'
    print(file_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
print('success here')

# with ThreadPoolExecutor() as executor:
#     futures = {executor.submit(process_task, index, text): index for index, text in enumerate(text_list)}

#     # 使用tqdm显示进度条
#     for future in tqdm(futures, desc="Processing", total=len(futures)):
#         try:
#             future.result()
#         except Exception as exc:
#             print(f'Generated an exception: {exc}')
            
with ThreadPoolExecutor() as executor:
    futures = {executor.submit(process_task, index, text): index for index, text in enumerate(text_list)}

# 等待所有线程完成
for future in futures:
    try:
        future.result()
    except Exception as exc:
        print(f'Generated an exception: {exc}')