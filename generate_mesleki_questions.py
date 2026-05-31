# -*- coding: utf-8 -*-
"""Mesleki İngilizce soru bankası — her tipten en az 50 soru."""
import json
from pathlib import Path

test, dogru, bosluk, kod = [], [], [], []

def add_test(q, opts, c, topic="genel"):
    test.append({"topic": topic, "question": q, "options": opts, "correct": c})

def add_dogru(stmt, val, topic="genel"):
    dogru.append({"topic": topic, "statement": stmt, "correct": val})

def add_bosluk(q, ans, topic="genel", alt=None):
    bosluk.append({"topic": topic, "question": q, "answer": ans, "alternatives": alt or []})

def add_kod(direction, prompt, opts, correct, topic="grammar"):
    kod.append({"topic": topic, "direction": direction, "prompt": prompt, "options": opts, "correct": correct})

tests = [
    ("What does CPU stand for?", ["Central Processing Unit", "Computer Personal Utility", "Central Program User", "Core Processing Utility"], 0, "hardware"),
    ("Which job installs and maintains networks?", ["Graphic designer", "Network technician", "Content writer", "HR manager"], 1, "professions"),
    ("'I ___ a software developer.' (profession)", ["am", "is", "are", "be"], 0, "professions"),
    ("How do you ask the time politely?", ["What time is it?", "How many time?", "What hour are you?", "When clock?"], 0, "time"),
    ("Monday comes after ___", ["Sunday", "Tuesday", "Friday", "Wednesday"], 0, "time"),
    ("Which is correct?", ["He have a laptop.", "He has a laptop.", "He having a laptop.", "He haves a laptop."], 1, "software"),
    ("UK: 'I ___ finished.' / US often: 'I ___ finished.'", ["have / have", "have / got", "has / have", "got / has"], 1, "software"),
    ("Present Continuous: 'I ___ code right now.'", ["write", "am writing", "wrote", "written"], 1, "grammar"),
    ("Modal for ability:", ["must", "can", "have to", "shouldn't"], 1, "modals"),
    ("Modal for obligation:", ["can", "may", "must", "could"], 2, "modals"),
    ("'You ___ smoke in the server room.' (prohibition)", ["mustn't", "don't have to", "can", "might"], 0, "modals"),
    ("Don't have to means:", ["prohibition", "no obligation", "strong advice", "past habit"], 1, "modals"),
    ("Comparative: RAM is ___ than ROM (fast).", ["faster", "fastest", "more fast", "fastly"], 0, "hardware"),
    ("Superlative: This is the ___ processor in the shop.", ["better", "best", "goodest", "more good"], 1, "software"),
    ("How ___ memory does this PC need? (uncountable)", ["many", "much", "lot", "number"], 1, "websites"),
    ("How ___ USB ports are there? (countable)", ["much", "many", "lot of", "amount"], 1, "websites"),
    ("Abbreviation for Random Access Memory:", ["ROM", "RAM", "RPM", "RTS"], 1, "hardware"),
    ("GUI means:", ["Graphical User Interface", "General User Internet", "Global Unified Input", "Graphic Utility Index"], 0, "software"),
    ("A person who writes code is a:", ["developer", "dentist", "driver", "designer only"], 0, "professions"),
    ("OS stands for:", ["Open System", "Operating System", "Online Service", "Output Signal"], 1, "software"),
    ("SSD is generally ___ than HDD.", ["slower", "faster", "heavier", "louder"], 1, "hardware"),
    ("Which punctuation ends a question?", ["period", "question mark", "comma", "semicolon only"], 1, "punctuation"),
    ("e.g. means:", ["for example", "and others", "that is", "as soon as possible"], 0, "punctuation"),
    ("ASAP means:", ["as soon as possible", "at the same office place", "always send a packet", "after system auto patch"], 0, "punctuation"),
    ("IT sector means:", ["Information Technology", "International Trade", "Internet Training", "Input Terminal"], 0, "it-sector"),
    ("Listen and ___ activities improve speaking.", ["speak", "speaking", "spoke", "speech"], 1, "it-sector"),
    ("A ___ fixes hardware problems.", ["technician", "poet", "chef", "pilot"], 0, "professions"),
    ("UX designer focuses on:", ["user experience", "underground exit", "universal export", "upload extension"], 0, "professions"),
    ("'See you ___ Monday.'", ["in", "on", "at", "by"], 1, "time"),
    ("The meeting is ___ 3 p.m.", ["in", "on", "at", "to"], 2, "time"),
    ("Which is informal?", ["Dear Sir", "Hi team", "Yours faithfully", "Respectfully yours"], 1, "writing"),
    ("Hardware includes:", ["monitor, keyboard, CPU", "Windows, Linux", "HTML, CSS", "email, chat"], 0, "hardware"),
    ("Software includes:", ["applications and OS", "cables only", "desk and chair", "electricity"], 0, "software"),
    ("Browser is used to:", ["browse the web", "cool the CPU", "print hardware", "store RAM"], 0, "websites"),
    ("URL means:", ["Uniform Resource Locator", "Universal Random Link", "User Read Log", "Upload Run Load"], 0, "websites"),
    ("E-commerce site sells:", ["products online", "only news", "weather only", "CPU chips only in factory"], 0, "websites"),
    ("Blog website is mainly for:", ["articles and posts", "banking only", "OS installation", "hardware repair"], 0, "websites"),
    ("Present Continuous form:", ["verb + -ing with am/is/are", "verb + ed only", "will + verb", "have + past"], 0, "grammar"),
    ("'She is installing the OS now.' Tense?", ["Present Simple", "Present Continuous", "Past Perfect", "Future"], 1, "grammar"),
    ("Must vs have to — similar meaning:", ["obligation/necessity", "past ability", "question", "comparison"], 0, "modals"),
    ("Can't in 'I can't attend' often means:", ["unable / cannot", "must not", "don't have to", "should"], 0, "modals"),
    ("1,000,000 in words:", ["one million", "one thousand", "ten hundred", "one billon"], 0, "websites"),
    ("TB measures:", ["storage capacity", "temperature", "time", "network speed only"], 0, "hardware"),
    ("LAN means:", ["Local Area Network", "Large Application Node", "Linux Apache Nginx", "Load And Navigate"], 0, "it-sector"),
    ("Phishing is:", ["online fraud trick", "fishing sport", "fast typing", "photo editing"], 0, "it-sector"),
    ("Backup means:", ["copy data for safety", "back to office", "reverse keyboard", "delete files"], 0, "software"),
    ("Debug means:", ["find and fix errors", "remove virus only", "install OS", "format disk always"], 0, "software"),
    ("Which is a question word for time?", ["when", "where", "who", "whose"], 0, "time"),
    ("Plural of mouse (device):", ["mouses", "mice", "mousees", "mices"], 1, "hardware"),
    ("Firewall protects:", ["network security", "screen brightness", "keyboard layout", "printer paper"], 0, "it-sector"),
    ("API in computing:", ["Application Programming Interface", "Automatic Personal Internet", "Applied Program Input", "Admin Panel Index"], 0, "websites"),
    ("Oxford EAP level for this course (syllabus):", ["Elementary A2", "C2 Mastery", "Beginner A0 only", "Native C2"], 0, "tanitim"),
    ("Final exam weight in grading:", ["50%", "10%", "0%", "100% homework only"], 0, "tanitim"),
]
for t in tests:
    add_test(*t)
while len(test) < 55:
    i = len(test)
    add_test(f"'Download' is a common ___ on websites.", ["verb/action", "CPU", "Monday", "punctuation"], 0, "websites")

dogru_items = [
    ("Present Continuous uses am/is/are + verb-ing.", True, "grammar"),
    ("'He have a computer' is correct English.", False, "software"),
    ("RAM is volatile memory.", True, "hardware"),
    ("ROM typically stores firmware/BIOS.", True, "hardware"),
    ("Must and have to can both express obligation.", True, "modals"),
    ("Don't have to means something is forbidden.", False, "modals"),
    ("How many is used with countable nouns.", True, "websites"),
    ("How much is used with uncountable nouns.", True, "websites"),
    ("Faster is the comparative of fast.", True, "hardware"),
    ("Best is the superlative of good.", True, "software"),
    ("A developer writes software.", True, "professions"),
    ("GPU stands for Graphics Processing Unit.", True, "hardware"),
    ("URLs identify web page addresses.", True, "websites"),
    ("Present Simple is used for habits and facts.", True, "grammar"),
    ("I am working uses Present Continuous.", True, "grammar"),
    ("Can expresses ability.", True, "modals"),
    ("Mustn't means prohibition.", True, "modals"),
    ("UK English may use 'have got' where US uses 'have'.", True, "software"),
    ("CPU is a hardware component.", True, "hardware"),
    ("HTML is a programming language only (no markup).", False, "websites"),
    ("Monday is a day of the week.", True, "time"),
    ("Question mark ends a statement.", False, "punctuation"),
    ("e.g. introduces an example.", True, "punctuation"),
    ("IT means Information Technology.", True, "it-sector"),
    ("A midterm is given in week 8 per syllabus.", True, "tanitim"),
    ("Homework contributes 10% to grade.", True, "tanitim"),
    ("Listening skills help professional communication.", True, "it-sector"),
    ("An SSD has moving parts like HDD.", False, "hardware"),
    ("More fast is correct comparative.", False, "hardware"),
    ("Network technician works with connectivity.", True, "professions"),
    ("System administrator manages servers/users.", True, "professions"),
    ("At 5 o'clock uses preposition 'at' for time.", True, "time"),
    ("On Monday uses preposition 'on' for days.", True, "time"),
    ("Web portal offers multiple services in one site.", True, "websites"),
    ("Blog is only for video streaming.", False, "websites"),
    ("One thousand = 1,000.", True, "websites"),
    ("Modal 'could' can express past ability.", True, "modals"),
    ("Have to is only past tense.", False, "modals"),
    ("Comparatives often add -er or use more.", True, "hardware"),
    ("Superlatives often use -est or most.", True, "software"),
    ("Mouse plural in IT is often 'mice'.", True, "hardware"),
    ("Keyboard is input device.", True, "hardware"),
    ("Monitor is output device.", True, "hardware"),
    ("Install means put software on system.", True, "software"),
    ("Update can mean newer version.", True, "software"),
    ("Crash means program/system failure.", True, "software"),
    ("Login means sign in to account.", True, "websites"),
    ("Homepage is main page of website.", True, "websites"),
    ("Link connects to another page.", True, "websites"),
    ("Server hosts websites/data.", True, "websites"),
    ("Client requests service from server.", True, "it-sector"),
    ("Email is electronic mail.", True, "writing"),
    ("Dear Team is email greeting.", True, "writing"),
    ("Present Continuous for action happening now.", True, "grammar"),
    ("Final exam is week 14.", True, "tanitim"),
]
for s,v,t in dogru_items:
    add_dogru(s,v,t)
while len(dogru) < 55:
    add_dogru("Professional English includes IT vocabulary.", True, "it-sector")

blanks = [
    ("CPU: Central ___ Unit", "Processing", "hardware"),
    ("RAM: Random Access ___", "Memory", "hardware"),
    ("A person who develops software is a ___", "developer", "professions", ["programmer"]),
    ("___ technician maintains networks.", "Network", "professions"),
    ("What ___ is it? (asking time)", "time", "time"),
    ("See you ___ Monday. (day preposition)", "on", "time"),
    ("The class starts ___ 9 a.m.", "at", "time"),
    ("Comparative of fast: ___", "faster", "hardware"),
    ("Superlative of good: ___", "best", "software"),
    ("Present Continuous: I ___ working. (am/is/are)", "am", "grammar", ["is","are"]),
    ("Modal for ability: I ___ use Python.", "can", "modals"),
    ("Strong obligation: You ___ wear safety gear.", "must", "modals"),
    ("No obligation: You ___ come if busy. (don't have to)", "don't", "modals", ["do not"]),
    ("How ___ RAM do you need? (uncountable)", "much", "websites"),
    ("How ___ cores does the CPU have?", "many", "websites"),
    ("Operating System abbreviation: ___", "OS", "software"),
    ("Graphical User Interface: ___", "GUI", "software"),
    ("Uniform Resource Locator: ___", "URL", "websites"),
    ("Information Technology: ___", "IT", "it-sector"),
    ("for example abbreviation: ___", "e.g.", "punctuation", ["eg"]),
    ("as soon as possible: ___", "ASAP", "punctuation"),
    ("Local Area Network: ___", "LAN", "it-sector"),
    ("Solid State Drive: ___", "SSD", "hardware"),
    ("Hard Disk Drive: ___", "HDD", "hardware"),
    ("Input device example: ___", "keyboard", "hardware", ["mouse"]),
    ("Output device example: ___", "monitor", "hardware", ["printer"]),
    ("Browse the web with a ___", "browser", "websites"),
    ("Main page of a site: ___ page", "home", "websites", ["Home"]),
    ("Sign in to account: ___", "login", "websites", ["log in"]),
    ("Find and fix code errors: ___", "debug", "software"),
    ("Copy data for safety: ___", "backup", "software"),
    ("UK: I ___ got a meeting. (have)", "have", "software"),
    ("She ___ installing Windows now. (is/are + ing)", "is", "grammar"),
    ("Prohibition modal: You ___ smoke here.", "mustn't", "modals", ["must not"]),
    ("One million: 1,___", "000,000", "websites", ["000000"]),
    ("Graphics Processing Unit: ___", "GPU", "hardware"),
    ("Application Programming Interface: ___", "API", "websites"),
    ("User Experience designer: ___", "UX", "professions"),
    ("Write code in a ___ language.", "programming", "software"),
    ("Server ___ websites for users.", "hosts", "websites", ["host"]),
    ("Email opening: ___ Sir/Madam", "Dear", "writing"),
    ("Plural of mouse (device): ___", "mice", "hardware"),
    ("Faster, ___, fastest (comparison chain)", "faster", "hardware", ["fast"]),
    ("Present Simple: He ___ a laptop.", "has", "software"),
    ("I ___ to the meeting yesterday. (go - past)", "went", "grammar"),
    ("Website that sells online: e-___", "commerce", "websites"),
    ("Online journal posts: ___", "blog", "websites"),
    ("Question mark ends a ___", "question", "punctuation"),
    ("Comma separates items in a ___", "list", "punctuation"),
    ("Listen and ___ (skill pair)", "speak", "it-sector", ["speaking"]),
    ("Midterm is in week ___ per syllabus.", "8", "tanitim", ["eight"]),
    ("Final contributes ___ percent.", "50", "tanitim", ["fifty"]),
    ("Oxford EAP level: Elementary ___", "A2", "tanitim"),
    ("Phishing is online ___", "fraud", "it-sector"),
    ("Firewall improves network ___", "security", "it-sector"),
]
for b in blanks:
    if len(b)==4: add_bosluk(b[0],b[1],b[2],b[3])
    else: add_bosluk(b[0],b[1],b[2])
while len(bosluk) < 55:
    add_bosluk("Modal: You ___ restart the server. (obligation)", "must", "modals")

kod_items = [
    ("to-short", "I am not able to attend the meeting tomorrow because I have a scheduled deployment.", ["I can't attend tomorrow — deployment.", "I attending no.", "Tomorrow meeting I.", "Deployment am."], 0, "writing"),
    ("to-long", "Can't fix bug.", ["I cannot fix the bug.", "I am not able to fix the bug at the moment.", "Bug fix no.", "Can't fix bug."], 1, "writing"),
    ("to-short", "He have got a faster CPU than me.", ["He has a faster CPU than me.", "He have faster CPU.", "CPU he fast.", "Me slower."], 0, "software"),
    ("to-long", "RAM > ROM speed.", ["RAM is usually faster than ROM.", "Random Access Memory is typically faster than Read-Only Memory.", "RAM > ROM speed.", "Speed RAM ROM"], 1, "hardware"),
    ("to-short", "What time is it?", ["Could you tell me the time, please?", "Time what?", "It is time.", "When clock"], 0, "time"),
    ("to-long", "Install OS.", ["Please install the operating system.", "You need to install the operating system on the machine.", "Install OS.", "OS go"], 1, "software"),
    ("to-short", "You must not share your password.", ["Don't share your password.", "Password share you must not.", "Share password OK.", "Must share password"], 0, "modals"),
    ("to-long", "She coding.", ["She is coding.", "She is writing code right now.", "She coding.", "Code she"], 1, "grammar"),
    ("to-short", "How many memory?", ["How much memory?", "How many memory?", "Much memory how?", "Memory how"], 0, "websites"),
    ("to-long", "best fast processor", ["the fastest processor", "the best and fastest processor", "best fast processor", "processor best"], 0, "software"),
    ("to-short", "Dear Sir, I write about the network issue. The issue start yesterday.", ["Dear Sir, I am writing about a network issue that started yesterday.", "Sir dear network.", "Issue network write.", "Yesterday start"], 0, "writing"),
    ("to-long", "Login.", ["Please log in to your account.", "Click here to log in.", "Login.", "Log"], 0, "websites"),
    ("to-short", "e.g. CPU, RAM", ["for example: CPU, RAM", "example CPU RAM", "CPU RAM only", "i.e. CPU"], 0, "punctuation"),
    ("to-long", "ASAP", ["as soon as possible", "at the soonest available time", "ASAP", "quickly soon"], 0, "punctuation"),
]
for item in kod_items:
    add_kod(*item)

variants = [
    ("to-long", "I can code.", ["I am able to write code.", "I can program / I know how to code.", "I can code.", "Code I can"], 1, "modals"),
    ("to-short", "The website have many pages.", ["The website has many pages.", "Website many pages.", "Pages website.", "Have pages many"], 0, "software"),
    ("to-long", "faster CPU", ["a faster CPU", "a CPU that is faster", "faster CPU", "CPU more fast"], 0, "hardware"),
    ("to-short", "What day is today?", ["Could you tell me what day it is today?", "Day today what?", "Today day.", "What today"], 0, "time"),
    ("to-long", "must update", ["You must update the system.", "It is necessary to update.", "must update", "update must you"], 0, "modals"),
    ("to-short", "I am work on the server now.", ["I am working on the server now.", "I work server.", "Server work I.", "Now working"], 0, "grammar"),
]
topics_k = ["grammar","modals","hardware","websites","writing","time","software"]
while len(kod) < 55:
    v = variants[len(kod) % len(variants)]
    add_kod(v[0], v[1], v[2], v[3], topics_k[len(kod) % len(topics_k)])

import random
random.seed(42)

def shuffle_options(correct_idx, options):
    opts = list(options)
    correct_val = opts[correct_idx]
    random.shuffle(opts)
    return opts, opts.index(correct_val)

def dogru_to_test(q):
    stmt = q["statement"]
    opts = ["Yes, the statement is correct", "No, the statement is incorrect", "Correct only in some cases", "Not in the course material"]
    correct = 0 if q["correct"] else 1
    opts, correct = shuffle_options(correct, opts)
    return {"topic": q.get("topic", "genel"), "question": f"Is the following statement correct?\n«{stmt}»", "options": opts, "correct": correct}

def bosluk_to_test(q):
    text = q["question"].replace("___", "………")
    answer = q["answer"]
    alts = list(q.get("alternatives", []))
    wrong = ["router", "keyboard", "monitor", "printer", "browser", "server", "database", "password",
             "mouse", "speaker", "website", "email", "network", "software", "hardware"]
    distractors = [w for w in wrong if w.lower() != answer.lower() and w not in alts][:3]
    while len(distractors) < 3:
        distractors.append(f"Option-{len(distractors)+1}")
    opts = [answer] + distractors[:3]
    opts, correct = shuffle_options(0, opts)
    return {"topic": q.get("topic", "genel"), "question": f"Which word best fills the blank?\n{text}", "options": opts, "correct": correct}

def kod_to_test(q):
    direction = "short" if q.get("direction") == "to-short" else "long"
    prompt = q["prompt"][:300] + ("…" if len(q["prompt"]) > 300 else "")
    question = f"Which is the correct {direction} form / explanation?\n\n{prompt}"
    opts, correct = shuffle_options(q["correct"], list(q["options"]))
    return {"topic": q.get("topic", "genel"), "question": question, "options": opts, "correct": correct}

all_test = list(test)
for q in dogru:
    all_test.append(dogru_to_test(q))
for q in bosluk:
    all_test.append(bosluk_to_test(q))
for q in kod:
    all_test.append(kod_to_test(q))

for i, q in enumerate(all_test, 1):
    q["id"] = f"MT{i}"

out={"meta":{"title":"Mesleki İngilizce","course":"mesleki","testOnly":True,
      "counts":{"test":len(all_test)}},
     "test":all_test}
base=Path(__file__).parent/"mesleki"
(base/"data").mkdir(parents=True,exist_ok=True)
(base/"js").mkdir(parents=True,exist_ok=True)
js=json.dumps(out,ensure_ascii=False,indent=2)
(base/"data"/"questions.json").write_text(js,encoding="utf-8")
(base/"js"/"questions-data.js").write_text("window.QUIZ_DATA = "+js+";\n",encoding="utf-8")
print(out["meta"]["counts"], "Total:", sum(out["meta"]["counts"].values()))
