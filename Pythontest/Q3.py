def check_password(correct="python 123", max_attempts=3):
	attempts = 0
	while attempts < max_attempts:
		try:
			pwd = input("Enter password: ")
		except EOFError:
			
			print("No input received. Access denied")
			return False

		if pwd == correct:
			print("Access granted")
			return True
		else:
			attempts += 1
			remaining = max_attempts - attempts
			if remaining > 0:
				print(f"Incorrect password. {remaining} attempt(s) remaining.")
			else:
				print("Access denied")
				return False


if __name__ == "__main__":
	check_password()