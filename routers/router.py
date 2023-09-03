from views.maotai.qc_view import QrcodeView
from views.test.test_view import testController

api_router = [
    (testController, "/test",
     QrcodeView, "/qrcode"
     )
]