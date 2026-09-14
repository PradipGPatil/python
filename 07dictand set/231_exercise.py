text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# splite the text to create world

split_text=set(text.split())

preps_used=split_text.intersection(prepositions)
print(preps_used)
