import random

#Generate a random commit, optionally can include a keyword.
def lazy_commit_message(keyword=None):
    adj = ["last-minute", "quick", "weird", "funky", "questionable", "rushed", "lazy", "unessecary", "untested", "unsettling"]
    verb = ["fixed", "debugged", "patched", "destroyed", "created", "rewrote", "deleted", "commented out", "refactored", "restructured", "hotfixed", "broke"]
    noun = ["thing", "bug", "piece of code", "function", "loop", "class", "issue", "workaround", "problem", "feature", "line of code", "variable", "data set"]
    
    temps = [
        "{adj} {verb} a {noun}. Hopefully it works.",
        "Just {verb} a {noun}. Could be better, could be worse, no telling",
        "{adj} fix for a {noun} in the code. I'm sure it's fine.",
        "{verb} a {noun}. I'm sure this will work.",
        "I think I {verb} a {noun}. But now the code won't run???",
        "{adj} {verb} a {noun} because the other dev messed up the {noun}.",
        "Commiting a {noun}, i {verb} it really hard.",
        "this is a {adj} {noun} that i {verb} in the code.",
        "{adj} {verb} the code.",
        "The {noun} was {adj} so I {verb} it.",
        "This is so {adj}, just accept the pull request.",
    ]
    
    temp = random.choice(temps)
    
    message = temp.format(
        adj =random.choice(adj),
        verb=random.choice(verb),
        noun=random.choice(noun)
    )
    
    final_message = f"{keyword}: {message}"
    
    if keyword:
        return final_message
    else:
        return message

def lazy_pull_request():
    TODO = "TODO"
    
def lazy_test_excuse():
    TODO = "TODO"
    
def procastionation_tip():
    TODO = "TODO"

#print(lazy_commit_message())
#print(lazy_commit_message("Bugfix"))