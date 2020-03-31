import requests
import re

class LinkedIn:

    def __init__(self):
        self.s = requests.Session()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97"
            }
    def login(self,email,password):
        try:
            sc = self.s.get("https://www.linkedin.com/login", headers=self.headers).text
        except:
            return False
        csrfToken = sc.split('csrfToken" value="')[1].split('"')[0]
        sid = sc.split('sIdString" value="')[1].split('"')[0]
        pins = sc.split('pageInstance" value="')[1].split('"')[0]
        lcsrf = sc.split('loginCsrfParam" value="')[1].split('"')[0]
        data = {
            'csrfToken': csrfToken,
            'session_key': email,
            'ac': '2',
            'sIdString': sid,
            'parentPageKey': 'd_checkpoint_lg_consumerLogin',
            'pageInstance': pins,
            'trk': 'public_profile_nav-header-signin',
            'authUUID': '',
            'session_redirect': 'https://www.linkedin.com/feed/',
            'loginCsrfParam': lcsrf,
            'fp_data': 'default',
            '_d': 'd',
            'showGoogleOneTapLogin': 'true',
            'controlId': 'd_checkpoint_lg_consumerLogin-login_submit_button',
            'session_password': password,
            'loginFlow': 'REMEMBER_ME_OPTIN'
            }
        try:
            after_login = self.s.post("https://www.linkedin.com/checkpoint/lg/login-submit",headers=self.headers,data=data).text
        except:
            return False
        is_logged_in = after_login.split('<title>')[1].split('</title>')[0]
        if is_logged_in == "LinkedIn":
            return True
        else:
            return False

    def bulkScan(self, profiles):
        all_emails = []
        for profile in profiles:
            profile = profile + "/detail/contact-info/"
            sc = self.s.get(profile, headers=self.headers, allow_redirects=True).text
            emails_found = re.findall('[a-zA-Z0-9\.\-\_i]+@[\w.]+',sc)
            all_emails.extend(emails_found)
        return all_emails

    def singleScan(self, profile):
        profile = profile + "/detail/contact-info/"
        sc = self.s.get(profile, headers=self.headers, allow_redirects=True).text
        emails_found = re.findall('[a-zA-Z0-9\.\-\_i]+@[\w.]+',sc)
        return emails_found
