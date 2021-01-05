from instapy import InstaPy
import env

session = InstaPy(username=env.instagramId, password=env.instagramPassword)
session.login()

session.set_relationship_bounds(enabled=True,
				 #potency_ratio=1.34,
				  delimit_by_numbers=True,
				   max_followers=1000,
				    max_following=449000,
				     min_followers=30,
				      min_following=100)

session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True)

session.set_do_follow(True, percentage=100, times=2)

session.like_by_tags(['#instafood', '#vegfood', '#healthyfood', '#veganrecipes', '#vegetarianrecipes','#veganlife'], amount=50)

# session.set_comments(["Good!, I love this!", 
#     "Nice!!", "Excellent :)", "Perfect :)", "Great!!", "Amazing!!", 
#     "Beautiful :)", "Wonderful!!", "Good job", "pretty good.", "It looks great!", 
#     "You must be a man of ability.", "I like this.", "Good.", "Sweet!", 
#     "Beautiful :heart_eyes:"
#     ])
# session.set_do_comment(True, percentage=40)


session.set_dont_like(['selfi','naked','nsfw'])

session.end()