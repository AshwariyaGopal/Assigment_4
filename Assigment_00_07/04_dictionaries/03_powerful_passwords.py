import hashlib  # We'll need this for hashing

def hash_password(password):
    """
    Hashes a password using SHA-256
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Verifies if the provided password matches the stored hash for the given email
    
    Args:
        email (str): The user's email
        password_to_check (str): The password to verify
        stored_logins (dict): Dictionary of email-password hash pairs
    
    Returns:
        bool: True if password matches, False otherwise
    """
    # Check if email exists in stored_logins
    if email not in stored_logins:
        return False
    
    # Get the stored hash for this email
    stored_hash = stored_logins[email]
    
    # Hash the password to check
    password_hash = hash_password(password_to_check)
    
    # Compare the hashes
    return stored_hash == password_hash

# Example usage:
if __name__ == "__main__":
    # Example stored logins (in real life, this would be in a database)
    stored_logins = {
        "user@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"  # hash of "hello"
    }
    
    # Test the login function
    print(login("user@example.com", "hello", stored_logins))  # Should return True
    print(login("user@example.com", "wrong", stored_logins))  # Should return False