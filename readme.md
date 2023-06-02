# NNSonEncryptedData

本文实现了加密数据的最近邻搜索。[Klewi](https://klewi.com/)在其论文`Function-Hiding Inner Product Encryption is Practical`中提到的FHIPE应用方向其中之一 加密数据上的最近邻搜索。

## 环境依赖

### 部署项目

1. 首先根据[FHIPE](https://github.com/kevinlewi/fhipe)部署要求部署fhipe项目（包括其依赖库FLINT、charm的依赖库）
1. 克隆本仓库到fhipe相同路径下 `git clone https://github.com/ikun7355608/NNSonEncryptedData`
1.  安装并配置`Mysql`
1. 安装`pymysql PyQt5`库及对应依赖。
1. 配置Mysql`root@joker7355608`（或者修改`libsql`中所有相关信息为自己的`Mysql`账号密码）

### 项目结构

```

├── fhipe/             未添加子项目 自行配置
├── client.py          用户查询客户端
├── doc2vec
│   ├── doc2vec.ipynb
│   ├── output
│   │   ├── 1988_vec.txt
│   │   ├── 1989_vec.txt
│   │   ├── hetongA_vec.txt
│   │   ├── hetongB_vec.txt
│   │   ├── hongloumengA_vec.txt
│   │   ├── hongloumengB_vec.txt
│   │   ├── huozheA_vec.txt
│   │   ├── huozheB_vec.txt
│   │   ├── sharenA_vec.txt
│   │   ├── sharenB_vec.txt
│   │   ├── xusanguanA_vec.txt
│   │   └── xusanguanB_vec.txt
│   ├── stop_words.txt
│   ├── test
│   │   ├── 1988.txt
│   │   ├── 1989.txt
│   │   ├── hetongA.txt
│   │   ├── hetongB.txt
│   │   ├── hongloumengA.txt
│   │   ├── hongloumengB.txt
│   │   ├── huozheA.txt
│   │   ├── huozheB.txt
│   │   ├── sharenA.txt
│   │   ├── sharenB.txt
│   │   ├── xusanguanA.txt
│   │   └── xusanguanB.txt
│   └── train
│       ├── fengkuangxingqisi.txt
│       ├── hetongjiufen.txt
│       ├── hongloumeng.txt
│       ├── huozhe.txt
│       ├── sharen.txt
│       ├── xinwen.txt
│       ├── xusanguanmaixueji.txt
│       └── zhengfugongzuobaogao.txt
├── file	           文件相关操作界面类
│   ├── file_delete.py
│   └── file_management.py
├── lib	       辅助函数
│   ├── libconvertio.py
│   ├── libcrypto.py
│   └── libsql.py
├── management.py      用户管理界面实例化
├── readme.md
├── register.py        用户注册界面实例化
├── server.py          文件服务器
└── user	           用户相关界面类
    ├── user_infor.py
    ├── user_login.py
    ├── user_management.py
    ├── user_regist.py
    ├── user_select.py
    └── user_update.py
```

## 使用

### 用户相关信息管理

用户相关身份信息存储在`USER`及`USER_LOGIN`表中。其中，密码SHA256加密后存储。

#### 用户注册

```sh
python register.py
```

#### 信息管理

```sh
python management.py
```

修改用户相关身份信息，密码处不输入默认不更改。

### 文件向量化

该工作由`doc2vec.ipynb`完成。本文中文件向量化模型运行在`Kaggle`上，部署本地时需要安装相关依赖库。以下，将针对运行在`Kaggle`中进行描述。

#### 相关说明

1. 本文中，停用词存放在私有数据集`word2vec-test`中。具体使用时，根据自己上传位置修改文件读取路径
2. 模型构建时向量的维度设定依照`server.py`中矩阵B的维度进行更改（`模型维度 = 矩阵维度 - 2`）。同时，源码中包含内积加密`setup`函数的都需要对应更改维度
3. 本文所采用的训练预料包括：最高人民法院指导的杀人案、购房合同纠纷案、近30年政府工作报告、「活着」、「徐三观卖血记」、「红楼梦」。训练集可根据自己需求修改

#### 使用

如果使用系统假定的向量维度则直接运行即可。

### 服务器

```sh
python server.py
```

服务器运行时，启动三个进程

1. 绘制文件服务器界面，该界面提供文件数据库的增删改查功能（「改」的功能体现在「增」上,「增」之前会判定是否存在，存在则「增」，不存在则「改」）
2. 监听用户登录端口。使用用户发送的`id`在数据表中进行查找，与用户发过来的`hash(passwd)`进行比对进行身份认证，成功后分发`msk`。
3. 监听用户查询请求端口。与数据库中数据进行解密运算，返回最相似文件`id`。根据`id`提取AES密文，然后返回给用户。

#### 注意事项

- 由于服务器端寻找向量的方式为：`path/filename.txt  --> path/filename_vec.txt`需要将向量文件与文件一起放在同一个文件夹下。
- 文件`file/file_management.py`中第24行为创建数据表语句，初次使用项目时默认开启，后续不需要可以自行关闭（打开项目时shell中会输出`exists`的原因）
- 服务器端在退出时会自动清空两个密文数据表中的内容（下次使用时，`g1 g2 alpha beta`会重新随机选择，留着之前的密文也不会解密成功，且影响解密速度。）

### 客户端

```sh
python client.py
```

身份认证后，选择相应文件进行相似度查找，等待返回结果。

#### 注意事项

- 向量寻找方式同上
- 查找时未创建新进程，界面会卡死
- 运行前需要保证服务器运行
- 查询前不做检查，直接点查询会导致一些问题（未实验）
- 用户身份信息认证失败没有设计对应响应



## Others

- 元素均为`group.Element`类型，虽然看上去像一个数组。（传输、存取时注意类型转换）
  - `libconvertio`中提供了根据`charm`库的序列化、反序列化进行了一定封装
- `FHIPE`矩阵选取伪随机（`n`维矩阵中的数据根据随机种子确定，如果使用默认则`n`维矩阵内容一直固定）
- 如有问题，联系邮箱 goudan.wang@outlook.com


