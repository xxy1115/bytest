@pytest.fixture(autouse=True,scope="",params=["",""])
def abc(request):
    username=request.param
    yield username
说明：
scope="function",每个测试用例方法前后调用
scope="module",相当于setup_class,在类前后调用
autouse为True时,测试用例方法无需调用abc;否则需要传入abc调用，从abc直接获取fixture的返回值 

allure windows需要下载zip安装包

selenium借助AutoIt识别上传文件
https://www.cnblogs.com/fnng/p/4188162.html


# 运行文件保存结果到result1目录下：pytest_cases>pytest test_05_allure.py --alluredir ./result1 -vs
# 生成报告-直接查看：allure serve ./result1
# 生成报告-本地生成文件夹：allure generate ./result1
# 生成报告-指定生成到report文件夹：allure generate ./result1 -o report

