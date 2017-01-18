# easyutils

希望能提供一些股市常用的接口，减少重复劳动

## Install

```
pip install easyutils
```

## Usage

```
import easyutils
easyuitls.is_holiday_today()
```

## is_holiday

```
def is_holiday(day):
    """
    判断是否节假日
    :param day: 日期， 格式为 '20160404'
    :return: Bool
```

## is_holiday_today

```
def is_holiday_today():
    """
    判断今天是否时节假日
    :return: bool
    """
```

## is_tradetime_now

```
def is_tradetime_now():
    """
    判断目前是不是交易时间, 并没有对节假日做处理
    :return: bool
```

## get_stock_type

```
def get_stock_type(stock_code):
    """判断股票ID对应的证券市场
    匹配规则
    ['50', '51', '60', '90', '110'] 为 sh
    ['00', '13', '18', '15', '16', '18', '20', '30', '39', '115'] 为 sz
    ['5', '6', '9'] 开头的为 sh， 其余为 sz
    :param stock_code:股票ID, 若以 'sz', 'sh' 开头直接返回对应类型，否则使用内置规则判断
    :return 'sh' or 'sz'"""
```

## get_code_type

```
def get_code_type(code):
    """
    判断代码是属于那种类型，目前仅支持 ['fund', 'stock']
    :return str 返回code类型, fund 基金 stock 股票
    """
```



## get_all_stock_codes

```
def get_all_stock_codes():
    """获取所有股票 ID"""
```

