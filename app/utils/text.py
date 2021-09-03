
def emoji_progress_bar(percentage: int) -> str:
	active = int(percentage / 25)
	inactive = 4 - active
	return active * "🌝" + inactive * "🌚"
