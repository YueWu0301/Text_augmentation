# Text_augmentation
Augment Text Via LLM
使用GLM， 类似于WizardLM 构建了self-evolution 演化言语策略

通过运行 main函数进行增广，main 中通过调用depth 等进行wizard 演化增广
如果想更改增广的prompt 可以从depth等里面改


通过selection_perplexity 算出perplex
通过 selection_diversity 算出diversity
selection_rank 进行总分计算以及排序

注意到 main_1_t 这些后缀： 1表示第1个人， t表示同事的评论 x表示下级（由于每个人都不齐 所以分开写的xxx）