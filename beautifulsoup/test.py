from bs4 import BeautifulSoup
import requests

# inputFile = open("test.htm")
requestFile = requests.get('http://www.baidu.com', timeout=10)

html_markup="""
<div class="ecopyramid">
    <ul id="producers">
        <li class="producerlist">
            <div class="name">plants</div>
            <div class="number">100000</div>
        </li>
        <li class="producerlist">
            <div class="name">algae</div>
            <div class="number">100000</div>
        </li>
    </ul>
</div>
"""


# 修改标签名称
soup = BeautifulSoup(html_markup,'lxml')
producer_entries = soup.ul
print(producer_entries.name)
producer_entries.name = "div"
print(producer_entries.prettify())

# 修改标签属性
# 更新标签现有的属性值
producer_entries['id'] = "producers_new_value"
print(producer_entries.prettify())
# 标签添加新的属性值
producer_entries['class'] = "newclass"
print(producer_entries.prettify())
# 删除标签属性值
del producer_entries['class']
print(producer_entries.prettify())

# 添加新的标签
# 我们可以使用 new_tag 方法来生成一个新的标签，然后使用 append() 、insert() 、insert_after() 、insert_before()方法来将标签添加到 HTML 树中。
# 例如在上述的 HTML 文档的 ul 标签中添加一个 li 标签 。首先要生成新的 li 标签，然后将其插入到 HTML 树结构中 。并在 li 标签中插入相应的 div 标签。
# 添加新的标签
# new_tag 生成一个 tag 对象
new_li_tag = soup.new_tag("li")
# 标签对象添加属性的方法
new_atag = soup.new_tag("a",href="www.example.com" rel="external nofollow" )
new_li_tag.attrs = {'class':'producerlist'}
soup = BeautifulSoup(html_markup,'lxml')
producer_entries = soup.ul
# 使用 append() 方法添加到末尾
producer_entries.append(new_li_tag)
print(producer_entries.prettify())
# 生成两个 div 标签,将其插入到 li 标签中
new_div_name_tag = soup.new_tag("div")
new_div_name_tag['class'] = "name"
new_div_number_tag = soup.new_tag("div")
new_div_number_tag["class"] = "number"
# 使用 insert() 方法指定位置插入
new_li_tag.insert(0,new_div_name_tag)
new_li_tag.insert(1,new_div_number_tag)
print(new_li_tag.prettify())


# 修改字符串内容
# 修改字符串内容可以使用 new_string()  、append() 、insert() 方法。
# 修改字符串内容
# 使用 .string 属性修改字符串内容
new_div_name_tag.string = 'new_div_name'
# 使用 .append() 方法添加字符串内容
new_div_name_tag.append("producer")
# 使用 soup 对象的 new_string() 方法生成字符串
new_string_toappend = soup.new_string("producer")
new_div_name_tag.append(new_string_toappend)
# 使用insert() 方法插入
new_string_toinsert = soup.new_string("10000")
new_div_number_tag.insert(0,new_string_toinsert)
print(producer_entries.prettify())



# 删除标签节点
# Beautiful Soup 模块提供了 decompose() 和 extract() 方法来删除节点。
# decompose() 方法删除节点，不仅会删除当前节点，还会把其子节点一块删除了。
# extract() 方法用来从 HTML 树中删除节点或者字符串内容。

# 删除节点
third_producer = soup.find_all("li")[2]
# 使用 decompose() 方法删除 div 节点
div_name = third_producer.div
div_name.decompose()
print(third_producer.prettify())
# 使用 extract() 方法删除节点
third_producer_removed = third_producer.extract()
print(soup.prettify())



# 删除标签内容
# 标签可能有 NavigableString 对象或者 Tag 对象作为它的子节点，移除所有的这些子节点可以使用 clear() 方法。这将会移除标签的所有的 .content。
# 修改内容的其他方法
# 除了上面说到的方法，还有其他方法用来修改内容。
# insert_after() 和 insert_before() 方法
# 上面的两个方法能够在标签或者字符串的前面或者后面插入一个标签或者字符串。方法只能接收一个参数，要么是 NavigableString 对象要么是 Tag 对象。
# replace_with() 方法
# 该方法是用一个新的标签或字符串内容替代原来的标签或者字符串，能够接收一个标签或者字符串作为输入。

# wrap() 和 unwrap() 方法
# wrap() 方法是用另一个标签来包裹一个标签或者字符串。
# unwrap() 方法则和 wrap() 方法相反。

# wrap()方法
li_tags = soup.find_all('li')
for li in li_tags:
    new_div_tag = soup.new_tag('div')
    li.wrap(new_div_tag)
print(soup.prettify())
# unwrap()方法
li_tags = soup.find_all("li")
for li in li_tags:
    li.div.unwrap()
print(soup.prettify())