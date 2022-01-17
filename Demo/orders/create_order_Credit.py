from pathlib import Path
import importlib.util
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent # orders
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk",
    f"{BASE_DIR}/ecpay_payment_sdk.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


# extend_params_1 = {
#     'BindingCard': 0,
#     'MerchantMemberID': '',
# }

# extend_params_2 = {
#     'Redeem': 'N',
#     'UnionPay': 0,
# }

# inv_params = {
    # 'RelateNumber': 'Tea0001', # 特店自訂編號
    # 'CustomerID': 'TEA_0000001', # 客戶編號
    # 'CustomerIdentifier': '53348111', # 統一編號
    # 'CustomerName': '客戶名稱',
    # 'CustomerAddr': '客戶地址',
    # 'CustomerPhone': '0912345678', # 客戶手機號碼
    # 'CustomerEmail': 'abc@ecpay.com.tw',
    # 'ClearanceMark': '2', # 通關方式
    # 'TaxType': '1', # 課稅類別
    # 'CarruerType': '', # 載具類別
    # 'CarruerNum': '', # 載具編號
    # 'Donation': '1', # 捐贈註記
    # 'LoveCode': '168001', # 捐贈碼
    # 'Print': '1',
    # 'InvoiceItemName': '測試商品1|測試商品2',
    # 'InvoiceItemCount': '2|3',
    # 'InvoiceItemWord': '個|包',
    # 'InvoiceItemPrice': '35|10',
    # 'InvoiceItemTaxType': '1|1',
    # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
    # 'DelayDay': '0', # 延遲天數
    # 'InvType': '07', # 字軌類別
# }

# 建立實體
ecpay_payment_sdk = module.ECPayPaymentSdk(
    MerchantID='2000132',
    HashKey='5294y06JbISpM5x9',
    HashIV='v77hoKGq4kWxNNIS'
)

# 合併延伸參數
# order_params.update(extend_params_1)
# order_params.update(extend_params_2)

# # 合併發票參數
# order_params.update(inv_params)
