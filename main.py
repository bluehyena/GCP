from instapy import InstaPy
import env

session = InstaPy(username=env.instagramId, password=env.instagramPassword)
session.login()
session.like_by_tags(["hunger", "unicef", "vegan"], amount=5)