import os
from cryptography.fernet import Fernet
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine

# 1. Generate or load your encryption key (Store this safely in environment variables, e.g., AWS Secrets Manager, Vault)
# Run Fernet.generate_key() once and save the output.
SECRET_KEY = os.environ.get("FERNET_ENCRYPTION_KEY", Fernet.generate_key().decode())

Base = declarative_base()


class UserToken(Base):
  __tablename__ = "user_tokens"

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, index=True)

  # 2. Define the security token column with automatic Fernet encryption
  secure_token = Column(
      EncryptedType(String, SECRET_KEY, FernetEngine, "aes")
  )


# 3. Setup PostgreSQL database connection
DATABASE_URL = "postgresql://username:password@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# --- Example Usage: Inserting a Token (Encrypted Automatically) ---
new_record = UserToken(user_id=101, secure_token="super-secret-token-12345")
session.add(new_record)
session.commit()

# --- Example Usage: Querying a Token (Decrypted Automatically) ---
user_token_obj = (
    session.query(UserToken).filter(UserToken.user_id == 101).first()
)
print(
    f"Plaintext token loaded via ORM: {user_token_obj.secure_token}"
)  # Decrypted on load
