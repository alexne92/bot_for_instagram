import json
import argparse


if __name__ == '__main__':

	# parse arguments from user
	parser = argparse.ArgumentParser(description='Import username and password for the user on instagram')
	parser.add_argument('-u','--username', type=str, required=True, help='Username of user')
	parser.add_argument('-p','--password', type=str, required=True, help='Password of user')
	args = parser.parse_args()

	print("You have inserted the following values:")
	print(f"Username: {args.username}")
	print(f"Password: {args.password}")

	# Store credentials into a dictionary
	credentials = {
		"instagram_username": args.username,
		"instagram_password": args.password
	}

	# Store dictionary to .json file
	try:
		with open('credentials.json', 'w') as json_file:
			json.dump(credentials, json_file)
			json_file.close()
		print("Credentials have been succesfully stored to credentials.json file.")
	except Exception as e:
		print("While saving the credentials, the following error occured:")
		print(e)