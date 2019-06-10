from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram.with_credentials('username', 'password', 'path/to/cache/folder')
instagram.login()

medias = instagram.get_medias_by_tag('instagood', count=20)

for media in medias:
    print(media)
    print('Account info:')
    account = media.owner
    print('Id', account.identifier)
    # print('Username', account.username)
    # print('Full Name', account.full_name)
    # print('Profile Pic Url', account.getProfilePicUrlHd())
    print('--------------------------------------------------')