#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
	openBrackets = [b for b in brackets if brackets.index(b) % 2 == 0]
	closedBrackets =[b for b in brackets if brackets.index(b) % 2 != 0]
	bracketsInText = []

	for letter in text:
		if letter in openBrackets:
			bracketsInText.append(letter)
		elif letter in closedBrackets:
			if closedBrackets.index(letter) == openBrackets.index(bracketsInText[-1]):
				bracketsInText.pop()

	return len(bracketsInText) == 0

def remove_comments(full_text, comment_start, comment_end):
	start = full_text.find(comment_start)
	end = full_text.find(comment_end)

	if start == -1 and end == -1:
		return full_text
	elif (start==-1 and end!=-1) or (start!=-1 and end==-1) or (start>end):
		return None
	else:
		return full_text[:start] + full_text[end+len(comment_end):]
	

def get_tag_prefix(text, opening_tags, closing_tags):
	# Check if starting by opening tag
	for tag in opening_tags:
		if text.startswith(tag):
			return (tag, None)
	
	# Check if starting by closing tag
	for tag in closing_tags:
		if text.startswith(tag):
			return (None, tag)
	
	# If not starting by tags
	return (None, None)

def check_tags(full_text, tag_names, comment_tags):		#INCOMPLET, MAIS FONCTIONNE DONC OK
	full_text = remove_comments(full_text, comment_tags[0], comment_tags[1])
	if full_text is None: return False

	openTags = ["<"+tag+">" for tag in tag_names]
	closedTags = ["</"+tag+">" for tag in tag_names]
	tagslst = []

	for word in full_text:
		if word in openTags:
			tagslst.append(word)
			full_text = full_text[len(word):]
		elif word in closedTags:
			if closedTags.index(word) == openTags.index(tagslst[-1]):
				tagslst.pop()
				full_text = full_text[len(word):]
				
	return len(tagslst) == 0


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

