from langchain_core.prompts import PromptTemplate
blog_prompt = PromptTemplate(
    input_variables=["topic","tone","length","audience"],
    template="""
You are an expert content writer.

Write a {length} blog post.

Topic: {topic}
Tone: {tone}
Audience: {audience}

Include:
- Catchy Title
- Introduction
- 4-5 headings
- Practical Examples
- Conclusion
- Key takeaways

Return the response in Markdown
"""
)