name = "chuanzhiboke"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

message1 = f"company: {name},stock code: {stock_code},current stock price: {stock_price}"
message2 = f"daily growth factor is {stock_price_daily_growth_factor},after {growth_days},achieve %.2f"%(stock_price * stock_price_daily_growth_factor ** growth_days)
message3 = "daily growth factor is %.1f,after %d days,achieve %.2f" %(stock_price_daily_growth_factor,growth_days,stock_price * stock_price_daily_growth_factor ** growth_days)
print(message1)
print(message2)
print(message3)
