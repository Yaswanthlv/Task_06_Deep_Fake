from gtts import gTTS
import os

# Interview Q&A
dialogue = [
    ("Interviewer", "Hey Claude! Welcome back. Today, I’ve got the World Happiness Report 2019 dataset with me. Let’s walk through some insights together — ready?"),
    ("Claude", "Absolutely! Let’s dive into the data and find out what makes countries happy."),

    ("Interviewer", "Let’s start simple — which country tops the happiness list in this report?"),
    ("Claude", "That would be Finland, with a happiness score of 7.769. They've been consistently leading the charts for several years."),

    ("Interviewer", "And on the other end — who’s unfortunately at the bottom?"),
    ("Claude", "South Sudan, with a score of 2.853. The country has faced ongoing conflict and economic hardship, which reflects in its happiness ranking."),

    ("Interviewer", "How many countries are represented in this dataset?"),
    ("Claude", "The dataset includes 156 countries."),

    ("Interviewer", "What’s the average happiness score across all these countries?"),
    ("Claude", "The global average is around 5.41. So, countries scoring above that can be considered relatively happier than the global norm."),

    ("Interviewer", "Interesting. Which 5 countries have the highest GDP per capita?"),
    ("Claude", "Here's the top 5: 1. Qatar (1.684), 2. Luxembourg (1.609), 3. Singapore (1.572), 4. United Arab Emirates (1.503), 5. Kuwait (1.500)."),

    ("Interviewer", "Out of all the factors, which one is most positively linked with happiness?"),
    ("Claude", "GDP per capita shows the strongest correlation — around 0.794 — with happiness. More wealth per person tends to predict higher happiness, generally."),

    ("Interviewer", "What about life expectancy — what’s the average?"),
    ("Claude", "The average healthy life expectancy across all countries is approximately 0.725 (normalized score)."),

    ("Interviewer", "Who’s the most generous country according to this report?"),
    ("Claude", "Myanmar stands out, with a generosity score of 0.566."),

    ("Interviewer", "If a country wants to boost its happiness score by 1 point, which single factor should it invest in first — and why?"),
    ("Claude", "Definitely GDP per capita. It has the strongest positive correlation and varies significantly between countries — so increasing it can have a high payoff."),

    ("Interviewer", "Can you rank the six main factors by how much they contribute to happiness?"),
    ("Claude", "Sure! Based on correlation: 1. GDP per capita — 0.794, 2. Healthy life expectancy — 0.780, 3. Social support — 0.777, 4. Freedom to make life choices — 0.567, 5. Perceptions of corruption — 0.386, 6. Generosity — 0.076."),

    ("Interviewer", "Which country is the best all-rounder if we normalize and average all six contributing factors equally?"),
    ("Claude", "That would be Singapore — it performs well across all dimensions."),

    ("Interviewer", "Are there any generous countries that aren’t exactly happy?"),
    ("Claude", "Yes — countries like Myanmar, Haiti, Kenya, Gambia, Syria, and Comoros rank high in generosity but have below-average happiness scores."),

    ("Interviewer", "Is there a clear social support threshold above which countries tend to be happier?"),
    ("Claude", "Yes — countries with social support greater than or equal to 1.44 tend to have happiness scores above 7. That seems to be a strong threshold."),

    ("Interviewer", "Any patterns between corruption perceptions and happiness?"),
    ("Claude", "Yes — there’s a positive correlation of about 0.386. Countries perceived as less corrupt are generally happier."),

    ("Interviewer", "Are there outliers — countries that are happier than their GDP would suggest?"),
    ("Claude", "Definitely! Countries like Costa Rica, Finland, Somalia, Guatemala, Nicaragua, and others show higher happiness than predicted by GDP alone — likely due to strong social support or freedom."),

    ("Interviewer", "Last one — if I’m advising low-happiness countries, where should we start improving?"),
    ("Claude", "Again, GDP per capita is your best bet. The gap between the top 10 and bottom 20 countries is widest there, so improving that can yield big gains."),

    ("Interviewer", "Claude, thank you for your insights! That was enlightening."),
    ("Claude", "Always happy to help make the world a bit brighter with data!")
]

# Output directory
output_dir = "outputs/audio"
os.makedirs(output_dir, exist_ok=True)

# Step 1: Generate individual mp3s
temp_files = []
for i, (speaker, line) in enumerate(dialogue):
    filename = os.path.join(output_dir, f"line_{i:02d}_{speaker}.mp3")
    tts = gTTS(text=line, lang="en")
    tts.save(filename)
    temp_files.append(filename)
    print(f"✅ Saved: {filename}")

# Step 2: Merge into one MP3 (no ffmpeg, just binary append)
final_output = "outputs/interview_audio.mp3"
with open(final_output, "wb") as merged:
    for file in temp_files:
        with open(file, "rb") as f:
            merged.write(f.read())

print(f"\n🎧 Merged interview saved to: {final_output}")
