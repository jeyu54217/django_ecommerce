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
