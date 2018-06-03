from dev_identify import DevIdentify

result = DevIdentify.email('example@gmail.com').save('/path/image_name.jpg').toJson()

print(result)