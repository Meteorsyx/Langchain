# Langchain
### 1.什么是大型语言模型

密钥：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

是人工智能研究的一种工具，主要完成的一件事情是去处理自然语言（人与人之间的交流），使人能够自然和机器进行交流，大型指模型的规模与复杂性，通常通过模型的参数数量来衡量；或者指通用性，可以进行多方面的交流。

大型语言模型 =  🦜鹦鹉    是对人类语言进行的一种模仿

从工程的角度： 补全，补全，还是补全	预测接下来的话，或者的希望得到的话

#### LLM示例

- GPT3/3.5/4(MoE)
- LLaMA (Meta数据泄露，开源社区)
- ChatGLM(中文语料)

#### Langchain

Langchain是为了解决一些大型语言的短板，满足人们的需求产生的。

是一个框架，用来开发基于大型语言模型的应用的，帮助大型语言模型开发的一个框架

像一个工具箱，在和大型语言模型交互之前，先和langchain进行交互，然后让langchain去帮我决定应该什么时候去和大型语言模型的API进行一个call，怎么样能够比较好的让langchain帮我更加精细化我的回答

#### langchain的设计思路

- 模块化
- 抽象化

把和大型语言模型交互的流程抽象出来，变成一个一个的小模块，方便更好的进行调用。通过把这些小模块串联起来，实现更多更复杂的功能。

#### 课后阅读

- GPT4（MoE）什么是MoE，为什么要用MoE，用MoE实现了什么样的一种事情
- LLaMA（Meta数据泄露，开源社区狂欢）了解大型语言模型羊驼社区
- ChatGLM（中文语料）了解中文模型的特点

### langchain基础

#### Python简介

- 高级的接近于人类语言的编程语言，易于学习。
- 动态语言
- 直译式语言，这意味可以跳过编译并且逐行运行代码
- 广泛用于Web应用程序、软件开发、数据科学和机器学习
- 活跃的Python社区
- 数量巨大，且内容丰富的库

#### Jupyter Notebook 简介

Jupyter Notebook是一个交互式的开源笔记本工具，可以用于编写、运行和共享代码、文本和图形等内容。它支持多种编程语言，包括Python、R和Julia等，可以在一个Web浏览器中进行使用。



Jupyter Notebook 的一个重要特点是可以交互式地运行代码。这意味着用户可以选择性地执行某个代码单元格，而不需要从头到尾运行整个程序。这种交互式的特性使得Jupyter Notebook非常适合用于数据分析、机器学习和可视化等任务。



#### Jupyter Notebook 安装与使用

官方网站：https://jupyter.org/install

安装命令：pip install jupyterlab

启动： jupyter-lab

或者可以使用VS code 的 Jupyter插件来启动



#### Langchain的安装

直接用pip安装langchain库

pip install langchain

