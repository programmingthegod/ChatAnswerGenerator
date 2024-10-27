import pandas as pd
import random

# Function to generate dummy chat messages
def generate_chat():
    topics = [
        "renewable energy", "artificial intelligence"
    ] #other topics can be added
    messages = {
        "renewable energy": [
            "What are the latest advancements in renewable energy?",
            "There have been significant improvements in solar and wind technologies.",
            "Can you elaborate on the solar advancements?",
            "Sure, the efficiency of solar panels has increased dramatically.",
            "That's impressive. What about wind energy?",
            "Wind turbines are now more efficient and less expensive to maintain.",
            "How do these advancements impact the environment?",
            "They help reduce carbon emissions and reliance on fossil fuels.",
            "Are there any new innovations in this field?",
            "Yes, there are ongoing research and development in storage technologies.",
            "Storage is crucial for renewable energy. How is that progressing?",
            "Battery storage technology is advancing, making renewable energy more reliable.",
            "That's great news. What are the future prospects?",
            "The future looks promising with continuous improvements and investments.",
            "Thank you for the information!"
        ],
        "artificial intelligence": [
            "How has AI impacted various industries?",
            "AI has revolutionized healthcare, finance, and transportation.",
            "Can you give examples in healthcare?",
            "AI is used in diagnostic tools and personalized medicine.",
            "What about finance?",
            "AI helps in fraud detection and algorithmic trading.",
            "How is AI used in transportation?",
            "Self-driving cars and traffic management systems use AI.",
            "Are there ethical concerns with AI?",
            "Yes, privacy and job displacement are major concerns.",
            "What measures are being taken?",
            "Regulations and ethical guidelines are being developed.",
            "How can AI be made more ethical?",
            "By ensuring transparency and accountability in AI systems.",
            "What is the future of AI?",
            "AI will continue to grow, with more emphasis on ethical use.",
            "Thank you for the insights!"
        ]
        # Additional topics can be added similarly
    }
    topic = random.choice(topics)
    return messages[topic], topic

# Function to generate dummy MCQs based on the topic
def generate_mcqs(topic):
    mcqs = {
        "renewable energy": [
            {
                "question": "What is one of the latest advancements in solar technology?",
                "correct_answer": "Increased efficiency of solar panels.",
                "distractors": [
                    "Decrease in solar panel prices.",
                    "New types of solar power plants.",
                    "Increased size of solar panels."
                ]
            },
            {
                "question": "How do advancements in wind energy benefit the environment?",
                "correct_answer": "They help reduce carbon emissions.",
                "distractors": [
                    "They increase energy consumption.",
                    "They cause more pollution.",
                    "They make energy more expensive."
                ]
            }
        ],
        "artificial intelligence": [
            {
                "question": "How has AI impacted healthcare?",
                "correct_answer": "AI is used in diagnostic tools and personalized medicine.",
                "distractors": [
                    "AI is used to increase hospital costs.",
                    "AI is used to reduce patient care quality.",
                    "AI is used to create new diseases."
                ]
            },
            {
                "question": "What is a major concern with AI?",
                "correct_answer": "Privacy and job displacement.",
                "distractors": [
                    "Increased production costs.",
                    "Reduced technological growth.",
                    "Less data availability."
                ]
            }
        ]
        # Additional topics can be added similarly
    }
    return mcqs[topic]

# Function to generate dummy articles based on the topic
def generate_article(topic):
    articles = {
        "renewable energy": (
            "Recent advancements in renewable energy have shown significant improvements, particularly in solar and wind technologies. "
            "Solar panels have seen a dramatic increase in efficiency, making them more effective in harnessing sunlight. "
            "Similarly, wind turbines have become more efficient and less costly to maintain. "
            "These advancements contribute to reducing carbon emissions and decreasing reliance on fossil fuels. "
            "Ongoing research in storage technologies, especially battery storage, is crucial for making renewable energy more reliable. "
            "The future of renewable energy looks promising with continuous improvements and investments."
        ),
        "artificial intelligence": (
            "Artificial intelligence (AI) has had a profound impact on various industries, including healthcare, finance, and transportation. "
            "In healthcare, AI is used in diagnostic tools and personalized medicine, improving patient outcomes. "
            "In finance, AI helps in fraud detection and algorithmic trading, enhancing security and efficiency. "
            "Transportation has benefited from AI through self-driving cars and advanced traffic management systems. "
            "Despite its advantages, AI raises ethical concerns, such as privacy issues and job displacement. "
            "To address these, regulations and ethical guidelines are being developed, emphasizing transparency and accountability. "
            "The future of AI is promising, with continued growth and a focus on ethical use."
        )
        # Additional topics can be added similarly
    }
    return articles[topic]

# Generating dataset
data = {
    "Chat ID": [],
    "Messages": [],
    "MCQ": [],
    "Correct Answer": [],
    "Distractors": [],
    "Article": []
}

num_entries = 2000
for i in range(num_entries):
    chat, topic = generate_chat()
    mcqs = generate_mcqs(topic)
    article = generate_article(topic)
    chat_id = i + 1
    for mcq in mcqs:
        data["Chat ID"].append(chat_id)
        data["Messages"].append(chat)
        data["MCQ"].append(mcq["question"])
        data["Correct Answer"].append(mcq["correct_answer"])
        data["Distractors"].append(mcq["distractors"])
        data["Article"].append(article)

df = pd.DataFrame(data)
df.to_csv("chat_mcq_article_dataset.csv", index=False)
