# gender-recognition
使用深度学习完成男女性别分类任务

本项目支持 前端使用springboot搭建服务，支持通过在线上传图片预测性别，后端模型部署在cpu或gpu都可以。如需使用，可以联系微信wc964083210

一、使用深度学习模型完成男女性别分类任务，其中模型使用Xception、MobileNet、ResNet50等。

根据配置文件face.json可以进行配置，在使用时主要修改：
1 train_dir ：训练集路径；
2 validation_dir ：测试集路径；
3 model_file_path：模型保存路径；
4 model_type：模型类型；

二、文件说明
1 CreateModel.py 创建模型
2 InferFace.py  在线推断时使用
3 TrainFace.py   训练模型时使用
4 server2.py 支持根据前段，使用socket通信，支持网页端显示


三 数据集和结果说明
数据集：
|   | 训练集   | 测试集  |
| ---- |----  | ----  |
| 男 | 23766 | 5808 |
| 女| 23243  | 5841 |

模型: 其中 ResNet50 精度0.97，MobileNet精度0.96
数据链接：
链接：https://pan.baidu.com/s/1Ylhy68N3LwbHGFx9E7Ty9g 
提取码：ep9i
