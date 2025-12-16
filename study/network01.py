import numpy as np#y用于数组
# from utils.features import prepare_for_training
# from utils.hypothesis import sigmoid,sigmoid_gradient

class MultilayerPerceptron:
    #__init__构造函数
    def __init__(self,data,labels,layers,normalize_data =False):
        data_processed= prepare_for_training(data,normalize_data=normalize_data)
        #形参等于实参
        self.data=data_processed
        self.labels=labels
        self.layers=layers#784 25 10
        self.data=data_processed
        self.normalize_data=normalize_data
        #对权重参数进行随机初始化
        self.thetas=MultilayerPerceptron.thetas_init(layers)
    @staticmethod
    def thetas_init(layers):
        num_layers = len(layers)#层的个数
        thetas={}
        """
        会执行两次，得到两组参数矩阵：25*785,10*26都算上了偏置，倒过来看
        """
        #eg：比如说三层只需要两组权重参数
        for layer_index in range(num_layers-1):
            in_count=layers[layer_index]#layers里存的是数量784 25 10
            out_count=layers[layer_index+1]

            #把偏置项给加进去了，偏置的个数跟输出的结果是一致的，所以要在输入项加1，乘法分配律
            #参数值初始化时要小一点，如果大了不好收敛
            thetas[layer_index]=np.random.rand(out_count,in_count + 1) * 0.05









