import boto3
import json

# Initialize Secrets Manager client
secret_manager = boto3.client('secretsmanager')


def get_secret():
    secret_name = "arn:aws:secretsmanager:eu-north-1:381492064618:secret:myrds-J2xJxf"
    
    try:
        get_secret_value_response = secret_manager.get_secret_value(SecretId=secret_name)
        
        # Parse the secret values
        secret_dict = json.loads(get_secret_value_response['SecretString'])
        db_username = secret_dict['username']
        db_password = secret_dict['password']
        return db_username, db_password
    except Exception as e:
        print(f"Error retrieving secret: {str(e)}")
        return None, None

def main():
    db_username, db_password = get_secret()
    
    if db_username and db_password:
        print(f"Retrieved username: {db_username}")
        print(f"Retrieved password: {db_password}")

if __name__ == "__main__":
    main()
