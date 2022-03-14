# main.py
#Elpoireau

from random import choice

def main():
	print("top ten "*4 + "list entry numbers:")
	for n1 in reversed(range(10)):
		n1 = str(n1+1) + ":"
		for n2 in reversed(range(10)):
			n2 = str(n2+1) + ":"
			list_numbers = [i+1 for i in range(10)]
			for n3 in reversed(range(10)):
				n3 = str(n3+1) + ":"
				if n3 != "10:" and n2 != "  ":
					n2 = " "
				if n2 != "10:" and n1 != "  ":
					n1 = " "
				rn = choice(list_numbers)
				list_numbers.remove(rn)
				print(f"{n1} {n2} {n3} {rn}")

if __name__ == "__main__":
	main()
