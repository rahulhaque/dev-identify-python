from dev_identify import DevIdentify

result = DevIdentify.email('examplegmail.com').save('/path/image_name.jpg').toJson()

print(result)