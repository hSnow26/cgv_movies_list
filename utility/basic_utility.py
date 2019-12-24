#
# author : seol <kshzg26@gmail.com>
# basic utility
#
# TODO
# pip install requests

from requests import get

class BasicUtility:
    MY_IP  = get('https://api.ipify.org').text

    # 테스트 용도
    def switch(self, k, const):
        return {
            '13.124.60.0': const.DRIVER_PATH,
            '211.35.67.149': const.DRIVER_PATH_MAC
        }.get(k, const.DRIVER_PATH_DELL)

