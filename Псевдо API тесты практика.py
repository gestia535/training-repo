# response = {
#     "status": 200,
#     "data": {
#         "username": "admin",
#         "role": "admin",
#         "is_active": True
#     }
# }
response_error = {
    "status": 404,
    "error": "User not found"
}
def check_status(response):
    return response['status'] == 200

def check_error(response_error):
    return "OK" if response_error.get('status') == 200 else response_error.get('error', 'Unknown error')


def check_user(response):
    data = response.get('data', {})
    return data.get('username') == 'admin' and data.get('role') == 'admin'

def check_active(response):
    data = response.get('data', {})
    return 'ACTIVE' if data.get('is_active') else 'INACTIVE'

