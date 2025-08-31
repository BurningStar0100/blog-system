# app/models/__init__.py
from .users import User
from .post import Post

# # This ensures both models are loaded together
# # __all__ = ["User", "Post"]