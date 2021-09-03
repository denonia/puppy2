
def emoji_progress_bar(percentage):
	active = int(percentage / 25)
	inactive = 4 - active
	return active * "🌝" + inactive * "🌚"
