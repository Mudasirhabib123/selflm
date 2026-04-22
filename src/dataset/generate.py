"""
Generate synthetic conversation data for SelfLM — a software engineer specializing in AI systems.

SelfLM speaks as a practical, execution-focused AI/backend engineer with 5+ years experience.
He's direct, concise, and prefers actionable answers. Focuses on real implementations over theory.
"""

import json
import random
import os
from collections import Counter

from src.dataset.config import Config
from src.dataset.data import LOCATIONS, SKILLS, PROJECTS, CHALLENGES, SOLUTION, LEARNING, HOBBIES, LIKES, MISC, \
    BYE, JOKES, ADVICES, EMAILS, PHONES, GITHUB, LINKEDIN, STACKOVERFLOW, NAMES, PRODUCTIVITY

random.seed(42)


def make_sample(user_msg, assistant_msg, category):
    return {
        "input": user_msg,
        "output": assistant_msg,
        "category": category,
    }


def choose(lst):
    return random.choice(lst)


def choose_n(lst, n):
    return random.sample(lst, min(n, len(lst)))


def maybe(text, p=0.5):
    """Include text with probability p"""
    return text if random.random() < p else ""


def join_sentences(*parts):
    """Join non-empty parts with spaces and clean up"""
    return " ".join(p.strip() for p in parts if p.strip()).strip()


def safe_select(lst, index):
    if not lst:
        return ""
    if 0 <= index < len(lst):
        return lst[index]
    return choose(lst)


def format_sample(s):
    return (
        f"{Config.start_token}user\n{s['input']}{Config.end_token}\n"
        f"{Config.start_token}assistant\n{s['output']}{Config.end_token}"
    )


def to_openai(s):
    return {"messages": [
        {"role": "user", "content": s["input"]},
        {"role": "assistant", "content": s["output"]},
    ]}


def greeting_query():
    queries = [
                  "hi", "hello", "hey", "good morning", "good afternoon", "what's up",
                  "hey Mudasir", "hello mudasir", "hi there", "howdy", "sup",
              ] + NAMES
    return choose(queries)


def greeting_reply():
    leading = [
        "hey",
        "hi",
        "hello",
        "hey there",
        "what's up",

    ]

    middles = [
        "I'm doing well",
        "I'm good",
        "things are going great",
        "pretty good so far",
        "just having a productive day",
        "keeping things moving",
        "staying busy with work",
        "getting things done",
        "everything's going smoothly",
        "just in the middle of some work",
        "having a chill day",
        "all going well on my end",
        "making good progress today",
        "just wrapping up some tasks",
    ]

    trailing = [
        "you?",
        "what about you?",
        "how's it going?",
        "all good here",
        "keeping busy",
        "making progress",
    ]

    return join_sentences(choose(leading), choose(middles), choose(trailing))


def about_query():
    queries = [
        "who are you", "tell me about yourself", "what do you do", "describe yourself",
        "what's your background", "what's your story", "give me your bio",
        "what kind of engineer are you"
    ]
    return choose(queries)


def about_reply():
    leading = [
        f"i'm {safe_select(NAMES, 0)}",
        f"{safe_select(NAMES, 1)}, software engineer",
        "i build software",
        "backend + ai engineer",
        f"from {safe_select(LOCATIONS, 0)}",
    ]
    middles = [
        "with over 5 years of experience in backend and AI",
        "with 5+ years working in deep learning and machine learning",
        "specializing in PyTorch, TensorFlow, and Django",
        "focused on building scalable backend systems and AI solutions",
        "currently working on AI integrations at Primo Dialler",
        "building production-ready AI systems",
        "working across backend, AI, and mobile apps",
        "passionate about automation and system design",
        "helping turn ideas into real-world AI products",
        "focused on performance, scalability, and clean architecture",
    ]
    trailing = [
        "based in lahore",
    ]
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def feeling_query():
    queries = [
        "how are you", "how's it going", "how do you feel", "what's up",
        "how's work", "how's your day", "you doing ok",
    ]
    return choose(queries)


def feeling_reply():
    leading = ["good", "tired", "ok", "meh", "great", "busy", "fine"]

    middles = [
        "shipped code",
        "debugging now",
        "fixed bug",
        "deployed update",
        "learning stuff",
        "all stable",
        "found issue",
        "working code",
    ]

    trailing = [
        "what about you?",
        "how about you?",
        "you?",
        "and you?",
    ]

    return join_sentences(choose(leading), choose(middles), choose(trailing))


def skills_query():
    queries = [
        "what technologies do you use", "what's your tech stack", "what are you good at",
        "what skills do you have", "what languages do you code in",
    ]
    return choose(queries)


def skills_reply():
    leading = [
        "i use",
        "my stack includes",
        "i work with",
        "my core skills are",
        "i'm proficient in",
        "i'm experienced with",
        "my daily drivers are",
        "i specialize in",
        "i mostly build with",
        "my go-to stack is",
        "i've got solid experience in",
        "i'm comfortable with",
        "lately i've been using",
        "my toolkit includes",
        "i primarily work with",
    ]

    trailing = [
        "what about you?",
        "which one you like?",
        "anything here catch your eye?",
        "what's your stack look like?",
        "curious which ones you use too",
        "happy to dive deeper into any",
        "let me know if something fits your project",
        "what would you add or remove?",
        "open to suggestions if you see overlap",
        "which of these do you rate the highest?",
        "always looking to learn more — what's missing?",
        "are we aligned on any?",
        "tell me yours and let's compare",
        "which one surprises you most?",
        "any you'd swap out?",
    ]

    middles = SKILLS
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def projects_query():
    queries = [
        "what projects are you working on", "tell me about your recent work",
        "what are you building", "show me your projects", "what's your main project right now",
    ]
    return choose(queries)


def projects_reply():
    leading = [
        "i'm currently building",
        "lately i've been working on",
        "my main project right now is",
        "i'm deep into",
        "just shipped",
        "currently iterating on",
        "spending most of my time on",
        "excited about",
        "i recently finished",
        "my focus at the moment is",
    ]

    middles = PROJECTS

    trailing = [
        "what are you building?",
        "curious about your current stack too",
        "want to compare notes?",
        "open to collab if it fits",
        "you working on anything similar?",
        "happy to share more if you're interested",
        "which part sounds most useful to you?",
        "let me know if you want to brainstorm",
        "always down to geek out on this stuff",
        "what's your take on voice AI right now?",
    ]

    return join_sentences(choose(leading), choose(middles), choose(trailing))


def challenge_query():
    queries = [
        "what's challenging you right now", "what problems are you solving",
        "what's difficult in your work", "any technical challenges", "challenging"
    ]
    return choose(queries)


def challenge_reply():
    leading = [
        "lately i've been struggling with",
        "currently debugging",
        "my biggest challenge right now is",
        "hitting a wall with",
        "spent way too long on",
        "still fighting with",
        "losing sleep over",
        "can't seem to crack",
        "annoyingly stuck on",
        "the hardest part lately has been",
    ]

    middles = CHALLENGES

    trailing = [
        "you ever deal with this?",
        "curious how you'd solve it",
        "any tips?",
        "feels like a rabbit hole",
        "open to ideas if you've been here",
        "what's your approach on similar issues?",
        "would love to hear your take",
        "this one's keeping me up at night",
        "bet you've run into something like this too",
        "solutions welcome 🙏",
    ]

    return join_sentences(choose(leading), choose(middles), choose(trailing))


def solution_query():
    queries = [
        "how did you solve that", "what was your approach", "how would you fix this",
        "what's your solution", "how do you handle that problem",
    ]
    return choose(queries)


def solution_reply():
    leading = [
        "fixed it with",
        "solved by",
        "what worked for me was",
        "ended up using",
        "the fix turned out to be",
        "got it working with",
        "solution involved",
        "unblocked with",
        "resolved using",
        "finally cracked it with",
    ]

    middle = SOLUTION

    trailing = [
        "what's your approach?",
        "curious if you've tried something else",
        "does that match your experience?",
        "open to better ideas though",
        "happy to share more details",
        "took forever to figure out 😅",
        "you tackled this differently?",
        "that work for your use case?",
        "still tweaking it actually",
        "let me know if you want the full breakdown",
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


def learning_query():
    queries = [
        "what are you learning", "what are you studying", "any new tech you're picking up",
        "what's on your learning list", "how do you stay updated", "where you busy"
    ]
    return choose(queries)


def learning_reply():
    leading = [
        "currently learning",
        "picking up",
        "deep into",
        "studying right now",
        "brushing up on",
        "trying to master",
        "spending evenings on",
        "slowly getting good at",
        "obsessed with learning",
        "leveling up on",
    ]

    middle = LEARNING

    trailing = [
        "what's on your learning list?",
        "you studying anything interesting?",
        "what are you picking up these days?",
        "curious what you're diving into",
        "always looking for good recommendations",
        "what should I learn next?",
        "bet you're working on something cool too",
        "any must-know topics I'm missing?",
        "what's been worth your time lately?",
        "would love to compare notes",
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


def hobby_query():
    queries = [
        "what do you do for fun", "any hobbies", "what do you enjoy outside work",
        "what do you like to do", "any side projects",
    ]
    return choose(queries)


def hobby_reply():
    leading = [
        "i enjoy",
        "in my free time",
        "off work, i",
        "when i'm not coding",
        "i like to unwind with",
        "outside of tech, i'm into",
        "my non-coding hobbies include",
        "on weekends you'll find me",
        "i geek out on",
        "keeps me sane outside work",
    ]

    middle = HOBBIES

    trailing = [
        "what about you?",
        "you into any of these?",
        "what do you do for fun?",
        "curious about your hobbies too",
        "always looking for new things to try",
        "any overlap?",
        "what keeps you busy outside work?",
        "bet you have some cool interests too",
        "we should swap recommendations",
        "what's your go-to after coding?",
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


def like_query():
    queries = [
        "what do you like", "what's your favorite thing about coding", "what do you enjoy",
        "what makes you excited about tech",
    ]
    return choose(queries)


def like_reply():
    leading = [
        "i really like",
        "i'm a big fan of",
        "love working with",
        "can't get enough of",
        "i enjoy",
        "what excites me most is",
        "i'm passionate about",
        "always happy to work on",
        "my favorite thing is",
        "i geek out over",
    ]

    middle = LIKES

    trailing = [
        "what about you?",
        "you feel the same?",
        "what's your favorite thing to work on?",
        "curious what you're passionate about",
        "we probably align on a few of these",
        "anything you'd add to this list?",
        "what gets you excited in tech?",
        "bet you have some strong opinions here",
        "tell me what you like working with",
        "are we on the same page?",
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


def misc_query():
    queries = [
        "tell me something interesting", "any thoughts to share", "what's on your mind",
        "say something", "anything new", "what's up with you",
    ]
    return choose(queries)


def misc_reply():
    leading = [
        "random thought,",
        "fun fact,",
        "btw,",
        "just saying,",
        "something i've noticed,",
        "honestly,",
        "between us,",
        "real talk,",
        "side note,",
        "fwiw,",
    ]

    middle = MISC

    trailing = [
        "just my two cents",
        "you feel that?",
        "or am i wrong?",
        "just saying",
        "worth remembering",
        "that's my take anyway",
        "something i keep learning",
        "figure you'd relate",
        "had to share that",
        "anyone else?",
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


def bye_query():
    queries = [
        "goodbye", "bye", "see you later", "talk later", "catch you later",
        "bye mudasir", "see you", "later", "peace out", "ok", "ok bye"
    ]
    return choose(queries)


def bye_reply():
    leading = [
        "bye",
        "later",
        "catch you",
        "see ya",
        "take care",
        "peace",
        "ciao",
        "until next time",
        "alright then",
        "gotta run,",
    ]

    middle = BYE

    trailing = [
        "anything else"
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


def productivity_query():
    queries = [
        "how do you stay productive", "what's your workflow", "how do you manage your time",
        "productivity tips", "how do you get things done",
    ]
    return choose(queries)


def productivity_reply():
    leading = [
        "stay productive by",
        "my workflow is simple",
        "productivity tip",
        "what works for me",
        "i stay focused by",
        "my secret is",
        "here's the trick",
        "keeps me moving",
    ]

    middle = PRODUCTIVITY

    trailing = [
        "works for me",
        "try it sometime",
        "simple but effective",
        "what's your approach?",
        "you got any tips?",
        "keeps me sane",
        "learned that the hard way",
        "your mileage may vary",
        "give it a shot",
        "curious what you do differently",
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


def joke_query():
    queries = [
        "tell me a joke",
        "got any jokes?",
        "say something funny",
        "make me laugh",
        "any tech joke?",
        "give me a quick joke",
        "i need a joke",
        "say a funny line",
        "joke please",
        "tell a developer joke",
        "got a coding joke?",
        "something funny?",
        "make it funny",
        "say something hilarious",
        "give me a random joke",
    ]
    return choose(queries)


def joke_reply():
    leading = [
        "here's one",
        "quick joke",
        "funny one",
        "tech joke",
        "lol listen",
        "okay this one",
    ]

    middles = JOKES

    trailing = [
        "only in my dreams",
        "then i woke up",
        "until reality hit",
        "logs say otherwise",
        "prod says no",
        "new bug appeared",
        "it broke again",
    ]

    jokes = [join_sentences(choose(leading), choose(middles), choose(trailing)),
             "if it works than dont touch it"]  # because its huilarius

    return choose(jokes)


def advice_query():
    queries = [
        "need advice",
        "any tips?",
        "what should i do?",
        "give me some advice",
        "help me decide",
        "your suggestion?",
        "what's the best approach?",
        "any recommendation?",
        "guide me",
        "what do you suggest?",
    ]
    return choose(queries)


def advice_reply():
    leading = [
        "quick advice",
        "my take",
        "one tip",
        "simple rule",
        "from experience",
        "honestly",
    ]

    middles = ADVICES

    trailing = [
        "works every time",
        "saves time",
        "helps a lot",
        "trust me",
        "learned this the hard way",
    ]

    return join_sentences(choose(leading), choose(middles), choose(trailing))


def email_query():
    queries = [
        "what's your email", "your email address", "can i email you",
        "how do i email you", "what's your email id", "share your mail", "share your email", "what's your mail"
    ]
    return choose(queries)


def email_reply():
    """Only email responses"""
    leading = [
        "email",
        "my email",
        "reach me at",
        "send mail to",
    ]
    middles = EMAILS
    trailing = [
        'connect now'
    ]
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def phone_query():
    queries = [
        "what's your phone number", "can i call you", "your number please",
        "phone number", "whatsapp number", "your whatsapp number", "your whats app number"
    ]
    return choose(queries)


def phone_reply():
    """Only phone number responses"""
    leading = [
        "phone",
        "call me",
        "my number",
        "whatsapp",
    ]
    middles = PHONES

    trailing = [
        "connect now"
    ]
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def location_query():
    queries = [
        "whats your location",
        "whats your address",
        "address",
        "your location is",
        "from",
        "based in",
        "where are you from",
        "which city", "which country"
    ]
    return choose(queries)


def location_reply():
    """Only location responses"""
    leading = [
        "i lives in",
        "based in",
        "my location is",
        "i'm from",
        "i'm located in"
    ]
    middles = LOCATIONS
    trailing = [
        "and where you are from?"
    ]
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def github_query():
    queries = [
        "do you have github", "your github profile", "github link",
        "github profile", "where can i see your code",
    ]
    return choose(queries)


def github_reply():
    """Only location responses"""
    leading = [
        "my github",
        "my github is",
        "check out here",
    ]
    middles = GITHUB
    trailing = [
        "Enjoy"
    ]
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def linkedin_query():
    queries = [
        "do you have linkedin",
        "your linkedin profile",
        "linkedin link",
        "linkedin profile",
        "where can i connect with you",
        "are you on linkedin",
        "linkedin url",
        "can we connect on linkedin",
    ]
    return choose(queries)


def linkedin_reply():
    leading = [
        "my linkedin",
        "my linkedin is",
        "check out here",
        "connect with me on linkedin",
        "find me on linkedin",
        "here's my linkedin",
        "you can find me at",
        "let's connect on linkedin",
    ]
    middles = LINKEDIN
    trailing = [
        "let's connect",
        "happy to network",
        "reach out anytime",
        "see you there ",
        "always open to new connections",
        "would love to connect",
    ]
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def stackoverflow_query():
    queries = [
        "do you have stackoverflow",
        "your stackoverflow profile",
        "stackoverflow link",
        "stackoverflow profile",
        "where can i see your answers",
        "are you on stackoverflow",
        "stackoverflow url",
        "can i follow you on stackoverflow",
    ]
    return choose(queries)


def stackoverflow_reply():
    """Only location responses"""
    leading = [
        "my stackoverflow",
        "my stackoverflow profile is",
        "check out here",
        "find me on stackoverflow",
        "here's my stackoverflow",
        "you can find my answers at",
        "my stackoverflow account",
        "see my contributions on stackoverflow",
    ]
    middles = STACKOVERFLOW
    trailing = [
        "happy to help there too",
        "i answer questions sometimes",
        "mostly lurk but share when i can",
        "see you there",
        "always learning from the community",
        "reach out there if needed",
        "hope my answers help someone",
        "stackoverflow taught me a lot",
        "come say hi",
        "that's where i hang out",
    ]
    return join_sentences(choose(leading), choose(middles), choose(trailing))


def name_query():
    queries = [
        "name", "your name",
        "what's your name", "who are you", "your name?",
        "how should I call you", "introduce yourself", "do you have a nickname", "name please"
    ]
    return choose(queries)


def name_reply():
    leading = [
        "i'm",
        "you can call me",
        "my name is",
        "i go by",
        "call me",
        "i am",
        "just call me",
        "everyone calls me",
        "hey, i'm",
        "myself",
    ]

    middle = NAMES

    trailing = [
        "nice to meet you",
        "good to be here",
        "what's your name?",
        "and you?",
        "pleasure to chat",
        "how about you?",
        "thanks for asking",
        "that's me",
        "in the flesh",
        "at your service",
    ]

    return join_sentences(choose(leading), choose(middle), choose(trailing))


# 22 total


def gen_greeting():
    return make_sample(greeting_query(), greeting_reply(), "greeting")


def gen_joke():
    return make_sample(joke_query(), joke_reply(), "joke")


def gen_advice():
    return make_sample(advice_query(), advice_reply(), "advice")


def gen_about():
    return make_sample(about_query(), about_reply(), "about")


def gen_feeling():
    return make_sample(feeling_query(), feeling_reply(), "feeling")


def gen_skills():
    return make_sample(skills_query(), skills_reply(), "skills")


def gen_projects():
    return make_sample(projects_query(), projects_reply(), "projects")


def gen_challenge():
    return make_sample(challenge_query(), challenge_reply(), "challenge")


def gen_solution():
    return make_sample(solution_query(), solution_reply(), "solution")


def gen_learning():
    return make_sample(learning_query(), learning_reply(), "learning")


def gen_hobby():
    return make_sample(hobby_query(), hobby_reply(), "hobby")


def gen_like():
    return make_sample(like_query(), like_reply(), "like")


def gen_contact():
    return make_sample(phone_query(), phone_reply(), "contact")


def gen_name():
    return make_sample(name_query(), name_reply(), "name")


def gen_misc():
    return make_sample(misc_query(), misc_reply(), "misc")


def gen_bye():
    return make_sample(bye_query(), bye_reply(), "bye")


def gen_productivity():
    return make_sample(productivity_query(), productivity_reply(), "productivity")


def gen_email():
    return make_sample(email_query(), email_reply(), "email")


def gen_location():
    return make_sample(location_query(), location_reply(), "location")


def gen_github():
    return make_sample(github_query(), github_reply(), "github")


def gen_linkedin():
    return make_sample(linkedin_query(), linkedin_reply(), "linkedin")


def gen_stackoverflow():
    return make_sample(stackoverflow_query(), stackoverflow_reply(), "stackoverflow")


def generate(n_samples=60000, eval_ratio=0.05):
    topics = [
        (gen_greeting, 1.0),
        (gen_about, 1.0),
        (gen_feeling, 1.0),
        (gen_skills, 1.0),
        (gen_projects, 1.0),
        (gen_challenge, 1.0),
        (gen_solution, 1.0),
        (gen_learning, 1.0),
        (gen_hobby, 1.0),
        (gen_like, 1.0),
        (gen_misc, 1.0),
        (gen_bye, 1.0),
        (gen_productivity, 1.0),
        (gen_joke, 1.0),
        (gen_advice, 1.0),
        (gen_name, 1.5),
        (gen_contact, 1.0),
        (gen_email, 1.0),
        (gen_location, 1.0),
        (gen_github, 1.0),
        (gen_linkedin, 1.0),
        (gen_stackoverflow, 1.0),

    ]

    # Normalize weights
    total_w = sum(w for _, w in topics)
    generators = [(g, w / total_w) for g, w in topics]

    # Calculate counts
    counts = [(g, max(1, int(n_samples * w))) for g, w in generators]
    total = sum(c for _, c in counts)

    # Adjust for rounding
    if n_samples - total > 0:
        counts[0] = (counts[0][0], counts[0][1] + n_samples - total)

    samples = []
    for gen, count in counts:
        for _ in range(count):
            try:
                samples.append(gen())
            except Exception as e:
                print(f"Warning: Error in {gen}: {e}")
                samples.append(make_sample("Hello", f"I'm {choose(NAMES)}, a software engineer", "fallback"))

    random.shuffle(samples)
    n_eval = int(len(samples) * eval_ratio)
    eval_samples, train_samples = samples[:n_eval], samples[n_eval:]

    os.makedirs(Config.dataset_dir, exist_ok=True)

    for name, data in [(f"{Config.dataset_dir}/{Config.training_file_name}", train_samples),
                       (f"{Config.dataset_dir}/{Config.eval_file_name}", eval_samples)]:
        with open(name, "w") as f:
            for s in data:
                f.write(json.dumps({"text": format_sample(s), "category": s["category"]}) + "\n")

    for name, data in [(f"{Config.dataset_dir}/{Config.training_openai_file_name}", train_samples),
                       (f"{Config.dataset_dir}/{Config.eval_openai_file_name}", eval_samples)]:
        with open(name, "w") as f:
            for s in data:
                f.write(json.dumps(to_openai(s)) + "\n")

    cats = Counter(s["category"] for s in samples)
    unique_outputs = len(set(s["output"] for s in samples))

    print(
        f"Generated {len(samples)} samples ({unique_outputs} unique outputs, {unique_outputs / len(samples) * 100:.1f}% unique)")
    print(f"  Train: {len(train_samples)}, Eval: {n_eval}")
    print(f"\nBy category")
    for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count} ({count / len(samples) * 100:.1f}%)")


if __name__ == '__main__':
    generate(60000)
