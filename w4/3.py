import argparse


def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', type = int)

	return parser


def fib(n):
	if n in (1, 2):
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


parser = create_parser()
namespace = parser.parse_args()

print(fib(namespace.n))
