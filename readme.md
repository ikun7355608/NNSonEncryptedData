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
├── doc2vec		Kaggle上模型训练相关文件
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
├── file_vector  存放文件及向量的文件夹
│   ├── 1988.txt
│   ├── 1988_vec.txt
│   ├── 1989.txt
│   ├── 1989_vec.txt
│   ├── doc2vec.ipynb
│   ├── hetongA.txt
│   ├── hetongA_vec.txt
│   ├── hetongB.txt
│   ├── hetongB_vec.txt
│   ├── hongloumengA.txt
│   ├── hongloumengA_vec.txt
│   ├── hongloumengB.txt
│   ├── hongloumengB_vec.txt
│   ├── huozheA.txt
│   ├── huozheA_vec.txt
│   ├── huozheB.txt
│   ├── huozheB_vec.txt
│   ├── sharenA.txt
│   ├── sharenA_vec.txt
│   ├── sharenB.txt
│   ├── sharenB_vec.txt
│   ├── xusanguanA.txt
│   ├── xusanguanA_vec.txt
│   ├── xusanguanB.txt
│   └── xusanguanB_vec.txt
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

### 参数修改

- 修改相关语料库进行其他文件的查找时（更改向量维度），需要更改以下配置

  1. `doc2vec/doc2vec.ipynb`中的`Doc2Vec(vector_size=8, min_count=1, window=5)`的`vector_size`修改为向量维度大小`size`

  2. 执行`grep -n -r ipe.setup {your_dir}/`显示出的所有包含`ipe.setup`的文件所对应的文件及所在行（样例如下）

     ```shell
     grep -n -r ipe.setup /home/joker/aaa/
     
     /home/joker/aaa/server.py:59:	# (pp, sk) = ipe.setup(10)
     /home/joker/aaa/server.py:119:	(pp, sk) = ipe.setup(10)
     /home/joker/aaa/server.py:134:# (pp, sk) = ipe.setup(10)
     /home/joker/aaa/file/file_management.py:26:        (self.pp,self.msk) = ipe.setup(10)
     /home/joker/aaa/user/user_login.py:22:        (self.pp,self.msk) = ipe.setup(10)
     /home/joker/aaa/user/user_select.py:20:        (self.pp,self.msk) = ipe.setup(10)
     ```

  3. 将上面得到的所有文件所在行的`ipe.setup()`的参数修改为`size + 2`（向量扩展后大小）

- 换其他语料库及文本时，提取文件及其特征向量将`file.txt`及`file_vec.txt`同时存放在`file_vector/`路径下

### 模拟文件相似度检测流程

`register.py`注册完用户信息之后

- 运行`server.py`选择`file_vector`中相应明文文件上传（维护文件数据库）
  - 明文AES加密，向量`ipe.encrypt`加密后序列化
  - 加密后的两个密文分别上传至两个密文表中
- 运行`client.py`登录后，选择`file_vector`中要进行检测的文件`file.txt`点击查找等待返回结果
  - 登录时，发起身份认证，成功后拿到内积加密`msk`
  - 选择相应文件时向量`ipe.keygen`后序列化发送给server
    - 服务器提取出`IPE_CIPHER`数据表中的`id + cipher`，ipe密文反序列化后与用户发送的`keygen`结果进行`ipe.decrypt`解密操作
    - 解密后排序，得到`id + distance` 根据`distance`最小值的id在AES密文中取出相应文件的AES密文
    - AES解密后，返回给客户端

## 文件说明

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

1. 理论上，应该提前训练好模型并将其保存在本地，然后程序内部应该是加载model后根据明文提取出相应的特征向量。（`ipe.setup()`也应该根据model使用时得到的向量大小去自适应）但考虑到复用性将该过程分离，所有的要使用的明文文件需要提前统一提取相应的向量
2. 本文中，停用词存放在私有数据集`word2vec-test`中。具体使用时，根据自己上传位置修改文件读取路径
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
- **服务器**端在**退出时**会自动**清空两个密文数据表**中的内容（下次使用时，`g1 g2 alpha beta`会重新随机选择，留着之前的密文也不会解密成功，且影响解密速度。）
- `most_similarity()`中阈值设定为`5w`，且仅能范围最相似的一个。具体阈值、返回个数可自行修改。
  - `lib/libcrypto.py`中包含了向量扩展的形式，理论上扩大$10^{7}$可忽略误差（提取后的数组为float32类型，7位有效数字）。但由于解密得到的是**实际距离的平方**，距离则扩大$10^{14}$。阈值修改需要适应该距离。


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
  - `libconvertio`中根据`charm`库的序列化、反序列化函数进行了一定的封装
- `FHIPE`矩阵选取伪随机（`n`维矩阵中的数据根据随机种子确定，如果使用默认则`n`维矩阵内容一直固定）
- 如有问题，联系邮箱 goudan.wang@outlook.com

