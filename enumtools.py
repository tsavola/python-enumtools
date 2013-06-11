# Public domain.

def initialmarker(iterable):
	first = True

	for obj in iterable:
		yield first, obj
		first = False

def finalmarker(iterable):
	first = True

	for curr in iterable:
		if not first:
			yield False, prev

		prev = curr
		first = False

	if not first:
		yield True, prev

if __name__ == "__main__":
	for initial, x in initialmarker(range(4)):
		if initial:
			print(x, "is first")
		else:
			print(x)

	print()

	for final, x in finalmarker(range(4)):
		if final:
			print(x, "is last")
		else:
			print(x)
