import random

#Generate a random commit, optionally can include a keyword.
def lazy_commit_message(keyword=None):
    adj = ["last-minute", "quick", "weird", "funky", "questionable", "rushed", "unessecary", "untested", "unsettling"]
    verb_act = ["fixed", "debugged", "patched", "created", "rewrote", "deleted", "commented out", "refactored", "restructured", "hotfixed", "broke"]
    verb_hap = ["crashed", "failed", "froze", "worked", "loaded", "compiled"]
    noun = ["thing", "bug", "piece of code", "function", "loop", "class", "issue", "workaround", "problem", "feature", "line of code", "variable", "data set"]
    
    temps = [
        "a {adj} {noun} was {verb_act}. Hopefully it works.",
        "Just {verb_act} a {noun}. Could be better, could be worse, no telling",
        "implented a {noun} fix. It was {adj}, i'm sure it's fine.",
        "I {verb_act} the {noun}. maybe this will work?",
        "I think I {verb_act} a {noun}. But now the code won't run???",
        "This {noun} was {adj}, so I {verb_act} it.",
        "{verb_act} a {adj} {noun} because the other dev messed up the {noun}.",
        "Commiting a {noun}, i {verb_act} it really hard.",
        "this is a {adj} {noun} that i {verb_act} in the code.",
        "{verb_act} the code.",
        "The {noun} was {adj} so I {verb_act} it.",
        "{verb_hap}. No idea why, but here we are.",
        "The {noun} was {adj}, and it somehow {verb_hap}.",
        "After some tweaks, the {noun} {verb_hap}. Not sure if that's good or bad.",
        "I touched the {noun} and it {verb_hap} for some reason?",
        "it was {adj}, suddenly it {verb_hap}.",
        "Tried fixing a {noun}, now it just {verb_hap}.",
        "The {noun} {verb_hap} again... just trust me."
    ]
    
    temp = random.choice(temps)
    
    message = temp.format(
        adj =random.choice(adj),
        verb_hap=random.choice(verb_hap),
        verb_act=random.choice(verb_act),
        noun=random.choice(noun)
    )
    
    final_message = f"{keyword}: {message}"
    
    if keyword:
        return final_message
    else:
        return message

#Generate a pull request title; returns a purely random PR title or one with given words, verb first, noun second.
def lazy_pull_request(inputVerb="", inputNoun=""):
    verbs = ["added", "fixed", "patched", "created", "refactored", "enhanced", "updated", "implemented", "broke"]
    nouns = ["feature", "bug", "piece of code", "function", "issue", "something", "everything", "problem"]
    
    sentences = [
        "{verb} a {noun}. Just accept the pull request.",
        "Just {verb} a {noun}.",
        "{verb} stuff for a {noun}",
        "Very insignificant change, {verb} a {noun}.",
        "{noun} has been {verb}, accept quickly",
        "Important, please review quickly: {verb} a {noun}",
        "Critical: {verb} a {noun}",
        "{verb} {noun} to new version",
        "{verb} {noun} to align with new version",
    ]
    
    sentence = random.choice(sentences)
    if (inputVerb == ""):
        tempverb = random.choice(verbs)
    else:
        tempverb = inputVerb
    if (inputNoun == ""):
        tempnoun = random.choice(nouns)
    else:
        tempnoun = inputNoun

    message = sentence.format(
        verb = tempverb,
        noun = tempnoun
    )

    return message
    

    
def lazy_test_excuse(reason=None):
    excuses=["I ran it once, it did not crash.",
             "I'll add tests later...",
             "We need to refactor before adding tests.",
             "I was going to write tests, but {reason}.",
            "Everything looks runnng, no need for test.",
            "If it compiles it works.",
            "Tests make the code slower."
             ]
    
    selected_excuse=random.choice(excuses)
    if reason:
        return selected_excuse.format(reason=reason)
    else: 
        return selected_excuse.replace("{reason}", "I had more important things to do")
    #^need a filler for reason input 
    
def procastionation_tip():
    TODO = "TODO"

#print(lazy_commit_message())
print(lazy_commit_message())

#print(lazy_pull_request())
#print(lazy_pull_request("noun", "verb"))