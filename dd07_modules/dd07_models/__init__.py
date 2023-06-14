from .main import login_manager, sess_users, sess_cage, sess_bls, \
    engine_users, engine_cage, engine_bls, text, Base, \
    Users, BlogPosts, CageCompanies, IndustryNames, \
    IndustryValues, CommodityNames, CommodityValues

# import os


# ############################################################################
# ## This is one of the first files to execute so make dirs here

# if not os.path.exists(os.environ.get('DB_ROOT')):
#     os.makedirs(os.environ.get('DB_ROOT'))

# # config.DIR_DB_AUXILARY directory:
# if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"auxilary")):
#     os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"auxilary"))
# # config.DIR_DB_AUX_IMAGES_PEOPLE directory:
# if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"auxilary","images_people")):
#     os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"auxilary","images_people"))

# # # config.DIR_DB_FILES_UTILITY directory:
# # if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"files_utility")):
# #     os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"files_utility"))

# # # config.DIR_DB_QUERIES directory:
# # if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"queries")):
# #     os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"queries"))
# # #######################################################################################
# # ## NOTE: Unsure if needed since html files will be stored in templates directory ##
# # if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"blog_html_files")):
# #     os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"blog_html_files"))
# ######################################################################################



# #Build DB_NAME_USERS
# if os.path.exists(os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_USERS'))):
#     print(f"db already exists: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_USERS'))}")
# else:
#     Base.metadata.create_all(engine_users)
#     print(f"NEW db created: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_USERS'))}")

# #Build DB_NAME_CAGE
# if os.path.exists(os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_CAGE'))):
#     print(f"db already exists: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_CAGE'))}")
# else:
#     Base.metadata.create_all(engine_cage)
#     print(f"NEW db created: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_CAGE'))}")

# #Build DB_NAME_BLS
# if os.path.exists(os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_BLS'))):
#     print(f"db already exists: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_BLS'))}")
# else:
#     Base.metadata.create_all(engine_bls)
#     print(f"NEW db created: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME_BLS'))}")