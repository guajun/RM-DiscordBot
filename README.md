# Bot

# 需求
## General
* 存储人员数据，集中管理
  * Junior, Senior 身份
  * itsc
  * gmail
  * school
  * major
  * ....
* 根据用户权限，允许/禁止 操作
  * 细节待定
  * 例如，Junior不能查看其他人的itsc，只能查看/修改自己的，而Senior可以查看所有人的

* 允许用户通过google sheet 查看、更新数据库中的人员数据

* 战队通过谷歌的问卷等，收集人员信息时，自动同步至数据库
  * 例如，gmail，discord名称
    >如果不能实时监测问卷对应的sheet内容，就周期性检测或者给用户一个确认键

* 日志，log操作
  * 分级

## Order, Review
* 用户 创建/修改/查看/删除 购买请求（称为Order）
   *  interface: Discord + google sheet
   *  一般情况下，用户在 创建/修改/查看/删除 购买请求时，通过google sheet 操作购买请求中的数据
   *  特殊情况下，用户可以通过Discord 机器人操作购买请求，此类操作比较简单，Discord足够实现
      *  例如，为Order添加Shipment，添加快递单号，Reviewer review Order
* 购买请求创建后，自动通知reviewer
* 自动通知请求创建者review结果
## Shipment
* 用户 为Order添加Shipment 数据，例如快递单号、目的地
* 自动通知集运负责人Order中添加的快递单号
  * 当集运负责人确认已经集运/送达，为用户的Shipment更新状态后，自动通知对应的用户

## Recruitment
* 服务器新成员加入时，自动收集一定的信息，尝试与数据库中已有的信息匹配并自动更新其身分组
  * 例如：在招新过程中，某新生使用科大问卷进行注册登记，此时他存在于微信群以及战队的数据库，但是不在discord服务器。当他正式加入战队，按照要求加入discord时，机器人根据他先前在战队登记的discord账号信息，将这个discord账户和数据库中的人员信息进行匹配，自动更新他的身份组


# 模块
## 日志
### 可读日志
logging 模块

给管理员看，可以在discord频道始终print
### checkpoint
用来断电恢复 

## 菜单
* Finance
  * View Purchase Request / Order
    * Recent
    * Pending to be reviewed
    * Order number
  * Review Purchase Request (You have ## request to be reviewed!)
    
    *Particular Position Needed*
  * Create Purchase Request / Order
* Shipment
  * Batch operation
    * Consolidate
    * Arrive

    *Particular Position Needed*
  * Add Shipment Info To Order
  * 
### 一级菜单
机器人的第一级右键菜单，不包括后续的子选项。

需要仔细考虑。不能太多

直接对机器人右键菜单/频道发送指令
* 财务
* 物流
* 个人信息更新
### 二级菜单
用户在使用一级菜单后，机器人和用户私信，显示二级菜单

用户通过消息的按钮选择菜单
## 数据导入、导出、比对
导入、导出、比对的数据库的脚本

暂时不搞

考虑用前端实现

## 物流信息增查删改

## 物流信息通知
1. 主动发送私信通知相关人员

## 财务审批请求增查删改
### 添加
#### 权限&职位
* 自己的：Junior+
* 所有人的：Senior
#### 流程：
1. 用户点击菜单
2. Bot创建空google sheet，配置表头格式内容权限等
3. Bot将google sheet通过私信发送给用户，包括发送后续操作的UI（完成，取消）
4. 用户填写Order信息，或取消添加，若取消，直接删除google sheet，结束流程
5. 用户填写完毕，按完成按钮
6. Bot检查输入内容，若格式出错，直接在私信通知用户，返回步骤4
7. 格式检查通过，Bot将内容私信发送给用户，确认内容，若用户需要修改，返回步骤4
8. 用户不需要修改，写入数据库，包括日志。
9. 若需要通知Reviewer，此时直接通知
### 搜索Order
#### 流程：
1. 用户点击菜单

    子选项：
    * 文本搜索 - 匹配文字
    * 淘宝订单号码搜索
    * 日期搜索

2. 用户输入搜索内容，Bot根据搜索结果给出搜索内容摘要
3. 如果用户需要详情，Bot创建空google sheet，配置表头格式内容权限等，写入
4. Bot将google sheet通过私信发送给用户，包括发送后续操作的UI（完成）
5. 一段时间后自动关闭详情，尝试*检测用户活跃情况（未测试可行性）*，先提醒后关闭
## 财务审批请求应答
1. 主动发送私信通知相关人员（Reviewer）
2. 若不通过，填写理由


## 抽象类/功能
* 通知
  * 各类更新可复用，例如Order，Shipment更新
  * 支持更新回调？装饰器？
* 写入表格至数据库：读取修改后的表格，校验，确认，写入
* 从数据库读取表格：生成，发送，超时
* 超时回调，用于回收google sheet

