baseUrl = "https://api.growave.io/api/"
headersAuth = {'Authorization': 'Bearer 954ca61526bf958954779fed2d6fb4fbe94ddb43'}
headersBasic = {'Authorization': '<BASIC auth>',
                'Content-Type': 'multipart/form-data;'}
data1 = {
    "user_id": 4,
    "product_id": "6976031883396"
}

formData = {
    "client_id": "458bb512dfcd42aa5d51639961d31255",
    "client_secret": "bb41b910eaf036c2cef2b127d6603b35",
    "grant_type": "client_credentials",
    "scope": "read_user write_user read_wishlist write_wishlist read_review write_review read_gallery read_reward write_reward app_install",
}
params = {
    "ssw_custom_project": "kolbai"
}

header1 = {'accept-language': 'ru-RU',
           'connectTimeout': '60000',
           'content-type': 'application/json',
           'followRedirects': 'true',
           'receiveTimeout': '60000',
           'responseType': 'ResponseType.json',
           'user-build': '20002462',
           'user-client': 'mobile-private',
           'user-version': '10.7.0'
           }


