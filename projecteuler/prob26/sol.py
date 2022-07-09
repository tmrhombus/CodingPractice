
import itertools


def compute():
	ans = max(range(1, 10), key=reciprocal_cycle_len)
	return str(ans)


def reciprocal_cycle_len(n):
	print("On number: {}".format(n))
	seen = {}
	x = 1
	for i in itertools.count():
		print(" i={}, x={}".format(i,x))
		if x in seen:
			return i - seen[x]
		else:
			seen[x] = i
			print(" seen: {}".format(seen))
			x = x * 10 % n
			print("  newx = {}".format(x))


if __name__ == "__main__":
	print(compute())
