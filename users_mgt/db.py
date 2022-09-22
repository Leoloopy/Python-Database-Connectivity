import dotenv
import os
dotenv.load_dotenv()


user = os.getenv('user')

print(os.getenv('user'))
